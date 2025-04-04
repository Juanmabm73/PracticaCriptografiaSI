import base64

# --------------- ENCODE_BASE64 ---------------
def encode_base64(data):

    if isinstance(data, str): # comprobamos si data es un string        
        data = data.encode('utf-8') # la convertimos a bytes mediante UTF-8
    
    encoded = base64.b64encode(data) # codificamos esos datos que hemos pasado a bytes en base64
    
    return encoded.decode('utf-8') # transformamos la cadena codificada y la devolvemos

# --------------- DECODE_BASE64 ---------------
def decode_base64(encoded_data):
    
    if isinstance(encoded_data, str):        
        encoded_data = encoded_data.encode('utf-8')
    
    decoded = base64.b64decode(encoded_data) # decodificamos los datos de base64
    
    return decoded.decode('utf-8') # convertimos lo bytes a texto y lo devolvemos


# --------------- MAIN ---------------
number = "" 

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
        
        code = input("Introduce el texto a codificar: ")
        
        encoded = encode_base64(code)
        
        print(f"Codificado: {encoded}")
        
    elif number == "2":
        
        code = input("Introduce el texto a decodificar: ")
        
        decoded = decode_base64(code)
        
        print(f"Decodificado: {decoded}")
        
    else:
        # Si el usuario introdujo cualquier otro valor
        
        print("Opción no válida. Intente de nuevo.")
        # Muestra un mensaje de error