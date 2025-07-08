class vehicule:
    def __init__(self, marque, couleur, vitesse=0):
        self.marque = marque
        self.couleur = couleur
        self.vitesse = vitesse

    def deplacer(self):
        if self.vitesse > 0:
            print(f"Le vehicule, {self.marque} est en mouvement ")
        else:
            return f"Le vehicule {self.marque}, est qu repot"


class voiture(vehicule):
    def __init__(self, marque, couleur, vitesse=0, nbrePorte=4):
        super().__init__(marque, couleur, vitesse)
        self.nbrePorte = nbrePorte

    def deplacer(self):
        return f"La voiture {self.marque} roule à {self.vitesse} km/h."


class velo(vehicule):
    def __init__(self, marque, couleur, vitesse=0, roue=2):
        super().__init__(marque, couleur, vitesse)
        self.roue = roue

    def deplacer(self):
        return f"Le velo {self.marque} roule à {self.vitesse} km/h."
