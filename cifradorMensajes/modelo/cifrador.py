import string
from abc import abstractmethod, ABC


class ReglaCifrado(ABC):
    def __init__(self, token: int):
        self.token: int = token

    @abstractmethod
    def mensaje_valido(self, mensaje: str) -> bool:
        ...

    @abstractmethod
    def encriptar(self, mensaje: str) -> str:
        ...

    @abstractmethod
    def desencriptar(self, mensaje: str) -> str:
        ...

    def encontrar_numeros_mensaje(self, mensaje: str) -> list:
        numeros_mensaje: list = []
        for posicion, caracter in enumerate(mensaje):
            if caracter.isdigit():
                numeros_mensaje.append(posicion)
        return numeros_mensaje

    def encontrar_no_ascci_mensaje(self, mensaje: str) -> list:
        no_ascci_mensaje: list = []
        for posicion, caracter in enumerate(mensaje):
            if ord(caracter) > 127:
                no_ascci_mensaje.append(posicion)
        return no_ascci_mensaje


class ReglaCifradoTraslacion(ReglaCifrado):
    def __init__(self, token: int):
        super().__init__(token)

    def desencriptar(self, mensaje: str) -> str:
        if self.mensaje_valido(mensaje):
            ...


    def encriptar(self, mensaje: str, token: int) -> str:
        if self.mensaje_valido(mensaje):
            alfabeto_list = [letra for letra in string.ascii_lowercase]
            encriptado: list = []
            for caracter in mensaje:
                for posicion, letra in enumerate(alfabeto_list):
                    if letra == caracter and posicion + token <= len(alfabeto_list):
                        encriptado.append(alfabeto_list[posicion + token])
                    elif letra == caracter:
                        encriptado.append(alfabeto_list[(posicion + token) - len(alfabeto_list)])
            return "".join(encriptado)

    def mensaje_valido(self, mensaje: str) -> bool:
        ...

class ReglaCifradoNumerico(ReglaCifrado):
    def __init__(self, token: int):
        super().__init__(token)

    def encriptar(self, mensaje: str) -> str:
        ...

    def desencriptar(self, mensaje: str) -> str:
        ...

    def mensaje_valido(self, mensaje: str) -> bool:
        ...


class Cifrador:
    def __init__(self, agente: ReglaCifrado):
        self.agente: ReglaCifrado = agente

    def encriptar(self, mensaje: str) -> str:
        ...

    def desencriptar(self, mensjae: str) -> str:
        ...

