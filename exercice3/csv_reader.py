import os


#class CsvException(Exception):
class CsvException(Exception):
    pass

#exception pour fichier introuvable
class FichierIntrouvableException(CsvException):
     def __init__(self, chemin):
          super().__init__(f"Fichier introuvable : {chemin}")
          self.chemin = chemin

#exception pour ligne invalide
class LigneInvalideException(CsvException):
     def __init__(self, numero_ligne, raison):
          super().__init__(f"Ligne {numero_ligne} invalide : {raison}")
          self.numero_ligne = numero_ligne
          self.raison = raison

#exception pour prix négatif
class PrixNegatifException(CsvException):
     def __init__(self, numero_ligne, valeur, raison="prix invalide"):
          super().__init__(f"Ligne {numero_ligne} : {raison} ({valeur!r}).")
          self.numero_ligne = numero_ligne
          self.valeur = valeur
          self.raison = raison


#  Lecture 
def charger_csv(chemin):
     articles = []

     # Existence du fichier 
     if not os.path.isfile(chemin):
          raise FichierIntrouvableException(chemin)

     with open(chemin, "r", encoding="utf-8") as fichier:
          # Sauter l'en-tête 
          entete = fichier.readline()
          if not entete:
               return articles 

          # Boucle sur les données, numérotation physique correcte
          for numero, ligne in enumerate(fichier, start=2):
               #  Ignorer les lignes vides 
               if not ligne.strip():
                    continue

               colonnes = ligne.strip().split(";")

               
               if len(colonnes) != 3:
                    raise LigneInvalideException(
                         numero,
                         f"{len(colonnes)} colonne(s) au lieu de 3.",
                    )

               id_article, nom, prix_str = colonnes

               #  Champ obligatoire
               if not id_article or not nom:
                    raise LigneInvalideException(
                         numero, "champ 'id' ou 'nom' vide."
                    )

               #  Prix numérique
               try:
                    prix = float(prix_str)
               except ValueError:
                    raise LigneInvalideException(
                         numero, f"le prix doit être numérique (reçu : {prix_str!r})."
                    ) from None

               #  Prix strictement positif
               if prix <= 0:
                    raise PrixNegatifException(numero, prix, "prix négatif ou nul")

               articles.append({"id": id_article, "nom": nom, "prix": prix})

     return articles