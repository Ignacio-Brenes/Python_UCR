'''Restar'''
# Esta es una funcion para restar numeros ingresados por un usuario
# El usuario debe ingresar dos numeros
# El resultado de la suma se guarda en el file "output_file_resta.txt"

def resta():
    '''Funcion para Restar'''
# Recursividad
    while True:
        resta_uno = int(input("Ingrese el primer Numero: "))
        resta_dos = int(input("Ingrese el segundo Numero: "))
        total = resta_uno - resta_dos
        print(f"El resultado de la resta de ambos valores es: {total}.")
        output_file = open("output_file_resta.txt", "a") # Open/create output file in append mode
        output_file.write(f"El resultado de resta total de {resta_uno} - {resta_dos} es: {total}\n") # Appends the results to an output file
        output_file.close() # Closes the file

# Preguntar al usuario si desea continuar
        continuar = str(input("Indique (Y/N) para realizar otra resta: "))
        continuar = continuar.upper() 
        if continuar == "N":
            print("Gracias!!!")
            break
        else:
            continue

