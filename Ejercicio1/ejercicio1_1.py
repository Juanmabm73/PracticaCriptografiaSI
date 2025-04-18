
# --------------- CESAR DECODER ---------------
def cesar_decoder(message):
    # message = "ROGZZ3P4O-Q1J3"  # Texto cifrado

    print("Texto decodificado en todos los desplazamientos: ")
    for shift in range(26):  # Probamos todos los desplazamientos de 0 a 25
        decrypted_text = ""
        for c in message:
            if c.isalpha():  # Solo descifrar letras
                ascii_offset = ord('A') if c.isupper() else ord('a')
                new_char = chr((ord(c) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                new_char = c  #  numeros y simbolos sin cambios
            decrypted_text += new_char
        
        print(f"Desplazamiento {shift}: {decrypted_text}")

# --------------- CESAR ENCODER ---------------
def cesar_encoder(message, shift):
    encrypted_text = ""         # Texto cifrado 
    for c in message:
        if c.isalpha():  #ciframos letras
            ascii_offset = ord('A') if c.isupper() else ord('a')
            new_char = chr((ord(c) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            new_char = c  # numeros y simbolos sin cambios
        encrypted_text += new_char
    
    return encrypted_text

# --------------- MAIN ---------------
print("Bienvenido al cifrador y descifrador Cesar")
option = ""
while(option != "3"):
    print("Por favor, elige una opcion pulsando el numero de la funcion que quieras realizar:")
    print("1. Cifrar")
    print("2. Descifrar")
    print("3. Salir")

    option = input("Opción: ")
    if option == "1":
        message = input("Introduce el mensaje a cifrar: ")
        shift = int(input("Introduce el desplazamiento (0-25): "))
        if shift < 0 or shift > 25:
            print("Desplazamiento no valido. Debe ser un numero entre 0 y 25.")
            continue        # devolvemos al menu
        result = cesar_encoder(message, shift)
        print(f"Texto cifrado: {result}")
    elif option == "2":
        message = input("Introduce el mensaje a descifrar: ")
        cesar_decoder(message)
    elif option == "3":
        print("Saliendo...")
    else:
        print("Opcion no valida. Por favor, elige 1, 2 o 3.")