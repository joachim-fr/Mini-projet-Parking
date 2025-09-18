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
        self.detenteur_par_abonnement = None