from parking import Parking
from voiture import Voiture
from proprietaire import Abonne

# Création d'un parking fictif avec 5 niveaux et 30 places par niveau
repartition = {0: 30, 1: 30, 2: 30, 3: 30, 4: 30}

# Création de voitures fictives
voitures = [
    {"immatriculation": "AA-123-AA", "marque": "Volvo", "nom_proprietaire": "Michel", "place": 1},
    {"immatriculation": "BB-456-BB", "marque": "Toyota", "nom_proprietaire": "Jean", "place": 2},
    {"immatriculation": "CC-789-CC", "marque": "Tesla", "nom_proprietaire": "Alice", "place": 3}
]

# Création d'abonnés fictifs
abonnes = [
    {"nom": "Alice", "immatriculation": "CC-789-CC", "place": 3, "marque": "Tesla"},
    {"nom": "Paul", "immatriculation": "DD-000-DD", "place": 4, "marque": "Ford"}
]

# Initialisation du parking
parking_test = Parking("Parking Test", repartition, voitures, abonnes)

# Affichage des statistiques du parking
print("Statistiques du parking :")
print(parking_test.get_statistiques())

# Vérification des places libres et occupées
print("\nPlaces libres :", parking_test.places_libres)
print("Places occupées :", parking_test.places_occupees)

# Vérification des abonnés
print("\nPlaces réservées aux abonnés :", len(parking_test.places_reservees))
print("Voitures des abonnés :", [voiture for voiture in parking_test.get_statistiques("voitures_abonnes")])

# Représentation d'un niveau du parking
niveau = parking_test.get_statistiques("etages")[0]
representation = ["O" if place.get_statistiques("occupation") else " a" for place in niveau.get_statistiques("places")]
print("\nReprésentation du niveau 0 :")
print("".join(representation))

# Liste des places d'abonnés occupées par d'autres voitures
places_occupees_abonnes = [
    place.get_statistiques("numero")
    for place in parking_test.get_statistiques("places")
    if place.get_statistiques("proprietaire_de_la_place") and place.get_statistiques("occupation")
    and place.get_statistiques("voiture_occupant").get_statistiques("immatriculation") != place.get_statistiques("proprietaire_de_la_place").get_statistiques("voiture").get_statistiques("immatriculation")
]
print("\nPlaces d'abonnés occupées par d'autres voitures :", places_occupees_abonnes)

# Nombre de places libres sans compter les places réservées aux abonnés
places_libres_sans_abonnes = parking_test.places_libres - len(parking_test.places_reservees)
print("\nNombre de places libres sans compter les places réservées aux abonnés :", places_libres_sans_abonnes)