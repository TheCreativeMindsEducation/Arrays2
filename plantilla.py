def read_numbers():
    """
    Lee números desde stdin hasta que se introduce una línea vacía.
    Almacena los números en una lista y la devuelve.

    Returns:
        list: Una lista de números leídos.
    """
    numbers = []
    print("Introduce números (uno por línea). Deja una línea vacía para terminar:")

    while True:
        try:
            line = input()
            if not line.strip():  # Termina al recibir una línea vacía
                break
            number = float(line)  # Convertir a número (float o int según lo que necesites)
            numbers.append(number)
        except ValueError:
            print("Entrada no válida. Introduce un número válido.")

    return numbers

# Ejemplo de uso
if __name__ == "__main__":
    numbers = read_numbers()
    print("Números leídos:", numbers)
