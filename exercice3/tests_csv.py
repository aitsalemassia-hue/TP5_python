import tempfile
import unittest
from pathlib import Path

from csv_reader import charger_csv,FichierIntrouvableException,LigneInvalideException,PrixNegatifException


class TestCSV(unittest.TestCase):
     def setUp(self):
          
          self.tmp = tempfile.TemporaryDirectory()
          self.addCleanup(self.tmp.cleanup)
          self.fichier = str(Path(self.tmp.name) / "articles.csv")

     def ecrire(self, contenu):
          Path(self.fichier).write_text(contenu, encoding="utf-8")

    # Cas nominal 
     def test_csv_valide(self):
          self.ecrire(
               "id;nom;prix\n"
               "Article1;Clavier;200\n"
               "Article2;Souris;150\n"
               "Article3;Écran;300\n"
               "Article4;Casque;100\n"
          )
          articles = charger_csv(self.fichier)
          self.assertEqual(len(articles), 4)
          self.assertEqual(articles[0]["nom"], "Clavier")
          self.assertEqual(articles[0]["prix"], 200.0)
          self.assertEqual(articles[3]["nom"], "Casque")

     # Fichier absent 
     def test_fichier_absent(self):
          with self.assertRaises(FichierIntrouvableException) as ctx:
               charger_csv(str(Path(self.tmp.name) / "nope.csv"))
          self.assertIn("nope.csv", ctx.exception.chemin)

     # Prix non numérique 
     def test_prix_non_numerique(self):
          self.ecrire("id;nom;prix\n1;Ordi;abc\n")
          with self.assertRaises(LigneInvalideException):
               charger_csv(self.fichier)

     #  Prix négatif 
     def test_prix_negatif(self):
          self.ecrire("id;nom;prix\n1;Ordi;-500\n")
          with self.assertRaises(PrixNegatifException):
               charger_csv(self.fichier)

     #  Prix nul 
     def test_prix_zero(self):
          self.ecrire("id;nom;prix\n1;Ordi;0\n")
          with self.assertRaises(PrixNegatifException):
               charger_csv(self.fichier)

     #  Colonne manquante 
     def test_colonne_manquante(self):
          self.ecrire("id;nom;prix\n1;Ordi\n")
          with self.assertRaises(LigneInvalideException):
               charger_csv(self.fichier)

     #  Colonne excédentaire 
     def test_colonne_excedentaire(self):
          self.ecrire("id;nom;prix\n1;Ordi;500;extra\n")
          with self.assertRaises(LigneInvalideException):
               charger_csv(self.fichier)

     #  Lignes vides ignorées 
     def test_lignes_vides_ignorees(self):
          self.ecrire(
               "id;nom;prix\n"
               "1;Ordi;500\n"
               "\n"
               "2;Clavier;200\n"
               "\n"
          )
          articles = charger_csv(self.fichier)
          self.assertEqual(len(articles), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)