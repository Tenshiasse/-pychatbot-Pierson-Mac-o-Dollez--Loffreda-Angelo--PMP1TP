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


def TF(fichier: str, repertoire: str) -> dict:
    TF_dict = {}
    fichier_path = os.path.join(repertoire, fichier)

    with open(fichier_path, "r", encoding="utf-8") as file:
        content = file.read().lower()

    words = content.split(" ")
    for word in words:
        if word in TF_dict:
            TF_dict[word] += 1
        else:
            TF_dict[word] = 1

    return TF_dict


def IDF(repertoire: str) -> dict:
    All_Tf = {}
    nombre_de_document = len(os.listdir(repertoire))

    for fichier in os.listdir(repertoire):
        All_Tf[fichier] = {}
        for mot in TF(fichier, repertoire):
            All_Tf[fichier][mot] = True

    IDF_dict = {}
    for fichier in All_Tf:
        for mot in All_Tf[fichier]:
            IDF_dict[mot] = 0
            for fichier2 in All_Tf:
                if mot in All_Tf[fichier2]:
                    IDF_dict[mot] += 1

    for mot in IDF_dict:
        IDF_dict[mot] = round(math.log10(nombre_de_document / IDF_dict[mot]), 2)

    return IDF_dict


def transposer(matrice):
    return [list(i) for i in zip(matrice)]


def TF_IDF(repertoire: str) -> dict:
    TF_IDF_dict = []
    mots = []

    for i, filename in enumerate(os.listdir(repertoire)):
        TF_IDF_dict.append([])
        for mot, value in IDF(repertoire).items():
            if value != 0:
                try:
                    TF_test = TF(filename, repertoire)[mot]
                except KeyError:
                    TF_test = 0
            else:
                TF_test = 0
            TF_IDF_dict[i].append(TF_test * value)
            mots.append(mot)

    transposed = transposer(TF_IDF_dict)
    return transposed

caca