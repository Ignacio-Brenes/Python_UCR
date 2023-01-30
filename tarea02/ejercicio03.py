#Strings intercaladas: Escriba un programa que reciba dos strings del mismo
#largo por parte del usuario e imprima una nueva string con los caracteres de
#ambos inputs intercalados.

def intercalar(a, b):
    i = 0
    cadena = ""
    while(i < len(a)):
        # en lugar de estar imprimiendo dentro del bucle
        # vas a guardar en una variable la nueva cadena en la 
        # cual se soluciona el ejercicio
        cadena += a[i] + b
        # cadena toma lo que ya tenga almacenado (+=) y guarda una letra
        # de la cadena a (a[i]) mas la segunda cadena es decir cadena b
        i = i + 1
    return cadena

# recuerda que en python 3 raw_input paso a ser input
a = input("Ingrese palabara a: ") 
b = input("Ingrese palabara b: ")

print(intercalar(a, b))