from random import randint

class Personnage:
    """definit un personnage avec son nom et ses PV (indication: entre 75 et 150)"""
    def __init__(self, name:str, hp:int) -> None:
        self.name = name
        self.hp = hp

    def combat(self, other):
        """méthode combat : attaque le personnage spécifié"""
        other.hp -= randint(5, 15) # retire entre 5 et 15 pv à 'hp' de l'adversaire