
# 📌 Calculadora de Conversión de Bases en Python

## 📖 Descripción

El programa tiene como objetivo convertir un número decimal ingresado por el usuario a las bases:

* **Binaria (2)**
* **Octal (8)**
* **Hexadecimal (16)**

La conversión se realiza mediante el **algoritmo de divisiones sucesivas**.

---

## 🔹 Entrada de Datos

```python
numero = int(input("Ingresa un número decimal: "))
```

* `input()` captura un valor ingresado por el usuario en formato cadena.
* `int()` convierte esa cadena a un número entero.
* El valor convertido se almacena en la variable `numero`.

---

## 🔹 Definición de la Función `convertir`

```python
def convertir(numero, base):
```

Se define una función que recibe dos parámetros:

* `numero`: valor decimal a convertir.
* `base`: base destino (2, 8 o 16).

---

## 🔹 Caso Base

```python
if numero == 0:
    return "0"
```

Si el número es 0, la función retorna directamente `"0"` para evitar ejecutar el ciclo.

---

## 🔹 Tabla de Dígitos Válidos

```python
digitos = "0123456789ABCDEF"
```

Se define una cadena que contiene los símbolos necesarios para representar números hasta base 16.

Esto permite mapear los residuos obtenidos a su representación correspondiente.

**Ejemplo:**

* Residuo 10 → `A`
* Residuo 15 → `F`

---

## 🔹 Inicialización de la Variable Resultado

```python
resultado = ""
```

Se crea una cadena vacía donde se almacenará el número convertido.

---

## 🔹 Algoritmo de Conversión (Divisiones Sucesivas)

```python
while numero > 0:
    residuo = numero % base
    resultado = digitos[residuo] + resultado
    numero = numero // base
```

### 📌 Proceso:

* `numero % base` → obtiene el residuo de la división.
* `digitos[residuo]` → obtiene el carácter correspondiente al residuo.
* Se concatena al inicio de la cadena `resultado` (porque los residuos se generan en orden inverso).
* `numero // base` → realiza división entera para continuar el proceso.

Este ciclo se repite hasta que el número sea 0.

---

## 🔹 Retorno del Resultado

```python
return resultado
```

Devuelve el número convertido en formato cadena.

---

## 🔹 Impresión de Resultados

```python
print("\nResultados:")
print("Binario:", convertir(numero, 2))
print("Octal:", convertir(numero, 8))
print("Hexadecimal:", convertir(numero, 16))
```


Si quieres, también puedo prepararte el **README completo listo para tu repositorio de GitHub**, con sección de instalación y ejemplo de ejecución 🚀
