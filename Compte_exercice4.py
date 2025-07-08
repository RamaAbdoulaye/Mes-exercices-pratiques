class Compte:
    def __init__(self, SoldeInitial):
        self.Solde = SoldeInitial

    def Deposer(self):
        entrer = int(input("Entrer le montant du depôt : "))
        if entrer > 0:
            self.Solde += entrer
            return f"Depôt reusi, le montant est : {self.Solde} $"
        else:
            return "il n'ya pas eu d'ajout"

    def Retirer(self):
        retirer = int(input("Saisissez le montant a retirer : "))
        if retirer > 0:
            self.Solde -= retirer
            return f" Le solde actuel est egal à : {self.Solde}"
        elif retirer > self.Solde:
            return "Le montant est superieur au solde"
        else:
            return "il n'ya pas eu de retrait"


C1 = Compte(500)
C2 = Compte(60)
print(C2.Deposer())
print(C2.Retirer())

print("-" * 40)

print("Compte 1 :")
print(C1.Deposer())
print(C1.Retirer())
