#Calculadora de FREY

def calculadora():
    while True:
        print("\n ===CALCULADORA===\n  Elija un Opcion")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        try:
            opcion = int(input("Ingrese una opción: "))
        
            if opcion == 5:
                print("Saliendo...\ngracias por usar la calculadora")
                break
            
            elif opcion not in(1,2,3,4):
                print("Opción no valida, selecciona otra opción")
                continue

        
            numero1 = float(input("ingrese el primer numero: "))
            numero2 = float(input("ingrese el primer numero: "))

            if opcion == 1:
                resultado = numero1 + numero2

            elif opcion == 2:
                resultado = numero1 - numero2

            elif opcion == 3:
                resultado = numero1 * numero2

            elif opcion == 4:
                if numero2 == 0:
                    print("Error, no se puede divir por cero")
                    continue
                else:
                    resultado = numero1 / numero2
            print("Resultado: ",resultado)

        except ValueError:
            print("Error: debe ingresar valores numericos")


calculadora()

