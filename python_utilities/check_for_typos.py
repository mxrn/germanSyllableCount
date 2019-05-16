import csv

csv_file_name = input('Name of CSV file: ')

def check_spelling(word,syllabified_word,line):
        joined_syllables = "".join(syllabified_word.split("|"))
        if word != joined_syllables:
            print("L" + str(line) + ": " + "spelling: "
                      + word + " vs. " + joined_syllables)

def check_pipe_symbol(word,syllabified_word,line):
    if "|" in word or syllabified_word.startswith("|") or syllabified_word.endswith("|"):
        print("L" + str(line) + ": " + "pipe: "
                  + word + "," + syllabified_word)

with open("../syllabified_words/" + csv_file_name, "r") as file:
    line = 0
    for row in file:
        line = line + 1
        if str(row).count(",") != 1:
            print("L" + str(line) + ": " + "comma: " + str(row).rstrip())
        
with open("../syllabified_words/" + csv_file_name) as csv_file:
    full_list = csv.reader(csv_file, delimiter = ",")
    line = 0
    for row in full_list:
        line = line + 1
        check_spelling(row[0],row[1],line)
        check_pipe_symbol(row[0],row[1],line)

