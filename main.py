print("Bienvenido a la calculadora mas simple del mundo.")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "No se puede dividir por 0"
    return a / b

while True:
    try:
        num_1 = int(input("Ingrese el primer nro: "))
        if num_1 > 0 or num_1 <= 0:
            break
    except ValueError:
        print("Dato invalido.")
while True:
    try:
        num_2 = int(input("Ingrese el segundo nro: "))
        if num_2 > 0 or num_2 <= 0:
            break
    except ValueError:
        print("Dato invalido.")
while True:
    try:
        operacion = input("Ingrese una operación aritmética básica (suma, resta, mult, div): ").lower()
        if operacion in ("mult", "div", "suma", "resta"):
            break
    except ValueError:
        print("Dato invalido.")

if operacion == 'suma':
    print("El resultado es: ")
    print(suma(num_1, num_2))
    print("Gracias por utilizar el programa...\nAdiós.")
elif operacion == 'resta':
    print("El resultado es: ")
    print(resta(num_1, num_2))
    print("Gracias por utilizar el programa...\nAdiós.")
elif operacion == 'mult':
    print("El resultado es: ")
    print(mult(num_1, num_2))
    print("Gracias por utilizar el programa...\nAdiós.")
elif operacion == 'div':
    print("El resultado es: ")
    print(div(num_1, num_2))
    print("Gracias por utilizar el programa...\nAdiós.")
else:
    print("Operacion inválida")