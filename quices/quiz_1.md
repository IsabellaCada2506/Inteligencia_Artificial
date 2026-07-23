# Ficha de análisis

## 1. Nombre del Space

**Nombre:** Gemma 4 - Vision Token Budget

**Enlace:** https://huggingface.co/spaces/google/gemma4_vision_token_budget

------------------------------------------------------------------------

## 2. ¿Qué hace el agente?

Este Space me permitió cargar una imagen para que el modelo de inteligencia artificial Gemma 4 la analizara utilizando diferentes niveles de tokens visuales. Su objetivo es mostrar las dimensiones de la imagen y cómo la cantidad de tokens asignados influye en el nivel de detalle con el que el modelo representa y procesa la imagen. Un uso de tokens bajo permite un procesamiento más rápido, mientras que uno más alto conserva mayor información visual, facilitando la identificación de pequeños detalles y mejorando la calidad del análisis.

<img width="630" height="654" alt="image" src="https://github.com/user-attachments/assets/98a40c6c-81bd-44fa-b4d7-2a7c9f84ab26" />

<img width="1420" height="645" alt="image" src="https://github.com/user-attachments/assets/a1a76e98-7dbf-48d3-87e3-c279229ba48f" />


------------------------------------------------------------------------

## 3. Análisis PEAS


| Elemento        | Respuesta                                                                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Performance (Medida de desempeño)**| Analizar correctamente la imagen, representar la mayor cantidad de información visual posible según el nivel de tokens seleccionado y mostrar una representación coherente con las dimensiones y el nivel de detalle esperados|
| **Environment (Entorno)**  | Imágenes cargadas por el usuario y la interfaz de las dimensiones y tokens.                                                                               |
|  **Actuators (Actuadores)**   | Procesar la imagen y mostrar cómo se representa con distintos niveles de tokens visuales.                                              |
|  **Sensors (Sensores)**     | La imagen proporcionada por el usuario y el valor del nivel de tokens seleccionado.                                                   |


------------------------------------------------------------------------

## 4. Clasificación del entorno


| **Propiedad**    | **Clasificación**           | **Justificación**                                                                                                                                                                                                |
| ---------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Observable**   | **Total** | El agente únicamente puede analizar la información presente en la imagen proporcionada. No conoce el contexto completo ni información externa que no aparezca en ella.  |
| **Determinista** | **Sí**                      | Si se utiliza la misma imagen y el mismo presupuesto de tokens visuales, el sistema genera el mismo análisis y representación de la imagen, ya que sigue el mismo proceso de procesamiento.                      |
| **Episódico**    | **Sí**                      | Cada imagen se procesa de forma independiente. El análisis realizado sobre una imagen no influye en el procesamiento de las siguientes imágenes.                                                                 |
| **Estático**     | **Sí**                      | Durante el procesamiento, la imagen permanece fija y no cambia, por lo que el entorno no se modifica mientras el agente realiza el análisis.                                                                     |
| **Discreto**     | **Sí**                      | El agente recibe entradas definidas, como una imagen y un nivel de tokens visuales, y produce una salida específica correspondiente al análisis de esa configuración.                                      |
| **Conocido**     | **Sí**                      | El agente conoce el funcionamiento del entorno porque fue entrenado previamente para procesar imágenes y aplicar el nivel de tokens visuales siguiendo reglas establecidas por el modelo.                  |


------------------------------------------------------------------------

## 5. ¿Qué tipo de programa de agente creen que es?

### **Respuesta: Agente de reflejo simple**

En mi opinión, este Space se puede considerar un **agente de reflejo simple** porque responde de inmediato a lo que el usuario hace. Cuando se carga una imagen y se selecciona un nivel de tokens visuales, el sistema la procesa y muestra el resultado correspondiente. No tiene en cuenta imágenes anteriores ni recuerda lo que se hizo antes; simplemente analiza la imagen que recibe en ese momento y genera el resultado. Por eso considero que actúa como un agente de reflejo simple.

<img width="541" height="584" alt="image" src="https://github.com/user-attachments/assets/adcc1e31-0481-4d80-abc1-5673f85d284b" />

------------------------------------------------------------------------

# Reto adicional

## 1. Totalmente observable, determinista y episódico

[**Space seleccionado:** **Unlimited OCR**](https://huggingface.co/spaces/baidu/Unlimited-OCR)


### Justificación

Escogí Unlimited OCR porque el sistema puede ver toda la información del documento que el usuario carga, por lo que es totalmente observable. También es determinista, ya que si se utiliza el mismo documento el resultado será siempre el mismo. Además, es episódico porque cada documento se procesa por separado y una ejecución no influye en la siguiente.

---

## 2. Parcialmente observable, estocástico y secuencial

[**Space seleccionado:** **Gemma Avatar**](https://huggingface.co/spaces/victor/gemma-avatar)


### Justificación

Escogí Gemma Avatar porque solo conoce la información que el usuario le proporciona durante la conversación, por lo que es parcialmente observable. Es estocástico porque las respuestas pueden variar y no siempre serán exactamente iguales. Además, es secuencial porque cada mensaje influye en el desarrollo de la conversación y en las respuestas posteriores.


-----------------------------------------------
## Ejemplos elaborados por mí
-----------------------------------------------

## 1. Encuentre un Space que sea totalmente observable, determinista y episódico

**Ejemplo:** Un Space que convierte texto a mayúsculas.

**Justificación:**

* **Totalmente observable:** recibe todo el texto de entrada.
* **Determinista:** siempre genera exactamente la misma salida para la misma entrada.
* **Episódico:** cada texto se procesa de forma independiente.

---

## 2. Encuentre un Space que sea parcialmente observable, estocástico y secuencial

**Ejemplo:** Un chatbot conversacional basado en IA.

**Justificación:**

* **Parcialmente observable:** el modelo no conoce toda la información del usuario ni del mundo.
* **Estocástico:** una misma pregunta puede generar respuestas diferentes.
* **Secuencial:** cada respuesta depende del historial de la conversación.

-----------------------------------------------


