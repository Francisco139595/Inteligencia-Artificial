"""
Algunos dicen que el Dígito de la Vida es un dígito calculado usando el cumpleaños de alguien. Es simple: solo necesitas sumar todos los dígitos de la fecha. Si el resultado contiene más de un dígito, se debe repetir la suma hasta obtener exactamente un dígito. Por ejemplo:

1 Enero 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 es el dígito que buscamos y encontramos.

Tu tarea es escribir un programa que:

Le pregunté al usuario su cumpleaños (en el formato AAAAMMDD o AAAADMM o MMDDAAAA; en realidad, el orden de los dígitos no importa).
Dé como salida El Dígito de la Vida para la fecha ingresada.
Prueba tu código utilizando los datos que te proporcionamos."""

#EJEMPLO

birth_date = input("Ingresa tu fecha de nacimiento (en formato AAAAMMDD): ")

while len(birth_date) > 1:
    digit_sum = 0
    for digit in birth_date:
        digit_sum += int(digit)
    
    birth_date = str(digit_sum)

print("Tu Dígito de la Vida es:", birth_date)
