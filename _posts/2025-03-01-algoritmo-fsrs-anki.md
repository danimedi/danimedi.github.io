---
title:  "Algoritmo FSRS en Anki"
date:   2025-03-02
permalink: /blog/algoritmo-fsrs-anki/
categories: [Estudio y Anki]
tags: []
author: DaniMedi
excerpt: "Explicación del algoritmo FSRS en Anki y tutorial de cómo usarlo"
layout: post
image: /assets/images/anki-logo.png
published: true
last_modified_at: 2025-03-02
redirect_from:
---
Pensé que había tocado este tema hace tiempo. Hace unos días recibí un correo de un suscriptor solicitando recomendaciones sobre qué intervalos estaba usando en mis configuración de las opciones de mis mazos de Anki, le recomendé usar el algoritmo FSRS que llevo usando hace ya un par de años, y pensaba pasarle el link de mi post en el que explicaba este tema, pero quedé sorprendido al darme cuenta que no había realizado ningún post o video. Así que gracias a Claudio que pude darme cuenta y aquí va la explicacíon pendiente.

!Comencemos!

<div style="border: 2px solid #000; padding: 10px; border-radius: 5px; background-color: #f8f8f8;">
  <i>Nota: prácticamente todo el contenido de esta explicación fue obtenido de la sección correspondiente del <a href="https://docs.ankiweb.net/deck-options.html#fsrs">manual oficial de Anki</a>.</i>
</div>

<br>

## ¿Qué es FSRS?

FSRS (Free Spaced Repetition Scheduler) es un sistema de repetición espaciada que reemplaza el algoritmo SM-2 utilizado tradicionalmente por Anki. Su objetivo es mejorar la predicción de la curva de olvido, permitiéndote recordar más información en menos tiempo.

Una explicación más detallada de su funcionamiento puede encontrarse en los links de [esta página web](https://github.com/open-spaced-repetition/fsrs4anki/wiki).

## ¿Cómo usarlo en Anki?

### Antes de activarlo

Antes de habilitar FSRS en Anki, asegúrate de que todas tus plataformas sean compatibles:

- Anki 23.10 o versiones más recientes
- AnkiMobile 23.10 o versiones más recientes
- AnkiWeb
- AnkiDroid 2.17 o versiones más recientes

Si alguna versión de Anki que usas no es compatible, podrían ocurrir errores en la programación de los intervalos de tus flashcards. Además, si previamente usaste una versión personalizada de FSRS, es importante eliminar cualquier configuración anterior antes de activarlo.

### Configuración

1. Ve a las opciones del mazo y busca la sección "FSRS" en la parte inferior.
2. Activa FSRS (se aplicará globalmente a todos los mazos).
3. Asegúrate de que los pasos de aprendizaje y reaprendizaje sean menores a 1 día (se recomienda 10m o 30m).
4. Ajusta la retención deseada (proporción de flashcards que quieres recordar en cada revisión). El valor por defecto es 90%, que equilibra carga y eficiencia.
5. Pulsa "Optimizar" en la sección de "Parámetros FSRS".

![](/assets/images/anki-set-fsrs-options.gif)

### Determinando la retención deseada

El ajuste de la retención deseada afecta directamente la frecuencia de revisiones:

- A 90%, revisarás una flashcard en 100 días.
- A 95%, la revisarás en 46 días (2x más revisiones).
- A 97%, la revisarás en 27 días (3.7x más revisiones).
- A 99%, la revisarás en 9 días (10x más revisiones).

Un valor mayor a 97% puede ser abrumador, mientras que valores muy bajos generan demasiados olvidos. Se recomienda mantenerse entre 90% y 97%.

![](/assets/images/FSRS_retetion_workload.png)
*Imagen extraída del [manual oficial de Anki](https://docs.ankiweb.net/deck-options.html#fsrs).*

### Optimización y evaluación de parámetros FSRS

FSRS usa aprendizaje automático para ajustar los intervalos de tus flashcards en base a tu desempeño y tu retención deseada. Para optimizar los parámetros del algoritmo en base a esto simplemente debes pulsar "Optimizar".

*Nota: el botón "Evaluar" sirve para evaluar los parámetros actuales.*

No es necesario realizar esta optimización de los parámetros de forma constante. Personalmente, lo realizo una vez al mes (lo tengo programado en [Todoist](https://app.todoist.com/)). Anki tiene la opción de realizar la optimización en todos los diferentes *presets* de opciones que tengamos con un solo botón.

![](/assets/images/anki-optimize-all-presets.gif)

### Simulador de carga de trabajo

FSRS permite estimar cuánto estudiarás diariamente:

- Días a simular: predice revisiones futuras.
- Flashcards nuevas por día: cómo afectan la carga de trabajo.
- Máximo de revisiones por día.

En realidad se entiende mejor experimentando con él.

## Consideraciones importantes

### Compatibilidad con complementos

FSRS puede no ser compatible con algunos complementos que afectan la programación de las revisiones. Si usas complementos que modifican los intervalos de flashcards, es posible que FSRS no funcione correctamente.

### Importancia de ser "sincero"

Una recomendación que se brinda en el propio manual de Anki es no usar el botón "Difícil" en lugar de "De nuevo" si has olvidado una flashcard. Indica que el algoritmo FSRS asumirá que la recordaste y ajustara los parámetros en base a ello, lo que programará intervalos demasiado largos que no reflejan tu desempeño y aprendizaje.

## Conclusión

El algoritmo FSRS busca mejorar la eficiencia del estudio en Anki, reduciendo la carga de revisiones sin comprometer la retención. Yo lo llevo usando desde que salió (alrededor de noviembre de 2023) y la verdad me siento muy cómodo usándolo, así que desde mi experiencia personal lo recomiendo también.

Espero que este post haya podido servir para explicar de forma simple lo que es y la forma de implementarlo en Anki. Si tienen más dudas recomiendo leer la sección correspondiente a FSRS en el [manual de Anki](https://docs.ankiweb.net/deck-options.html#fsrs) que contiene la información brindada en este post y más.
