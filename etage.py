from place import *

class Etage:
    """
    Etage d'un parking
    
    __init__ :
        - parking : le parking dans lequel est l'étage
        - numero_etage : le numéro de l'étage
        - nombre_place : le nombre de place dans l'étage
    """

    def __init__(self, parking, numero_etage: int, nombre_place: int) -> None:

        places = []

        for place in range(nombre_place):
            numero_place = int(str(numero_etage) + str(place))
            if place < 100:
                numero_place = int(str(numero_etage) + "0" + str(place))
            places.append(Place(parking, self, numero_place))

        self.parking = parking
        self.numero = numero_etage
        self.places = places

    def __str__(self) -> str:
        """Affichage personnalisé de la classe"""
        return str(self.numero)

    def get_statistiques(self, statistique: str | None = None) -> dict | int | list | str | None:
        """Assesseur personnalisé de la classe retournant les différentes statistiques de l'étage.
        Si 'statistique' est précisé, retourne uniquement la valeur correspondante.
        Sinon, retourne un dictionnaire avec toutes les statistiques.
        """
        stats = {
            "parking": self.parking,
            "numero": self.numero,
            "places": self.places
        }
        if statistique is not None and statistique in stats:
            return stats[statistique]
        return stats
