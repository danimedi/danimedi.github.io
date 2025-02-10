---
id: 715
title: 'Tutorial de Anki: diseñando tipos de notas (avanzado)'
date: '2022-02-13T23:57:32+00:00'
author: DaniMedi
layout: post
guid: 'https://danimedi.com/?p=715'
permalink: /blog/tutorial-de-anki-disenando-tipos-de-notas-avanzado/
enclosure:
    - "https://danimedi.com/wp-content/uploads/2022/02/customize_basic_note_type.mp4\n2008522\nvideo/mp4\n"
    - "https://danimedi.com/wp-content/uploads/2022/02/add_card_type.mp4\n1301398\nvideo/mp4\n"
    - "https://danimedi.com/wp-content/uploads/2022/02/conditional_card_types.mp4\n2629276\nvideo/mp4\n"
    - "https://danimedi.com/wp-content/uploads/2022/02/note_type_styling.mp4\n1628007\nvideo/mp4\n"
image: /wp-content/uploads/2022/02/thumbnail.png
categories:
    - Anki
---

En un [anterior tutorial](https://danimedi.com/blog/anki-disenando-tipos-de-nota-desde-cero/) expliqué aspectos básicos de cómo diseñar tipos de notas. En ese tutorial se explicaron las cosas más importantes y se realizó la explicación utilizando el tipo de nota *Cloze*. En este tutorial se asumirá que ya se tienen estos conocimientos básicos y a partir de ahí se explicará algunas cosas adicionales. En este tutorial se utilizará como ejemplo la creación de tipos de notas a partir del tipo básico, en lugar del *Cloze*, y se podrá observar las diferencias en el uso de estos tipos de notas. En el canal de YouTube también se tienen [videos](https://youtube.com/playlist?list=PLiR4mMxzSHWiRa3V-Uf51nTf5EP3Gl78G) que explican algunos ejemplos de posibles usos de estos tipos de notas.

Este tutorial está acompañado de un [video en YouTube](https://youtu.be/WwDLDdzTmhQ).

## Incluyendo campos

Cómo conectar los campos (*fields*) con la estructura (tipo de nota) es algo que ya se explicó en el [tutorial anterior](https://danimedi.com/blog/anki-disenando-tipos-de-nota-desde-cero/). En el caso del tipo de nota *Cloze* esto no es tan importante para formar las preguntas o las respuestas, pero en este tutorial sí habrá que tener un poco más de consideración con esto.

En este tutorial, como se mencionó anteriormente, se explicarán los temas a partir del tipo de nota básico. Un ejemplo nos permitirá poder recordar o entender nuevamente algunas cosas desarrolladas en el tutorial básico anterior. En el siguiente video se pueden observar los siguientes procesos: clonar tipo de nota → funcionamiento del tipo básico → realizar cambios → cambiar nombre de los campos.

<figure class="wp-block-video"><video controls="" src="https://danimedi.com/wp-content/uploads/2022/02/customize_basic_note_type.mp4"></video></figure>Hasta aquí no hay diferencia significativa con el tipo de nota Cloze. Básicamente tenemos diferentes campos y podemos usarlos para formar preguntas y respuestas con información adicional de la forma que queramos, como nuestra imaginación lo decida.

Aquí hay un [video en el canal](https://youtu.be/vA-O3hVKQrs) relacionado justamente a esto, en el que podemos observar cómo podemos diseñar un tipo de nota nuevo usando diferentes campos.

<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper"><div class="nv-iframe-embed"><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0" height="675" loading="lazy" src="https://www.youtube.com/embed/vA-O3hVKQrs?feature=oembed" title="Personalización del tipo de nota | Tutorial intermedio de Anki" width="1200"></iframe></div></div></figure>## Más flashcards a partir de una nota (*card types*)

Un siguiente paso en el diseño de nuestro tipo de nota es poder crear más de una flashcard a partir de la información que incluimos en los campos. Esto lo podemos hacer agregando tipos de tarjetas (*card types*) en la ventana de personalización del tipo de nota. En cada uno de estos *card types* podemos reformular nuevamente nuestras flashcards, pudiendo crear diferentes preguntas y respuestas a partir de la misma información, esto puede entenderse mejor con un ejemplo:

<figure class="wp-block-video"><video controls="" src="https://danimedi.com/wp-content/uploads/2022/02/add_card_type.mp4"></video></figure>En el ejemplo mostrado se estarían creando dos flashcards por cada vez que se agregue la información (al presionar “Add” o agregar). En una la pregunta muestra el nombre común y se debe recordar y responder cuál es el nombre científico, mientras que la otra tiene como pregunta la imagen y se debe responder con el nombre del animal. Como se puede observar somos libres de incluir los campos que queramos de la forma que queramos y si deseamos podemos agregar otros *card types* con diferentes combinaciones y formas de preguntar las cosas.

## Creando flashcards condicionalmente

Alguno puede darse cuenta de un problema que puede aparecer cuando se crean varias flashcards es que, en caso se tenga algún campo vacío, flashcards con información faltante podrían ser creadas. Para esto se podría hacer uso de la creación de flashcards condicional, esta estrategia también podría usarse de otras formas para decidir el número o la forma de las flashcards por crear en el tipo de nota.

Este concepto es, en esencia, el mismo que el de los [campos condicionales](https://danimedi.com/blog/anki-disenando-tipos-de-nota-desde-cero/). Simplemente que esto tiene un efecto especial cuando se agrega en la parte de *Front Template*, pudiendo decidirse de esta manera si es que la flashcard se crea o no dependiendo del contenido de algún campo (o más de uno).

<figure class="wp-block-video"><video controls="" src="https://danimedi.com/wp-content/uploads/2022/02/conditional_card_types.mp4"></video></figure>En el ejemplo podemos observar el uso de estos campos condicionales para decidir si crear o no flashcards. Además, esto se puede combinar con el uso tradicional de campos condicionales para tener tipos de notas dinámicos que no creen flashcards innecesarias y que se ajusten a lo que queremos. Además, podemos usar otros campos como condiciones (en base a si están llenos o no) para crear algunas flashcards o no. Podemos dejar volar nuestra creatividad para el diseño de nuestros tipos de notas.

## Utilidad del “styling”

Es aquí en realidad donde tiene más utilidad la parte de *Styling*, ya que si se tiene múltiples tarjetas/flashcards en nuestro tipo de nota, podría ser muy tedioso personalizar las cosas en cada una de estas flashcards que serán generadas. Una propiedad del *Styling* es que su contenido se aplica a todos los *card types*, muy útil si tenemos una gran cantidad de *card types* (imagina cambiar el color de la pregunta en más de 20).

<figure class="wp-block-video"><video controls="" src="https://danimedi.com/wp-content/uploads/2022/02/note_type_styling.mp4"></video></figure>Como se puede observar en el ejemplo podemos ir agregando clases como `NombreComun` o `question` en las partes “Front Template” y “Back Template” de los diferentes *card types*, para luego personalizar todo desde un lugar único: “Styling”.

## Posibles usos o estrategias

En lo personal uso con más frecuencia el tipo de nota Cloze con algunas modificaciones, como las presentadas en el [tutorial básico](https://danimedi.com/blog/anki-disenando-tipos-de-nota-desde-cero/) de diseño de tipos de notas. Sin embargo, en algunas situaciones sí puede ser muy útil el uso de estos tipos de notas más personalizadoss. En mi experiencia he identificado los siguientes:

- Asociar cosas específicas, por ejemplo: vocabulario de otro idioma (asociar palabra, imagen, audio), geografía (país, mapa, capital, bandera), etc.
- Crear flashcards a partir de otras fuentes, como una base de datos ([video mostrando un ejemplo](https://youtu.be/7suFVcB6HM4)).
- Crear flashcards de forma estructurada, como una plantilla para tomar apuntes.

Sobre este último punto tengo pensado realizar algún video y/o post en el futuro. Básicamente es para tener una forma de tomar apuntes estructurados de forma directa en Anki, creando flashcards en el proceso. Por ejemplo, en caso tengamos que leer y aprender información de múltiples artículos científicos, podría ser de utilidad poder tomar apuntes de forma estructurada anotando la información en campos como autor, fecha, hallazgo principal, diseño de estudio, entre otros.

A pesar de todo eso, en lo personal, sigo considerando que el tipo de nota Cloze suele ser más versátil en la mayoría de situaciones.

Aquí se encuentra el video complementario a este tutorial:

<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper"><div class="nv-iframe-embed"><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0" height="675" loading="lazy" src="https://www.youtube.com/embed/WwDLDdzTmhQ?feature=oembed" title="Tutorial de Anki: diseñando tipos de notas (avanzado)" width="1200"></iframe></div></div></figure>