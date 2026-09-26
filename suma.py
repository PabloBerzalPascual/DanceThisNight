# suma.py

def suma(a, b):
    return a + b

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python suma.py <num1> <num2>")
        sys.exit(1)
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Both arguments must be numbers.")
        sys.exit(1)
    result = suma(num1, num2)
    print(f"Resultado: {result}")
