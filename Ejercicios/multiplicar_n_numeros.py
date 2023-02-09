def multiplicar():
    resultado = 1
    num_count = int(input("Ingresa la cantidad de números que deseas multiplicar: "))
    for i in range(num_count):
        num = input(f"Ingresa el número {i + 1}: ")
        if num == "Salir":
            break
        resultado *= int(num)
    return resultado

print("El resultado de la multiplicación es:", multiplicar())


# El programa solicita primero al usuario la cantidad de números que desea multiplicar. 
# Luego, en un bucle for, se solicita al usuario que ingrese cada uno de los números y se multiplican. 
# Si el usuario ingresa la palabra "Salir", se rompe el bucle y se devuelve el resultado de la multiplicación.