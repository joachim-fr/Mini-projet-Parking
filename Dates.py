class Date:
    """"
    Date

    __init__:
        - jour : jour de la date
        - mois : mois de la date
        - annee : annee de la date
    """

    __nom_mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]
    __nb_jours = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31} 

    def __init__(self, jour:int, mois:int, annee:int): 

        if jour <= 0:
            print("Le jour ne peut pas être négatif, modification à la date la plus proche : jour = 1")
            jour = 1

        if mois <= 0:
            print("Le mois ne peut pas être négatif, modification à la date la plus proche : mois = 1.")
            mois = 1

        if mois > 12:
            print("Le mois ne peut pas excéder le nombre de mois par ans, modification à la date la plus proche : mois = 12")
            mois = 12

        if mois == 2 and ((annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)) and jour >= 29:
            if jour > 29:
                print("La date ne peut pas excéder le nombre de jour du mois, modification à la date la plus proche : jour = 29.")
            jour = 29
        elif jour > Date.__nb_jours[mois]:
            print(f"La date ne peut pas excéder le nombre de jour du mois, modification à la date la plus proche : jour = {Date.__nb_jours[mois]}.")
            jour = Date.__nb_jours[mois]
                    

        self.jour = jour
        self.mois = mois
        self.annee = annee

    def __str__(self):
        """Affichage personnalisé de la classe"""
        return f"{self.jour} {Date.__nom_mois[self.mois-1]} {self.annee}"
    
    def __eq__(self, other):
        """Egalité personnalisée de la classe"""
        return self.jour == other.jour and self.mois == other.mois and self.annee == other.annee
    
    def __lt__(self, other):
        """Comparaison personnalisée de la classe"""
        if self.annee != other.annee:
            return self.annee < other.annee
        elif self.mois != other.mois:
            return self.mois < other.mois
        else:
            return self.jour < other.jour
        
    def lendemain(self):
        """Retourne la date du lendemain de la date entrant dans la méthode"""
        if self.mois == 2 and self.jour >= 28 and ((self.annee % 4 == 0 and self.annee % 100 != 0) or (self.annee % 400 == 0)):
            if self.jour == 28:
                return Date(29, 2, self.annee)
            if self.jour == 29:
                return Date(1,3, self.annee)
        else:    
            if self.mois == 12 and self.jour == 31:
                return Date(1, 1, self.annee + 1)
            elif self.jour == Date.__nb_jours[self.mois]:
                return Date(1, self.mois + 1, self.annee)
            else:
                return Date(self.jour + 1, self.mois, self.annee)

date_1 = Date(20, 1, 2012)
date_2 = Date(28, 2, 2022)

# Assert __init__

date_assert_1 = Date(32, 14, 2020)
date_assert_2 = Date(31, 2, 2024)
date_assert_3 = Date(31, 2, 2025)
date_assert_4 = Date(-6, -73, -2)

assert date_assert_1.jour == 31
assert date_assert_1.mois == 12
assert date_assert_2.jour == 29
assert date_assert_3.jour == 28

# Assert __lt__

date_assert_1 = Date(14, 6, 2024)
date_assert_2 = Date(15, 6, 2024)
date_assert_3 = Date(15, 3, 2024)
date_assert_4 = Date(14, 6, 1924)

assert date_assert_1 < date_assert_2
assert date_assert_3 < date_assert_1
assert date_assert_4 < date_assert_3

# Assert .lendemain()

date_assert_2 = Date(31, 12, 2024)
date_assert_3 = Date(28, 2, 2024)
date_assert_4 = Date(29, 2, 2024)
date_assert_5 = Date(31, 12, 2025)

assert date_assert_1.lendemain() == Date(15, 6, 2024)
assert date_assert_2.lendemain() == Date(1, 1, 2025)
assert date_assert_3.lendemain() == Date(29, 2, 2024)
assert date_assert_4.lendemain() == Date(1, 3, 2024)
assert date_assert_5.lendemain() == Date(1, 1, 2026)