from abc import ABC, abstractmethod


class ErrorContenido(ABC, Exception):

    def __init__(self, detalles: str):
        self.detalles: str = detalles


class ContieneNoAscci(ErrorContenido):
    def __init__(self):
        super().__init__()


class ContieneNumero(ErrorContenido):
    def __init__(self):
        super().__init__()

class ErrorFormato(ABC, Exception):
    ...


class DobleEspacio(ErrorFormato):
    ...


class SinLetras(ErrorFormato):
    ...


class NoTrim(ErrorFormato):
    ...
