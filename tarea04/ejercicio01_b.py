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
    
    return (números, letras, caracteres_especiales)

entrada_del_usuario = input("Ingrese su entrada: ")
números, letras, caracteres_especiales = contar_caracteres(entrada_del_usuario)

print("Números:", números)
print("Letras:", letras)
print("Caracteres especiales:", caracteres_especiales)

# Cuando ejecutes este programa, se te pedirá que ingreses una entrada. 
# Después de que ingreses la entrada, el programa te dirá cuántas letras, números y caracteres especiales tiene.
