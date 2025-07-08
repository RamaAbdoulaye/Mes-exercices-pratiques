class client:
    def __init__(self, identifiant, nom, nas):
        self.id = identifiant
        self.nom = nom
        self._nas = nas
        self.compte = []

    def ajouterCompte(self, compte):
        self.compte.append(compte)

    def chercherCompte(self, numCpt):
        for compte in self.compte:
            if compte.numCompteC == numCpt or compte.numCompteE == numCpt:
                return compte
        return None

    @property
    def nas(self):
        return self._nas

    def Afficher(self):
        print(f"votre identifiant est : {self.id}")
        print(f"votre nom correspondant est :{self.nom}")
        print(f"votre numero d'assurance social est : {self.nas}")


class Compte:
    def __init__(self, numCptE, numCptC, sldC, sldE):
        self.numCompteC = numCptC
        self.numCompteE = numCptE
        self._soldeC = sldC
        self._soldeE = sldE
        self.proprietaire = None

    def set_propietaire(self, Client):
        self.proprietaire = Client
        Client.ajouterCompte(self)

    @property
    def soldeC(self):
        return self._soldeC

    @soldeC.setter
    def soldeC(self, value):
        if value >= 0:
            self._soldeC = value
        else:
            raise ValueError("Le solde ne peut pas être négatif")

    @property
    def soldeE(self):
        return self._soldeE

    @soldeE.setter
    def soldeE(self, value):
        if value >= 0:
            self._soldeE = value
        else:
            raise ValueError("Le solde ne peut pas être négatif")

    def deposer(self, montant):
        if montant > 0:
            self.soldeC += montant
            return f"Dépôt réussi, le montant est : {self.soldeC}"
        else:
            return "Il n'y a pas eu d'ajout"

    def retirer(self, montant):
        if montant > 0:
            if montant <= self.soldeC:
                self.soldeC -= montant
                return f"Retrait réussi, le montant actuel est : {self.soldeC}"
            else:
                return "Le montant est supérieur au solde actuel"
        else:
            return "Le montant doit etre positif"

    def transferer(self, montant, cpteDest):
        if montant > 0 and montant <= self.soldeC:
            self.soldeC -= montant
            cpteDest.soldeC += montant
            return f"{montant}$ transféré vers le compte {cpteDest.numCompteC}"
        else:
            return "le montant est superieur à votre solde"

    def Afficher(self):
        print(f"votre numero de compte courant est : {self.numCompteC}")
        print(f"votre numero de compte epargne est : {self.numCompteE}")
        print(f"votre solde du compte courant est : {self.soldeC}")
        print(f"votre solde du compte epargne est : {self.soldeE}")


class Cheque(Compte):
    def __init__(self, numCptE, numCptC, sldC, sldE, C):
        super().__init__(numCptE, numCptC, sldC, sldE)
        self.nbrCheque = C

    def demanderCheque(self):
        nombre = int(input("Combien de cheques voulez-vous demander ? "))
        if nombre > 0:
            self.nbrCheque += nombre
            return f"Vous avez demandé {nombre} cheques"
        else:
            return "Le nombre de cheques doit etre positif"

    def Afficher(self):
        super().Afficher()
        print(f"Le nombre de cheques est : {self.nbrCheque}")


class Epargne(Compte):
    def __init__(self, numCptE, numCptC, sldC, sldE, T):
        super().__init__(numCptE, numCptC, sldC, sldE)
        self.tauxInteret = T

    def Afficher(self):
        super().Afficher()
        print("Le taux d'intérêt de votre compte d'épargne est :",
              self.tauxInteret, "%")


# Création du client
c1 = client("cl001", "Diallo", "123456789")

# Création des comptes (on ne met plus les infos client ici)
compte1 = Compte("E001", "C001", 1000, 500)
compte1.set_propietaire(c1)

epargne1 = Epargne("E002", "C002", 2000, 800, 2.5)
epargne1.set_propietaire(c1)

# Opérations
print(compte1.deposer(200))
print(compte1.retirer(100))
print(compte1.transferer(150, epargne1))
# Affichages
compte1.Afficher()
epargne1.Afficher()
c1.Afficher()
