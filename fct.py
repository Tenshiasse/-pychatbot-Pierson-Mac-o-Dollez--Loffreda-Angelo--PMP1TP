import os
import math

#Resource dans une liste chaque fichier texte#
def list_of_files(directory, extension):

 files_names = []
 for filename in os.listdir(directory):
    if filename.endswith(extension):
        files_names.append(filename)
 return files_names

#--------------------------------#

#Fonction permetant de nettoyer les fichiers textes du dossier fourni par l'utilisateur#
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

#--------------------------------#

#TF_IDF créer pour permettre de calculer les valeur de répétition d'un motdans les discours de président pour voir les mots avec les plus important#
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

#Fonction transposage, permet d'interchanger les colonnes et les lignes pour la fonction TF_IDF#
def transposer(matrice):
    return [list(i) for i in zip(*matrice)]

def TF_IDF(repertoire):
    TF_IDF_dict = []
    mots = []
    for i in range(len(os.listdir(repertoire))):
        TF_IDF_dict.append([])
        for mot, value in IDF(repertoire).items():
            if value != 0:
                try:
                    TF_test = TF(os.listdir(repertoire)[i], repertoire)[mot]
                except:
                    TF_test = 0
            else:
                TF_test = 0
            TF_IDF_dict[i].append(TF_test * value)
            mots.append(mot)

#On retourne la transposer pour avoir le TF_IDF complet#

    transposed = transposer(TF_IDF_dict)
    return transposed

#--------------------------------#

def mot_pas_important():
    tf_idf = TF_IDF("clean")
    mot_non_impotant=[]
    for i in range(len(tf_idf[1])):
        s=0
        for j in range(len(tf_idf[1][i])):
            if tf_idf[1][i][j]==0.0:
                s+=1
        if s==len(tf_idf[1][i]):
            mot_non_impotant.append(tf_idf[0][i])
    return mot_non_impotant
#Cette fonction retourne la list de mots qui ont le TF-IDF le plus élévée dans le dossier cleaned. Il n'y a donc pas besoin de mettre une variable pour appeler cette fonction.

def mot_important():
    tf_idf = TF_IDF("clean")
    mot_impotant=[]
    val=[]
    M=0
    for i in range(len(tf_idf[1])):
        s=0
        for j in range(len(tf_idf[1][i])):
            s+=tf_idf[1][i][j]
        if s>M:                             #recherche de maximum
           M=s
        val.append([s,i])
    for i in range(len(val)):
       if val[i][0]==M:
            mot_impotant.append(tf_idf[0][val[i][1]])
    return mot_impotant
#Retourne la list des mots les plus répété par le président Chirac en enlevant les mots nom impartant. Il n'y a pas besoin de mettre de variable en entré.

#--------------------------------#

def mot_plus_repeter_par_chirac():
    TF_score = {}
    mot_plus_dit= []
    files = list_of_files("clean", "txt")
    for i in range(0,2):                            #calcule le nombre de fois que chriac à prononcé un mot
        with open("clean/"+files[i], "r", encoding="utf-8") as f1:
            line = f1.readline()
            while line != "":
                k = TF(line)
                for keys in k.keys():
                    if keys in TF_score.keys() :
                        TF_score[keys] += k[keys]
                    else :
                        TF_score[keys] = k[keys]
                line = f1.readline()
    M=0
    for key,values in TF_score.items() :            #recherche le maximum de fois que chirac à proncé un même mot
        if values>M:
            mot_plus_dit= []
            mot_plus_dit.append(key)
        else:
            if values==M:
                mot_plus_dit.append(key)
    return mot_plus_dit
#Cette fonction renvoie le nom du ou des présidents qui ont le plus parler de la Nation. C'est pour cela qu'il n'y apas de varable en entré.

#--------------------------------#

def nation(list):
    president = list_of_files("clean", "txt")
    president = list
    tf_idf = TF_IDF("clean")
    n=0
    i=0
    while i <len(tf_idf[0]) and tf_idf[0][i]!="nation":
        i+=1
    n=i
    m=1
    i=0
    while i<len(tf_idf[1][n-1]):
        if tf_idf[1][n][i]!=0.0:
            if m>tf_idf[1][n][i]:
                m=tf_idf[1][n][i]
                nom=president[i]
            i+=1
        else:
            del(president[i])
            del(tf_idf[1][n][i])
    president=retourne_nom_president(president)
    print(f"Le nom des présidents qui ont le parler de la nation sont {president} et celui qui en à le plus parler est {nom}.")
#retourne de nom du premier président qui à parler de l'écologie et/ou du réchauffement climatique. Il n'y a donc pas de variable d'entré.

#--------------------------------#

def ecologie(list):
    president_nom=["Giscard dEstaing","Mitterrand","Chirac","Hollande","Sarkozy","Macron"]
    president = list_of_files("clean", "txt")
    president = list
    tf_idf = TF_IDF("clean")
    n=0
    i=0
    while i <len(tf_idf[0]) and tf_idf[0][i]!="écologique":
        i+=1
    n=i
    nom=len(president_nom)
    for i in range(len(tf_idf[1][n-1])):
        if tf_idf[1][n][i]!=0.0:
            for j in range(len(president_nom)):
                if president[i]== president_nom[j] and j<nom:
                    nom=j
    print(f"Le premier président qui a parlé de l'écologie est {president_nom[nom]}.")
#Cette fonction renvoie les mots évoquées par tous les présidents et qui ne sont pas non important.Elle n'a pas besoin de variable d'entré pour cette raison.

