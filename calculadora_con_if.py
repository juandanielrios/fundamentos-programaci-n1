print("====Calculadora====")
print("Elija una operación")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")

opcion = int(input("Ingrese la opción deseada: "))

if opcion == 1:
    num1 = float(input("ingrese primer numero:"))
    num2 = float(input("igrese segundo numero:"))
    resultado = num1 + num2
    print("la suma de estos valores es", resultado)
elif opcion == 2:
    num1 = float(input("ingrese primer numero:"))
    num2 = float(input("igrese segundo numero:"))
    resultado = num1 - num2
    print("la resta de estos valores es", resultado)
elif opcion == 3:
    num1 = float(input("ingrese primer numero:"))
    num2 = float(input("igrese segundo numero:"))
    resultado = num1 * num2
    print("la multiplicacion de estos valores es", resultado)
elif opcion == 4:
    num1 = float(input("ingrese primer numero:"))
    num2 = float(input("igrese segundo numero:"))
    if num2 == 0:
        print("Error, no se puede dividir por 0")
    else:
        resultado = num1 / num2
        print("la division de estos valores es", resultado)  
elif opcion == 5:
    print("Saliendo de la calculadora")
else:
    print("Opcion invalida, por favor ingrese una opción válida")