from fct import list_of_files
from fct import filemodif
import os
directory = "./speeches"
files_names = list_of_files(directory, "txt")
'''--------------------------------'''
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
#------------------------------
for i in range(len(list_nom)):
    if list_nom[i] == 'Chirac':
        list_nom[i] = 'Jacques Chirac'
    elif list_nom[i] == 'Giscard dEstaing':
        list_nom[i] = 'Valéry Giscard dEstaing'
    elif list_nom[i] == 'Hollande':
        list_nom[i] = 'François Hollande'
    elif list_nom[i] == 'Macron':
        list_nom[i] = 'Emmanuel Macron'
    elif list_nom[i] == 'Mitterand':
        list_nom[i] = 'François Mitterrand'
print(list_nom)

#minuscules clean

filemodif(files_names)