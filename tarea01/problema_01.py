#Se necesita crear un programa que reciba del usuario una frase y decida si esa
#frase es un palíndromo o no. Un palíndromo se puede leer de igual forma de
#izquierda a derecha, que de derecha a izquierda. Ejemplo: "Anita lava la tina".



my_str = input("Ingrese su palabra:")

# Omitir formato de palabra (CAPS)
my_str = my_str.casefold()

# Invertir el string
rev_str = reversed(my_str)

# Revisar si la palabra es palíndromo
if list(my_str) == list(rev_str):
   print("La palabra es palíndrome.")
else:
   print("La palabra no es palíndrome.")
