"""Ya conoces como funiona el método split(). Ahora queremos que lo pruebes.

Tu tarea es escribir tu propia función, que se comporte casi como el método original split(), por ejemplo:

Debe aceptar únicamente un argumento: una cadena.
Debe devolver una lista de palabras creadas a partir de la cadena, dividida en los lugares donde la cadena contiene espacios en blanco.
Si la cadena está vacía, la función debería devolver una lista vacía.
Su nombre debe ser mysplit().
Utiliza la plantilla en el editor. Prueba tu código con cuidado.


Salida Esperada
Output
['A', 'ser', 'o', 'no', 'a', 'ser', 'eso', 'es', 'el', 'pregunta']
['A', 'ser', 'o', 'no', 'a', 'ser, eso', 'es', 'el', 'pregunta']
[]
['a B C']
[]"""

#EJEMPLO

def mysplit(strng):
    word_list = []
    current_word = ""
    for char in strng:
        if not char.isspace():
            current_word += char
        elif current_word:
            word_list.append(current_word)
            current_word = ""
            
    if current_word:
        word_list.append(current_word)
        
    return word_list


print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))