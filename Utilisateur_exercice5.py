class Utilisateur:
    def __init__(self, Identifiant, nom, prenom, motPasse, etatConnexion):
        self.Identifiant = Identifiant
        self.nom = nom
        self.prenom = prenom
        self.motPasse = motPasse
        self.etatConnexion = etatConnexion

    def seConnecter(self):
        if not self.etatConnexion:
            self.etatConnexion = True
            return f"Bonjour {self.prenom} {self.nom}, vous êtes connecté(e)"
        else:
            return "Ooops, vous êtes déjà connecté(e)"

    def seDeconnecter(self):
        if self.etatConnexion:
            self.etatConnexion = False
            return f"{self.prenom} {self.nom}, vous êtes déconnecté(e)"
        else:
            return "Ooops, vous n'êtes pas connecté(e)"


U1 = Utilisateur("u1009", "Diallo", "Abdoulaye", "Rama90", False)
U2 = Utilisateur('u2003', "Bah", "Kadija", "alp098", True)

print(U1.seConnecter())
print(U1.seDeconnecter())

print("-" * 50)

print(U2.seConnecter())
print(U2.seDeconnecter())
