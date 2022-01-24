class Personne:
    def __init__(self, nom: str, prenom: str, ssn: str):
        self.nom = nom
        self.prenom = prenom
        self.ssn = ssn


    def Encapsuler(self):
        print("Bonjour, je m'appelle  " + self.nom + self.prenom + ", mon numéro est:  " + str(self.ssn) )

    def has_valide_ssn(self):
        return self.ssn

personne1 = Personne("Jean", "Marie", "12")
personne1.Encapsuler()
personne1.has_valide_ssn()

