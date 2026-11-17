
from csv_reader import charger_csv ,FichierIntrouvableException,LigneInvalideException,PrixNegatifException


if __name__ == "__main__":

     chemin = "exercice3/articles.csv"

     try:
          articles = charger_csv(chemin)

          print("Importation réussie !")
          print("Liste des articles :")

          for article in articles:
               print(article)

     except FichierIntrouvableException as e:
          print("Erreur :", e)

     except LigneInvalideException as e:
          print("Erreur de format :", e)

     except PrixNegatifException as e:
          print("Erreur de prix :", e)

