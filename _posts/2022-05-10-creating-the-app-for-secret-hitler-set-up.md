---
id: 967
title: 'Creating the app for Secret Hitler set up'
date: '2022-05-10T13:07:38+00:00'
author: DaniMedi
layout: post
guid: 'https://danimedi.com/?p=967'
permalink: /blog/creating-the-app-for-secret-hitler-set-up/
image: /assets/images/secret-hitler-long-image.jpg
categories:
    - Programación
---

Secret Hitler is probably my favorite board game ever. I think that one of the coolest parts is the set up, everyone receives the secret role in an envelope and then, then, once everyone knows their roles, everybody close their eyes and only the fascists recognize each other. I found that part somewhat mystic and funny, however it can be slow, especially after the first games (yeah, sometimes I play a lot of games).

So, one day, my brother told me one idea he had about automatizing this process by creating a a computer program. He explained to me the details and I thought that it could be a challenge for me and something really interesting to try. So I did it and this is how I did it.

*NOTE: this is not a tutorial about how to create this Shiny app, but I might make one in the future. This post contains general information about the conceptual process of creating this app and only some simple technical considerations.*

## Basic idea

The basic idea was achieving two things with the app:

1. Create a <span style="text-decoration: underline;">game</span> with IDs for the players.
2. Randomize the <span style="text-decoration: underline;">IDs</span> and give the information according to the roles (e.g., the IDs of the team mates for those who are in the fascist team).

It was a simple idea, so I decided to create an app. I am not an amazing programmer, actually I am only proficient in one programming language: R. And, probably, this is not the best programming language out there to create a web app, but that’s the tool I had.

I built the app using R and the ‘shiny’ package. So I created a “Shiny app”.

## First prototypes

### Centralized idea

The first idea was creating an app that could be used by *one computer*. The idea was creating the game and then obtaining the IDs of the players in the same computer, so the players take turns to check their information.

**Pros:** it was easier, simpler randomization, it could use the real names of the players, it doesn’t need a server to host the app on the internet.

**Cons:** it is not so easily available to everyone, it needs a computer (not only a cell phone), it needs the appropriate software (R and the packages).

### Decentralized using numbers

Based on those cons, I decided that it would be a better idea to create an app that can be used *by each player on their phones*, and find a way to connect all those players, so they receive the information of the same game. A simple solution was using a controlled randomization using a seed to synchronize all the players into the same game, then give each player a number so they can access their information.

**Pros:** no need for a computer, no need for specialized software (only a browser and internet access), available to multiple players and multiple games at the same time.

**Cons:** cheating is easy and it can even occur just by mistake, you only need to insert another number instead of yours and you will access the information.

### Decentralized using random IDs

So, to fix the problem of cheating I changed some things of the app to have the final result. My solution to the problem of cheating was using *random IDs*, so the players are not able to know the IDs of the other players and insert them to have access to their information.

**Pros:** same as before, less chance of cheating.

**Cons:** the IDs are not so simple, and the players need to find a way to recognize their team-mates after they receive the information (there are multiple ways of doing this though).

## Final result

So, that was the process of creating the app. The history of the changes can be found in the [GitHub repo of the app](https://github.com/danimedi/secret_hitler_game). And the app, with its instructions and examples of how to use it, is available on [this other post](https://danimedi.com/blog/secret-hitler-app/).
