# Cree una función que cuente todas las apariciones de cada caracter en una string; esta string debe recibirse como parámetro. El resultado debe ser un diccionario y debe ser impreso en pantalla.
# Ejemplo: Input: “papaya” Resultado: {“p”: 2, “a”: 3, “y”: 1}

def count_characters(string):
    """
    Recibe una string como parámetro y devuelve un diccionario con la cuenta de apariciones de cada caracter
    """
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

string = "Hola Mundo"
result = count_characters(string)
print(result)


