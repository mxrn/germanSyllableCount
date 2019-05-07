import os

directory = "../syllabified_words/"
master_list = []

for file in os.scandir(directory):
    if file.path.endswith(".csv"):
        with open(file.path,'r') as entries:
            for entry in entries:
                if entry not in master_list:
                    if entry.endswith("\n"):
                        master_list.append(entry)
                    else:
                        master_list.append(entry+"\n")
with open(directory+"_full_list.csv", mode = "w+", encoding = "utf-8") as fobj:
    for entry in set(master_list):
        fobj.write(entry)
