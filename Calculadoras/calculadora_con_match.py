while True:
  print("====Calculadora====")
  print("Elija una operación")
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Dividir")
  print("5. Salir")
  

  opcion = int(input("Ingrese la opción deseada: "))

  match opcion:
      case 1:
        num1 = float(input("Ingrese primer numero: "))
        num2 = float(input("Ingrese segundo numero: "))
        resultado = num1 + num2
        print(f"la suma de estos valores es {resultado}")
      case 2:
        num1 = float(input("Ingrese primer numero: "))
        num2 = float(input("Ingrese segundo numero: "))
        resultado = num1 - num2
        print(f"la resta de estos valores es {resultado}")

      case 3:
        num1 = float(input("Ingrese primer numero: "))
        num2 = float(input("Ingrese segundo numero: "))
        resultado = num1 * num2
        print(f"la multiplicacion de estos valores es {resultado}")

      case 4:
        num1 = float(input("Ingrese primer numero: "))
        num2 = float(input("Ingrese segundo numero: "))
        if num2 != 0:
          resultado = num1 / num2
        else: print("Error, no se puede dividir por 0")

        print(f"la division de estos valores es {resultado}")
      
      case 5: 
        print("Saliendo de la calculadora")
        break
      
      case _:
        print("Opcion invalida, por favor ingrese una opción válida")


      

      