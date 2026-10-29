#Codigo Calculadora corredigo en calse

#calculadora con Match Case

while True:
    print("====Calculadora====")
    print("Elija una operación")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Ingrese la opción deseada: "))

    if opcion == 5:
        print("gracias por usar la calculadora")
        break
    elif opcion < 1 or opcion >5:
         print("Opcion invalida, por favor ingrese una opción válida")
         break

    num1 = float(input("ingrese numero 1: "))
    num2 = float(input("ingrese numero 2: "))



    match opcion:
        case 1:
            resultado = num1 + num2
            print(f"la suma de estos valores es {resultado}")

        case 2:
            resultado = num1 - num2
            print(f"la resta de estos valores es {resultado}")

        case 3:
            resultado = num1 * num2
            print(f"la multiplicacion de estos valores es {resultado}")

        case 4:
            if num2 != 0:
                resultado = num1 / num2
                print(f"la division de estos valores es {resultado}")
            else: print("Error, no se puede dividir por 0")





