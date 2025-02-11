---
id: 853
title: 'Anki: problemas y soluciones de mazos colaborativos'
date: '2022-03-13T20:26:10+00:00'
author: DaniMedi
layout: post
guid: https://danimedi.com/?p=853
permalink: /blog/anki-problemas-y-soluciones-de-mazos-colaborativos/
image: /assets/images/collaborative-anki-image.png
categories:
- Estudio y Anki
---

Anki es un gran programa para crear y estudiar flashcards, aprovechando la repetición espaciada y el recuerdo activo. Está de más decir que es mi programa de estudio favorito, considerando que gran parte del contenido de mi [canal de YouTube](https://www.youtube.com/c/DaniMedi555), así como varios [posts]({{ '/blog/tutorial-de-anki-desde-cero/' | relative_url }}) en la página web son relacionados a este programa. Sin embargo, lógicamente, hay algunas cosas en las que se puede mejorar.

Un aspecto del programa con el que se suele tener cierta dificultad y que tiene mucho margen de mejora y gran potencial es el de la creación de mazos/decks colaborativos. Actualmente, la creación de flashcards en grupo no es tan óptima como podría ser y existen numerosos problemas encontrados por aquellos que intentan crear flashcards en grupo, pero también hay algunas soluciones para algunos de estos problemas e incluso algunos proyectos que podrían solucionar más cosas en el futuro.

Este tema ya es discutido en la comunidad de Anki, es de destacar el [post](https://www.milchior.fr/blog_en/index.php/post/2020/05/02/Collaborative-decks-in-Anki) de Arthur Milchior a través de su blog personal.

En mi canal de YouTube hay un video explicando este tema: <https://youtu.be/c1FVcq5qGWw>.

## Importancia

El [aprendizaje colectivo](https://www.oxfordreference.com/view/10.1093/acref/9780190622664.001.0001/acref-9780190622664-e-874) es una de las cosas que nos hace especiales como humanos. Aprender en grupo es más eficiente, menos propenso a errores y más divertido. Esto es algo que realizamos todo el tiempo, simplemente usando información aprendida y compartida por otras personas y compartiendo la información que aprendemos nosotros (a través de conversaciones, libros, videos, blogs u otros medios).

Entonces, es de gran utilidad poder incorporar esto en nuestro estudio cotidiano. En el caso de Anki, esto sería a través de compartir información a través de flashcards a otras personas. Esto ahorraría bastante tiempo en el estudio, ya que la parte que demora más en el estudio de flashcards es justamente crear las mismas.

Además, las flashcards contienen pedazos de información individual que puede ser discutida entre distintas personas, y esta discusión del contenido de las flaschards es sumamente valiosa para el aprendizaje, tanto para asegurarnos que la información sea correcta y esté presentada de la mejor forma posible, como también para aprender de la propia discusión y generar una comunidad involucrada en el contenido del mazo.

Actualmente, en Anki se tienen opciones que no brindan del todo las herramientas necesarias para crear más eficientemente mazos en grupo. Si bien hay formas de realizar esto y existen ejemplos destacados de decks de muy buena calidad realizadas de este modo (como [Ultimate Geography](https://github.com/anki-geo/ultimate-geography) y [AnKing Overhaul](https://www.ankipalace.com/step-1-deck)), aún hay dificultades en la creación de este tipo de mazos y su existencia es aún limitada a un grupo muy reducido de decks, la inmensa mayoría de mazos compartidos son creados por personas individuales.

## Problemas

Existen dos problemas principales para la creación de mazos de forma colectiva:

1. No existe alguna herramienta específica para crear flashcards simultáneamente.
2. No existe alguna forma sencilla de poder sincronizar y actualizar cambios en los mazos de los usuarios.

Estos problemas traen consigo dificultades en la distribución del trabajo, coordinación de la forma de organización a través de mazos y/o etiquetas que deben tener el mismo nombre, estandarización del tipo de nota, entre otras.

Se puede recurrir a algunas soluciones alternativas, pero son en gran medida subóptimas, como la creación de una cuenta específica para la creación de algún mazo a la que tengan acceso aquellos que estén creando el mazo.

## Soluciones existentes

Actualmente existen algunas herramientas que permiten lidiar con algunas de las dificultades que se tienen. Por ejemplo, el programa permite importar y exportar decks de forma muy sencilla a través de su plataforma web ([AnkiWeb](https://ankiweb.net/shared/decks/)).

También se puede recurrir a alguna forma de ir publicando versiones de algún mazo cada cierto tiempo y lidiar con los cambios usando algún add-on como el [Special Fields](https://ankiweb.net/shared/info/1102281552).

Además, se pueden crear mazos comunitarios de alguna manera a través de “herencia”. Esto quiere decir que alguna persona se hace cargo del mazo que otra persona ha realizado anteriormente y lo mejora o lo amplía y posteriormente este proceso puede repetirse. Esta es una forma muy común de mejorar mazos en la [comunidad en inglés de Anki de medicina](https://www.reddit.com/r/medicalschoolanki/).

Un add-on que brinda una solución más completa, a través de algún sistema de control de versiones como GitHub es [CrowdAnki](https://ankiweb.net/shared/info/1788670778). Sin embargo, esto tiene la dificultad de que requiere tener cierto entendimiento sobre el uso de este sistema de control de versiones.

### Algunas cosas aprendidas

En mi caso he intentado ya algunas veces realizar mazos en grupo. En muchos de estos casos me he encontrado con dificultades y considero que es importante tener en consideración algunas cosas:

- Hacer las cosas lo más simples posibles, especialmente si los participantes no tienen mucha experiencia con Anki. Evitar complicar las cosas (ej. exigir cierta organización por etiquetas).
- Tener las cosas claras, se puede crear un documento explicando las cosas necesarias para realizar el proyecto (ej. tipo de nota, forma de crear flashcards, referencias usadas) y algún tutorial de referencia para lidiar con problemas típicos, para evitar realizara la misma explicación varias veces. En esta página web se tiene un [tutorial básico]({{ '/blog/tutorial-de-anki-desde-cero/' | relative_url }}).
- Tener algún sistema sencillo de detección de errores y sugerencias. Esto podría realizarse de diferentes formas, como con un cuestionario/formulario de Google que incluya cosas como:
    - Tipo de error o cosa por cambiar.
    - Note ID (identificador de la nota).
    - Explicación del motivo del cambio.
    - Cuál sería el contenido de la flashcard de ser cambiada o agregada.
- Ser flexible y tener una buena comunicación y trabajo en equipo. Tener objetivos en común.

## Posibles soluciones futuras

Entre las posibles soluciones futuras que considero tienen mayor potencial destaco a [AnkiHub](https://courses.ankipalace.com/ankihub). Este proyecto tiene el potencial de poder ser la herramienta que permita solucionar gran parte de los problemas que actualmente se tiene respecto al tema. Es posible que no falte mucho para su lanzamiento oficial y, en lo personal, estoy bastante interesado en la forma en la que este proyecto podría cambiar la forma de crear flashcards en conjunto.

## Ideas

Uno puede permitirse soñar a veces y, cuando uno aún no tiene los medios para poder llevar alguna idea a cabo, simplemente quedan ahí, como ideas, como deseos. En lo personal hay algunas ideas que considero podrían ser interesantes si se llevaran a cabo y que me gustaría poder hacer yo mismo, si fuera más inteligente o tuviera más recursos que al momento no tengo.

Una idea podría ser tener una red especie de red social de flashcards, en la que cada post sea una flashcard y se pueda tener una discusión que pueda terminar en cambios o adiciones. Esto puede hacerse de tal manera que la discusión sea interesante incluso para aquellos que no usen flashcards, ya que gran parte de los que hace a las flashcards bien hechas interesantes es el hecho de que presentan información importante de forma concisa, como lista para ser debatida. Algunas herramientas adicionales podrían ser la opción de descargar automáticamente posts/flashcards a los que dimos like, detectar y sincronizar cambios en las flashcards descargadas de la red social, seguir (con descargas automáticas) a personas o instituciones de nuestro interés (ej. alguna sociedad científica).

Una discusión más amplia sobre el tema discutido en este post puede encontrarse en el [post de Arthur Milchior](https://www.milchior.fr/blog_en/index.php/post/2020/05/02/Collaborative-decks-in-Anki) sobre este tema.

En mi canal de YouTube hay un video explicando este tema:

<iframe width="560" height="315" src="https://www.youtube.com/embed/c1FVcq5qGWw?si=rP-8ODbfawC6DP6A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
