---
title:  "Programa para realizar el informe final del SERUMS de forma automatizada"
date:   2025-03-07
permalink: /blog/programa-informe-final-serums/
categories: [Programación, Medicina]
tags: []
author: DaniMedi
excerpt: "Programa en Python para realizar de forma automatizada el informe final del SERUMS a partir de archivos planos del HIS MINSA"
layout: post
image: /assets/images/logo-ministerio-de-salud.jpg
published: true
last_modified_at: 2025-03-07
redirect_from:
---
Actualmente estoy completando el programa SERUMS 2024-I, que finaliza el 30 de abril. Al culminar, se requiere elaborar un informe final, registrando mensualmente la información en el [aplicativo del Ministerio de Salud](https://serums.minsa.gob.pe/).

El registro es intuitivo, pero contar manualmente las actividades puede ser tedioso, especialmente si se deja para el último momento. Además, algunos encargados de estadística no siempre facilitan los datos individuales necesarios. Para solucionar esto, creé un programa en Python que automatiza el proceso a partir de los "Archivos planos" que se pueden descargar del HIS MINSA.

*Nota: Para ejecutar el programa, es necesario instalar [Python](https://www.python.org/), disponible gratuitamente.*

## Forma de registrar los datos

Ya existen recursos que explican cómo realizar el registro de los datos en el aplicativo SERUMS que pueden revisar para tener una noción general de en qué consiste:

- <https://youtu.be/rUp4SSdG8tY?si=r46FMdEMRbAb7SMW>
- <https://youtu.be/EbqbGNGUhic?si=bLLKSs9v4NKpjMes>
- <https://youtu.be/Y_pwEmqXZ4A?si=d4O8joN8HLZJdsuV>

El registro en sí es intuitivo, siempre y cuanto contemos con la información necesaria. Se necesitan:

1. Número de atendidos en cada mes
2. Número de atenciones en cada mes
3. Actividades realizadas y su cantidad en cada mes

Con estos datos, basta con ingresarlos en la sección "Anexos" del [aplicativo SERUMS](https://serums.minsa.gob.pe/). Aquí un GIF mostrando el proceso:

![](/assets/images/serums-aplicativo-informe-final.gif)

## Datos

Obtener los datos necesarios puede tener algunas complicaciones. En mi caso, la Microrred no me facilitó mis registros individuales filtrados para que pueda realizar mi SERUMS de forma sencilla, pero la Dirección Regional de Salud de Moquegua me indicó que podía solicitar el archivo plano y extraerlos yo mismo.

### Archivo plano

Este archivo contiene todos los registros HIS de un período y lugar específicos. En mi Microrred, estadística los descarga mensualmente y contiene la inforamción registrada en HIS de todo el personal de salud de la Microrred.

### Encontrando los códigos de identificación

El archivo plano es una base de datos con muchas variables, el programa se encarga de trabajar con las necesarias, pero debemos tener dos datos de este archivo plano:

1. **RENIPRESS** de su establecimiento (columna `renipress`, no confundir con columna `Id_Establecimiento`)
2. **Código personal asistencial** (columna `Id_Personal`)

El código RENIPRESS de su establecimiento es fácil de encontrar, pueden hacerlo en la [plataforma de SUSALUD](http://app20.susalud.gob.pe:8080/registro-renipress-webapp/listadoEstablecimientosRegistrados.htm?action=mostrarBuscar#no-back-button). Por otro lado, el código personal asistencial (`Id_Personal`) no es el DNI, sino un número asignado. Para encontrarlo, pueden filtrar por establecimiento y analizar fechas de atención y diagnósticos.

#### ¿Cómo trabajar con un archivo CSV?

Algo por mencionar es que los Archivos Planos están en formato CSV, es decir separados por comas. Podemos usar varios programas para manejar este tipo de archivos, quizá el más popular sea Microsoft Excel. Sin embargo, a veces necesitamos realizar un paso extra para que realice la lectura adecuadamente. En el siguiente GIF les realizo una demostración de cómo hacerlo.

![](/assets/images/load-csv-file-excel.gif)

Como mencioné, debemos identificar cuál `Id_Personal` corresponde a nosotros.

### Base de datos de códigos y diagnósticos

El Archivo plano usa códigos para diagnósticos y actividades, pero no contiene registrado lo que representan. Para interpretarlos, se necesita una base de datos como diccionario. Comparto la que creé para facilitar el proceso:

[<i class="fa-solid fa-download"></i> Descargar base de datos de códigos y diagnósticos](/assets/data/cie-10.csv)

Pueden agregar nuevos códigos a este archivo si es necesario.

## Código

### Organización de archivos

Coloquen la base de datos descargada (`cie-10.csv`) y los archivos planos mensuales en una misma carpeta con un formato de nombre consistente (como se muestra en el esquema). También creen los archivos `find_missing_diagnoses.py` y `generate_reports.py` (se indicará a continuación cómo llenarlos).

```plaintext
informe_serums/
│-- 2024_mayo-archivo_plano.csv
│-- 2024_junio-archivo_plano.csv
│-- 2024_julio-archivo_plano.csv
│-- ...
│-- cie-10.csv
│-- find_missing_diagnoses.py
│-- generate_reports.py
```

### find_missing_diagnoses.py

Antes de generar los reportes es importante que detecten cuáles códigos no están registrados en su "diccionario" (`cie-10.csv`).

*Nota: modificar los datos de la primera sección del código según se indica*

```python
# ---- MODIFICAR ESTA ÁREA PARA REGISTRAR SUS DATOS ----
path = "D:\informe_serums"
months = ["2024_mayo", "2024_junio", "2024_julio", "2024_agosto", "2024_septiembre",
          "2024_octubre", "2024_noviembre", "2024_diciembre", "2025_enero"]
renipress = 1234
id_personal = 123456789
# ------------------------------------------------------

import pandas as pd
import os
os.chdir(path)
file_names = [x + "-archivo_plano.csv" for x in months]
codes = []
for file in file_names:
    df = pd.read_csv(file)
    i = (df["renipress"] == renipress) & (df["Id_Personal"] == id_personal)
    df = df[i]
    codes.append(df["Codigo_Item"])

codes = [item for sublist in codes for item in sublist]
unique_codes = list(set(codes))

# Read my database of codes (ICD-10 and activities)
codes = pd.read_csv("cie-10.csv")
codes_dict = dict(zip(codes["codigo"], codes["diagnostico"]))
# Find the codes without diagnosis
meanings = [codes_dict.get(code, "Unknown") for code in unique_codes]
i = [x == "Unknown" for x in meanings]
missing_diagnoses = [code for code, keep in zip(unique_codes, i) if keep]
print(missing_diagnoses)
with open("missing_diagnoses.txt", "w") as file:
    for line in missing_diagnoses:
        file.write(line + "\n") # Use the list to manually add the diagnoses
```

Al ejecutarse, este código generará un archivo llamado `missing_diagnoses.txt` que tendrá en su interior la lista de los códigos que no cuentan con diagnóstico. Si este archivo generado está en blanco, no es necesario hacer nada, si tiene códigos, agreguen esos códigos manualmente a `cie-10.csv`.

*¿Cómo ejecutar el código?: hay varias maneras de ejecutar códigos en Python, una de estas maneras es usando el IDLE de Python:*

![](/assets/images/search-idle-python.jpg)

![](/assets/images/python-idle-run.gif)

### generate_reports.py

Luego de asegurarnos que todos nuestros códigos están registrados, podemos ejecutar el siguiente script, que genera todos nuestros reportes automáticamente.

*Nota: modificar los datos de la primera sección del código según se indica.*

```python
# ---- MODIFICAR ESTA ÁREA PARA REGISTRAR SUS DATOS ----
path = "D:\informe_serums"
months = ["2024_mayo", "2024_junio", "2024_julio", "2024_agosto", "2024_septiembre",
          "2024_octubre", "2024_noviembre", "2024_diciembre", "2025_enero"]
renipress = 1234
id_personal = 123456789
# ------------------------------------------------------

import pandas as pd
codes = pd.read_csv("cie-10.csv")
for mes in months:
    # Download data
    dat = pd.read_csv(mes + "-archivo_plano.csv")
    # Prepare and filter data
    i = (dat["renipress"] == renipress) & (dat["Id_Personal"] == id_personal)
    dat = dat[i]
    dat = dat.merge(codes, how="left", left_on="Codigo_Item", right_on="codigo")
    print(dat["Fecha_Atencion"])
    # Atendidos & Atenciones
    atendidos_atenciones = dat.groupby("Id_Cita").agg({
        "Id_Condicion_Servicio": "first",
        "Id_Condicion_Establecimiento": "first"
    }).reset_index()
    atenciones = ((atendidos_atenciones["Id_Condicion_Servicio"] == "R") |
             (atendidos_atenciones["Id_Condicion_Servicio"] == "N") |
             (atendidos_atenciones["Id_Condicion_Servicio"] == "C")).sum()
    print(atenciones)
    atendidos = ((atendidos_atenciones["Id_Condicion_Servicio"] == "R") |
             (atendidos_atenciones["Id_Condicion_Servicio"] == "N")).sum()
    print(atendidos)
    with open(f"atendidos_atenciones_{mes}.txt", "w") as file:
        file.write(f"Atendidos: {atendidos}. Atenciones: {atenciones}" + "\n")
    # Create file for Actividades preventivo-promocionales for each month
    counts = dat["diagnostico"].value_counts().sort_index()
    total = dat.shape[0]
    keys, values = counts.index.tolist(), counts.values.tolist()
    text_list = [f"{key} ({value})" for key, value in zip(keys, values)]
    final_text = " , ".join(text_list)
    final_text = f"NUMERO DE ACTIVIDADES: {total}\n\n" + final_text
    print(final_text)
    with open(f"actividades_{mes}.txt", "w") as file:
        file.write(final_text + "\n")
```

Al ejecutarlo, el script produce dos archivos por cada mes:

- Uno con el conteo de atendidos y atencions (`atendidos_atenciones_MES.txt`)
- Otro con el conteo y listado de actividades (`actividades_MES.txt`)

*Nota: vi que en algunos videos de YouTube del tema indican que se debe seleccionar solamente las actividades preventivo-promocionales (excluyendo a los diagnósticos de enfermedades) para el informe. Sin embargo, en mi Microrred, se incluyen todos los códigos, incluyendo diagnósticos.*

## Registro final

Ahora solo queda ingresar los datos generados en el [aplicativo SERUMS](https://serums.minsa.gob.pe/) en las secciones que correspondan.

*Aquí un ejemplo del archivo de texto de actividades preventivo-promocionales de un mes (listo para copiar y pegar):*

![](/assets/images/ejemplo-output-actividades-programa-serums.jpg)

## Aclaración

Este método está diseñado para obtener informes que tienen el formato observado en informes finales de procesos SERUMS anteriores en mi Microrred. Vi que en algunos lugares seleccionan solamente las actividades preventivo-promocionales, no incluyendo los diagnósticos de patologías. Es posible que diferentes Redes o Microrredes de salud tengan otros requerimientos, por lo que tal vez sea necesario ajustar el código para esos casos.

## Opinión

Considero que este proceso debería automatizarse desde las unidades de estadística. Con conocimientos básicos de programación, pude generar mi informe fácilmente de forma semi-automatizada. Con un enfoque adecuado, un método similar podría implementarse a nivel nacional, ahorrando tiempo y recursos.

Entiendo que este método presentado pueda resultar un poco extraño o incluso complicado para alguien que nunca antes ha usado algún lenguaje de programación. Por tal motivo, continúo trabajando en este programa en un repositorio privado en GitHub para mejorar sus capacidades. En caso encuentre una manera más conveniente para que ustedes puedan hacer sus informes SERUMS la estaré compartiendo por este medio.

Pueden escribirme si tienen alguna duda :)
