intentos = 0

while intentos < 3:
    usuario = input("Ingresa tu usuario: ")
    contraseña = input("Ingresa tu contraseña: ")

    # Validar usuario
    if usuario == "" or not usuario.isalnum():
        print("Usuario inválido. No debe estar vacío y solo debe tener letras y números.")
        intentos += 1
        continue

    # Validar contraseña
    if len(contraseña) < 8:
        print("Lerolero no es correcto lerolero")
        intentos += 1
        continue

    tiene_letra = False
    tiene_numero = False

    for c in contraseña:
        if c.isalpha():
            tiene_letra = True
        if c.isdigit():
            tiene_numero = True

    if not tiene_letra or not tiene_numero:
        print("debe contener al menos 1 letra y 1 digito")
        intentos += 1
        continue

    # Verificar credenciales correctas
    if usuario == "admin" and contraseña == "Admin2026":
        print("Acceso concedido ")
        break
    else:
        print("Credenciales incorrectas.")
        intentos += 1

# Si llega a 3 intentos
if intentos == 3:
    print("Demasiados intentos. Programa terminado ")
