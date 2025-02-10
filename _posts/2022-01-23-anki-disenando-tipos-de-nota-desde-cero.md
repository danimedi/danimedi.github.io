---
id: 519
title: 'Tutorial de Anki: Diseñando tipos de nota desde cero (básico)'
date: '2022-01-23T23:55:39+00:00'
author: DaniMedi
layout: post
guid: 'https://danimedi.com/?p=519'
permalink: /blog/anki-disenando-tipos-de-nota-desde-cero/
enclosure:
    - "https://danimedi.com/wp-content/uploads/2022/01/create_note_type.mp4\n480082\nvideo/mp4\n"
    - "https://danimedi.com/wp-content/uploads/2022/01/customize_cards_window.mp4\n422046\nvideo/mp4\n"
    - "https://danimedi.com/wp-content/uploads/2022/01/visualize_cards.mp4\n290942\nvideo/mp4\n"
    - "https://danimedi.com/wp-content/uploads/2022/01/erase_info_templates.mp4\n246415\nvideo/mp4\n"
    - "https://danimedi.com/wp-content/uploads/2022/01/first_field_cloze_customization.mp4\n330084\nvideo/mp4\n"
    - "https://danimedi.com/wp-content/uploads/2022/01/adding_extra_field.mp4\n840279\nvideo/mp4\n"
    - "https://danimedi.com/wp-content/uploads/2022/01/adding_info_field.mp4\n791733\nvideo/mp4\n"
    - "https://danimedi.com/wp-content/uploads/2022/01/adding_link_field.mp4\n904734\nvideo/mp4\n"
    - "https://danimedi.com/wp-content/uploads/2022/01/create_new_class.mp4\n454418\nvideo/mp4\n"
image: /wp-content/uploads/2022/01/thumbnail-1.png
categories:
    - Anki
---

