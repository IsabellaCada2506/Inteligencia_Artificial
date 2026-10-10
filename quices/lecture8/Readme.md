# Semana 8 — Transfer Learning y detección de objetos

## Descripción

Esta carpeta reúne las actividades de la semana 8 del curso de
**Inteligencia Artificial**.

Esta semana trabajamos las redes neuronales convolucionales,
el aprendizaje por transferencia, el fine-tuning y la detección
de objetos con YOLO.

## Autor

**Isabella Cadavid Posada**  
Estudiante de Ingeniería de Sistemas

## Transfer Learning

| Notebook | Descripción | Enlace |
|---|---|---|
| Transfer Learning con Keras 3 | Uso de VGG16 preentrenada para clasificar gatos y perros mediante extracción de características y fine-tuning. | [Ver notebook](transfer_learning/CNN_Transfer_Keras3.ipynb) |
| Taller con datos propios | Construcción de un dataset de bicicletas, buses y motocicletas; entrenamiento con EfficientNetB0 y análisis de resultados. | [Ver taller](transfer_learning/taller_transfer_learning_datos_propios_keras3.ipynb) |

## YOLO

| Notebook | Descripción | Enlace |
|---|---|---|
| Introducción a YOLO | Inferencia con un modelo preentrenado, visualización de detecciones y prueba con una imagen propia. | [Ver introducción](yolo/Lecture_08_Yolo_Intro.ipynb) |
| Entrenamiento con fútbol | Entrenamiento de YOLO con un dataset de detección de jugadores de fútbol descargado desde Roboflow. | [Ver entrenamiento](yolo/Lecture_08_Yolo_training.ipynb) |
| Entrenamiento con SiteSafety | Entrenamiento de YOLO con el proyecto SiteSafety configurado en el notebook. | [Ver notebook](yolo/Lecture_08_Yolo_training_own_data.ipynb) |

## Material complementario

| Carpeta | Contenido | Enlace |
|---|---|---|
| Imágenes | Imagen de ejemplo utilizada en la introducción a YOLO. | [images](yolo/images/) |
| Deployment | Ejemplos de aplicaciones para detección en video, cámara y uso mediante una API. | [deployment](yolo/deployment/) |

## Temas trabajados

- Redes neuronales convolucionales.
- Modelos preentrenados en ImageNet.
- Extracción de características y base congelada.
- Fine-tuning con una tasa de aprendizaje pequeña.
- Preparación, revisión y separación de imágenes.
- Data augmentation y evaluación por clase.
- Detección de objetos con YOLO.
- Bounding boxes y umbrales de confianza.
- Entrenamiento con datasets de Roboflow.

## Cómo revisar las actividades

Los notebooks contienen el código, las salidas y los análisis.
Para ejecutarlos, ábrelos en Google Colab y corre las celdas en orden.
Se recomienda utilizar GPU para los entrenamientos.

Los notebooks de entrenamiento de YOLO requieren una API key
de Roboflow, que se ingresa durante la ejecución y no se incluye
en el repositorio.

## Lo que aprendí

Aprendí a reutilizar el conocimiento de un modelo preentrenado
y a distinguir entre entrenar un clasificador con la base congelada,
hacer fine-tuning y entrenar una red desde cero.

También comprendí la importancia de revisar la calidad de las
imágenes y evaluar los resultados con métricas por clase.

Con YOLO aprendí que detectar objetos implica identificar su clase
y ubicación dentro de una imagen, y que el umbral de confianza
cambia qué detecciones se muestran.