class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque  
        self.modele = modele  

    def demarrer(self):
        print(f"La {self.marque} {self.modele} démarre.")

