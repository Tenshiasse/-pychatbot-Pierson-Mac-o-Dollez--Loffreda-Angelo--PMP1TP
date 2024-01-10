import os
import math
def list_of_files(directory, extension):

 files_names = []
 for filename in os.listdir(directory):
    if filename.endswith(extension):
        files_names.append(filename)
 return files_names

def clean(directory):
    clean_directory = os.path.join("./", 'clean')
    if not os.path.exists(clean_directory):
        os.makedirs(clean_directory)

    fichiers = [f for f in os.listdir(directory) if f.endswith(".txt")]

    for fichier in fichiers:
        directory_entree = os.path.join(directory, fichier)
        directory_sortie = os.path.join(clean_directory, fichier)

        with open(directory_entree, "r", encoding="utf8") as entree:
            lignes = entree.readlines()

        liste = []
        for ligne in lignes:
            liste.append(str(ligne).replace("\n", " "))

        liste = [ligne.replace("'", " ").replace("!", " ").replace(".", " ").replace(",", " ").replace(":", " ")
                 .replace(";", " ").replace("-", " ").replace("?", " ").replace("  ", " ").replace("   ", " ")
                 .replace("    ", " ").replace("     ", " ").lower() for ligne in liste]

        with open(directory_sortie, "w", encoding="utf8") as sortie:
            for ligne in liste:
                sortie.write(ligne)