# Proyecto de Morosidad Bancaria — Ciencia de Datos

Este repositorio contiene el **proyecto completo de análisis de morosidad crediticia**, desarrollado en Python, Power BI y herramientas de IA.  
Su objetivo es **predecir la probabilidad de que un cliente incurra en mora** mediante el uso de modelos supervisados, y generar automáticamente reportes visuales e informes ejecutivos.

---

## Estructura del proyecto

| Carpeta / Archivo | Descripción |
|--------------------|-------------|
| **proyecto_morosidad.ipynb** | Cuaderno principal de análisis y modelamiento en Python. Incluye limpieza de datos, balanceo con SMOTE, entrenamiento de modelos (Regresión Logística, Árbol de Decisión, Bosque Aleatorio) y evaluación con métricas AUC-ROC, F1 y precisión. |
| **Funciones.py** | Contiene las funciones auxiliares para la conexión con la base de datos SQLite, limpieza automática de los datos y creación de las tablas `train`, `test` y `sample`. |
| **prompt.py** | Archivo que utiliza la **API de OpenAI o Groq** para generar automáticamente análisis de texto y descripciones basadas en los resultados. Permite crear reportes automáticos y resúmenes ejecutivos en texto plano o integrarlos con PowerPoint. |
| **morosidad.pbix** | Archivo de **Power BI** con las visualizaciones del proyecto: distribución de morosos, ingresos promedio, dispersión edad-ingreso y ranking de variables más influyentes. |
| **Powerpoint.py** | Script que genera automáticamente un **PowerPoint con los resultados y gráficos de Power BI**, mediante integración con la API del asistente de IA. |
| **Carpeta PowerBI_image/** | Contiene las imágenes exportadas automáticamente desde Power BI que son utilizadas en la generación del informe PowerPoint. |
| **Comentarios.txt** | Archivo que documenta brevemente las secciones del cuadernillo, indicando en qué líneas de código se encuentra cada función o análisis. |
| **PushBot / push.bat** | Script estándar para automatizar la subida del repositorio a GitHub. Permite hacer un `git add`, `commit` y `push` automáticamente con un solo clic. |

---


Descripción general del proyecto

El proyecto **“Análisis de Morosidad Bancaria”** busca determinar los factores socioeconómicos y financieros que influyen en la probabilidad de que un cliente entre en mora.  
Se realiza mediante las siguientes etapas:

1. **Preprocesamiento:** limpieza de valores nulos, codificación y balanceo con SMOTE.  
2. **Modelamiento:** comparación entre modelos supervisados (`Regresión Logística`, `Árbol de Decisión`, `Bosque Aleatorio`).  
3. **Evaluación:** métricas de rendimiento (Precisión, Recall, F1-score y AUC-ROC).  
4. **Visualización:** análisis de resultados en Power BI.  
5. **Automatización:** generación automática de reportes con IA (prompt.py + Powerpoint.py).  

---

## Cómo usar la API (Groq / OpenAI)

1. Crea un archivo `.env` en la raíz del proyecto con tu clave:
   ```bash
   GROQ_API_KEY="tu_clave_aqui"
2.response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="Analiza la base de datos de morosidad y sugiere visualizaciones...")
    El resultado del analisis automatico se guarda 
    PowerBI/insight_openai.txt
3.Automatizacion con push.bat
    En el archivo ya estan los comandos ya establecidos para que se guarde los cambios del proyecto a github
    solo al llamar .\push.bat en el bash


