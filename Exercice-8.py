class Robot:
    """ robot initialisé avec les coordonnées X,Y et la direction (optionnel, 'haut', 'bas', 'droite' ou 'gauche')"""
    def __init__(self, x, y, direction=None) -> None:
        self.x = x
        self.y = y
        self.dir = direction

    def avancer(self):
        if self.dir == 'haut':
            self.y += 1
        elif self.dir == 'bas':
            self.y -= 1
        elif self.dir == 'droite':
            self.x += 1
        elif self.dir == 'gauche':
            self.x -= 1