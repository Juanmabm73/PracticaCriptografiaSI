from Crypto.Cipher import AES

# --------------- ENCRYPT TEXT ---------------
def encrypt_text(plain_text, key, iv=None):
    # Convierte el texto a bytes
    data = plain_text.encode('utf-8')
    
    # Añade padding PKCS7 (múltiplo de 16)
    pad_len = 16 - (len(data) % 16)
    padded_data = data + bytes([pad_len]) * pad_len
    
    # Determina el modo y crea el objeto de cifrado
    if iv:
        cipher = AES.new(key, AES.MODE_CBC, iv)
    else:
        cipher = AES.new(key, AES.MODE_ECB)
        
    # Cifra y devuelve el resultado
    return cipher.encrypt(padded_data)

# --------------- DECRYPT TEXT ---------------
def decrypt_text(encrypted, key, iv=None):
    # Crea el objeto de descifrado
    if iv:
        cipher = AES.new(key, AES.MODE_CBC, iv)
    else:
        cipher = AES.new(key, AES.MODE_ECB)
    
    # Descifra
    decrypted = cipher.decrypt(encrypted)
    
    # Quita el padding
    pad_len = decrypted[-1]
    unpadded = decrypted[:-pad_len]
    
    # Convierte de bytes a texto
    return unpadded.decode('utf-8')


# --------------- MAIN ---------------
while True:
    print("\nCifrado AES-128")
    print("------------")
    print("1- Cifrar texto")
    print("2- Descifrar texto")
    print("0- Salir")
    print("------------")
    opcion = input("Introduce la opción: ")

    if opcion == "0":
        break
    
    # Determina si usamos CBC (con IV) o ECB
    modo = input("¿Usar modo CBC con IV? (s/n): ").lower()
    usar_iv = modo.startswith('s')
    
    # Obtiene la clave
    clave = input("Introduce la clave (16 caracteres): ")
    if len(clave) != 16:
        print("Error: La clave debe tener 16 caracteres")
        continue
    key = clave.encode('utf-8')
    
    # Obtiene el IV si es necesario
    iv = None
    if usar_iv:
        vector = input("Introduce el IV (16 caracteres): ")
        if len(vector) != 16:
            print("Error: El IV debe tener 16 caracteres")
            continue
        iv = vector.encode('utf-8')

    # Procesa según la opción elegida
    if opcion == "1":
        texto = input("Introduce el texto a cifrar: ")
        try:
            cifrado = encrypt_text(texto, key, iv)
            print("Texto cifrado (hex):", cifrado.hex().upper())
        except Exception as e:
            print("Error:", e)
    
    elif opcion == "2":
        hex_input = input("Introduce el texto cifrado (hex): ")
        try:
            cifrado = bytes.fromhex(hex_input)
            texto = decrypt_text(cifrado, key, iv)
            print("Texto descifrado:", texto)
        except ValueError:
            print("Error: Formato hexadecimal inválido")
        except Exception as e:
            print("Error:", e)
    
    else:
        print("Opción no válida")