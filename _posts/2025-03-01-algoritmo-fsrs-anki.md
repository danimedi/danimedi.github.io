---
title:  "Algoritmo FSRS en Anki"
date:   2025-03-01
permalink: /blog/algoritmo-fsrs-anki/
categories: [Estudio y Anki]
tags: []
author: DaniMedi
excerpt: "Explicación del algoritmo FSRS en Anki y tutorial de cómo usarlo"
layout: post
image: /assets/images/anki-logo.png
published: false
last_modified_at: 2025-03-01
redirect_from:
---
Pensé que había tocado este tema hace tiempo. Hace unos días recibí un correo de un suscriptor solicitando recomendaciones sobre qué intervalos estaba usando en mis configuración de las opciones de mis mazos de Anki, le recomendé usar el algoritmo FSRS que llevo usando hace ya un par de años, y pensaba pasarle el link de mi post en el que explicaba este tema, pero quedé impactado al darme cuenta que no había hablado de este tema. Así que gracias a Claudio que pude darme cuenta y aquí va la explicacíon pendiente.

!Ahora comencemos la explicación!

*Nota: prácticamente todo el contenido de esta explicación fue obtenido de la sección correspondiente del [manual oficial de Anki](https://docs.ankiweb.net/deck-options.html#fsrs)*

## ¿Qué es FSRS?

FSRS (Free Spaced Repetition Scheduler) es un sistema avanzado de repetición espaciada que reemplaza el algoritmo SM-2 utilizado tradicionalmente por Anki. Su objetivo es mejorar la predicción de la curva de olvido, permitiéndote recordar más información en menos tiempo.

Una explicación más detallada de su funcionamiento puede encontrarse en los links de [esta página web](https://github.com/open-spaced-repetition/fsrs4anki/wiki).

## ¿Cómo usarlo en Anki?

### Antes de activarlo

Antes de habilitar FSRS en Anki, asegúrate de que todas tus plataformas sean compatibles:

- Anki 23.10 o superior
- AnkiMobile 23.10 o superior
- AnkiWeb
- AnkiDroid 2.17+

Si alguna versión de Anki que usas no es compatible, podrían ocurrir errores en la programación de las revisiones. Además, si previamente usaste una versión personalizada de FSRS, es importante eliminar cualquier configuración anterior antes de activarlo.

### Configuración

1. Ve a las opciones del mazo y busca la sección "FSRS" en la parte inferior.
2. Activa FSRS (se aplicará globalmente a todos los mazos).
3. Asegúrate de que los pasos de aprendizaje y reaprendizaje sean menores a 1 día (se recomienda 10m o 30m).
4. Pulsa "Optimizar" en la sección de "Parámetros FSRS".
5. Ajusta la "Retención deseada" (proporción de flashcards que quieres recordar en cada revisión). El valor por defecto es 90%, que equilibra carga y eficiencia.
6. **Importante:** No uses "Difícil" en lugar de "De nuevo" si has olvidado una flashcard, ya que FSRS asumirá que la recordaste y programará intervalos demasiado largos.


		[Colocar un GIF explicativo]

### Determinando la retención deseada

El ajuste de la retención deseada afecta directamente la frecuencia de revisiones:

- A 90%, revisarás una flashcard en 100 días.
- A 95%, la revisarás en 46 días (2x más revisiones).
- A 97%, la revisarás en 27 días (3.7x más revisiones).
- A 99%, la revisarás en 9 días (10x más revisiones).

Un valor mayor a 97% puede ser abrumador, mientras que valores muy bajos generan demasiados olvidos. Se recomienda mantenerse entre 90% y 97%.


		[Colocar la imagen explicatoria]


### Optimización y evaluación de parámetros FSRS

FSRS usa aprendizaje automático para ajustar la programación según tu historial de revisiones. Para optimizar:

1. Pulsa "Optimizar" para que FSRS analice tus revisiones y genere los mejores parámetros.
2. Para evaluar los parámetros actuales, usa el botón "Evaluar".
3. No copies parámetros de otras personas, ya que FSRS ajusta la programación según tu propio rendimiento.

		[Explicar con qué frecuencia uso optimizar y qué coloco en la opción de buscar para optimizar]

### Simulador de carga de trabajo

FSRS permite estimar cuánto estudiarás diariamente:

- Días a simular: predice revisiones futuras.
- flashcards nuevas por día: cómo afectan la carga.
- Máximo de revisiones por día.

### Compatibilidad con complementos

FSRS puede no ser compatible con algunos complementos que afectan la programación de las revisiones. Si usas addons que modifican los intervalos de flashcards, es posible que FSRS no funcione correctamente.

## Conclusión

FSRS mejora la eficiencia del estudio en Anki, reduciendo la carga de revisiones sin comprometer la retención. Ajustando correctamente sus parámetros, puedes optimizar tu tiempo de estudio y mejorar tu aprendizaje a largo plazo.



		[Agregar mi opinión y experiencia personal, así como las opciones que estoy usando yo al momento]


Manual de Anki: https://docs.ankiweb.net/deck-options.html#fsrs


Si tienen cualquier duda pueden colocarla en los comentarios o consultarme directamente.
