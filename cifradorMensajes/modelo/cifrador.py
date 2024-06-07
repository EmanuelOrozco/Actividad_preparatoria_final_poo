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
        posicion: int = -1
        numeros_mensaje: list = []
        lista: list = list(mensaje)
        for caracter in lista:
            posicion += 1
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
    def desencriptar(self, mensaje: str) -> str:
        ...

    def encriptar(self, mensaje: str) -> str:
        ...

    def mensaje_valido(self, mensaje: str) -> bool:
        ...

class ReglaCifradoNumerico(ReglaCifrado):
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

