class Operation:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def somme(self):
        return self.n1+self.n2

    def soustraction(self):
        return self.n1 - self.n2

    def multiplication(self):
        return self.n1 * self.n2

    def division(self):
        if self.n2 != 0:
            return self.n1 / self.n2
        else:
            return "Erreur : division par zéro"


O1 = Operation(20, 10)
print("Somme :", O1.somme())
print("Soustraction :", O1.soustraction())
print("Multiplication :", O1.multiplication())
print("Division", O1.division())
