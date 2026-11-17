#exception pour les réservations
class ReservationException(Exception):
     def __init__(self, message):
          super().__init__(message)


#exception pour la capacité dépassée
class CapaciteDepasseeException(ReservationException):
     def __init__(self, message="Capacité maximale dépassée."):
          super().__init__(message)

#exception pour le nombre de places invalide
class NombreInvalideException(ReservationException):
     def __init__(self, message="Nombre de places invalide (doit être > 0)."):
          super().__init__(message)

#exception pour le nom du client invalide
class NomClientInvalideException(ReservationException):
     def __init__(self, message="Nom du client requis (non vide)."):
          super().__init__(message)

#la classe représentant un événement
class Evenement:
     def __init__(self, nom, capacite):
          self.nom = nom
          self.capacite = capacite
          self.places_reservees = 0

     def reserver(self, nom_client, nb_places):
          if not nom_client.strip():
               raise NomClientInvalideException("Nom du client requis.")
          if nb_places <= 0:
               raise NombreInvalideException("Nombre de places invalide.")
          if self.places_reservees + nb_places > self.capacite:
               raise CapaciteDepasseeException("Capacité dépassée.")

          self.places_reservees += nb_places
          print(f"Réservation confirmée pour {nom_client} ({nb_places} places).")

     def afficher(self):
          print(f"Événement: {self.nom} — {self.places_reservees}/{self.capacite} places réservées")