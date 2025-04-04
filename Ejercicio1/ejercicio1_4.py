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
    
    return result # una vez ya ha recorrido todo el texto lo devuelve

def format_output(data): # esta funcion formatea el resultado
    hex_output = data.hex() # convierte el resultado a hexadecimal
    
    try:
        text_output = data.decode('utf-8') # intenta convertir el resultado a texto
        return f"Texto: {text_output}\nHex: {hex_output}" # devuelve el resultado en texto y hexadecimal
    except UnicodeDecodeError:
        return f"Hex: {hex_output} (No se puede representar como texto)" # si no se puede convertir a texto devuelve solo el hexadecimal


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
        print(f"Codificado: {format_output(encoded)}")
    elif number == "2":
        input_type = input("¿Quieres introducir el texto en formato hexadecimal? (s/n): ").lower()
        
        if input_type == 's':
            try:
                hex_input = input("Introduce el texto hexadecimal a decodificar: ")
                # Convert hex string to bytes
                message = bytes.fromhex(hex_input)
            except ValueError:
                print("Error: Formato hexadecimal inválido")
                continue
        else:
            message = input("Introduce el texto a decodificar: ")
            
        key = input("Introduce la clave: ")
        
        if not key:
            print("Error: La clave no puede estar vacía")
            continue
            
        decoded = xor_encrypt_decrypt(message, key)
        print(f"Decodificado: {format_output(decoded)}")
    else:
        print("Opción no válida. Intente de nuevo.")