class Voiture:
    def __init__(self, marque, anneeDeSortie, vitesseMaximale, kilometrage):
        self.marque = marque
        self.anneeDeSortie = anneeDeSortie
        self.vitesseMaximale = vitesseMaximale
        self.kilometrage = kilometrage

    def affichage(self):
        print(f"La marque est : {self.marque}")
        print(f"La voiture date de : {self.anneeDeSortie}")
        print(f"La vitesse maximal est : {self.vitesseMaximale} km/h")
        print(f"Le kilometrage est : {self.kilometrage} km")
        print("-" * 40)


Voiture1 = Voiture("KIA", 2022, 180, 30)
Voiture2 = Voiture("Toyota", 2020, 180, 20)
Voiture1.affichage()
Voiture2.affichage()
