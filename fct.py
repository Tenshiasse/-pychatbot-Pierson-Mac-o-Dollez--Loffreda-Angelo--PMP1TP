import os
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

def occurrences(chaine):
    occurrences = {}

    mots = chaine.split()

    for mot in mots:
        occurrences[mot] = occurrences.get(mot, 0) + 1
    return occurrences

def tf(occurrences, total_mots):
    tf_scores = {}

    for mot, occurrence in occurrences.items():
        tf_scores[mot] = occurrence / total_mots

    return tf_scores

directory = "./clean"
files_names = list_of_files(directory, "txt")

for filename in files_names:
    with open(os.path.join(directory, filename), "r", encoding="utf8") as file:
        texte = file.read()
        occurrences_mots = calculer_occurrences_mots(texte)
        total_mots = len(texte.split())
        tf_scores = calculer_tf(occurrences_mots, total_mots)

        print(f"TF Scores for {filename}: {tf_scores}")