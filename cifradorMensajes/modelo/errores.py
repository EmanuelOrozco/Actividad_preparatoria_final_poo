from abc import ABC, abstractmethod

class ErrorContenido(ABC, Exception):
    @abstractmethod
    def __init__(self, detalles: str):
        ...


class ContieneNoAscci(ErrorContenido):
    def __init__(self):
        super().__init__()


class ContieneNumero(ErrorContenido):
    ...


class ErrorFormato(ABC, Exception):
    ...


class DobleEspacio(ErrorFormato):
    ...


class SinLetras(ErrorFormato):
    ...


class NoTrim(ErrorFormato):
    ...