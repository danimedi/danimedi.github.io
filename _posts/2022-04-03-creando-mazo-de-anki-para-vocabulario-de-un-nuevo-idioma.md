---
id: 864
title: Creando mazo de Anki para vocabulario de un nuevo idioma
date: '2022-04-03T14:30:44+00:00'
author: DaniMedi
layout: post
guid: https://danimedi.com/?p=864
permalink: /blog/creando-mazo-de-anki-para-vocabulario-de-un-nuevo-idioma/
image: /assets/images/languages-poster.jpg
categories:
- Study & Anki
- Study & Anki
- Programming
---

Como mencioné en un [post anterior sobre mi estrategia para aprender nuevos idiomas]({{ '/blog/estrategia-personal-para-aprender-un-nuevo-idioma/' | relative_url }}), el vocabulario es algo sumamente importante en etapas tempranas del aprendizaje de un nuevo idioma.

La forma que más me sirvió (y me gustó) para aprender vocabulario es usando el programa Anki (programa al que le dedico varios posts y [videos](https://youtu.be/O0DHrkgPhNA)).

Hay un video en el canal de YouTube sobre esto: <https://youtu.be/L-tq2LEdlZE>

## ¿Cómo surgió la idea?

Llegó un punto en el que estudiaba muchas cosas en Anki, especialmente cosas relacionadas a medicina. Entonces, quería poder incorporar el aprendizaje de idiomas a Anki también. El punto en el que terminé de convencerme de que era una buena idea y también obtuve bastante información relacionada al tema, como algunos consejos, ideas y otros detalles fue con la lectura del libro [Fluent Forever](https://fluent-forever.com/book/) de Gabriel Wyner. En este libro justamente se presentan algunas formas de usar Anki para el aprendizaje de idiomas, así como consejos generales para aprender idiomas. Uno de estos consejos fue justamente el de aprender vocabulario de forma temprana en el aprendizaje del idioma.

A partir de esto decidí hacer las cosas a mí manera.

## Creación del proyecto

El libro brindó un recurso valioso para comenzar a aprender el vocabulario de un idioma, este fue una [lista de 625 palabras](https://blog.fluent-forever.com/base-vocabulary-list/) con significado concreto que son las más frecuentemente usadas. Esto hace que puedan ser aprendidas mediante imágenes fácilmente, sin necesidad de tener que aprender mediante la traducción de palabras en algún otro idioma. Entonces, me propuse realizar justamente esto, crear una deck en Anki con el vocabulario de estas palabras.

Sin embargo, al intentar crear la deck me encontré con algunos problemas. Me demoraba bastante tiempo escogiendo imágenes manualmente y también tardaba bastante descargando audios con la pronunciación de cada palabra. Sentía que podía hacerse de forma más eficiente.

Justamente, por esos tiempos, estaba aprendiendo a programar y me propuse a mí mismo poder aliviar algunos de estos procesos mediante el uso de la programación y eso fue lo que hice. En realidad comencé a automatizar algunas cosas, pero me di cuenta que mis habilidades de programación eran mayores de lo que esperaba, así que finalmente terminé automatizando más cosas de las que esperaba.

El proyecto que terminé realizando se puede categorizar en las siguientes partes:

1. Creación de la lista de palabras
2. Descarga de imágenes
3. Traducción de la lista de palabras
4. Descarga de audios con la pronunciación
5. Creación de la base de datos para importar a Anki
6. Importar base de datos (+ audios e imágenes) a Anki
7. Diseñar tipo de nota (flashcards)

## Lista de palabras

Mi punto de partida fue la lista de [625 palabras](https://blog.fluent-forever.com/base-vocabulary-list/) de Fluent Forever que mencioné anteriormente. A partir de ahí completé con algunas palabras que consideraba que eran importantes también, esto lo hice a partir de algunas listas de frecuencia de palabras. Por ejemplo, otra lista que usé y que fue conveniente para obtener imágenes fue la lista de [inglés básico con figuras de Wikipedia](https://simple.wikipedia.org/wiki/Wikipedia:Basic_English_picture_wordlist).

Finalmente terminé con una lista de palabras de 713 palabras comúnmente usadas con significado concreto.

## Imágenes

A partir de esta lista de palabras decidí obtener imágenes para cada una. Esto fue lo primero que hice mediante programación.

Usé el lenguaje de programación [R](https://www.r-project.org/), con el paquete ‘[rvest](https://rvest.tidyverse.org/)‘ para realizar el web scraping. Esto lo hice en tres partes:

1. Descargar imágenes disponibles en la [página de Wikipedia de inglés básico con figuras](https://simple.wikipedia.org/wiki/Wikipedia:Basic_English_picture_wordlist) mencionada. Para esto usé el paquete
2. Descargar imágenes a partir de la búsqueda de las mismas. Esto lo hice en la página web de [pixabay](https://pixabay.com/images/search/) (si no recuerdo mal).
3. Revisar y corregir imágenes manualmente. Lógicamente a veces pueden ocurrir errores y al culminar las partes automatizadas realicé una inspección de que las imágenes eran las adecuadas.

Estas imágenes fueron guardadas con nombres específicos en una carpeta.

## Traducción

Lo mencionado hasta ahora fue realizado netamente en inglés, entonces faltaba realizar la traducción a algún otro idioma. Esto se realizó en una base de datos en la que la primera columna era la lista de palabras (en inglés), la siguiente columna era la misma lista, pero sin comentarios adicionales (algunas palabras tenían cosas adicionales como para diferenciar cosas; ejemplo: ‘back (body)’ y ‘back (direction)’), las siguientes columnas estaban dedicadas a otros idiomas. Los idiomas que decidí incluir fueron: español, portugués, francés, chino, cantonés, hindi, árabe y ruso.

Esta traducción lógicamente sería muy tediosa de hacerse manualmente y más cuando uno no sabe el idioma, por este motivo se realizó una herramienta interesante.

Resulta que el servicio de traducción de Google tiene una función que puede ser usada en [Google Sheets](https://www.google.com/sheets/about/). Esta función es `<a href="https://gsuitetips.com/tips/sheets/translate-languages-in-google-sheets/" rel="noreferrer noopener" target="_blank">GOOGLETRANSLATE()</a>`. Esto fue bastante conveniente para mí porque me permitió poder copiar mi base de datos a Google Sheets, realizar la traducción de las palabras a los distintos idiomas y volverla a pasar a mi computadora. Además, otras funciones me permitieron poder realizar traducciones más exactas; por ejemplo, si ya tengo la columna de palabras en inglés y palabras en español y quiero obtener la traducción al francés, puedo traducir ambas columnas al francés y la traducción debería coincidir, de lo contrario quizá haya algún error, lo mismo puede hacerse parar las demás columnas y usando más idiomas.

![](https://lh6.googleusercontent.com/jLzqvno1bNDOos4KmKidyBWtMC2kC8dc8E8M2ZR6H1I28b08d8DOqgmYxZQQdZct5aWoNdm61RNNrshwbDDsFt29CUa4FSy6YccoAwd1k3T4XXeJaT8mnNctlFjvoAk8ryb-pN-w)

Con las palabras con conflictos o aquellas en las que no se pudo realizar la traducción me encargué de traducirlas manualmente mediante el uso de algunas páginas web como [WordReference](https://www.wordreference.com/) o [Linguee](https://www.linguee.com/). En realidad hubieron bastantes palabras en las que hubo conflictos en la traducción, especialmente en los verbos.

Al culminar, consideré importante que una persona que sepa hablar el idioma revisara la traducción. Esto lo hice yo mismo para el español y algunos conocidos para el portugués y el francés. Los otros idiomas no recibieron esta revisión adicional.

## Audios

Descargar audios es especialmente tedioso, comparado con descargar imágenes. Entonces, de todas formas debía encontrar una forma de hacerlo de forma automatizada.

Para conseguir esto decidí optar por otra estrategia, el uso de APIs. Esto permite poder comunicar diferentes computadoras (mi computadora con una página web) para poder obtener información de forma automatizada mediante programación. En mi caso esto significaba poder descargar audios a partir de las palabras que tenía de los diferentes idiomas.

Algunos lenguajes de programación (ej. python) ya cuentan con libraries para usar la API de Forvo. En mi caso usé R y tuve que crear mis propias herramientas “desde cero” para trabajar con esta API.

Primero intenté usar un [servicio gratuito](https://soundoftext.com/) que usa la voz de la traducción de Google. Sin embargo, el audio no era del todo natural y encontraba algunos problemas para traducir algunas palabras. Por este motivo decidí optar por una opción de pago. Entonces, usé la API de [Forvo](https://forvo.com/), que es una plataforma con audios de hablantes nativos muy popular. Con esta API y programando mi propio sistema de descarga de audios pude descargar los audios para las palabras de todos los idiomas incluidos en mi base de datos. Estos audios fueron guardados en carpetas específicas con nombres apropiados.

Este programa que creé se encuentra en mi repositorio: <https://github.com/danimedi/vocabulaRy>

## Completando la base de datos

Hasta este punto ya tenía bastantes cosas listas para poder crear mi deck en Anki, pero aún faltaba incluir algunas columnas poder crear un mazo/deck a partir de lo que tenía. En un [video de mi canal de YouTube](https://youtu.be/6BCdyIRW_m4) explico en detalle cómo es que se realiza la importación de bases de datos a Anki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6BCdyIRW_m4?si=V7joJj6brjckCUfE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Lo que me faltaba era agregar una columna con los nombres de los archivos de las imágenes y también otra con los nombres de los archivos de los audios. Esto lo realicé también mediante programación y finalmente pude obtener bases de datos específicas para cada idioma según quisiera.

Luego de importar la base de datos, así como las imágenes y los audios, terminé con flashcards con el siguiente contenido:

![](/assets/images/example-anki-vocabulary.png)

Cabe mencionar que para importar ya se debe contar con un tipo de nota para el contenido, esto lo mencionaré a continuación para que se entienda mejor.

## Diseñando el tipo de nota

Algo genial de Anki es que le da a uno la libertad de poder aprender de la forma que uno quiere, mediante el diseño libre de las flashcards. Esto se hace mediante el diseño de tipos de nota y ya realicé un [post hablando de esto]({{ '/blog/anki-disenando-tipos-de-nota-desde-cero/' | relative_url }}) con mayor profundidad.

En realidad esto depende probablemente de cómo uno quiera aprender y del idioma que uno quiera aprender, pero en mi caso yo realicé dos flashcards por cada conjunto de información (“nota”). Las flashcards que incluí fueron las siguientes:

1. Aprender significado: audio en la parte de adelante como pregunta (“Front”); palabra e imagen en la parte de atrás como respuesta (“Back”).
2. Aprender pronunciación/palabra: imagen en la parte de adelante como pregunta (“Front”); palabra y audio en la parte de atrás como respuesta (“Back”).

Aquí están los ejemplos de ambas flashcards:

![](/assets/images/example-anki-vocabulary-2.png)

Lógicamente hay otras formas de hacerlo, como darle más prioridad a aprender la palabra escrita. Cada uno es libre de hacerlo a su manera.

## Aprendizaje

Posteriormente me encontré con algunos problemas que los solucioné en el camino. Por mencionar alguno, incluí un primer campo “First field” para poder realizar actualizaciones del mazo/deck en caso hayan cambios en las imágenes, audios o palabras en la base de datos, esto hace que el mazo/deck sea dinámico y pueda adaptarse a cambios sin tener que comenzar a aprender las flashcards de cero en caso hayan cambios menores.

### Cosas que haría diferente si lo hiciera de nuevo

Al inicio del proyecto mis habilidades de programación eran bastante limitadas, hacer todo eso me sirvió mucho para aprender a programar y obtener datos de internet de forma automatizada. Sin embargo, mi falta de conocimientos iniciales me hizo cometer muchos errores y hacer las cosas de forma bastante desorganizada.

Si hiciera las cosas de nuevo le prestaría más atención a la organización del proyecto. Por ejemplo, tener la estructura propia de un proyecto de programación y no una estructura un tanto improvisada, que terminó incluso con una estructura de paquete de R (cosa que también estaba aprendiendo en su momento). Además, poder separar la base de datos en más bases de datos para algunas cosas quizá era apropiado (por ejemplo la columna del pinyin del chino mandarín).

Otra cosa a la que le prestaría atención, que va de la mano con el manejo de la base de datos, es al género de las palabras. Esto se podría manejar en una base de datos adicional y es de gran importancia para aprender correctamente el vocabulario en algunos idiomas.

Lógicamente, muchas de estas cosas aún se pueden mejorar y solucionar en el proyecto y es posible que este sea el caso.

### Cosas que me gustaría hacer pero no sé cómo

Quizá por diferentes motivos (falta de capacidad intelectual, actitud, tiempo) hay cosas que no sé cómo lograr con este proyecto.

#### Conseguir dinero

Realizar este proyecto me costó dinero. Por ejemplo, para tener acceso a la API de Forvo para descargar los audios.

Y también me costó mucho tiempo. Aunque parezca que no es mucho, para alguien con conocimientos casi nulos de programación (inicialmente) fue un gran trabajo. Además, también realicé la traducción manual de muchas palabras y consulté a bastantes personas sobre las traducciones para estar seguro de que eran las correctas.

Poder recuperar el dinero invertido y ganar dinero a partir de mi trabajo es algo en lo que he pensado, pero no he llegado a concretar aún. Sé que existe el problema para personas creativas (considero que soy relativamente creativo) de generar ingresos por sus creaciones. [Jordan Peterson habla de este problema](https://medium.com/illumination/jordan-peterson-is-right-2b75cd2c919b), de esta “maldición” de las personas creativas, quienes suelen encontrar dificultades para poder conseguir dinero a partir de su creatividad. Lógicamente no quiero estar en esa situación.

Por último, considero que ganar dinero es una forma de mejorar las cosas, si hay más dinero se pueden hacer más cosas. Por ejemplo, se podrían solucionar los posibles problemas por copyright, contratar a personas para realizar la traducción exacta, crear nuevas herramientas, entre muchas otras cosas.

#### Crear una comunidad

Hay cosas que se pueden mejorar en comunidad y más aún en los idiomas y me di cuenta de inmediato cuando trabajé en la creación de este proyecto. Considero que poder mejorar el proyecto (ej. corregir traducciones, conseguir mejores imágenes y audios) se presta mucho a la colaboración.

En una situación un tanto utópica se podría tener una comunidad con hablantes de distintos idiomas colaborando con las traducciones, creando imágenes que sean específicas para cada idioma (un perro en Perú quizá no se vea igual que un perro en Finlandia), agregando ejemplos del uso de las palabras en oraciones, agregar información sobre el género de la palabra, entre otros. Incluso podría darse la situación en la que las personas ya no trabajen en una base de datos fuera de Anki, sino directamente desde Anki. Quizá esto vaya de la mano con el tema de mazos colaborativos (tema al que ya le dediqué un [post]({{ '/blog/anki-problemas-y-soluciones-de-mazos-colaborativos/' | relative_url }})).

Entiendo que para esto se requieren algunos problemas similares a los de conseguir dinero, como lidiar con los temas de copyright. También se tendría que elegir alguna plataforma y encontrar incluso una forma de manejar dinero para poder impulsar el desarrollo de herramientas más complejas en beneficio de la comunidad.

---

En este post he mencionado bastantes cosas relacionadas a la obtención de información de internet, considero que es una habilidad bastante útil, especialmente hoy en día que cada vez más cosas se encuentran disponibles por medios digitales. Tengo pensado realizar algún curso, tutorial o escribir algún libro sobre cómo realizar esto. Estén al tanto del contenido si están interesados 😀

Video en el canal de YouTube sobre esto:

<iframe width="560" height="315" src="https://www.youtube.com/embed/L-tq2LEdlZE?si=Ncf3Ct90jW_FP-2T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
