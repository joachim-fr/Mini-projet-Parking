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
            places.append(Place(parking, self, int(str(numero_etage) + str(place))))

        self.parking = parking
        self.numero = numero_etage
        self.places = places

    def __str__(self) -> str:
        """Affichage personnalisé de la classe"""
        return self.numero

    def get_statistiques(self) -> dict:
        """Assesseur personnalisé de la classe retournant les différentes statistiques de l'etage"""
        return {"parking": self.parking, "numero": self.numero, "places": self.places}
