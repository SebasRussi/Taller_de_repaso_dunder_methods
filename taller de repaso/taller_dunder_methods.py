from dataclasses import dataclass


@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if self.nombre == other.nombre:
            return True
        return False


class Conjunto:

    contador = 0

    def __init__(self, nombre):
        self.elementos: list[Elemento] = []
        self.nombre = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento) -> bool:
        return elemento in self.elementos

    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)




