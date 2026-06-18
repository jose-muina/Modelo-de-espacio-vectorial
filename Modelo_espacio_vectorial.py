import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Documentos sobre animales
documents = {
    "doc1": "El veloz zorro marrón salta sobre el perro perezoso.",
    "doc2": "Un perro marrón persiguió al zorro.",
    "doc3": "El perro es perezoso."
}

# Convertir documentos a vectores usando TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents.values())

# Calcular la similitud del coseno entre los documentos
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Graficar la matriz de similitud
labels = list(documents.keys())

plt.figure(figsize=(6, 5))
sns.heatmap(
    cosine_sim,
    annot=True,
    fmt=".2f",
    cmap="Blues",
    xticklabels=labels,
    yticklabels=labels,
)
plt.title("Matriz de Similitud del Coseno")
plt.show()