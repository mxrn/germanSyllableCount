import os

directory = "../syllabified_words/"
full_list = []

for fileobj in os.scandir(directory):
    if fileobj.path.endswith(".csv"):
        if fileobj.path.endswith("_full_list.csv"):
            pass
        else:
            with open(fileobj.path,'r') as entries:
                for entry in entries:
                    if entry not in full_list:
                        if entry.endswith("\n"):
                            full_list.append(entry)
                        else:
                            print(entry+"\n")
                            full_list.append(entry+"\n")

with open(directory+"_full_list.csv", mode = "w+", encoding = "utf-8") as fobj:
    for entry in set(full_list):
        fobj.write(entry)
