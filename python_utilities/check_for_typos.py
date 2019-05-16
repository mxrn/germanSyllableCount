import csv

csv_file_name = input('Name of CSV file: ')

with open("../syllabified_words/" + csv_file_name) as csv_file:
    full_list = csv.reader(csv_file, delimiter = ",")
    line = 0
    for row in full_list:
        line = line + 1
        joined_syllables = "".join(row[1].split("|"))
        if row[0] != joined_syllables:
            print("Error in line " + str(line) + ": "
                      + row[0] + " vs. " + joined_syllables)
