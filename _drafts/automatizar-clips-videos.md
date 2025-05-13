---
title:  "Cómo automatizar creación de clips para videos largos"
date:
permalink: /blog/automatizar-clips-videos/
categories: [Programación]
tags: []
author: DaniMedi
excerpt: ""
layout: post
image: /assets/images/
published: true
last_modified_at:
redirect_from:
---

Como creador de contenido en YouTube he tenido problemas entrando en formatos de videos cortos, como TikTok, Instagram u otros. Creo que me gusta tomarme mi tiempo para expresar a mi ritmo las cosas que quiero decir y compartir. Sin embargo, hoy en día muchas personas prefieren consumir contenido de una duración más corta.

Algo que estuve realizando es hacer videos cortos introductorios o promocionales para poder realizar videos en YouTube. Otras personas como mi hermano Diego (canal de YouTube) y también Kimberly (@lory.steps) me recomendaron que realizar clips de mi contenido y subirlo en varias plataformas podría ser de utilidad. Sin embargo, me ha resultado complicado por motivos de tiempo.

Ante esta problemática estuve pensando en posibles soluciones, siendo una de ellas automatizar lo más que se pueda la creación de clips de mis videos. Luego de este camino de aprendizaje logré poder crear clips (videos cortos de fragmentos de algún video largo destinado para YouTube) de forma semi-automatizada mediante un programa que genera estos clips a partir de especificar el tiempo de inicio y fin de los clips en el video.

Esto hace que crear los clips de los videos sea tan simple como:


## Requirements

- ffmpeg
- Python

## Cut the video using time stamps

Create a CSV file using time stamps.

Then use the following code to cut the video (requires FFMPEG:

```
import subprocess
import pandas as pd

def cut_ffmpeg(input_file, start, end, output_file):
    cmd = [
        'ffmpeg',
        '-ss', start,
        '-to', end,
        '-i', input_file,
        '-c', 'copy',
        output_file
    ]
    subprocess.run(cmd)

original_video = "hablemos-del-serums.mp4"
duration = 5 # minutes

for i in range(duration):
    cut_ffmpeg(input_file=original_video,
               start=f"00:{i:02}:00",
               end=f"00:{i:02}:59",
               output_file=f"clip_{i+1}.mp4")

time_stamps = pd.read_csv("time_stamps.csv")
for i in range(len(time_stamps)):
    cut_ffmpeg(original_video,
               start=time_stamps["start"][i],
               end=time_stamps["end"][i],
               output_file=f"clip_{i+1}.mp4")

```

## Adding an outro

1. Create a PNG or JPG image (e.g., outro.png) that includes your promo text. You could use tools like Canva, Paint, or any other.
2. Convert the image in a 5-second video clip using ffmpeg:

```
ffmpeg -loop 1 -i outro.png -t 5 -vf "scale=1080:1920" -c:v libx264 -pix_fmt yuv420p -y outro.mp4
```
-loop 1: repeats the image
-t 5: total duration = 5 seconds
scale=1080:1920: optional, makes it TikTok vertical format
outro.mp4: the video version of the image

However, in Canva you can create videos.



3. Concatenate each clip with the outro using ffmpeg

```
import subprocess
import os

def run_cmd(cmd):
    subprocess.run(cmd, check=True)

def concat_with_outro(clip_file, outro_file, output_file):
    # Generate intermediate filenames
    clip_fixed = "clip_fixed.mp4"
    outro_fixed = "outro_fixed.mp4"
    clip_ts = "clip.ts"
    outro_ts = "outro.ts"

    # Step 1: Re-encode both input files for compatibility
    run_cmd([
        "ffmpeg", "-i", clip_file,
        "-c:v", "libx264", "-c:a", "aac", "-pix_fmt", "yuv420p",
        "-y", clip_fixed
    ])
    run_cmd([
        "ffmpeg", "-i", outro_file,
        "-c:v", "libx264", "-c:a", "aac", "-pix_fmt", "yuv420p",
        "-y", outro_fixed
    ])

    # Step 2: Convert both to .ts format
    run_cmd([
        "ffmpeg", "-i", clip_fixed, "-c", "copy",
        "-bsf:v", "h264_mp4toannexb", "-f", "mpegts", clip_ts
    ])
    run_cmd([
        "ffmpeg", "-i", outro_fixed, "-c", "copy",
        "-bsf:v", "h264_mp4toannexb", "-f", "mpegts", outro_ts
    ])

    # Step 3: Concatenate the .ts files and convert back to mp4
    run_cmd([
        "ffmpeg", "-i", f"concat:{clip_ts}|{outro_ts}",
        "-c", "copy", "-bsf:a", "aac_adtstoasc", "-y", output_file
    ])

    # Optional: Clean up intermediate files
    for file in [clip_fixed, outro_fixed, clip_ts, outro_ts]:
        if os.path.exists(file):
            os.remove(file)


n_clips = 5
for i in range(n_clips):
    concat_with_outro(f"clip_{i+1}.mp4", "outro.mp4", f"clip_{i+1}_final.mp4")
```
