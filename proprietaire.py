class Proprietaire:
    """
    Propriétaire d'une voiture dans un parking

    __init__ :
        - nom : nom du propriétaire
        - voiture : voiture possédée
    """

    def __init__(self, nom, voiture) -> None:
        
        self.nom = nom
        self.voiture = voiture

    

class Abonne(Proprietaire):
    """
    Abonné possédant une place

    __init__ :
        Les mêmes attributs pour un propriétaire sont requis
        - place : place que l'abonné détient
    """

    def __init__(self, nom, voiture, place) -> None:
        super().__init__(nom, voiture)

        self.place = place
