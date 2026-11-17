
from Exception_reservation import Evenement, ReservationException

if __name__ == "__main__":
    event = Evenement("Formation Python", 40)
    print(f"{event.nom} (capacité {event.capacite}) \n")

    #  Cas d'erreurs 
    for nom, nb in [(" ", 2), ("Assiya", 0), ("Salma", -1), ("Mostapha", 10)]:
          try:
               event.reserver(nom, nb)
          except ReservationException as e:
               print(f" Erreur ({nom!r}, {nb}) : {e}")

    #  Réservations valides 
    event.reserver("Yasmine", 3)
    event.reserver("Fatima", 2)

    event.afficher()