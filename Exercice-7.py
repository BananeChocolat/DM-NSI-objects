from random import randint

class Personnage:
    """definit un personnage avec son nom et ses PV (entre 75 et 150)"""
    def __init__(self, name, hp) -> None:
        self.name = name
        self.hp = hp

    def combat(self, other):
        other.hp -= randint(5, 15)