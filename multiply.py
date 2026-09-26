# file: multiply.py

"""Script de multiplicación.

Este script define una función `multiplicar` que recibe dos números y devuelve
su producto. Además, incluye un bloque de ejecución principal que permite al
usuario introducir dos valores por consola y muestra el resultado.
"""

def multiplicar(a, b):
    """Devuelve el producto de a y b.

    Parameters
    ----------
    a : int | float
        Primer número.
    b : int | float
        Segundo número.

    Returns
    -------
    int | float
        El resultado de a * b.
    """
    return a * b

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Uso: python multiply.py <num1> <num2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Los argumentos deben ser números.")
        sys.exit(1)

    resultado = multiplicar(num1, num2)
    print(f"El resultado de {num1} * {num2} es {resultado}")
