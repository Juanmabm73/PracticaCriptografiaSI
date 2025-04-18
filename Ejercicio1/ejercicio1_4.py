
# --------------- XOR ENCRYPT/DECRYPT ---------------
def xor_encrypt_decrypt(text, key):
    # Comprueba si text y key son cadenas de texto
    if isinstance(text, str):
        text = text.encode('utf-8')
    if isinstance(key, str):
        key = key.encode('utf-8')
    
    result = bytearray() # almacena el resultado
    for i in range(len(text)):
        # coge cada byte del texto, le aplica la funcion XOR y lo añade al resultado
        key_byte = key[i % len(key)]
        result.append(text[i] ^ key_byte)
    
    return result.decode('utf-8', errors='replace') # devuelve el resultado como texto

# --------------- MAIN ---------------
while True:
    print("Quieres codificar o decodificar?")
    print("------------")
    print("1- Codificar")
    print("2- Decodificar")
    print("0- Salir")
    print("------------")
    number = input("Introduzca la opcion: ")

    if number == "0":
        exit()
    elif number == "1":
        message = input("Introduce el texto a codificar: ")
        key = input("Introduce la clave: ")
        
        if not key:
            print("Error: La clave no puede estar vacía")
            continue
            
        encoded = xor_encrypt_decrypt(message, key)
        print(f"Codificado: {encoded}")
    elif number == "2":
        message = input("Introduce el texto a decodificar: ")
        key = input("Introduce la clave: ")
        
        if not key:
            print("Error: La clave no puede estar vacía")
            continue
            
        decoded = xor_encrypt_decrypt(message, key)
        print(f"Decodificado: {decoded}")
    else:
        print("Opción no válida. Intente de nuevo.")