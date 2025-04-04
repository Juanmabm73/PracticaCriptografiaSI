from Crypto.Cipher import AES

BLOCK_SIZE = 16 # Tamaño de bloque para AES-128

def add_padding(data_bytes): # añade relleno al texto
    pad_len = BLOCK_SIZE - (len(data_bytes) % BLOCK_SIZE) # calcula el tamaño del relleno
    return data_bytes + bytes([pad_len]) * pad_len # añade el relleno al texto

def remove_padding(data_bytes): # elimina el relleno del texto
    pad_len = data_bytes[-1] # obtiene el tamaño del relleno
    if pad_len < 1 or pad_len > BLOCK_SIZE: # comprueba si el tamaño del relleno es válido
        raise ValueError("El relleno (padding) no es válido")
    return data_bytes[:-pad_len] # elimina el relleno del texto

def encrypt_text(plain_text, key, iv, mode): # cifra el texto
    data = plain_text.encode('utf-8') # convierte el texto a bytes
    padded_data = add_padding(data) # añade el relleno al texto
    if mode == AES.MODE_CBC: # comprueba si el modo es CBC
        cipher = AES.new(key, mode, iv) # crea el objeto de cifrado con el IV
    else: # si el modo no es CBC, usa ECB
        cipher = AES.new(key, mode) # crea el objeto de cifrado sin IV
    encrypted_text = cipher.encrypt(padded_data) # cifra el texto
    return encrypted_text # devuelve el texto cifrado

def decrypt_text(encrypted, key, iv, mode): # descifra el texto
    if mode == AES.MODE_CBC: # comprueba si el modo es CBC
        cipher = AES.new(key, mode, iv) # crea el objeto de cifrado con el IV
    else:
        cipher = AES.new(key, mode) # crea el objeto de cifrado sin IV
    decrypted_data = cipher.decrypt(encrypted) # descifra el texto
    unpadded_data = remove_padding(decrypted_data) # elimina el relleno del texto
    return unpadded_data.decode('utf-8') # convierte el texto a utf-8

def choose_mode():
    print("Elige el modo de operación:")
    print("------------")
    print("1- CBC (usa IV)")
    print("2- ECB (no usa IV)")
    opcion = input("Introduce la opción: ")
    if opcion == "1":
        return AES.MODE_CBC, True
    elif opcion == "2":
        return AES.MODE_ECB, False
    else:
        print("Modo no reconocido, se usará CBC por defecto")
        return AES.MODE_CBC, True

def get_16_chars(prompt):
    entrada = input(prompt)
    if len(entrada) != 16:
        print("Error: La entrada debe tener exactamente 16 caracteres.")
        return None
    return entrada.encode('utf-8')

while True:
    print("\nCifrado AES-128 - Ejemplo para seguridad informática")
    print("------------")
    print("1- Cifrar texto")
    print("2- Descifrar texto")
    print("0- Salir")
    print("------------")
    opcion = input("Introduce la opción: ")

    if opcion == "0":
        exit()

    # Elige el modo de operación
    mode, need_iv = choose_mode()

    # Solicita la clave y el IV
    key = None
    while key is None:
        key = get_16_chars("Introduce la clave (16 caracteres): ")

    iv = None
    if need_iv:
        while iv is None:
            iv = get_16_chars("Introduce el IV (16 caracteres): ")

    if opcion == "1":
        plain_text = input("Introduce el texto a cifrar: ")
        try:
            encrypted_result = encrypt_text(plain_text, key, iv, mode)
            print("Texto cifrado (hex):", encrypted_result.hex().upper())
        except Exception as error:
            print("Error al cifrar:", error)
    elif opcion == "2":
        hex_text = input("Introduce el texto cifrado en formato hexadecimal: ")
        try:
            encrypted_data = bytes.fromhex(hex_text)
        except ValueError:
            print("Error: El formato hexadecimal es inválido.")
            continue
        try:
            decrypted_text = decrypt_text(encrypted_data, key, iv, mode)
            print("Texto descifrado:", decrypted_text)
        except Exception as error:
            print("Error al descifrar:", error)
    else:
        print("Opción no válida. Intenta de nuevo.")