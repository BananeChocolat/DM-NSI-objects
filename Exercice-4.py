class Domino:
    """Classe Domino. arguments : face1, face2"""
    def __init__(self, A:int, B:int) -> None:
        self.face1 = A
        self.face2 = B
    
    def affichePoints(self):
        return f"face A = {self.face1} & face B = {self.face2}"

    def total(self) -> int:
        return self.face1+self.face2