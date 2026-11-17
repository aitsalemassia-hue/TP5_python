
from Exceptions_compte_Bancaire import CompteBancaire, MontantNegatifException, SoldeInsuffisantException, TransactionException


if __name__ == "__main__":
     compte = CompteBancaire("Assiya", 1050)
     print("Compte initial:")
     compte.afficher()


     #test des opérations valides
     compte.deposer(50)
     print("Après dépôt de 50DH:")
     compte.afficher()
     compte.retirer(30)
     print("Après retrait de 30DH:")
     compte.afficher()
    #  retrait supérieur au solde
     try:
          compte.retirer(2000)
     except SoldeInsuffisantException as e:
          print("Erreur:", e)   

    #  dépôt négatif
     try:
          compte.deposer(-50)
     except MontantNegatifException as e:
          print("Erreur:", e)

    #  capture générique via la classe mère
     try:
          compte.retirer(-10)
     except TransactionException as e:
          print("Erreur (générique):", e)

     