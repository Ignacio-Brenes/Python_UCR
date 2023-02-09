def calculator():
    # Toma dos números del usuario
    num1 = float(input("Ingresa un número: "))
    num2 = float(input("Ingresa otro número: "))

    # Toma la operación deseada del usuario
    print("Selecciona la operación a realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    choice = int(input("Ingresa tu opción (1/2/3/4): "))

    if choice == 1:
        result = num1 + num2
        print(num1, "+", num2, "=", result)
    elif choice == 2:
        result = num1 - num2
        print(num1, "-", num2, "=", result)
    elif choice == 3:
        result = num1 * num2
        print(num1, "*", num2, "=", result)
    elif choice == 4:
        result = num1 / num2
        print(num1, "/", num2, "=", result)
    else:
        print("Opción inválida. Intenta de nuevo.")

# Llamamos a la función calculator
calculator()
