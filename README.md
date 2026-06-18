# Modelo de Espacio Vectorial
Implementacion de un motor de busqueda por similitud sobre una coleccion  de documentos en español usando el modelo de espacio vectorial.

## ¿Qué hace?

- Convierte documentos de texto en vectores numéricos usando TF-IDF
- Calcula la similitud del coseno entre todos los pares de documentos
- Visualiza los resultados como un mapa de calor (heatmap)

## ¿Para qué sirve?

El modelo de espacio vectororial permite medir qué tan parecidos son 
dos documentos en base a los términos que comparten. Un valor cercano 
a 1 indica alta similitud y cercano a 0 indica que los documentos 
poseen palabras poco similares.

## Librerías

| Librería | Uso |
|---|---|
| `sklearn` | Vectorización TF-IDF y similitud del coseno |
| `seaborn` / `matplotlib` | Visualización del mapa de calor |
| `numpy` | Manejo de matrices
