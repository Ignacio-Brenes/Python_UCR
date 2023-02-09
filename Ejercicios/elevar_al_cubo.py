def elevate_to_cube(num):
  return num**3

input_num = int(input("Ingrese un número entero: "))
result = elevate_to_cube(input_num)
print("El resultado de elevar su número al cubo es:", result)

# Este programa pide al usuario que ingrese un número, luego lo convierte en un entero usando la función int(). 
# A continuación, llama a la función elevate_to_cube() y pasa input_num como argumento. 
# La función elevate_to_cube() eleva el número a la tercera potencia y devuelve el resultado. 
# Finalmente, el programa imprime el resultado en la consola.