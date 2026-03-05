intentos = 3
acceso_concedido = False 

while True:
    while intentos > 0:
        print(f"\nINICIO DE SESIÓN (INTENTOS RESTANTES: {intentos})")
        
        UsuarioNombre = input("Usuario: ")
        UsuarioContraseña = input("Contraseña: ")
        
        # Validaciones de contraseña
        tiene_numero = any(c.isdigit() for c in UsuarioContraseña)
        tiene_letra = any(c.isalpha() for c in UsuarioContraseña)
        masde8 = len(UsuarioContraseña) >= 8
        error_detectado = False

        # Lógica de validación
        if not UsuarioNombre.isalnum():
            print("Error: El usuario no puede estar vacío ni tener símbolos.")
            error_detectado = True
        elif UsuarioNombre != "admin":
            print("Error: Usuario incorrecto.")
            error_detectado = True
        elif not masde8:
            print("Error: La contraseña debe tener al menos 8 caracteres.")
            error_detectado = True
        elif not tiene_letra or not tiene_numero:
            print("Error: La contraseña debe tener letra y número.")
            error_detectado = True
        elif UsuarioContraseña != "Admin2026":
            print("Contraseña incorrecta.")
            error_detectado = True
        
        if not error_detectado:
            print(f"Bienvenido {UsuarioNombre} acceso concedido")
            acceso_concedido = True
            
            # MENÚ
            while acceso_concedido:
                print("\n1. Clasificar Número\n2. Categoría edad\n3. Calcular tarifa\n4. Cerrar sesión\n5. Salir")
                seleccion = input("Opción: ")
                
                if seleccion == "1":
                    print("--- Ejecutando: Número clasificado ---")
                    while True:
                        try:
                            num = int(input("Ingrese un número: "))
                            if num > 0:
                                print(f"El número {num} es positivo.")
                            elif num < 0:
                                print(f"El número {num} es negativo.")
                            else:
                                print(f"El número {num} es cero.")
                            if num % 2 == 0:
                                print(f"El número {num} es par.")
                            else:
                                print(f"El número {num} es impar.")
                            break
                        except ValueError:
                            print("Error: Debe ingresar un número entero válido.")
                
                elif seleccion == "2":
                    print("--- Ejecutando: Categoría de edad ---")
                    while True:
                        try:
                            edad = int(input("Ingrese la edad: "))
                            identificacion = input("Cuentas con INE s/n.")
                            licencia = input("Cuentas con licencia s/n.")
                            if 0 <= edad < 120:
                                print("Error: La edad no puede ser negativa.")
                            elif edad <= 12:
                                print(f"Con {edad} años, eres un mocoso.")
                            elif edad <= 17:
                                print(f"Con {edad} años, eres un adolescente.")
                            elif edad <= 64:
                                print(f"Con {edad} años, eres un adulto.")
                            else: edad >= 64
                            print(f"Con {edad} años, eres un viejo.")
                            if edad >=13:
                                print("puedes registrarte")
                            elif edad >= 18:
                                print("puedes registrarse sin tutor")
                            elif edad < 18:
                                print("puedes registrarte con tutor")
                            elif edad >= 18:
                                print("puedes concundir")
                            elif edad >= 21:
                                print("acceso a servicio premium")
                            break
                        except ValueError:
                            print("Error: Debe ingresar una edad válida (número entero).")  
                
                elif seleccion == "3":
                    print("Calculando Tarifa. ")
                    precio_base = 200.0
                    recargo = 0.0
                    descuento = 0
                    
                    #Datos Necesarios para continuar#
                    edad = int(input("Ingresa tu edad (0 a 120): "))
                    if 0 <= edad <= 12:
                        descuento += 50
                    elif 13 <= edad <= 17:
                        descuento += 20
                    elif edad >= 65:
                        descuento += 30
                    else:
                        print("Edad invalida")
                    dia = int(input("Día de la semana (1=Lun...7=Dom): "))
                    if tiene_numero:
                        print("1.Lunes")
                        print("2.Martes")
                        print("3.Miercoles")
                        print("4.Jueves")
                        print("5.Viernes")
                        print("6.Sabado")
                        print("7.Domingo")
                    
                elif seleccion == "4":
                    print("Cerrando Sesión...")
                    acceso_concedido = False 
                    intentos = 3            
                
                elif seleccion == "5":
                    print("Saliendo del programa.")
                    exit() 
                else:
                    print("Opción no válida.")
            
            if not acceso_concedido:
                continue

        else:
            intentos -= 1 # Restamos intento si hubo error de validación

    if intentos == 0 and not acceso_concedido:
        print("\nAcceso bloqueado. Has agotado tus 3 intentos.")
        break 
