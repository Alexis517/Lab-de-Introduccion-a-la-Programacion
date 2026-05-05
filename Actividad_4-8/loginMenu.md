def palabra10():
    palabra = input("Introduce una palabra: ")
    for i in range(10):
        print(palabra)

def edad():
    try:
        edad_usuario = int(input("Introduce tu edad: "))
        for i in range(edad_usuario):
            print(f"+{i+1} año(s)")
    except ValueError:
        print("Error: Ingresa un número válido.")

def numerosimpares():
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero < 0:
            print("Por favor, introduce un número entero positivo.")
        else:
            for i in range(1, numero + 1, 2):
                print(f"{i}, ", end="")
            print() 
    except ValueError:
        print("Por favor, introduce un número entero válido.")

def cuenta_regresiva():
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero < 0:
            print("Por favor, introduce un número entero positivo.")
        else:
            for i in range(numero, -1, -1):
                print(f"{i}, ", end="")
            print()
    except ValueError:
        print("Por favor, introduce un número entero válido.")

def inversion():
    try:
        inversion_cantidad = float(input("Cantidad a invertir: "))
        anual = float(input("Tasa de interés anual (%): "))
        años = int(input("Número de años: "))
        interes_compuesto = inversion_cantidad * (1 + anual / 100) ** años
        print(f"El monto total después de {años} años es: {interes_compuesto:.2f}")
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")

def triangulo():
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero < 0:
            print("Por favor, introduce un número entero positivo.")
        else:
            for i in range(1, numero + 1):
                print("*" * i)
    except ValueError:
        print("Por favor, introduce un número entero válido.")

def tablas():
    print(f"TABLA DE MULTIPLICAR DEL 1 AL 10")
    for i in range(1, 11):
        print(f"--- Tabla del {i} ---")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()

def piramide_impares():
    try:
        n = int(input("Introduce la altura del triángulo: "))
        for i in range(1, n + 1):
            for j in range(2 * i - 1, 0, -2):
                print(j, end=" ")
            print()
    except ValueError:
        print("Error: Ingresa un número entero.")

def contraseña():
    password_correcta = "laboratorio"
    intento = ""
    while intento != password_correcta:
        intento = input("Ingresa la contraseña: ")
    print("Contraseña correcta. Acceso concedido.")

def num_entero_primo():
    try:
        num = int(input("Ingresa un número entero positivo: "))
        if num < 2:
            print(num, "no es primo.")
            return
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(num, "no es primo.")
                return
        print(num, "es primo.")
    except ValueError:
        print("Error: Ingresa un número.")

def palabra_al_reves():
    palabra = input("Ingresa una palabra: ")
    for i in range(len(palabra) - 1, -1, -1):
        print(palabra[i])

def frase_letra():
    frase = input("Ingresa una frase: ")
    letra = input("Ingresa una letra: ")
    contador = 0
    for caracter in frase:
        if caracter == letra:
            contador += 1
    print(f"La letra '{letra}' aparece {contador} veces en la frase.")

def eco():
    palabra = ""
    while palabra.lower() != "salir":
        palabra = input("Ingresa una palabra (o 'salir' para terminar): ")
        if palabra.lower() != "salir":
            print(palabra)

# --- MENÚ PRINCIPAL ---
try:
    print("\nBienvenido al menú de ejercicios.")
    opcion = int(input("Elige una opción (1-13): "))

    match opcion:
        case 1: palabra10()
        case 2: edad()
        case 3: numerosimpares()
        case 4: cuenta_regresiva()
        case 5: inversion()
        case 6: triangulo()
        case 7: tablas()
        case 8: piramide_impares()
        case 9: contraseña()
        case 10: num_entero_primo()
        case 11: palabra_al_reves()
        case 12: frase_letra()
        case 13: eco()
        case _: print("Esa opción no existe.")
except ValueError:
    print("Error: Debes ingresar un número para elegir una opción.")
