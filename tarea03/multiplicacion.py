# PROGRAMA PARA MULTIPLICACION DE 2 O MAS NúMEROS

total = 1
while True:
  number = float(input("Ingresa un número y seguiré multiplicando hasta que ingreses 1 para SALIR: \n"))
  if number == 1:
    print(f"El total de la multiplicación es: {total}")
    break
  else:
    total *= number