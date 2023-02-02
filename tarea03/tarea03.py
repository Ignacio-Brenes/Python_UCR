# Debe crear una aplicación que funcione como una calculadora. Debe tomar en cuenta las siguientes consideraciones:
# La aplicación debe ser capaz de ejecutar las siguientes operaciones: Suma: entre n números Resta: entre 2 números Multiplicación: entre n números División: entre 2 números Factorial: de 1 número Potencia: 1 número elevado al otro
# Esta aplicación debe ejecutar operaciones indicadas por el usuario hasta que este decida salir. Debe desplegar el resultado de cada operación ejecutada y además se debe escribir la operación realizada y su resultado en un archivo de texto creado
# en el directorio principal de la aplicación. La aplicación no debe tener una interfaz gráfica, todas las interacciones del usuario se deben dar por medio de la terminal. El código se debe separar en módulos especializados. La distribución del
# código en estos módulos queda a su criterio basado en los conceptos vistos en clase. Debe utilizar las estructuras de datos vistas en clase. No debe utilizarlas todas necesariamente, utilice su criterio y los conceptos vistos en clase para
# decidir qué estructura de datos amerita a usar en cada caso. Los nombres de módulos, funciones y variables deben ser significativos y deben seguir los estándares de nombramiento que se han visto en clase. También se pueden referir a este link (si tienen problemas con el inglés, les
# recomiendo utilizar Google Translate, funciona bastante bien): https://peps.python.org/pep-0008/#naming-conventions Debe crear documentación interna de su código a través de comentarios. La tarea se puede realizar en parejas y es la manera recomendada.


#Paso 01: Entender el problema, se debe crear una calculadora que realice operaciones matemáticas básicas.
#Paso 02: Desplegar menú de opciones: SUMA, RESTA, MULTIPLICACION,DIVISION, POTENCIAL, FACTORIAL
#Paso 03: Recibir input del usuario (2 o más números para suma, multiplicación) (2 números solamente para resta, división, potencia) (1 número para potencial), y guardarlos en una lista
#Paso 04: Usar una lista para las operaciones que reciben 2 o más números.
#Paso 05: Para las operaciones de 2 números, usar variables.

#INICIA MENU

menu = {}
menu['1']="Suma" 
menu['2']="Resta"
menu['3']="Multiplicación"
menu['4']="División"
menu['5']="Factorial"
menu['6']="Potencia"
menu['7']="SALIR"

while True:
    options=menu.keys()
    #options.sort() #ni idea que hace este sort
    for entry in options: 
        print (entry, menu[entry])
    selection=input("Please Select:") 
    if selection =='1': # Suma
      # Aqui vamos a crear una lista
      # primer_numero = int(input("Ingrese el primer Numero: "))
      # segundo_numero = int(input("Ingrese el segundo Numero: "))
      # total = primer_numero + segundo_numero
      # print(f"La suma de {primer_numero} + {segundo_numero} es: {total}.")
    elif selection == '2': # Resta
      resta_uno = int(input("Ingrese el primer Numero: "))
      resta_dos = int(input("Ingrese el segundo Numero: "))
      total = resta_uno - resta_dos
      print(f"La resta de ambos valores es: {total}.")
    elif selection == '3':
      print ("\n Multiplicación \n")
    elif selection == '4':
      print ("\n División \n")
    elif selection == '5':
      print ("\n Factorial \n")
    elif selection == '6':
      print ("\n Potencia \n")
    elif selection == '7':
      print("Muchas Gracias! \n")
      break      
    else: 
      print ("\n Opción no válida \n" )
      #LINEA DE PRUEBA