class Place:
    """
    Place d'un parking

    Attributs :
        - parking : le parking auquel appartient la place
        - etage : l'étage auquel appartient la place
        - numero : le numéro unique de la place
        - occupation : indique si la place est occupée (True) ou libre (False)
        - voiture_occupant : la voiture occupant la place (None si la place est libre)
        - proprietaire_de_la_place : le propriétaire de la place (None si la place n'est pas réservée)

    Méthodes :
        - __init__ : initialise une place avec un parking, un étage et un numéro
        - __str__ : retourne le numéro de la place sous forme de chaîne
        - get_statistiques : retourne les statistiques de la place
        - attribuer_voiture : attribue une voiture à la place
        - attribuer_proprietaire : attribue un propriétaire à la place
    """

    def __init__(self, parking, etage, numero: int) -> None:
        self.parking = parking
        self.etage = etage
        self.numero = numero
        self.occupation = False
        self.voiture_occupant = None
        self.proprietaire_de_la_place = None

    def __str__(self) -> str:
        """Affichage personnalisé de la classe"""
        return str(self.numero)
    
    def get_statistiques(self, statistique: str | None = None) -> dict | int | bool | str | None:
        """Assesseur personnalisé de la classe retournant les différentes statistiques du parking.
        Si 'statistique' est précisé, retourne uniquement la valeur correspondante.
        Sinon, retourne un dictionnaire avec toutes les statistiques.
        """
        stats = {
            "parking": self.parking,
            "numero": self.numero,
            "etage": self.etage,
            "occupation": self.occupation,
            "voiture_occupant": self.voiture_occupant,
            "proprietaire_de_la_place": self.proprietaire_de_la_place
        }
        if statistique is not None and statistique in stats:
            return stats[statistique]
        return stats

    def attribuer_voiture(self, voiture) -> None:
        """Attribue une voiture a une place"""
        if self.occupation:
            print("La place est déjà occupée.")
        else:
            self.occupation = True
            self.voiture_occupant = voiture
    
    def attribuer_proprietaire(self, proprietaire) -> None:
        """Attribue un abonné à une place"""
        if self.proprietaire_de_la_place == None:
            self.proprietaire_de_la_place = proprietaire
        else:
            print("La place est déjà réservée")

if __name__ == "__main__":
    # Création d'un parking et d'un étage fictifs pour les tests
    class ParkingFictif:
        pass

    class EtageFictif:
        pass

    parking_test = ParkingFictif()
    etage_test = EtageFictif()

    # Création d'une place pour les tests
    place_test = Place(parking_test, etage_test, numero=101)

    # Assert pour __init__
    assert place_test.numero == 101, "Le numéro de la place devrait être 101."
    assert place_test.occupation is False, "La place devrait être initialement libre."
    assert place_test.voiture_occupant is None, "Aucune voiture ne devrait occuper la place initialement."

    # Assert pour __str__
    assert str(place_test) == "101", "La représentation de la place devrait être '101'."

    # Assert pour .get_statistiques()
    stats = place_test.get_statistiques()
    assert stats["numero"] == 101, "La statistique 'numero' devrait être 101."
    assert stats["occupation"] is False, "La statistique 'occupation' devrait indiquer que la place est libre."
    assert stats["voiture_occupant"] is None, "La statistique 'voiture_occupant' devrait être None."

    # Test d'une statistique spécifique
    assert place_test.get_statistiques("numero") == 101, "La méthode devrait retourner 101 pour la statistique 'numero'."
    assert place_test.get_statistiques("occupation") is False, "La méthode devrait indiquer que la place est libre."

    # Assert pour attribuer_voiture()
    class VoitureFictive:
        pass

    voiture_test = VoitureFictive()
    place_test.attribuer_voiture(voiture_test)
    assert place_test.occupation is True, "La place devrait être occupée après l'attribution d'une voiture."
    assert place_test.voiture_occupant == voiture_test, "La voiture attribuée devrait occuper la place."

    # Assert pour attribuer_proprietaire()
    class ProprietaireFictif:
        pass

    proprietaire_test = ProprietaireFictif()
    place_test.attribuer_proprietaire(proprietaire_test)
    assert place_test.proprietaire_de_la_place == proprietaire_test, "Le propriétaire attribué devrait être enregistré."

    print("Tous les tests pour la classe Place sont passés avec succès.")
