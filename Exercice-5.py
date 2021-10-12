class CompteBancaire:
    """Classe Compte bancaire, initialisé avec : nom puis solde"""
    def __init__(self, nom:str, solde=0) -> None:
        self.nom = nom
        self.solde = solde
    
    def depot(self, somme):
        """éthode depot : ajoute la somme spécifiée au solde"""
        self.solde += somme
    
    def retrait(self, somme):
        """éthode depot : retire la somme spécifiée au solde"""
        self.solde -= somme
    
    def affiche(self):
        """Affiche le solde actuel du compte"""
        return self.solde