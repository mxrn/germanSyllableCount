import os

directory = "../syllabified_words/"
full_list = []
i=0
for fileobj in os.scandir(directory):
    if fileobj.path.endswith(".csv"):
        with open(fileobj.path,'r') as entries:
            print(fileobj.path)
            for entry in entries:
                if entry not in full_list:
                    if entry.endswith("\n"):
                        full_list.append(entry)
                        i=i+1
                    else:
                        print(entry+"\n")
                        full_list.append(entry+"\n")
            print('added '+str(i)+' entries from file '+fileobj.path)
i=0
with open(directory+"_full_list.csv", mode = "w+", encoding = "utf-8") as fobj:
    for entry in sorted(set(full_list)):
        fobj.write(entry)
        i=i+1
print(i)
