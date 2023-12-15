import os
def list_of_files(directory, extension):

 files_names = []
 for filename in os.listdir(directory):
    if filename.endswith(extension):
        files_names.append(filename)
 return files_names

def filemodif(files_names):
    for i in range(len(files_names)):
        f_name = files_names[i]
        afiles = open(f_name, "w")
        clean = afiles.read().lower()
        clean = clean.replace("'"," ")
        clean = clean.replace("!"," ")
        clean = clean.replace(".", " ")
        clean = clean.replace(",", " ")
        clean = clean.replace(":", " ")
        clean = clean.replace(";", " ")
        clean = clean.replace("-", " ")
        clean = clean.replace("?", " ")



    afiles.close()