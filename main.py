from fct import list_of_files
import os
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)

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
print(list_nom)
