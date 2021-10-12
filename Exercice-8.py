from typing import Dict


class Robot:
    """ robot initialisé avec les coordonnées X,Y et la direction (optionnel, 'haut', 'bas', 'droite' ou 'gauche')"""
    
    def __init__(self, x, y, direction=None) -> None:
        self.x = x
        self.y = y
        self.dir = direction

    def avancer(self, direction:str) -> None:
        """permet au robot d'avancer d'une unité vers la direction spécifiée:'haut', 'bas', 'droite' ou 'gauche'"""

        if direction == 'haut':
            self.y += 1
        elif direction == 'bas':
            self.y -= 1
        elif direction == 'droite':
            self.x += 1
        elif direction == 'gauche':
            self.x -= 1