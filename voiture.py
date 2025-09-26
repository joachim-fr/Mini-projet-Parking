class Voiture:
    """
    Voiture garée dans un parking

    __init__ :
        - parking : parking dans lequel est garée la voiture
        - place : place ou est garée la voiture
        - immatriculation : immatriculation de la voiture
        - marque : marque de la voiture
        - proprietaire : proprietaire de la voiture
    """
    
    def __init__(self, parking, place, immatriculation: str, marque: str, proprietaire=None):

        immatriculation_corrigee = self.__correct_user_value(immatriculation)

        self.parking = parking
        self.place = place
        self.immatriculation = immatriculation_corrigee
        self.marque = marque
        self.proprietaire = proprietaire

    def __str__(self) -> str:
        """Affichge personnalisé de la classe"""
        if self.immatriculation == None:
            return "La plaque d'immatriculation de ce véhicule est incorrecte, elle ne sera donc pas prise en compte."
        return str(self.immatriculation)

    def __correct_user_value(self, immatriculation: str):
        """Correction des entrées utilisateurs"""
        immatriculation.upper()

        if len(immatriculation) != 9:
            return None
        
        if not (immatriculation[2] == '-' or immatriculation[2] == ' '):
            return None
        if not (immatriculation[6] == '-' or immatriculation[6] == ' '):
            return None
        
        for i in [0, 1, 7, 8]:
            if not ('A' <= immatriculation[i] <= 'Z'):
                return None
        for i in [3, 4, 5]:
            if not ('0' <= immatriculation[i] <= '9'):
                return None
            
        return immatriculation

    def get_statistiques(self, statistique: str | None = None) -> dict | str | int | None:
        """Assesseur personnalisé de la classe retournant les différentes statistiques de la voiture.
        Si 'statistique' est précisé, retourne uniquement la valeur correspondante.
        Sinon, retourne un dictionnaire avec toutes les statistiques.
        """
        stats = {
            "parking": self.parking,
            "place": self.place,
            "immatriculation": self.immatriculation,
            "marque": self.marque,
            "proprietaire": self.proprietaire
        }
        if statistique is not None and statistique in stats:
            return stats[statistique]
        return stats

    def ajouter_proprietaire(self, proprietaire):
        """Mutateur de l'attribu proprietaire"""
        self.proprietaire = proprietaire


if __name__ == "__main__":
    # Création d'un parking et d'une place fictifs pour les tests
    class ParkingFictif:
        pass

    class PlaceFictive:
        pass

    parking_test = ParkingFictif()
    place_test = PlaceFictive()

    # Création d'une voiture pour les tests
    voiture_test = Voiture(parking_test, place_test, "AA-123-AA", "Volvo")

    # Assert pour __init__
    assert voiture_test.immatriculation == "AA-123-AA", "L'immatriculation devrait être 'AA-123-AA'."
    assert voiture_test.marque == "Volvo", "La marque devrait être 'Volvo'."
    assert voiture_test.parking == parking_test, "Le parking devrait correspondre au parking de test."
    assert voiture_test.place == place_test, "La place devrait correspondre à la place de test."
    assert voiture_test.proprietaire is None, "Le propriétaire devrait être None initialement."

    # Assert pour __str__
    assert str(voiture_test) == "AA-123-AA", "La représentation de la voiture devrait être 'AA-123-AA'."

    # Assert pour .get_statistiques()
    stats = voiture_test.get_statistiques()
    assert stats["immatriculation"] == "AA-123-AA", "La statistique 'immatriculation' devrait être 'AA-123-AA'."
    assert stats["marque"] == "Volvo", "La statistique 'marque' devrait être 'Volvo'."
    assert stats["parking"] == parking_test, "La statistique 'parking' devrait correspondre au parking de test."
    assert stats["place"] == place_test, "La statistique 'place' devrait correspondre à la place de test."

    # Test d'une statistique spécifique
    assert voiture_test.get_statistiques("marque") == "Volvo", "La méthode devrait retourner 'Volvo' pour la statistique 'marque'."

    # Assert pour ajouter_proprietaire()
    class ProprietaireFictif:
        pass

    proprietaire_test = ProprietaireFictif()
    voiture_test.ajouter_proprietaire(proprietaire_test)
    assert voiture_test.proprietaire == proprietaire_test, "Le propriétaire devrait correspondre au propriétaire de test."

    # Assert pour __correct_user_value()
    voiture_invalide = Voiture(parking_test, place_test, "INVALID", "Tesla")
    assert voiture_invalide.immatriculation is None, "L'immatriculation invalide devrait être None."

    print("Tous les tests pour la classe Voiture sont passés avec succès.")