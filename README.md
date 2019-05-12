# germanSyllableCount

Knowing the number of syllables in a word can be useful for calculating readability indices. But determining the number of syllables in German words is hard for computers. Purpose of this repository is to collect words and their syllabifications in a machine-readable format. 

Examples for use cases:
- look-up tables
- statistical research
- machine learning


## Data

The data is stored in CSV files. All data files are stored in the
```syllabified_words``` directory.

All entries can be found in ```syllabified_words/_full_list.csv```

### Data records

The records are stored in CSV files.

All entries of a reviewed file are copied to ```_full_list.csv```. The file
is subsequently deleted.

A record consists of a german word and its syllabified version, separated by a comma. The syllables are separated using the pipe symbol (|).

Records are sorted alphabetically.

Examples:
```
Daten,Da|ten
Einträge,Ein|trä|ge
Silben,Sil|ben
```

## Syllabification rules

When in doubt, Duden is authoritative.

### tz

_tz_ is usually split between _t_ and _z_.

```
Katze,Kat|ze
Bodenschätze,Bo|den|schät|ze
```

### ng

_ng_ is usually split between _n_ and _g_, except when a word ends
with _ng_.

```
Lunge,Lun|ge
hängen,hän|gen
```

but

```
Verwandlung,Ver|wand|lung
Verbindung,Ver|bin|dung
```

### tion, tial

_tion_ is usually split between  _ti_ and _on_. _tial_ is usually split between  _ti_ and _al_.

```
Kommunikation,Kom|mu|ni|ka|ti|on
partitionieren,par|ti|ti|o|nie|ren
Potential,Po|ten|ti|al
```
### ck

Words are usually split before _ck_, except when _ck_ appears as part
of the last syllable.

```
Trecker,Tre|cker
abrackern,ab|ra|ckern
```

but

```
Müllsack,Müll|sack
vertrackt, ver|trackt
```

Do __not__ split _ck_, especially not into _k_ and _k_. It's
deprecated, makes spell checking harder and does not add a lot of
information regarding syllable count.

### st

There are several possibilities:

1. _st_ spoken as "s(c)ht" is kept together. It is frequently found at
   the beginning of a word or the beginning of composita, followed by
   a vowel.
2. _st_ at the end of a word is kept together.
3. _st_ followed by a vowel in the middle of a word is frequently
split (except for case 1).
4. _st_ followed by a consonant is usually kept together and marks the
   end of a syllable.

```
stehlen,steh|len
Entstehung,Ent|ste|hung
Rassist,Ras|sist
rassistisch,ras|sis|tisch
Kasten,Kas|ten
erste,ers|te
rastlos,rast|los
```
