class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def changer_age(self, nouvel_age):
        self.age = nouvel_age

personne1 = Personne("Alice", 30)
print(personne1.age)          
personne1.changer_age(31)     
print(personne1.age)          


