
# --------------- VIGENERE ENCRYPT ---------------
def vigenere_encrypt(plaintext, key):
    """Cifra un texto usando el cifrado Vigenère"""
    if not key:
        return plaintext.upper()
    
    # Prepara el texto y la clave
    plaintext = ''.join(c for c in plaintext.upper() if c.isalpha())
    key = ''.join(c for c in key.upper() if c.isalpha())
    
    result = ""
    for i, char in enumerate(plaintext):
        # Calcula el desplazamiento y aplica el cifrado directamente
        shift = ord(key[i % len(key)]) - ord('A')
        result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    
    return result

# --------------- VIGENERE DECRYPT ---------------
def vigenere_decrypt(ciphertext, key):
    """Descifra un texto cifrado con Vigenère"""
    if not key:
        return ciphertext.upper()
    
    # Prepara el texto cifrado y la clave
    ciphertext = ''.join(c for c in ciphertext.upper() if c.isalpha())
    key = ''.join(c for c in key.upper() if c.isalpha())
    
    result = ""
    for i, char in enumerate(ciphertext):
        # Calcula el desplazamiento inverso y descifra
        shift = ord(key[i % len(key)]) - ord('A')
        result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
    
    return result

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
        encoded = vigenere_encrypt(message, key)
        print(f"Codificado: {encoded}")
    elif number == "2":
        message = input("Introduce el texto a decodificar: ")
        key = input("Introduce la clave: ")
        decoded = vigenere_decrypt(message, key)
        print(f"Decodificado: {decoded}")
    else:
        print("Opción no válida. Intente de nuevo.")