# 🔐 Práctica de Criptografía 🔐
Este repositorio contiene una colección de implementaciones de diferentes algoritmos criptográficos clásicos y modernos desarrollados en Python. ¡Explora y aprende sobre criptografía de manera interactiva!

## 📂 Contenido
### 📜 ejercicio1_1.py - Cifrado César
El clásico cifrado por desplazamiento usado por Julio César. Permite cifrar textos desplazando cada letra un número fijo de posiciones en el alfabeto.

- ✅ Cifra mensajes con cualquier desplazamiento entre 0-25
- 🔍 Descifra mostrando todas las posibles combinaciones
- 🔤 Conserva números y símbolos sin cambios

### 🔠 ejercicio1_2.py - Codificación Base64
Implementación de Base64, un método para codificar datos binarios en texto ASCII.

- 🔄 Convierte texto a formato Base64
- 🔙 Decodifica mensaje Base64 a su formato original
- 🧩 Maneja la conversión entre bytes y texto automáticamente

### 🗝️ ejercicio1_3.py - Cifrado Vigenère
Una evolución del cifrado César que usa una clave para cifrar, haciendo mucho más difícil el criptoanálisis.

- 🔒 Cifra usando una palabra clave que determina desplazamientos variables
- 🔓 Descifra conociendo la clave original
- 📝 Procesa solo caracteres alfabéticos, normalizando a mayúsculas


### ⚡ ejercicio1_4.py - Cifrado XOR
Un cifrado simple pero efectivo basado en la operación XOR bit a bit.

- ⚙️ Aplica operación XOR entre el texto y la clave
- 🔄 El mismo algoritmo sirve para cifrar y descifrar
- 🔁 Cíclico con claves de cualquier longitud

### 🛡️ ejercicio1_5.py - Cifrado AES
Implementa el estándar Advanced Encryption Standard, un algoritmo de cifrado por bloques.

- 🔐 Soporta modo AES-ECB (Electronic Codebook)
- 🧩 Soporta modo AES-CBC (Cipher Block Chaining) con vector de inicialización
- 📊 Incluye manejo automático de padding PKCS7
- 📤 Salida en formato hexadecimal para fácil visualización