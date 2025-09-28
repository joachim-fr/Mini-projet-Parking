class Proprietaire:
    """
    Propriétaire d'une voiture dans un parking

    Attributs :
        - nom : le nom du propriétaire
        - voiture : la voiture possédée par le propriétaire

    Méthodes :
        - __init__ : initialise un propriétaire avec un nom et une voiture
        - get_statistiques : retourne les statistiques du propriétaire
    """

    def __init__(self, nom, voiture) -> None:
        
        self.nom = nom
        self.voiture = voiture

    def get_statistiques(self, statistique: str | None = None) -> dict | str | int | list | None:
        """Assesseur personnalisé de la classe retournant les différentes statistiques du parking, si 'statistique' est précisé, retourne uniquement la valeur correspondante, sinon, retourne un dictionnaire avec toutes les statistiques"""
        stats = {
            "nom": self.nom,
            "voiture": self.voiture
        }
        if statistique is not None and statistique in stats:
            return stats[statistique]
        return stats

    

class Abonne(Proprietaire):
    """
    Abonné possédant une place réservée dans un parking

    Attributs :
        - nom : le nom de l'abonné (hérité de Proprietaire)
        - voiture : la voiture possédée par l'abonné (hérité de Proprietaire)
        - place : la place réservée par l'abonné

    Méthodes :
        - __init__ : initialise un abonné avec un nom, une voiture et une place
        - get_statistiques : retourne les statistiques de l'abonné
    """

    def __init__(self, nom, voiture, place) -> None:
        super().__init__(nom, voiture)

        self.place = place

    def get_statistiques(self, statistique: str | None = None) -> dict | str | int | list | None:
        """Assesseur personnalisé de la classe retournant les différentes statistiques du parking, si 'statistique' est précisé, retourne uniquement la valeur correspondante, sinon, retourne un dictionnaire avec toutes les statistiques"""
        stats = {
            "nom": self.nom,
            "voiture": self.voiture,
            "place": self.place
        }
        if statistique is not None and statistique in stats:
            return stats[statistique]
        return stats

if __name__ == "__main__":
    # Création d'une voiture fictive pour les tests
    class VoitureFictive:
        pass

    voiture_test = VoitureFictive()

    # Création d'un propriétaire pour les tests
    proprietaire_test = Proprietaire("Michel", voiture_test)

    # Assert pour __init__ de Proprietaire
    assert proprietaire_test.nom == "Michel", "Le nom du propriétaire devrait être 'Michel'."
    assert proprietaire_test.voiture == voiture_test, "La voiture du propriétaire devrait correspondre à la voiture de test."

    # Assert pour .get_statistiques() de Proprietaire
    stats = proprietaire_test.get_statistiques()
    assert stats["nom"] == "Michel", "La statistique 'nom' devrait être 'Michel'."
    assert stats["voiture"] == voiture_test, "La statistique 'voiture' devrait correspondre à la voiture de test."

    # Test d'une statistique spécifique pour Proprietaire
    assert proprietaire_test.get_statistiques("nom") == "Michel", "La méthode devrait retourner 'Michel' pour la statistique 'nom'."

    # Création d'un abonné pour les tests
    class PlaceFictive:
        pass

    place_test = PlaceFictive()
    abonne_test = Abonne("Alice", voiture_test, place_test)

    # Assert pour __init__ de Abonne
    assert abonne_test.nom == "Alice", "Le nom de l'abonné devrait être 'Alice'."
    assert abonne_test.voiture == voiture_test, "La voiture de l'abonné devrait correspondre à la voiture de test."
    assert abonne_test.place == place_test, "La place de l'abonné devrait correspondre à la place de test."

    # Assert pour .get_statistiques() de Abonne
    stats_abonne = abonne_test.get_statistiques()
    assert stats_abonne["nom"] == "Alice", "La statistique 'nom' devrait être 'Alice'."
    assert stats_abonne["voiture"] == voiture_test, "La statistique 'voiture' devrait correspondre à la voiture de test."
    assert stats_abonne["place"] == place_test, "La statistique 'place' devrait correspondre à la place de test."

    # Test d'une statistique spécifique pour Abonne
    assert abonne_test.get_statistiques("place") == place_test, "La méthode devrait retourner la place de test pour la statistique 'place'."

    print("Tous les tests pour les classes Proprietaire et Abonne sont passés avec succès.")