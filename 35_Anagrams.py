"""Un anagrama es una nueva palabra formada al reorganizar las letras de una palabra, usando todas las letras originales exactamente una vez. Por ejemplo, las frases "rail safety" y "fairy tales" son anagramas, mientras que "I am" y "You are" no lo son.

Tu tarea es escribir un programa que:

Le pida al usuario dos textos por separado.
Compruebe si los textos ingresados son anagramas e imprima el resultado.
Nota:

Supongamos que dos cadenas vacías no son anagramas.
Tratar a las letras mayúsculas y minúsculas como iguales.
Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.
Prueba tu código utilizando los datos que te proporcionamos.

Datos de Prueba
Entrada de Muestra:

Listen
Silent

Salida de muestra:

Output
Anagramas

Salida de muestra:

Output
No son anagramas

Entrada de Muestra:

modern
norman"""


#EJEMPLO

str_1 = input("Ingresa la primera cadena: ")
str_2 = input("Ingresa la segunda cadena: ")
str_1 = str_1.replace(' ', '').upper()
str_2 = str_2.replace(' ', '').upper()

if len(str_1) > 0 and sorted(str_1) == sorted(str_2):
    print("Anagramas")
else:
    print("No son anagramas")