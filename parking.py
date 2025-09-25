from etage import *
from voiture import *
from proprietaire import *

class Parking:
    """
    Parking

    __init__:
        - nom : nom du parking
        - repartition_place : dictionnaire indiquant comment se fait la répartition des places dans les étages (dictionnaire sous la forme {numero_de_l_etage : numero_de_la_place})
        - abonnes : dictionnaire indiquant les places déjà prisent par des abonnés
    """

    def __init__(self, nom: str, repartition_place: dict, voitures: list=[], abonnes: list=[]) -> None:

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
        self.places = self.__places_parking()
        self.voitures = []
        self.place_totale = place_totale
        self.places_libres = place_totale
        self.places_occupees = 0
        self.places_reservees = []
        self.voitures_abonnes = []

        # --- Ajout des voitures à l'initialisation

        self.__ajouter_voitures__init(voitures)

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

    def __ajouter_voitures__init(self, voitures: list) -> None:
        """Ajoute des voitures dans des places libres du parking"""
        for voiture in voitures:
            place = self.trouver_place(voiture["place"])
            if place:
                if voiture["immatriculation"] not in self.__immatriculations_voitures():   
                    objet_voiture = Voiture(self, place, voiture["immatriculation"], voiture["marque"])
                    self.voitures.append(objet_voiture)
                    place.attribuer_voiture(objet_voiture)
                    objet_voiture.ajouter_proprietaire(Proprietaire(voiture["nom_proprietaire"], objet_voiture))
                    self.places_libres -= 1
                    self.places_occupees += 1
                else:
                    print("La voiture ne peut avoir la même immatriculation qu'une autre voiture")
            else:
                print("La place n'existe pas dans ce parking")

    def __ajouter_abonnes__init(self, abonnes: list) -> None:
        """Ajoute des abonnés ayant payé pour ce parking"""
        for abonne in abonnes:
            place = self.trouver_place(abonne["place"])
            if place:
                if abonne["immatriculation_voiture"] not in self.__immatriculations_voitures():
                    objet_voiture = Voiture(self, None, abonne["immatriculation"], abonne["marque"])
                    if objet_voiture.immatriculation == None:
                        print("La plaque d'immatriculation d'un abonne doit être valide")
                        return
                    abonne_objet = Abonne(abonne["nom"], objet_voiture, place)
                    objet_voiture.ajouter_proprietaire(abonne_objet)
                    place.attribuer_proprietaire(abonne_objet)
                    self.places_reservees.append(place)
                    # FINIR INITIALISATION + MODIFIER GARER POUR VERIFIER PLAQUE ABONNE ET NOM DU PROPRIETAIRE

    def __abonnes_voitures_parking(self) -> list:
        """Assesseur renvoyant la liste de l'entièreté des voitures d'abonnés"""
        voitures = []

        for place in self.places:
            if place.get_statistiques("proprietaire_de_la_place") != None:
                voiture_proprietaire = place.get_statistiques("proprietaire_de_la_place").get_statistiques("voiture")
                voitures.append(voiture_proprietaire)

        return voitures

    def __places_parking(self) -> list:
        """Assesseur renvoyant la liste de l'entièreté des places d'un parking"""
        places = []

        for etage in self.etages:
            for place in etage.get_statistiques("places"):
                places.append(place)

        return places

    def __immatriculations_voitures(self) -> list:
        """Assesseur renvoyant la liste des plaques d'immatriculation des voitures garées danns un parking"""
        immatriculations = []

        for voiture in self.voitures:
            immatriculations.append(voiture.get_statistiques("immatriculation"))

        return immatriculations

    def get_statistiques(self, statistique: str | None = None) -> dict | str | int | list | None:
        """Assesseur personnalisé de la classe retournant les différentes statistiques du parking, si 'statistique' est précisé, retourne uniquement la valeur correspondante, sinon, retourne un dictionnaire avec toutes les statistiques"""
        stats = {
            "nom": self.nom,
            "etages": self.etages,
            "places": self.places,
            "place_totale": self.place_totale,
            "places_libres": self.places_libres,
            "places_occupees": self.places_occupees,
            "places_reservees": self.places_reservees
            "voitures_abonnes": self.voitures_abonnes
        }
        if statistique is not None and statistique in stats:
            return stats[statistique]
        return stats

    def trouver_place(self, numero_place: int) -> Place | bool:
        """Trouve une place dans le parking avec son numéro,renvoie False si la place n'existe pas"""
        for place in self.places:
            if numero_place == place.get_statistiques("numero"):
                return place
        return False

    def trouver_voiture(self, immatriculation: str) -> Voiture | bool:
        """Trouve une voiture dans le parking avec son immatriculation,renvoie False si la voiture n'existe pas"""
        for voiture in self.voitures:
            if immatriculation == voiture.get_statistiques("immatriculation"):
                return voiture
        return False

    def garer_voiture(self, voiture: dict, place: int | Voiture):
        """Mutateur garant une voiture à une place si elle existe et si elle n'est pas occupée"""
        if type(place) != Voiture:
            place = self.trouver_place(place)

        if place:
            if not place.occupation:
                if voiture["immatriculation"] not in self.__immatriculations_voitures():
                    objet_voiture = Voiture(self, place, voiture["immatriculation"], voiture["marque"])
                    self.voitures.append(objet_voiture)
                    place.attribuer_voiture(objet_voiture)
                    objet_voiture.ajouter_proprietaire(Proprietaire(voiture["nom_proprietaire"], objet_voiture))
                    self.places_libres -= 1
                    self.places_occupees += 1
                else:
                    print("La voiture ne peut pas avoir la même immatriculation qu'une autre voiture.")
            else:
                print("La place est déja occupée")
        else:
            print("La place n'existe pas dans ce parking")

    def retirer_voiture(self, voiture: str | Voiture):
        """Mutateur retirant une voiture garée dans un parking"""
        if type(voiture) != Voiture:
            voiture = self.trouver_place(voiture) 

        if voiture:
            if voiture in self.voitures:
                self.voitures.remove(voiture)
                voiture.get_statistiques("place").occupation = False
                voiture.get_statistiques("place").voiture_occupant = None
                voiture.place = None
                self.places_libres += 1
                self.places_occupees -= 1

repartition = {0:23, -1:56, 5:26}
voitures = [{"immatriculation": "AA-123-AA", "marque": "Volvo", "nom_proprietaire": "Michel", "place": -101}]
abonne = [{"nom_abonne": "Jean", "immatriculation_voiture": "", "place": 105, "marque": "Volvo"}]

test = Parking("Michel", repartition, voitures)
print(test)
print(test.get_statistiques("etages")[0].get_statistiques("places")[1].get_statistiques())
print(test.get_statistiques("etages")[0].get_statistiques("places")[2].get_statistiques())

test.garer_voiture({"immatriculation": "AA-123-BA", "marque": "Volvo", "nom_proprietaire": "Michel", "place": -101}, -102)
print(test.get_statistiques("etages")[0].get_statistiques("places")[2].get_statistiques("voiture_occupant"))



parking1 = Parking("quai de seine")

assert str(parking1) == "quai de seine"