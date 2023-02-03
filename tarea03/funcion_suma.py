# Esta es una funcion para sumar los numeros ingresados por un usuario
# El usuario puede ingresar la cantidad de numeros que desee
# Se debe ingresar cero para finalizar

def suma():
    
    lista = []
    sumar = int(input("Ingrese el numero que desea sumar (Ingrese 0 para finalizar):"))
    suma_numeros = 0
    while sumar !=0:
        lista.append(sumar)
        sumar = int(input("Ingrese el numero que desea sumar (Ingrese 0 para finalizar):"))
    print("Los numeros ingresados son: ")
    print(lista)
    for total in lista:
        suma_numeros += total
    print(f"El total de la suma de {lista} es:")
    print(suma_numeros)
suma()