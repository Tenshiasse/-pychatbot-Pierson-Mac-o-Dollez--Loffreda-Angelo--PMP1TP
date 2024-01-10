from fct import list_of_files
from fct import clean
from fct import TF_IDF
from fct import mot_pas_important
from fct import mot_important
from fct import mot_plus_repeter_par_chirac
from fct import nation
from fct import ecologie
import os
import time
directory = "./speeches"
files_names = list_of_files(directory, "txt")

#--------------------------------#

list_nom = []
for filename in files_names:
    if 'Nomination_Chirac1.txt' in filename:
        nom = 'Chirac'
        if nom not in list_nom:
            list_nom.append(nom)
    elif 'Nomination_Chirac2.txt' in filename:
        nom = 'Chirac'
        if nom not in list_nom:
            list_nom.append(nom)
    elif 'Nomination_Giscard dEstaing.txt' in filename:
        nom = 'Giscard dEstaing'
        if nom not in list_nom:
            list_nom.append(nom)
    elif 'Nomination_Hollande.txt' in filename:
        nom = 'Hollande'  # Fixed the typo in 'Hollande'
        if nom not in list_nom:
            list_nom.append(nom)
    elif 'Nomination_Macron.txt' in filename:
        nom = 'Macron'
        if nom not in list_nom:
            list_nom.append(nom)
    elif 'Nomination_Mitterrand1.txt' in filename:
        nom = 'Mitterrand'
        if nom not in list_nom:
            list_nom.append(nom)
    elif 'Nomination_Mitterrand2.txt' in filename:
        nom = 'Mitterrand'
        if nom not in list_nom:
            list_nom.append(nom)
# print(list_nom)#

#------------------------------

list_prenom = list_nom
for i in range(len(list_prenom)):
    if list_prenom[i] == 'Chirac':
        list_prenom[i] = 'Jacques Chirac'
    elif list_prenom[i] == 'Giscard dEstaing':
        list_prenom[i] = 'Valéry Giscard dEstaing'
    elif list_prenom[i] == 'Hollande':
        list_prenom[i] = 'François Hollande'
    elif list_prenom[i] == 'Macron':
        list_prenom[i] = 'Emmanuel Macron'
    elif list_prenom[i] == 'Mitterand':
        list_prenom[i] = 'François Mitterrand'
#print(list_prenom)#

#--------------------------------#

fichier_clean = clean("./speeches")

#--------------------------------#

for filename in files_names:
    rep = os.path.join("./clean")
    tf_idf = TF_IDF(rep)

#print(tf_idf)#

#--------------------------------#

n=1
while n!=8:
    print("Pour afficher tout les noms des répertoires tapez 1")
    time.sleep(0.5)
    print("Pour afficher les noms des présidents tapez 2")
    time.sleep(0.5)
    print("Pour afficher les noms et prénoms des présidents tapez 3")
    time.sleep(0.5)
    print("Pour afficher tout le TF_IDF tapez 4")
    time.sleep(0.5)
    print("Pour afficher tout les mots important du TF_IDF tapez 5")
    time.sleep(0.5)
    print("Pour afficher tout les mots peu important du TF_IDF tapez 6")
    time.sleep(0.5)
    print("Pour afficher tout les mots les plus répéter par Chirac tapez 7")
    time.sleep(0.5)
    print("Pour afficher tout les mots en rapport avec la nation tapez 8")
    time.sleep(0.5)
    print("Pour afficher tout les mots en rapport avec l'écologie tapez 9")
    print("Pour arrêter le programme tapez 10")

    time.sleep(0.5)
    n=0
    while n<1 or n>11 :
        n = int(input("Tapez le numéro auquel vous voulez accéder :"))

    if n==1 :
        print(files_names)
    elif n==2:
        print(list_nom)
    elif n==3:
        print(list_prenom)
    elif n==4:
        print(tf_idf)
    elif n==5:
        print(mot_important())
    elif n==6:
        print(mot_pas_important())
    elif n==7:
        print(mot_plus_repeter_par_chirac())
    elif n==8:
        print(nation(list_prenom))
    elif n==9:
        print(ecologie(list_prenom))
    elif n==10:
        print("Merci à bientôt !")
    time.sleep(5)
