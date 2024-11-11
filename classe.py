class Rectangle:
   
    def __init__(self, largeur, hauteur):
        self.largeur = largeur  
        self.hauteur = hauteur  

    
    def surface(self):
        return self.largeur * self.hauteur

    
    def afficher_dimensions(self):
        print(f"Largeur : {self.largeur}, Hauteur : {self.hauteur}")


mon_rectangle = Rectangle(5, 10)


print(mon_rectangle.surface()) 
mon_rectangle.afficher_dimensions()  
