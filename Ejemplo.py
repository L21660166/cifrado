# Función para cifrar un mensaje usando el cifrado afín
def cifrado_afin(mensaje, a, b):
    # Definimos el alfabeto como una cadena de letras mayúsculas de la A a la Z
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Inicializamos una cadena vacía para almacenar el mensaje cifrado
    mensaje_cifrado = ""
    
    # Recorremos cada letra del mensaje original
    for letra in mensaje:
        # Verificamos si la letra está en el alfabeto
        if letra in alfabeto:
            # Obtenemos el índice de la letra en el alfabeto (A=0, B=1, ..., Z=25)
            x = alfabeto.index(letra)
            
            # Aplicamos la función de cifrado afín: y = (a * x + b) % 26
            y = (a * x + b) % 26
            
            # Convertimos el índice resultante (y) de nuevo a una letra y la añadimos al mensaje cifrado
            mensaje_cifrado += alfabeto[y]
        else:
            # Si la letra no está en el alfabeto (por ejemplo, un espacio o un símbolo), la añadimos sin cambios
            mensaje_cifrado += letra
    
    # Devolvemos el mensaje cifrado
    return mensaje_cifrado


# Función para descifrar un mensaje cifrado usando el cifrado afín
def descifrado_afin(mensaje_cifrado, a, b):
    # Definimos el mismo alfabeto que se usó en el cifrado
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Inicializamos una cadena vacía para almacenar el mensaje descifrado
    mensaje_descifrado = ""
    
    # Calculamos el inverso modular de 'a' módulo 26
    # El inverso modular es un número 'a_inv' tal que (a * a_inv) % 26 = 1
    a_inv = pow(a, -1, 26)
    
    # Recorremos cada letra del mensaje cifrado
    for letra in mensaje_cifrado:
        # Verificamos si la letra está en el alfabeto
        if letra in alfabeto:
            # Obtenemos el índice de la letra cifrada en el alfabeto
            y = alfabeto.index(letra)
            
            # Aplicamos la función de descifrado afín: x = (a_inv * (y - b)) % 26
            x = (a_inv * (y - b)) % 26
            
            # Convertimos el índice resultante (x) de nuevo a una letra y la añadimos al mensaje descifrado
            mensaje_descifrado += alfabeto[x]
        else:
            # Si la letra no está en el alfabeto (por ejemplo, un espacio o un símbolo), la añadimos sin cambios
            mensaje_descifrado += letra
    
    # Devolvemos el mensaje descifrado
    return mensaje_descifrado


# Ejemplo de uso del cifrado y descifrado afín
if __name__ == "__main__":
    # Definimos el mensaje original que queremos cifrar
    mensaje = "HOLA"
    
    # Definimos las constantes 'a' y 'b' para el cifrado afín
    # 'a' debe ser coprima con 26 (es decir, no debe tener factores comunes con 26)
    a, b = 5, 8
    
    # Ciframos el mensaje usando la función 'cifrado_afin'
    cifrado = cifrado_afin(mensaje, a, b)
    
    # Imprimimos el mensaje cifrado
    print("Mensaje cifrado:", cifrado)
    
    # Desciframos el mensaje cifrado usando la función 'descifrado_afin'
    descifrado = descifrado_afin(cifrado, a, b)
    
    # Imprimimos el mensaje descifrado
    print("Mensaje descifrado:", descifrado)