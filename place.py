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
    
    def get_statistiques(self) -> dict:
        """Assesseur personnalisé de la classe retournant les différentes statistiques du parking"""
        return {"parking": self.parking, "numero": self.numero, "etage": self.etage, "occupation": self.occupation, "voiture_occupant": self.voiture_occupant, "propriétaire_de_la_classe": self.proprietaire_de_la_place}
