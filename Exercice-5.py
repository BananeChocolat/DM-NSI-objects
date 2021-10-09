class CompteBancaire:
    """Classe Compte bancaire, initialisé avec : nom puis solde"""
    def __init__(self, nom, solde=0) -> None:
        self.nom = nom
        self.solde = solde
    
    def depot(self, somme):
        self.solde += somme
    
    def retrait(self, somme):
        self.solde -= somme
    
    def affiche(self):
        return self.solde