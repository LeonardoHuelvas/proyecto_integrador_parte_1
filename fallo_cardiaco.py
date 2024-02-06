from datasets import load_dataset
import numpy as np

# Cargamos el dataset dado en plataforma
dataset = load_dataset("mstz/heart_failure")

# accedemos a todos los registos indexando por esa partición train
data = dataset["train"]

# Llamamos la lista de edades
edades = data["age"]
# Convertir la lista de edades a un arreglo de numpy
edades_np = np.array(edades)
# Acá se salcula el promedio de edades de edad que es de tipo float
promedio_edad = edades_np.mean()
# redondeamos el flotante al entero más cercano  que obtenemos de promedoi_edad
promedio_edad_redondeado = round(promedio_edad)

# Aquí imprimimos los resultados obtenidos de cada ejercicio 
print(f"\nLista de edades:\n {edades}")
print(f"\nArreglo de Numpy:\n {edades_np}")
print(f"\nEl Promedio de edad es: {promedio_edad_redondeado} años")
