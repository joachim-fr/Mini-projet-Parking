from etage import *

class Parking:
    """
    Parking

    __init__:
        - nom : nom di parking
        - repartition_place : dictionnaire indiquant comment se fait la répartition des places dans les étages (dictionnaire sous la forme {numero_de_l_etage : numero_de_la_place})
        - abonnes : dictionnaire indiquant les places déjà prisent par des abonnés
    """

    def __init__(self, nom:str, repartition_place:dict, abonnes:dict={}) -> None:

        place_totale = 0
        etages = []

        # --- Correction de la repartition des étages ---

        repartition_place_corrigee = self.__correct_user_value(repartition_place)

        # ---

        for etage, place in repartition_place_corrigee.items():
            etages.append(Etage(self, etage, place))
            place_totale += place

        self.nom = nom
        self.etages = etages
        self.place_totale = place_totale
        self.place_libre = place_totale
        self.place_occupee = 0

    def __str__(self) -> str:
        """Affichage personnalisé de la classe"""
        return self.nom
    
    def __correct_user_value(self, repartition_place: dict):
        """Correction des entrées utilisateurs"""
        liste_etages = []
        liste_places = []

        liste_etages_corrigee = []
        liste_places_corrigee = []

        repartition_place_corrigee = {}

        for etage, places in repartition_place.items():
            liste_etages.append(etage)
            liste_places.append(places)

        etage_reference = min(liste_etages, key=lambda e: abs(e))
        liste_places_corrigee.append(liste_places[liste_etages.index(etage_reference)])
        liste_places.pop(liste_etages.index(etage_reference))
        liste_etages.pop(liste_etages.index(etage_reference))
        liste_etages_corrigee.append(etage_reference)

        while any(etage > 0 for etage in liste_etages):
            etage_test = min(liste_etages, key=lambda e: e if e > 0 else float('inf'))

            liste_places_corrigee.append(liste_places[liste_etages.index(etage_test)])
            liste_places.pop(liste_etages.index(etage_test))

            if max(liste_etages_corrigee) - etage_test == -1:
                liste_etages_corrigee.append(etage_test)
                liste_etages.pop(liste_etages.index(etage_test))
            else:
                liste_etages_corrigee.append(max(liste_etages_corrigee) + 1)
                liste_etages.pop(liste_etages.index(etage_test))

        while len(liste_etages) != 0:
            etage_test = max(liste_etages)

            liste_places_corrigee.insert(0, liste_places[liste_etages.index(etage_test)])
            liste_places.pop(liste_etages.index(etage_test))

            if min(liste_etages_corrigee) - etage_test == 1:
                liste_etages_corrigee.insert(0, etage_test)
                liste_etages.pop(liste_etages.index(etage_test))
            else:
                liste_etages_corrigee.insert(0, min(liste_etages_corrigee) - 1)
                liste_etages.pop(liste_etages.index(etage_test))        

        for i in range(len(liste_etages_corrigee)):
            repartition_place_corrigee[liste_etages_corrigee[i]] = liste_places_corrigee[i]

        return repartition_place_corrigee

    def get_statistiques(self) -> dict:
        """Assesseur personnalisé de la classe retournant les différentes statistiques du parking"""
        return {"nom": self.nom, "etages": self.etages, "place_totale": self.place_totale, "place_libre": self.place_libre, "place_occupee": self.place_occupee}

repartition = {0:23, 1:56, 5:26}

test = Parking("Michel", repartition)
print(test)
print(test.get_statistiques()["etages"])