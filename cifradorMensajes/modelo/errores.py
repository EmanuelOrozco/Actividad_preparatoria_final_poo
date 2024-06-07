from abc import ABC, abstractmethod


class ErrorContenido(ABC, Exception):
    def __init__(self, detalles: str):
        super().__init__(detalles)


class ContieneNoAscci(ErrorContenido):
    def __init__(self, detalles: str):
        super().__init__(detalles)


class ContieneNumero(ErrorContenido):
    def __init__(self, detalles: str):
        super().__init__(detalles)


class ErrorFormato(ABC, Exception):
    def __init__(self):
        super().__init__()


class DobleEspacio(ErrorFormato):
    def __init__(self):
        super().__init__()


class SinLetras(ErrorFormato):
    def __init__(self):
        super().__init__()


class NoTrim(ErrorFormato):
    def __init__(self):
        super().__init__()
