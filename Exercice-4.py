class Domino:
    """Classe Domino. arguments : face1, face2"""
    def __init__(self, A:int, B:int) -> None:
        self.face1 = A
        self.face2 = B
    
    def affichePoints(self):
        """affiche les faces du domino"""
        print(f"face A = {self.face1} & face B = {self.face2}")
    
    def total(self) -> int:
        """renvoie la somme des 2 faces"""
        return self.face1+self.face2