

# NLP - Natural Language Processing Repository

Este repositorio contiene las prácticas realizadas durante el curso de Procesamiento de Lenguaje Natural (NLP), incluyendo los **assignments** de las sesiones y un **proyecto final** que aplica los conocimientos adquiridos. 

## Contenido

1. **Assignments**: Prácticas individuales de diferentes técnicas de NLP, cada una enfocada en conceptos como tokenización, lematización, análisis de frecuencia de palabras, entre otros. Cada práctica incluye:
   - Código fuente.
   - Descripción del problema y la solución propuesta.
   - Conclusiones.

2. **Proyecto Final**: El análisis detallado de un conjunto de datos compuesto por textos generados por humanos y por inteligencia artificial (IA), con el objetivo de diferenciar entre ambos. A continuación se describe en detalle.

---

## Proyecto Final: Análisis de Textos Generados por IA vs Humanos

### Introducción

El proyecto final consiste en aplicar técnicas de NLP para analizar un **dataset** que contiene ensayos generados por humanos y textos creados por IA. El objetivo principal es estudiar las diferencias lingüísticas entre ambos tipos de textos y entrenar un modelo capaz de predecir el origen de un texto (humano o IA).

El dataset utilizado puede encontrarse en [este enlace de Kaggle](https://www.kaggle.com/datasets/shanegerami/ai-vs-human-text/data).

### Objetivos

El análisis del dataset se enfoca en los siguientes aspectos:
- Riqueza léxica
- Palabras preferidas
- Longitud promedio de las palabras
- Palabras más y menos frecuentes
- Implementación de un modelo de **Regresión Logística** y una **Red Neuronal Convolucional (CNN)** para clasificar los textos.

### Preprocesamiento de Datos

- El dataset fue dividido en un **60%** para entrenamiento, **20%** para validación y **20%** para pruebas.
- Se seleccionaron al azar **25,000 elementos**, manteniendo una distribución balanceada entre textos humanos y de IA.
- Se eliminaron palabras comunes y de poco valor informativo (stop words).

### Análisis Léxico y Estadístico

1. **Riqueza Léxica**: 
   - La IA mostró una mayor diversidad léxica en los textos originales (0.45 frente a 0.43 para humanos), pero tras eliminar las stop words, los textos humanos exhibieron una mayor riqueza (0.899 frente a 0.877 para la IA).
   
2. **Palabras Preferidas**:
   - Los análisis mostraron una notable similitud en las palabras más utilizadas por humanos y IA, compuestas principalmente por stop words. Sin embargo, al eliminarlas, surgieron diferencias significativas entre los dos tipos de texto.

3. **Longitud Promedio de Palabras**:
   - Las palabras más frecuentes en los textos de IA tienden a ser más largas que en los textos humanos, lo que sugiere un uso más técnico y específico por parte de la IA.

### Clasificación y Predicción

Se implementaron dos modelos de clasificación:

1. **Regresión Logística**: Se entrenó un modelo utilizando características como:
   - Longitud de texto.
   - Porcentaje de stop words y palabras de enlace.
   - Frecuencia de palabras comunes.
   
   Los resultados mostraron métricas de precisión, recall y F1-score aceptables, con una distinción clara entre los textos generados por humanos y por IA.

2. **Red Neuronal Convolucional (CNN)**: 
   - Se utilizó un modelo CNN para mejorar la clasificación. Este modelo fue entrenado con capas de convolución y pooling de TensorFlow, obteniendo mejores resultados en términos de precisión y consistencia.
   
   La validación del modelo se realizó utilizando un **20%** del dataset, y se logró un buen ajuste entre las predicciones del modelo y los resultados reales.

### Conclusiones

El proyecto final muestra cómo las técnicas de procesamiento de lenguaje natural pueden utilizarse para distinguir entre textos generados por IA y humanos, basándose en la riqueza léxica, la estructura de las palabras y otros patrones lingüísticos. Además, la implementación de modelos de aprendizaje automático, como la regresión logística y redes neuronales, ofrece una forma efectiva de predecir el origen de los textos.

---

## Instrucciones de Uso

1. Clona este repositorio:
   ```bash
   git clone https://github.com/RubaGarcia/NLP.git
   ```
2. Accede a la carpeta del proyecto:
   ```bash
   cd NLP
   ```
3. Revisa los scripts de los **assignments** para ejemplos básicos de técnicas de NLP.
4. Para ejecutar el proyecto final, sigue las instrucciones en el archivo `proyecto_final.ipynb`.

---

## Autores

- **Rubén García**
- **Javier Mier**

Curso 2023/2024
