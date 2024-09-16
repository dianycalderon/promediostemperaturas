import random

# Inicializar los datos de ejemplo
ciudades = ["Quito", "Guayaquil", "Manta"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4


# Inicializar la matriz 3D con datos aleatorios de temperaturas
def generar_temperaturas(ciudades, dias, semanas):
    """
    Genera una matriz tridimensional de temperaturas aleatorias para ciudades, días y semanas.

    Parámetros:
    ciudades (list): Lista de nombres de ciudades.
    dias (list): Lista de nombres de días de la semana.
    semanas (int): Número de semanas.

    Devuelve:
    list: Matriz tridimensional con temperaturas aleatorias.
    """
    return [[[random.uniform(15.0, 35.0) for _ in range(semanas)] for _ in range(len(dias))] for _ in
            range(len(ciudades))]


# Función para calcular la temperatura promedio
def calcular_promedio_ciudad(temperaturas, ciudades, ciudad_buscada):
    """
    Calcula la temperatura promedio de una ciudad durante un período de tiempo.

    Parámetros:
    temperaturas (list): Matriz tridimensional con temperaturas.
    ciudades (list): Lista de nombres de ciudades.
    ciudad_buscada (str): Nombre de la ciudad para calcular el promedio.

    Devuelve:
    float: Promedio de temperatura para la ciudad especificada.
    """
    if ciudad_buscada not in ciudades:
        raise ValueError("Ciudad no encontrada.")

    index_ciudad = ciudades.index(ciudad_buscada)

    suma_temperaturas = 0
    conteo_dias = len(dias) * semanas

    for dia in range(len(dias)):
        for semana in range(semanas):
            suma_temperaturas += temperaturas[index_ciudad][dia][semana]

    promedio = suma_temperaturas / conteo_dias
    return promedio


# Ejemplo de uso
if __name__ == "__main__":
    temperaturas = generar_temperaturas(ciudades, dias, semanas)

    ciudad_input = input("Introduce el nombre de la ciudad (e.g., Ciudad1): ")

    try:
        promedio = calcular_promedio_ciudad(temperaturas, ciudades, ciudad_input)
        print(f"El promedio de temperatura en {ciudad_input} es: {promedio:.2f}°C")
    except ValueError as e:
        print(e)

