# Semana 7 — Redes neuronales con Keras 3

## Descripción

Esta carpeta reúne las actividades de la semana 7 del curso de
**Inteligencia Artificial**.

Esta semana estudiamos las redes neuronales densas, las funciones
de activación, el entrenamiento y la evaluación de modelos para
clasificar imágenes con Keras 3.

## Autor

**Isabella Cadavid Posada**  
Estudiante de Ingeniería de Sistemas

## Contenido

| Notebook | Descripción | Enlace |
|---|---|---|
| Fashion-MNIST | Introducción a la clasificación de prendas mediante regresión logística y una red neuronal densa. | [Ver notebook](YourFirstDeepNN_FashionMNIST_Keras3.ipynb) |
| CIFAR-10 en escala de grises | Clasificación de imágenes de 10 clases con una red densa y análisis de sus resultados. | [Ver notebook](Challenge_Keras3_CIFAR10_Grayscale.ipynb) |
| Olivetti Faces | Clasificación de rostros y reflexión sobre el sobreajuste cuando hay pocos ejemplos. | [Ver notebook](Challenge_Keras3_OlivettiFaces.ipynb) |

## Temas trabajados

- Preparación de imágenes y normalización de píxeles.
- Conversión de imágenes a vectores con `Flatten`.
- Capas `Dense` y activación `ReLU`.
- Logits, probabilidades y función `Softmax`.
- Función de pérdida y optimizador.
- Épocas y tamaño de los lotes.
- Curvas de entrenamiento y validación.
- Evaluación de predicciones y sobreajuste.

## Cómo revisar las actividades

Abre cada notebook para consultar el código, las salidas y las
respuestas. Para ejecutarlo, ábrelo en Google Colab y corre las
celdas en orden.

## Lo que aprendí

Aprendí cómo una red neuronal transforma los píxeles de una imagen
en predicciones y qué función cumplen sus capas, activaciones
y parámetros de entrenamiento.

También comprendí que un buen resultado en entrenamiento no
garantiza un buen desempeño en imágenes nuevas. Las curvas de
validación y el análisis de errores ayudan a identificar las
limitaciones del modelo.

Finalmente, entendí que las imágenes tienen una estructura espacial
que las redes convolucionales pueden aprovechar directamente.