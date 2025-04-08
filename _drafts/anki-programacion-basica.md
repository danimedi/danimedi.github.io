---
title: "Programación básica en Anki"
date:
permalink: /blog/anki-programacion-basica/
categories: [Programación, Estudio y Anki]
tags: []
author: DaniMedi
excerpt: "Cómo programar de forma básica en Anki utilizando la consola de Python"
layout: post
image: /assets/images/
published: true
last_modified_at:
redirect_from:
---

- Para qué podría ser útil
- Qué necesitaba hacer yo
- Cómo lo hice: acceder a consola, escribir código, ejecutar código
- Cómo aprender más funciones y realizar más cosas
- Escribir add-ons de Anki

```python
import re
from aqt import mw
from anki.utils import strip_html

def capitalize_first_word(text):
    if re.fullmatch(r'\s*(<img [^>]+>\s*)+', text.strip(), re.IGNORECASE):
        return text
    visible_text = strip_html(text)
    capitalized = re.sub(r'^(\s*)(\w)', lambda m: m.group(1) + m.group(2).upper(), visible_text)
    if visible_text != capitalized:
        # Replace only the first word in the HTML version
        # Use a regex that finds the first word outside of tags
        return re.sub(r'^(\s*)(\w)', lambda m: m.group(1) + m.group(2).upper(), text)
    else:
        return text

note_ids = mw.col.find_notes('deck:"General Knowledge" note:"Cloze-Daniel"')
fields = ["Text", "Extra"]

changed = 0
for note_id in note_ids:
    note = mw.col.get_note(note_id)
    for field in fields:
        modified = False
        original = note[field]
        new = capitalize_first_word(original)
        if new != original:
            note[field] = new
            modified = True
        if modified:
            mw.col.update_note(note)
            changed += 1

print(f"{changed} changes were made.")
```
