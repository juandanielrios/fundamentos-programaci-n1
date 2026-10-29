while True:
    print("====Calculadora====")
    print("Elija una operación")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("ingrese una opción: "))

    if opcion == 5:
        print("gracias por usar la calculadora")
        break
    elif opcion != 1 and opcion != 2 and opcion != 3 and opcion !=4:
        print("Opcion invalida, por favor ingrese una opción válida")
        break

    num1 = float(input("ingrese numero 1:"))
    num2 = float(input("ingrese numero 1:"))

    if opcion == 1:
        resultado = num1 + num2
        print(f"la suma de estos valores es {resultado}")
    elif opcion == 2:
        resultado = num1 - num2
        print(f"la resta de estos valores es {resultado}")
    elif opcion == 3:
        resultado = num1 * num2
        print(f"la multiplicacion de estos valores es {resultado}")
    elif opcion == 4:
        if num2 == 0:
            print("Error, no se puede dividir por 0")
        else:
            resultado = num1 / num2
            print(f"la divsion entre estos valores es {resultado}")
    