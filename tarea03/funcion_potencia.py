'''Potencia'''

# Esta es una funcion para obtner la potencia de un numero elevado a otro.
# El resultado de la operecion se guarda en el file "output_file_potencia.txt".
def potencia():
    while True:
        base = int(input("Ingrese el numero base: "))
        exponte = int(input("Ingrese el numero exponente: "))
        # Funcion pow() para obtener la potencia de un numero
        potencia = pow(base, exponte) 
        print(f"El numero {base} elevado al {exponte} es: {potencia}" )
        # Crear documento, escribir resultado y cerrar 
        output_file = open("output_file_potencia.txt", "a")
        output_file.write(f"\nEl numero {base} elevado al {exponte} es: {potencia}\n")
        output_file.close()
        # Preguntar al usuario si desea continuar
        continuar = str(input("Indique (Y/N) para continuar: ")) 
        continuar = continuar.upper()
        if continuar == "N":
            print("\nGracias!")
            break

