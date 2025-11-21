
# ---------------------------------------------------------
# 1. Carga y limpieza de datos
# ---------------------------------------------------------

# Explicación:
# Aquí se importan los archivos originales y se limpian las 
# variables, corrigiendo tipos, eliminando nulos y creando 
# columnas formateadas.

# Ir al código:
# data loading → funciones de limpieza
# archivo: Funciones.py línea 1
# ruta: ./Funciones.py:1


# ---------------------------------------------------------
# 2. Construcción de la base SQLite
# ---------------------------------------------------------

# Explicación:
# Se toma la información de los excels originales y se genera 
# automáticamente la base de datos data.sqlite con las tablas:
# - train
# - test
# - sample
# - all_data

# Ir al código:
# archivo: Funciones.py línea 45
# ruta: ./Funciones.py:45


# ---------------------------------------------------------
# 3. Análisis Exploratorio (EDA)
# ---------------------------------------------------------

# Incluye histogramas, boxplots y correlaciones generadas en:
# archivo: proyecto_morosidad.ipynb (sección EDA)

# Ruta sugerida:
# ./proyecto_morosidad.ipynb (buscar “Distribución”)

# Gráfico 1: Distribución de morosidad
# proyecto_morosidad.ipynb → línea 80


# ---------------------------------------------------------
# 4. Preprocesamiento del modelo
# ---------------------------------------------------------

# Contiene:
# - Imputación
# - SMOTE (balanceo)
# - Estandarización
# archivo: proyecto_morosidad.ipynb línea 140
# ruta: ./proyecto_morosidad.ipynb:140


# ---------------------------------------------------------
# 5. Entrenamiento de Modelos
# ---------------------------------------------------------

# Modelos:
# - Regresión Logística
# - Árbol de Decisión
# - Bosque Aleatorio

# Entrenamiento de todos los modelos:
# archivo: proyecto_morosidad.ipynb línea 200
# ruta: ./proyecto_morosidad.ipynb:200


# ---------------------------------------------------------
# 6. Curvas ROC comparativas
# ---------------------------------------------------------

# Aquí se generan las curvas ROC y se calculan los AUC.
# archivo: proyecto_morosidad.ipynb línea 240
# ruta: ./proyecto_morosidad.ipynb:240


# ---------------------------------------------------------
# 7. Selección del mejor modelo
# ---------------------------------------------------------

# Se escoge el modelo con mayor AUC (generalmente Random Forest)
# archivo: proyecto_morosidad.ipynb línea 290
# ruta: ./proyecto_morosidad.ipynb:290


# ---------------------------------------------------------
# 8. Generación de tabla para Power BI
# ---------------------------------------------------------

# Aquí se crean:
# - Probabilidades del modelo
# - Predicciones
# - Score de riesgo
# - Clasificación por riesgo
# archivo: test_modelado (sección PowerBI)
# ruta: ./proyecto_morosidad.ipynb:330


# ---------------------------------------------------------
# 9. Medidas DAX automáticas
# ---------------------------------------------------------

# Exportadas en:
# ruta: PowerBI/powerbi_medidas_dax.txt


# ---------------------------------------------------------
# 10. Exportación del PPT automático
# ---------------------------------------------------------

# Archivo:
# - Informe_Morosidad.pptx
# Ruta:
# ./PowerBI/Informe_Morosidad.pptx

# Código generador:
# archivo: powerpoint.py
# ruta: ./powerpoint.py:1
