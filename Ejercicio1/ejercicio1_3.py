# Esta línea es un comentario que indica la ruta del archivo

def vigenere_encrypt(plaintext, key):
    
    plaintext = ''.join(c for c in plaintext.upper() if c.isalpha()) # coge todos los caracteres alfabéticos, los convierte a mayúsculas y los une en una nueva cadena
    
    key = ''.join(c for c in key.upper() if c.isalpha()) # lo mismo con la clave
    
    if len(key) == 0: # si la clave esta vacía
        return plaintext # devuelve el texto sin cifrar
    
    ciphertext = "" # almacena texto cifrado
    
    key_index = 0 # contador de la clave
    
    for char in plaintext:
        
        if char.isalpha(): # si es un caracter alfabético
            
            # Convert letters to numbers (A=0, B=1, etc.)
            shift = ord(key[key_index % len(key)]) - ord('A') # c
            # Calcula el desplazamiento según el carácter actual de la clave
            # key_index % len(key) permite usar la clave cíclicamente
            # ord(key[...]) - ord('A') convierte la letra de la clave a un número (0-25)
            
            # Apply the shift and wrap around if needed
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # Aplica el desplazamiento:
            # 1. Convierte el carácter a un número (0-25)
            # 2. Suma el desplazamiento
            # 3. Aplica módulo 26 para asegurar que está en el rango 0-25
            # 4. Convierte de nuevo a un carácter ASCII
            
            ciphertext += encrypted_char
            # Añade el carácter cifrado al resultado
            
            # Move to the next character in the key
            key_index += 1
            # Avanza al siguiente carácter de la clave
            
        else:
            ciphertext += char
            # Si no es una letra, lo añade sin modificar
            
    return ciphertext
    # Devuelve el texto cifrado

def vigenere_decrypt(ciphertext, key):
    # Define una función para descifrar usando Vigenère
    
    # Convert to uppercase and remove non-alphabetic characters
    ciphertext = ''.join(c for c in ciphertext.upper() if c.isalpha())
    # Convierte el texto cifrado a mayúsculas y elimina caracteres no alfabéticos
    
    key = ''.join(c for c in key.upper() if c.isalpha())
    # Hace lo mismo con la clave
    
    if len(key) == 0:
        # Comprueba si la clave está vacía
        return ciphertext
        # Si está vacía, devuelve el texto sin descifrar
    
    plaintext = ""
    # Inicializa una cadena vacía para el texto descifrado
    
    key_index = 0
    # Inicializa un contador para la clave
    
    for char in ciphertext:
        # Itera sobre cada carácter del texto cifrado
        
        if char.isalpha():
            # Verifica si es una letra
            
            # Convert letters to numbers (A=0, B=1, etc.)
            shift = ord(key[key_index % len(key)]) - ord('A')
            # Calcula el desplazamiento según el carácter actual de la clave
            
            # Apply the reverse shift and wrap around if needed
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            # Aplica el desplazamiento inverso:
            # La diferencia con el cifrado es que aquí resta en lugar de sumar
            
            plaintext += decrypted_char
            # Añade el carácter descifrado al resultado
            
            # Move to the next character in the key
            key_index += 1
            # Avanza al siguiente carácter de la clave
            
        else:
            plaintext += char
            # Si no es una letra, lo añade sin modificar
            
    return plaintext
    # Devuelve el texto descifrado

while True:
    # Inicia un bucle infinito que solo se detendrá con exit()
    
    print("Quieres codificar o decodificar?")
    print("------------")
    print("1- Codificar")
    print("2- Decodificar")
    print("0- Salir")
    print("------------")
    # Muestra un menú con las opciones disponibles
    
    number = input("Introduzca la opcion: ")
    # Pide al usuario que elija una opción

    if number == "0":
        # Si elige salir
        exit()
        # Termina el programa
        
    elif number == "1":
        # Si elige codificar
        message = input("Introduce el texto a codificar: ")
        # Pide el texto a codificar
        
        key = input("Introduce la clave: ")
        # Pide la clave para la codificación
        
        encoded = vigenere_encrypt(message, key)
        # Llama a la función de cifrado de Vigenère
        
        print(f"Codificado: {encoded}")
        # Muestra el resultado
        
    elif number == "2":
        # Si elige decodificar
        message = input("Introduce el texto a decodificar: ")
        # Pide el texto cifrado
        
        key = input("Introduce la clave: ")
        # Pide la clave para decodificar
        
        decoded = vigenere_decrypt(message, key)
        # Llama a la función de descifrado de Vigenère
        
        print(f"Decodificado: {decoded}")
        # Muestra el resultado
        
    else:
        # Si introdujo una opción no válida
        print("Opción no válida. Intente de nuevo.")
        # Muestra un mensaje de error