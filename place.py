class Place:
    """
    Place dun parking

    __init__ :
        - parking : parking dans lequel est la place
        - etage : étage ou ce trouve la place
        - numero : numero de la place (sous la forme : "numero de l'étage" + "numéro de la place dans l'étage")
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
