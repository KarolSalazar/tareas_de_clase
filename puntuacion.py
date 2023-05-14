from string import punctuation
import random
 
"""
def palabra_a_vector(palabra):
    for i in punctuation:
        palabra = palabra.replace(i, "")
    tildes = "áéíóúÁÉÍÓÚ"
    for i in range(len(tildes)):
        palabra = palabra.replace(tildes[i], "áéíóúÁÉÍÓÚ"[i])
    palabra = palabra.split()
    vector = []
    for i in palabra:
        vector.append(len(i))
    return(vector)
"""

def palabras_a_vectores(lista_palabras):
    vectores = []
    for palabra in lista_palabras:
        for i in punctuation:
            palabra = palabra.replace(i, "")
        tildes = "áéíóúÁÉÍÓÚ"
        for i in range(len(tildes)):
            palabra = palabra.replace(tildes[i], "aeiouAEIOU"[i])
        vector = []
        vector.append(len(palabra))
        vectores.append(vector)
    return vectores

#Aquí puedes cambiar la frase

palabras = ["hola", "cómo", "estás"]
vectores = palabras_a_vectores(palabras)
print(vectores)


def matriznxn(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(random.randint(1, 10))
        matriz.append(fila)
    return matriz

def ordenar_indices(vector):
    indices = []
    for j in range(len(vector)):
        indices.append(j)
    for i in range(len(vector)):
        for j in range(len(vector)):
            if vector[j] < vector[i]:
                vector[j], vector[i] = vector[i], vector[j]
                indices[j], indices[i] = indices[i], indices[j]
    return indices

vector = [5, 10, 2, 8, 3, 7]
print(vector)
indices = ordenar_indices(vector)
print(indices)