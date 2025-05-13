import math

def obtener_operacion():
    operaciones_validas = ["+", "-", "*", "/", "%", "^", "F", "R", "PI"]
    while True:
        operacion = input("¿Qué operación quiere hacer? (+, -, *, /, %, ^, F, R, PI): ").upper()
        if operacion in operaciones_validas:
            return operacion
        print("Operación inválida. Intente de nuevo.")

def calcular(operacion):
    if operacion == "PI": 
        return math.pi

    if operacion == "F":
        numero = int(input("Ingrese un número entero positivo: "))
        return math.factorial(numero)

    if operacion == "R":
        numero = float(input("Ingrese el número para obtener la raíz cuadrada: "))
        return math.sqrt(numero)

    cantidad = int(input("¿Cuántos números desea usar?: "))
    numeros = [float(input(f"Ingrese el número {i+1}: ")) for i in range(cantidad)]

    resultado = numeros[0]
    for num in numeros[1:]:
        if operacion == "+":
            resultado += num
        elif operacion == "-":
            resultado -= num
        elif operacion == "*":
            resultado *= num
        elif operacion == "/":
            resultado /= num
        elif operacion == "%":
            resultado %= num
        elif operacion == "^":
            resultado **= num
    return resultado

def main():
    while True:
        print("\nCalculadora Básica")
        op = obtener_operacion()
        try:
            resultado = calcular(op)
            print("Resultado:", resultado)
        except Exception as e:
            print("Error:", e)

        seguir = input("¿Desea realizar otra operación? (s/n): ").lower()
        if seguir != 's':
            print("Gracias por usar la calculadora.")
            break

if __name__ == "__main__":
    main()
