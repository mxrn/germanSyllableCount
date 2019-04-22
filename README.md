# germanSyllableCount

Knowing the number of syllables in a word can be useful for calculating readability indices. But determining the number of syllables in German words is hard for computers. Purpose of this repository is to collect words and their syllabifications in a machine-readable format. 

Examples for use cases:
- look-up tables
- statistical research
- machine learning


## Data

The data is stored in CSV files. All data files are stored in the ```syllabified_words``` directory.

### Data records

The records are stored in CSV files. A single file covers a specific part of speech and relates to a domain e. g. biology or medicine.

A record consists of a german word and its syllabified version, separated by a comma. The syllables are separated using the pipe symbol (|).

Records are sorted alphabetically.

Examples:
```
Daten,Da|ten
Einträge,Ein|trä|ge
Silben,Sil|ben
```

### File names

File names are used to add some semantic to the lists. File names have the following format:

```
language.partOfSpeech.grammar.domain.subdomain.csv
```



