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

if __name__ == "__main__":
    # Création d'un parking fictif pour les tests
    class ParkingFictif:
        pass

    parking_test = ParkingFictif()

    # Création d'un étage pour les tests
    etage_test = Etage(parking_test, numero_etage=1, nombre_place=5)

    # Assert pour __init__
    assert etage_test.numero == 1, "Le numéro de l'étage devrait être 1."
    assert len(etage_test.places) == 5, "L'étage devrait contenir 5 places."

    # Assert pour __str__
    assert str(etage_test) == "1", "La représentation de l'étage devrait être '1'."

    # Assert pour .get_statistiques()
    stats = etage_test.get_statistiques()
    assert stats["numero"] == 1, "La statistique 'numero' devrait être 1."
    assert stats["parking"] == parking_test, "La statistique 'parking' devrait correspondre au parking de test."
    assert len(stats["places"]) == 5, "La statistique 'places' devrait contenir 5 places."

    # Test d'une statistique spécifique
    assert etage_test.get_statistiques("numero") == 1, "La méthode devrait retourner 1 pour la statistique 'numero'."
    assert etage_test.get_statistiques("places") == etage_test.places, "La méthode devrait retourner les places pour la statistique 'places'."

    print("Tous les tests pour la classe Etage sont passés avec succès.")