En este tutorial explicaré cómo crear un tipo de nota, que sería como la estructura que usaremos para crear flashcards (más información sobre esto y sobre cómo comenzar a usar Anki en el [tutorial de comenzando a usar Anki desde cero](https://danimedi.com/blog/tutorial-de-anki-desde-cero/)), utilizando un ejemplo. Para esto crearé un tipo de nota similar al que uso normalmente, esto servirá para explicar cómo podemos editar nuestro tipo de nota y cada uno es libre de personalizar el tipo de nota a su manera.

No es necesario tener conocimientos previos sobre HTML o CSS, se pueden simplemente copiar las partes y usarlas como plantilla.

El video comentando este tutorial se encuentra en: <https://youtu.be/Ze3wq3Enlx0>

También hay en la página web un [tutorial más avanzado](https://danimedi.com/blog/tutorial-de-anki-disenando-tipos-de-notas-avanzado/). Es un buen lugar para continuar, pues es la continuación directa de este post.

Además, en el canal de YouTube se tiene la siguiente playlist con videos relacionados a este tema de personalización de tipos de notas: <https://youtube.com/playlist?list=PLiR4mMxzSHWiRa3V-Uf51nTf5EP3Gl78G>

## Entendiendo la ventana de personalización

Para comenzar vamos a crear un nuevo tipo de nota para iniciar desde cero. Para crear un tipo de nota podemos clonar uno previamente existente, en este caso crearemos un tipo de nota en base al tipo de nota “Cloze” (más información sobre este tipo de nota en el [tutorial de comenzando a usar Anki desde cero](https://danimedi.com/blog/tutorial-de-anki-desde-cero/) ). Podemos hacer esto del siguiente modo:

![](/assets/images/create_note_type.gif)

Podemos editar este tipo de nota y personalizarlo como queramos, el primer campo será aquel campo especial del tipo Cloze que será utilizado para crear las preguntas y respuestas, los otros campos tendrán contenido adicional según queramos.

Entonces, comenzamos a personalizar. La personalización se realiza desde la ventana “Cards…” que se accede del siguiente modo:

![](/assets/images/customize_cards_window.gif)

Esta ventana tiene dos partes marcadas, una mitad (la izquierdo) es el área donde realizaremos nuestra personalización y en la otra mitad (la derecha) podremos visualizar el resultado de los cambios que haremos.

### Mitad izquierda

La mitad izquierda tiene 3 partes que pueden accederse con los botones: “Front Template”, “Back Template” y “Styling”; versiones antiguas de Anki tienen también estas partes pero todas visibles en esta mitad. Es en el contenido de estas partes donde realizaremos la personalización de nuestro tipo de nota.

![](/assets/images/note_type_customization.jpg)

Un poco de explicación sobre las partes:

- Front Template: establece el contenido que irá en la pregunta de la flashcard en formato HTML.
- Back Template: establece el contenido que irá en la respuesta de la flashcard en formato HTML.
- Styling: tiene el objetivo de personalizar el Front Template y el Back Template, está en formato CSS.

Esta forma de incluir contenido y personalizarlo es similar en gran medida al usado por páginas web, hay un [video en el canal sobre esto](https://youtu.be/okVnuGfvRyA).

### Mitad derecha

En la mitad derecha tenemos dos botones: “Front Preview” que nos muestra cómo luce la “pregunta” y “Back Preview” que nos muestra cómo luce la “respuesta”. Para poder visualizar esto tenemos que tener contenido agregado en los campos. También podemos visualizar cómo lucirían las otras preguntas y respuestas si tenemos varias, como se observa en el ejemplo:

![](/assets/images/visualize_cards.gif)

Los cambios realizados en la mitad izquierda se ven reflejados automáticamente en la mitad derecha, eso es bastante conveniente, incluso lo usé para practicar algunas cosas de HTML y CSS para páginas web.

## Comprendiendo cómo se generan las flashcards

Las flashcards son creadas utilizando el contenido que tenemos en los campos. Este contenido es incluido en las flashcards de acuerdo a cómo esté establecido en nuestro tipo de nota. Podemos entender esto con un ejemplo.

Vamos a crear nuestro propio desde cero, para esto en nuestro tipo de nota creado vamos a borrar todo el contenido de Front Tamplate y Back Template, del siguiente modo:

![](/assets/images/erase_info_templates.gif)

Entonces, ahora crearemos nuestro tipo de nota desde cero. Recordemos que en Front Template tenemos lo que corresponderá a la pregunta, para esto tenemos que saber el nombre del campo que contendrá esta información, este sería el contenido de nuestro primer campo con el nombre de “Text”, para agregar esta información rodeamos el nombre del campo con dos llaves (si tiene otro nombre, en lugar de “Text”, utilizamos ese otro nombre), entonces tendríamos algo así: `{{Text}}`, podemos observar que se observa el contenido; sin embargo, tenemos que agregar antes un indicador de que este campo es un campo Cloze, que es especial, para esto agregamos “cloze:” de la siguiente manera: `{{cloze:Text}}`, entonces tenemos el primer campo de la forma que queremos. Para la parte de Back Template, que sería la respuesta, hacemos exactamente lo mismo. El proceso sería el siguiente:

![](/assets/images/first_field_cloze_customization.gif)

Ahora, ya tenemos nuestra flashcard lista para usarla, si es que usamos solo el primer campo de contenido “Text”. Es una de las cosas que hace usar el tipo de nota Cloze algo bastante sencillo. Ahora, los demás campos pueden contener cosas adicionales, por ejemplo, podemos agregar el campo “Back Extra” que queremos que contenga contenido adicional, pero solo cuando se muestra la respuesta. También podemos cambiar el nombre del campo a “Extra” para demostrar cómo se hace desde “Fields…”.

![](/assets/images/adding_extra_field.gif)

En el video se puede observar el uso de `<br>` que es usado en HTML para crear un salto de línea, si agregamos múltiples de esos podemos crear más separación. Otra forma de agregar separación es haciendo que aparezca una línea horizontal, esto lo hacemos con `<hr>`.

## Agregando más contenido adicional

Se puede agregar contenido especial o contenido con características especiales, en lo personal me gusta incluir un campo que contenga un poco de información más extensa sobre la información de alguna flashcard, pero no me gusta que me muestre la información de inmediato junto con la respuesta. Para esto se puede agregar `hint:`. En este ejemplo se muestra cómo creamos un campo adicional con el nombre de “Info” y lo incluimos como se menciona. También se puede notar otras cosas adicionales, por ejemplo, cómo agregar un campo adicional y la línea horizontal.

![](/assets/images/adding_info_field.gif)

Notar cómo solo se muestra el contenido cuando se presiona con el mouse en el nombre del campo.

Otra cosa que me gusta tener a la mano es la referencia o referencias de la información que estoy utilizando para crear flashcards, para esto hay diferentes alternativas. Una opción es utilizar dos campos adicionales, uno para el título de la referencia (“Ref titulo”) y otro con el link de la referencia (“Ref link”). Entonces, podemos combinarlos usando HTML para crear un link.

![](/assets/images/adding_link_field.gif)

Al hacer click nos abrirá una ventana del buscador donde nos mostrará ese link que hemos agregado en el campo “Ref link”.

Notar que se incluye la etiqueta `<a>` para agregar el link, observar como se coloca el link y el título en HTML, se puede copiar de la misma forma esto para usarlo en otros contextos.

Al momento, nuestro tipo de nota personalizando ya va quedando bien y, con bastante poco, ya es muy funcional. Ahora, se pueden tener algunos detalles adicionales para poder que nuestras flashcards sean más estéticas.

## Personalizando

### Personalización general

Comencemos por lo simple. Las opciones que tenemos de personalizar son bastante amplias, ya que podemos personalizar nuestras flashcards de forma similar a páginas web, así que podemos entender que tenemos muchas opciones; sin embargo, no estamos diseñando páginas web, así que no necesitamos muchísima información respecto a esto, al menos en un inicio.

Algo importante es intentar realizar la personalización desde la parte “Styling” en la mitad izquierda de la ventana, usando CSS y no tanto en las ventanas “Front Template” y “Back Template”, ya que esto nos permite tener las cosas más ordenadas y personalizar aquí es un poco más sencillo.

Como algo muy básico, en Styling podemos copiar algo como esto:

```
/*General*/
.card {
  font-family: arial;
  font-size: 20px;
  text-align: center;
  color: black;
  background-color: white;
}
/*General modo noche*/
.card.nightMode {
  color: white;
}

/*Cloze general*/
.cloze {
 font-weight: bold;
 color: blue;
}
/*Cloze modo noche*/
.nightMode .cloze {
 color: lightblue;
}

```

Podemos ver que tenemos como secciones con cierto contenido dentro de llaves, esto es suficiente para comenzar a personalizar varias cosas, entre ellas el estilo de fuente, tamaño de fuente, la alineación del texto, el color del texto, el color de fondo. Podemos experimentar con estos valores para ver cómo nos gusta más. Nota: para los colores podemos usar el código HEX, el código RGB o un nombre normal que sea reconocido por CSS, aquí dejo una [lista de colores](https://htmlcolorcodes.com/color-names/) que pueden utilizar.

En lo personal lo dejo casi todo como está, de forma predeterminada, aunque últimamente he optado por alinear el texto a la izquierda en lugar de tener el contenido centrado.

### Personalizando elementos específicos

Ahora, podemos nosotros decidir personalizar cosas individuales, como decidir cambiar el color o tamaño de letra solo para el campo “Extra”. Esto lo podemos hacer de diferentes maneras, la más sencilla podría ser creando clases, esto lo podemos hacer agregando `<div class="<em>nombre</em>">` y luego personalizar esta clase desde Styling. Atentos al siguiente video:

![](/assets/images/create_new_class.gif)

De esta manera podemos sobrescribir algunas cosas para elementos específicos. Además, podemos asignar una misma clase para diferentes elementos y realizar cambios en esos elementos de la misma manera, podemos crear el número de clases que queramos.

## Campos condicionales

Lo explicado hasta ahora brinda una gran cantidad de posibilidades para poder personalizar nuestras flashcars, algo que nos da aún más posibilidades es usar los campos condicionales o el reemplazo condicional, esto significa poder mostrar u ocultar cosas de acuerdo a si un campo tiene contenido o no, esto se explica en la sección de [Reemplazo condicional del manual de Anki](https://apps.ankiweb.net/docs/manual.es.html#reemplazo-condicional) y en el siguiente [video del canal](https://youtu.be/HbVL-ovs1VU):

<iframe width="560" height="315" src="https://www.youtube.com/embed/HbVL-ovs1VU?si=rYDmS7FcESHMcmMG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Plantillas

Ahora, con la información presentada tenemos bastantes posibilidades de diseño de nuestras flashcards. Aquí incluyo las plantillas usadas por el ejemplo y también agrego algunas cosas más, como los campos condicionales y otros detalles. Pueden copiarlo y usarlo como plantilla o modificarlo para crear su tipo de nota propio.

### Front Template

```

{% raw %}
{{cloze:Text}}
{% endraw %}

```

### Back Template

Notar que se agrega ‘text:’ en los campos destinados a las referencias, esto es una recomendación de Anki para lidiar con posibles errores en los links cuando se agrega cierto formato al texto (ej. negritas, cursiva, subrayado).

```
{{cloze:Text}}<hr>
{{#Extra}}<div class="extra">{{Extra}}</div><br>{{/Extra}}
{{#Info}}{{hint:Info}}<br><br>{{/Info}}
{{#Ref titulo}}Link: <a href="{{text:Ref link}}">{{text:Ref titulo}}</a>{{/Ref titulo}}
```

### Styling

NOTA: notar que en las partes necesarias para el modo noche se agrega un poco más (las partes que contienen `.night_mode`), esto tiene utilidad para que los cambios también apliquen al modo noche de teléfonos móviles.

```

/*GENERAL*/
.card {
  font-family: arial;
  font-size: 20px;
  text-align: left;
  color: black;
  background-color: white;
}
/*Modo noche*/
.card.nightMode, .night_mode .card {
  color: white;
}

/*CLOZE*/
.cloze {
 font-weight: bold;
 color: blue;
}
/*Modo noche*/
.nightMode .cloze, .night_mode .cloze {
 color: lightblue;
}

/*EXTRA*/
.extra {
  color: navy;
}
/*Modo noche*/
.nightMode .extra, .night_mode .extra {
  color: pink;
}

/*INFO (HINT / INFORMACIÓN OCULTA)*/
a[href="#"] {
  text-decoration: underline;
}

```

## Más información

Este post tiene una [siguiente parte que es más avanzada](https://danimedi.com/blog/tutorial-de-anki-disenando-tipos-de-notas-avanzado/). Es un buen lugar para continuar aprendiendo sobre este tema, pues es la continuación directa de este post.

Para más información se pueden revisar algunos videos del canal de YouTube que se encuentran subidos en la siguiente playlist: <https://youtube.com/playlist?list=PLiR4mMxzSHWiRa3V-Uf51nTf5EP3Gl78G>. Esta playlist contiene información adicional también, como más ejemplos y cómo agregar audio en base al texto que tenemos (Text to speech \[TTS\]).

Además, el manual de Anki contiene información completa sobre personalización en la [sección de Card Templates](https://docs.ankiweb.net/templates/intro.html).

En sí, todo esto de la personalización, es en base a HTML y CSS, así que si alguno tiene conocimientos previos o adquiere conocimientos nuevos en estos temas debería poder usarlos para el diseño de las flashcards.
