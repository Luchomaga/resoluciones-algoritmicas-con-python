#Resoluciones algoritmicas con python:
#1)Contar el numero de ocurrecias de cada una de las letras del alfabeto que contiene una frace que ingrese el usuario por teclado.
#2)Escribir un algoritmo que solicite ingresar un numero entero. De acuerdo al numero ingresado, imprime si es negativo, positivo o igual a cero.
#el algortimo continua solicitando numeros, haste que el usuario ingrese asterisco(*).
#Esribir un algoritmo que solicite al usuario ingresar numeros enteros, hasta que el usuario ingrese cero. Guardar los numeros ingresados en una lista
#y calcular la sumatoria y el promedio de los valores que contiene dicha lista.
#4)Escribir un algoritmo que, dado un numero entero por el usuario, muestre la suma de todos sus digitos. Recorda que vas a necesitar obtener cada uno 
#de los digitos por separado para podersumarlos entre si.
#5) crea un menun, que permita acceder a todas las opcines anteriores
while True:
    print("-------- Resoluciones algortmicas con Python --------")
    print("1) Letras repetidas, en una frase ")
    print("2) Enteros(positivo, negativo o igual a cero)")
    print("3) Sumatoria de enteros, mayor a cero")
    print("4) Suma de todos los digitos de un entero")
    print("5) Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":     
        import string
        frase = input("Ingresa una frase: ")
        frase = frase.lower()
        ocurrencias = {}
        for letra in string.ascii_lowercase:
         ocurrencias[letra] = 0
        for letra in frase:
            if letra.isalpha():
                ocurrencias[letra] += 1
        for letra, contador in ocurrencias.items():
            if contador > 0:
                print(f"La letra '{letra}' aparece {contador} veces en la frase.")
    elif opcion == "2":
        print("Has seleccionado la opción 2.")
        while True:
            numero = input("Ingresa un número entero (o * para salir): ")
            if numero == "*":
                print("¡Hasta luego!")
                break
            numero = int(numero)
            if numero > 0:
                print("El número es positivo.")
            elif numero < 0:
                print("El número es negativo.")
            else:
                print("El número es igual a cero.")
    elif opcion == "3":
        print("Has seleccionado la opción 3.")
        numeros = []
        suma = 0
        while True:
               numero=int(input("Ingresa un número entero (o 0 para finalizar): "))
        if numero == 0:
            break
        numeros.append(numero)
        suma += numero
        promedio = suma / len(numeros)
        print("Lista de números ingresados:", numeros)
        print("Sumatoria:", suma)
        print("Promedio:", promedio)
    elif opcion == "4":
        print("Has seleccionado la opción 4.")
        
        numero = int(input("Ingresa un número entero: "))
 
        suma_digitos = 0

        while numero > 0:
            digito = numero % 10
            suma_digitos += digito
            numero //= 10

        print("La suma de los dígitos es:", suma_digitos)
    elif opcion == "5":
    
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")