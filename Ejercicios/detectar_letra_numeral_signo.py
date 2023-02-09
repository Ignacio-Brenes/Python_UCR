def recognize_characters(input_string):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    signs = "!@#$%^&*()_+-=[]{};':\"\\|,.<>/?`~ "
    
    output_string = ""
    for char in input_string:
        if char in letters:
            output_string += "Letra "
        elif char in numbers:
            output_string += "Número "
        elif char in signs:
            output_string += "Signo "
        else:
            output_string += "Desconocido "
    
    return output_string

input_string = "L / 21"
print(recognize_characters(input_string))
