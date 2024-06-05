'''
from abc import ABC, abstractmethod

class AbcAnimal(ABC):

    @abstractmethod
    def verso(self):

        pass


class Cane(AbcAnimal):
    def __init__(self, name: str) -> None:
        
        self.name: str = name
    
    def verso(self):
        
        print("Bau!")

class Gatto(AbcAnimal):
    def __init__(self, name: str) -> None:
        
        self.name: str = name
    
    def verso(self):
        
        print("Miao!")

class Coccodrillo(AbcAnimal):

    def __init__(self, name: str):
        
        self.name: str = name

    def verso(self):

        print("****")

gatto_1: Gatto = Gatto(name="Silverstro")
coccodrillo_1: Coccodrillo = Coccodrillo(name="Gianni")
cane_1: Cane = Cane(name="Pluto")

lista_animali: list[AbcAnimal] = [cane_1, gatto_1, coccodrillo_1]
for animale in lista_animali:
    animale.verso()

# gatto_1.verso()
# cane_1.verso()
# coccodrillo_1.verso()

a: dict[str, int | str] = {
    "key_1" : "val_1",
    "key_2" : "val_2",
    "key_3" : 3
}

from typing import Any

b: dict[str, Any] = {
    "key_1" : "val_1",
    "key_2" : "val_2",
    "key_3" : 3,
    "key_4" : [1, 2]
}

'''
i: int = 0

assert i == 0, f"the value must be equal to 0 insted of is {i}"


