Código de Calculadora de Conversión
Descripción del funcionamiento

Bueno lo que hice fue primero pedirle al usuario que escribiera un número decimal y lo guardé en una variable que se llama numero. Le puse int() porque si no, Python lo toma como texto y no se puede hacer la división.

Después hice una función que se llama convertir, que recibe el número y la base a la que lo quiero convertir. O sea, puede ser 2, 8 o 16.

Primero reviso si el número es 0, porque si es 0 pues ya no tiene sentido hacer el ciclo, entonces regreso directamente "0".

Luego hice una cadena que tiene todos los dígitos posibles hasta el 16, o sea del 0 al 9 y luego A, B, C, D, E y F. Eso lo uso porque en hexadecimal después del 9 siguen letras.

Después hice una variable que empieza vacía para ir guardando el resultado.

Luego viene lo importante: hago un while que se repite mientras el número sea mayor que 0. Dentro del ciclo saco el residuo usando el módulo %, y ese residuo me dice qué número va en esa posición. Luego lo busco en la cadena de digitos y lo voy agregando al principio del resultado, porque si lo agrego al final me saldría al revés.

Después divido el número entre la base usando // para que sea división entera y el ciclo siga hasta que llegue a 0.

Al final la función regresa el número convertido y luego simplemente mando a imprimir el binario, el octal y el hexadecimal llamando la función tres veces con diferentes bases.
