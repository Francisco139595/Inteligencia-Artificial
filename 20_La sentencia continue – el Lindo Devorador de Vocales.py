"""Escenario
Tu tarea aquí es aún más especial que antes: ¡Debes rediseñar el devorador de vocales (feo) del laboratorio anterior y crear un mejor devorador de vocales (lindo) mejorado! Escribe un programa que use:

un bucle for.
el concepto de ejecución condicional (if-elif-else).
la instrucción continue.
Tu programa debe:

pedir al usuario que ingrese una palabra.
utilizar user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
emplea la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A , E , I , O , U de la palabra ingresada.
asigna las letras no consumidas a la variable word_without_vowels e imprime la variable en la pantalla.
Analiza el código en el editor. Hemos creado word_without_vowels y le hemos asignado una cadena vacía. Utiliza la operación de concatenación para pedirle a Python que combine las letras seleccionadas en una cadena más larga durante los siguientes giros de bucle, y asignarlo a la variable word_without_vowels.

Prueba tu programa con los datos que le proporcionamos."""

#EJEMPLO

word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.
user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()


for letter in user_word:
    # Completa el cuerpo del bucle.
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter

# Imprimir la palabra asignada a word_without_vowels.
print(word_without_vowels)
