"""Ya estás familiarizado con el cifrado César, y es por eso que queremos que mejores el código que te mostramos recientemente.

El cifrado solo debe aplicarse a las letras latinas (por ejemplo, 'a' a 'z', 'A' a 'Z'). Todos los demás caracteres del mensaje deben permanecer intactos.

La capitalización de las letras debe conservarse (por ejemplo, 'A' encriptado se convertirá en 'B', y 'a' encriptado se convertirá en 'b').

Tu tarea es escribir un programa el cual:

Pida al usuario una línea de texto para encriptar.
Pida al usuario un valor de cambio (un número entero del rango 1..25 - nota: debes obligar al usuario a ingresar un valor de cambio válido (¡no te rindas y no dejes que los datos incorrectos te engañen!).
Imprime el texto codificado."""
#EJEMPLO

text = input("Ingresa una línea de texto para encriptar: ")

while True:
    try:
        shift = int(input("Ingresa el valor de cambio (un entero del 1 al 25): "))
        if shift not in range(1, 26):
            print("¡Error! El valor de cambio debe estar entre 1 y 25.")
            continue
        break
    except ValueError:
        print("¡Error! Debes ingresar un número entero.")

cipher = ''

for char in text:
    if char.isalpha():
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # Calcular la nueva posición del carácter
        code = (ord(char) - first + shift) % 26
        cipher += chr(first + code)
    else:
        cipher += char

print("Texto encriptado:", cipher)