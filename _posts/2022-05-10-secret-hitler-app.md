---
id: 969
title: 'Secret Hitler app (for the set up)'
date: '2022-05-10T13:07:58+00:00'
author: DaniMedi
layout: post
guid: 'https://danimedi.com/?p=969'
permalink: /blog/secret-hitler-app/
enclosure:
    - "https://danimedi.com/wp-content/uploads/2022/05/secret-hitler-app-create-game.mp4\n59483\nvideo/mp4\n"
    - "https://danimedi.com/wp-content/uploads/2022/05/secret-hitler-app-get-roles.mp4\n245051\nvideo/mp4\n"
image: /assets/images/secret-hitler-long-image.jpg
categories:
    - Programación
---

I created this web app to automatize the set up of the game Secret Hitler. The main objective of this app is accelerating the set up process of the game. The main idea is that the players enter to this website from their cell phones to get the information about their roles and their team-mates (according to the rules of the game).

## App

*Note: the app goes to sleep after a period of inactivity.*

<iframe frameborder="0" src="https://danimedi.shinyapps.io/secret_hitler_game/" style="border: 1px outset; width: 100%; height: 600px"></iframe>

## Instructions

### Creating a game

The first step is creating a game, this means generating a random code for the game. The only input you have to provide to the app is the number of players.

<video controls>
  <source src="/assets/videos/secret-hitler-app-create-game.mp4" type="video/mp4">
</video>

Then, after pressing the button, you obtain a code of a game that you can share to all the players and a list of IDs. You can give these IDs to the different players in different ways (eg, pieces of paper, WhatsApp messages).

### Getting the roles

So, with the code of the game and the ID as inputs of the web app, all the players get their roles and the IDs of their team-mates (according to the game rules).

<video controls>
  <source src="/assets/videos/secret-hitler-app-get-roles.mp4" type="video/mp4">
</video>

For recognizing their team-mates (for those who have access to that information), the players can screenshot or write the IDs of the team-mates, and then all the players can reveal their IDs in person.

## Personal comments

Personally, I think using the envelopes and cards has something special, and it is an important part of the game, especially for those playing the game for the first time. However, after a few games this process can be somewhat slow, so this is when this app could be handy.

If your are interested in the code and the process of the creation of this app you can check [this other post]({{ '/blog/creating-the-app-for-secret-hitler-set-up/' | relative_url }}) and the [GitHub repo of the app](https://github.com/danimedi/secret_hitler_game).

I recorded a video about this on my YouTube channel.

*Note: this is my first video on YouTube speaking in English, and I discovered that I mispronounced “fascist” during all the video* 😅*, sorry about that. [This is the right pronunciation](https://dictionary.cambridge.org/pronunciation/english/fascist).*

<iframe width="560" height="315" src="https://www.youtube.com/embed/ovJ35YKiGQE?si=Xgz_qQKsfnSVoGPu" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
