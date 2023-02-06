# Esta es una funcion para dividir dos numeros ingresados por un usuario
# El usuario debe ingresar dos numeros
# El resultado de la division se guarda en el file "output_file_division.txt"

def division():
    '''Funcion para Dividir'''
    while True:
        primer_numero = int(input("Ingrese el primer numero que desea dividir: "))
        segundo_numero = int(input(f"Ingrese el segundo numero que desea dividir: "))
        total = primer_numero // segundo_numero
        print(f"La division entre ambos numeros es: {total}")
        output_file = open("output_file_division.txt", "a") # Open/create output file in append mode
        output_file.write(f"El resultado de la division de {primer_numero} // {segundo_numero} es: {total}\n") # Appends the results to an output file
        output_file.close() # Closes the file
        # Preguntar al usuario si desea continuar
        continuar = str(input("Indique (Y/N) para continuar: ")) 
        continuar = continuar.upper()
        if continuar == "N":
            print("\nGracias!")
            break
division()
