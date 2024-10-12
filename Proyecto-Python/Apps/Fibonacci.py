# Función para generar la serie de Fibonacci hasta un número dado de términos
def fibonacci(n):
    # Los dos primeros términos de la serie
    a, b = 0, 1
    for _ in range(n):
        # Imprime el siguiente término de la serie
        print(a, end=' ')
        # Calcula el siguiente término
        a, b = b, a + b
    print()

# Solicita al usuario la cantidad de términos que desea generar
num_terminos = int(input("Introduce la cantidad de términos de la serie de Fibonacci: "))

# Llama a la función para generar y mostrar la serie de Fibonacci
fibonacci(num_terminos)