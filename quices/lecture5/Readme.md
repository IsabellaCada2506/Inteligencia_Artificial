# Semana 5 — Aprendizaje por Refuerzo

## Descripción

Esta carpeta reúne los materiales y las actividades de la semana 5 del curso de **Inteligencia Artificial**, dedicada al **Aprendizaje por Refuerzo** y al algoritmo **Q-Learning**.

Durante esta semana estudiamos cómo un agente aprende al interactuar con un ambiente, recibir recompensas y actualizar sus decisiones. Aplicamos estos conceptos en **CheeseWorld**, **FrozenLake** y **Taxi**.

---

## Contenido

| Archivo | Descripción | Enlace |
|---|---|---|
| **Guía de CheeseWorld** | Explicación de la interacción agente–ambiente, el retorno descontado, las funciones V y Q y la actualización de Q-Learning. Incluye ejercicios resueltos. | [Ver guía](./reinforcement_learning_cheeseworld.md) |
| **CheeseWorld Q-Learning** | Introducción práctica al aprendizaje de valores Q en un ambiente sencillo. | [Ver notebook](./01_cheeseworld_q_learning.ipynb) |
| **FrozenLake Q-Learning** | Aplicación de Q-Learning para aprender a llegar a la meta evitando los agujeros del ambiente. | [Ver notebook](./02_qlearning_frozenlake.ipynb) |
| **Taxi Q-Learning** | Entrenamiento de un agente para recoger y entregar pasajeros, comparación de su comportamiento y experimentación con epsilon. | [Ver notebook](./03_qlearning_taxi.ipynb) |

---

## Temas vistos esta semana

- Interacción entre el agente y el ambiente.
- Estados, acciones, recompensas y estados terminales.
- Retorno acumulado y factor de descuento.
- Función de valor V y función de valor de acción Q.
- Actualización de Q-Learning: TD target y TD error.
- Exploración y explotación mediante una política epsilon-greedy.
- Entrenamiento y comparación del comportamiento de los agentes.
- Efecto de los parámetros alpha, gamma y epsilon.

---

## Orden de consulta

1. Leer la [guía de CheeseWorld](./reinforcement_learning_cheeseworld.md).
2. Revisar el [notebook de CheeseWorld](./01_cheeseworld_q_learning.ipynb).
3. Continuar con el [notebook de FrozenLake](./02_qlearning_frozenlake.ipynb).
4. Revisar el [notebook de Taxi](./03_qlearning_taxi.ipynb).

Para ejecutar los notebooks, se pueden abrir en **Google Colab** o **Jupyter Notebook** y ejecutar sus celdas en orden.

---

## Lo que aprendí

Esta semana comprendí que un agente aprende a partir de las consecuencias de sus acciones. Aprendí que una buena decisión debe considerar tanto la recompensa inmediata como las recompensas futuras, y que Q-Learning permite actualizar esas estimaciones mediante la experiencia.

También entendí la importancia de equilibrar la exploración y la explotación: el agente necesita probar acciones para descubrir mejores alternativas y aprovechar lo aprendido para completar la tarea.

---

## Autor

**Isabella Cadavid Posada**

Estudiante de Ingeniería de Sistemas
