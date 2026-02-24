# Explicación Profesional del Código de Autenticación

## Introducción

El presente programa implementa un mecanismo básico de autenticación que limita el número de intentos de acceso a un máximo de tres. Su finalidad es validar las credenciales ingresadas por el usuario antes de conceder el acceso al sistema.

---

## Desarrollo

### 1. Control de Intentos

Se inicializa la variable `intentos` en cero, la cual funciona como contador para registrar la cantidad de intentos realizados.

Posteriormente, se establece un ciclo `while` con la condición:

```python
while intentos < 3:
Esta estructura permite que el proceso de validación se repita únicamente mientras no se haya alcanzado el límite de tres intentos.

2. Captura de Credenciales

Dentro del ciclo, el programa solicita al usuario ingresar:

Nombre de usuario

Contraseña

Esto se realiza mediante la función input().

3. Validación del Usuario

El sistema verifica que:

El usuario no esté vacío.

Contenga únicamente caracteres alfanuméricos utilizando el método isalnum().

En caso de no cumplir estas condiciones, se incrementa el contador de intentos y se utiliza la instrucción continue para reiniciar el ciclo.

4. Validación de la Contraseña

La contraseña debe cumplir con los siguientes requisitos:

Tener al menos 8 caracteres (len()).

Contener al menos una letra (isalpha()).

Contener al menos un número (isdigit()).

Para verificar la presencia de letras y números, se recorre la contraseña carácter por carácter mediante un ciclo for.

Si no se cumplen estas condiciones, el sistema incrementa el contador y reinicia el ciclo.
usuario == "admin" and contraseña == "Admin2026"

Si la comparación es verdadera:

Se muestra el mensaje de acceso concedido.

Se interrumpe el ciclo mediante la instrucción break.

En caso contrario:

Se incrementa el contador de intentos.

El proceso se repite hasta alcanzar el límite permitido.

Conclusión

El programa aplica estructuras de control como while, if, for, continue y break para gestionar el flujo de ejecución. Además, incorpora validaciones básicas de seguridad para garantizar que las credenciales cumplan ciertos criterios antes de permitir el acceso.

Este enfoque demuestra la aplicación práctica de estructuras de control y validación de datos en Python para la creación de un sistema sencillo de autenticación.
5. Verificación de Credenciales

Una vez superadas las validaciones estructurales, el programa compara las credenciales ingresadas con los valores predefinidos:
