class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def surface(self):
        return self.longueur*self.largeur


R1 = Rectangle(5, 15)
R2 = Rectangle(30, 78)
print("Surface du Rectangle 1 est : ", R1.surface())
print("Surface du rectangle 2 est : ", R2.surface())
