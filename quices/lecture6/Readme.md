# Semana 6 — Clasificación y flujo de Machine Learning

## Descripción

Esta carpeta reúne las actividades de la semana 6 del curso de
**Inteligencia Artificial**.

Esta semana trabajamos la preparación y exploración de datos,
el entrenamiento de modelos de clasificación, la validación cruzada
y la evaluación final. También revisamos los árboles de decisión
y las etapas de un proyecto de Machine Learning.

## Autor

**Isabella Cadavid Posada**  
Estudiante de Ingeniería de Sistemas

## Notebooks

El challenge utiliza el dataset Wine para clasificar tres clases
a partir de sus características numéricas.

| Actividad | Descripción | Enlace |
|---|---|---|
| Preparación de datos | Revisión de calidad, exploración y separación de entrenamiento y prueba. | [Notebook 1](challenge/01_data_challenge.ipynb) |
| Entrenamiento | Comparación de regresión logística, KNN y árbol de decisión mediante validación cruzada. | [Notebook 2](challenge/02_training_challenge.ipynb) |
| Evaluación y despliegue | Evaluación del modelo campeón, análisis de errores, validación de entradas y predicciones por lotes. | [Notebook 3](challenge/03_evaluation_deployment_challenge.ipynb) |

## Material de clasificación

| Recurso | Descripción | Enlace |
|---|---|---|
| Árbol de clasificación | Material interactivo para comprender los árboles de decisión. | [classification_tree.html](classification/classification_tree.html) |
| Guía de Machine Learning | Explicación de las etapas del flujo de trabajo. | [ml_pipeline_guide.html](classification/ml_pipeline_guide.html) |

Para utilizar los recursos interactivos, descarga los archivos HTML
y ábrelos en un navegador.

## Datos y resultados

| Contenido | Enlace |
|---|---|
| Datos originales | [data/raw](challenge/data/raw/) |
| Datos de entrenamiento y prueba | [data/processed](challenge/data/processed/) |
| Reportes generados | [reports](challenge/reports/) |
| Modelo y archivos de configuración | [artifacts](challenge/artifacts/) |
| Modelo campeón | [champion_model.joblib](challenge/artifacts/champion_model.joblib) |
| Contrato de datos | [data_contract.json](challenge/artifacts/data_contract.json) |
| Metadatos del entrenamiento | [training_metadata.json](challenge/artifacts/training_metadata.json) |

## Resultados principales

| Elemento | Resultado |
|---|---|
| Modelo campeón | LogisticRegression |
| Mejor parámetro | C = 1.0 |
| Accuracy promedio de validación cruzada | 97.91 % |
| Accuracy de prueba | 97.22 % |
| F1 macro de prueba | 0.9710 |
| Principal confusión | Una imagen de datos de la clase 2 fue clasificada como clase 1. |

El conjunto de prueba contiene 36 registros, por lo que las métricas
deben interpretarse considerando su tamaño.

## Lo que aprendí

Aprendí a revisar los datos antes de entrenar, comparar modelos
mediante validación cruzada y seleccionar un modelo considerando
su desempeño, variabilidad y complejidad.

También comprendí que la accuracy debe complementarse con métricas
por clase y una matriz de confusión, y que el conjunto de prueba
no debe utilizarse para ajustar los hiperparámetros.