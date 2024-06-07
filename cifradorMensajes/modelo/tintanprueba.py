import string

def encontrar_numeros_mensaje(mensaje: str) -> list:
    numeros_mensaje: list = []
    for posicion, caracter in enumerate(mensaje):
        if caracter.isdigit():
            numeros_mensaje.append(posicion)
    return numeros_mensaje

def encontrar_no_ascci_mensaje(mensaje: str) -> list:
    no_ascci_mensaje: list = []
    for posicion, caracter in enumerate(mensaje):
        if ord(caracter) > 127:
            no_ascci_mensaje.append(posicion)
    return no_ascci_mensaje


alfabeto_lista = [letra for letra in string.ascii_lowercase]
encriptado: list = []
for posicion, caracter in enumerate(alfabeto_lista):
    if caracter == "g":
        encriptado.append(alfabeto_lista[posicion + 5])

print(alfabeto_lista)

def encriptar(mensaje: str, token: int) -> str:
    alfabeto_list = [letra for letra in string.ascii_lowercase]
    encriptado: list = []
    for caracter in mensaje:
        for posicion, letra in enumerate(alfabeto_list):
            if letra == caracter and posicion + token <= len(alfabeto_list):
                encriptado.append(alfabeto_list[posicion + token])
            elif letra == caracter:
                encriptado.append(alfabeto_list[(posicion + token) - len(alfabeto_list)])
    return "".join(encriptado)


mensaje_encriptado = encriptar("mensajex", 5)
print(mensaje_encriptado)