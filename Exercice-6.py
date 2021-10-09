class Rectangle:
    """définit un rectangle avec les arguments longueur et largeur"""    
    def __init__(self, longueur, largeur) -> None:
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        return self.longueur*2 + self.largeur*2

    def aire(self):
        return self.longueur*self.largeur