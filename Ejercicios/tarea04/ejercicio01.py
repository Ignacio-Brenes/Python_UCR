# Cree una función que cuente e imprima en pantalla todos los números, letras, y caracteres especiales presentes en una string. Debe recibir esta string por parámetro.

def contar_caracteres(string):
    números = 0
    letras = 0
    caracteres_especiales = 0
    
    for carácter in string:
        if carácter.isdigit():
            números += 1
        elif carácter.isalpha():
            letras += 1
        else:
            caracteres_especiales += 1
    
    print("Números:", números)
    print("Letras:", letras)
    print("Caracteres especiales:", caracteres_especiales)


# Puedes llamar a esta función pasándole una string como argumento, y la función imprimirá en pantalla los conteos de números, letras y caracteres especiales presentes en la string.