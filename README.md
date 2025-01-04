# Lenguaje de Señas con Python

Este repositorio tiene el proyecto para la detección del Abecedario Lenguaje de Señas con MediaPipe  

## Integrantes:

●	Diomaris Durán ( ddg00011@red.ujaen.es )
●	Paúl Paillacho ( ppp00031@red.ujaen.es )


## Introducción

El proyecto "Detección del Abecedario en Lenguaje de Señas con MediaPipe” tiene el objetivo de explorar la tecnología para detectar puntos de referencia de cuerpos humanos. MediaPipe, la herramienta utilizada para este proyecto, pertenece a la empresa Google, es de código abierto y ofrece herramientas para el procesamiento de datos visuales en tiempo real.
La motivación del presente trabajo se centra en dos pilares; la exploración y aprendizaje de procesamiento de datos visuales, y generar una potencial herramienta en favor de grupos de atención prioritaria que ayude a una consolidación de una sociedad inclusiva. 
El lenguaje de señas es esencial para millones de personas, entre las que se encuentran personas con diferentes porcentajes de sordera, intérpretes y personas que trabajan dentro de los sectores de salud y educación. La dificultad en el aprendizaje de este lenguaje así como la variedad de signos que dependen tanto del idioma, del país e incluso de las regiones es un obstáculo en la masificación de su uso y correcta interpretación. 
El público objetivo al que está dirigido el presente trabajo son estudiantes, profesores, profesionales y cualquier persona interesada en aprender el lenguaje de señas.


## Tecnologías Utilizadas

MediaPipe: Herramienta de Google para la detección de puntos clave en tiempo real.

Python: Lenguaje de programación principal.

OpenCV: Biblioteca para el procesamiento de imágenes y video.

Scikit-learn: Biblioteca para la construcción de modelos de aprendizaje automático.

Numpy: Biblioteca para el cálculo numérico

Xgboost: Biblioteca de machine learning optimizada que se utiliza para tareas de clasificación y regresión. Se basa en el algoritmo de gradient boosting, que construye modelos predictivos a partir de un conjunto de árboles de decisión de manera iterativa.

## Requisitos Previos

Antes de comenzar con la implementación, debemos realizar la instalación de python versión Python 3.9.0.

## Instalación de dependencias
1. Clonar el repositorio e ingresar a la carpeta del proyecto
cd Lenguaje-de-senas-Multimodales

2. Crear un entorno virtual
python -m venv venv
En Windows: venv\Scripts\activate

3. Instalar dependencias

python.exe -m pip install --upgrade pip
pip install opencv-python mediapipe scikit-learn numpy
pip install xgboost


## Pasos para ejecutar el proyecto

1. Capturar datos

Ejecutar el archivo: python coleccion.py

El primer paso tiene como objetivo capturar datos de las letras del alfabeto en lenguaje de señas. Ejecuta el script collect_imgs.py para recoger imágenes de las letras:

- Inicializa MediaPipe Hands y la cámara utilizando OpenCV.
- Captura 100 imágenes de cada letra del abecedario, almacenándose en carpetas separadas.
- Muestra instrucciones para cambiar a la siguiente letra después de completar la captura de imágenes.

2. Capturar datos

Ejecutar el archivo: python creacion_dts.py

El objetivo es organizar las imágenes capturadas en un formato adecuado para el entrenamiento del modelo.

3. Entrenar el modelo

Ejecutar el archivo: python entrenamiento.py

Este script utilizará las imágenes capturadas para entrenar un modelo de clasificación.


4. Ejecución y predicción en tiempo real

Ejecutar el archivo: python ejecucion.py

Realizará predicciones en tiempo real mediante la utilización de la cámara:

Mediante el algoritmo utilizará el modelo entrenado para reconocer y mostrar la letra correspondiente en tiempo real.