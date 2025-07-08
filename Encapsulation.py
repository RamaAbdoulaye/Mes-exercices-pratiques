class Etudiant:
    def __init__(self, nom, note):
        self.nom = nom
        self._note = note

    def set_note(self, note):
        self._note = note
        return note

    def get_note(self):
        return self.get_note
