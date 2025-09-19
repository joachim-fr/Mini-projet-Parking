class Voiture:
    """
    Voiture garée dans un parking

    __init__ :
        - parking : parking dans lequel est garée la voiture
        - immatriculation : immatriculation de la voiture
        - marque : marque de la voiture
        - proprietaire : proprietaire de la voiture
    """
    
    def __init__(self, parking, immatriculation: str, marque: str, proprietaire):

        immatriculation_corrigee = self.__correct_user_value(immatriculation)

        self.parking = parking
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
