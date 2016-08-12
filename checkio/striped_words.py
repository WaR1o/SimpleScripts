# check the number of words where the vowels and consonants are alternating
# (no two vowels or consonants), words with one letter doesn't counts
import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

patt1 = re.compile(r'([AEIOUY][BCDFGHJKLMNPQRSTVWXZ])+')
patt2 = re.compile(r'([BCDFGHJKLMNPQRSTVWXZ][AEIOUY])+')
# split text in list of words
text = "My name is ..."
text = text.upper().split()
words_list = []
for n in range(len(text)):
    if text[n].isalpha():
        words_list.append(text[n])
# check each word in the list that it match the pattern and increment the count
counter = 0
for i in words_list:
    for l in words_list[i]:
        if len(words_list[i]) > 1 and patt1.match(words_list) or patt2.match(words_list):
           counter += 1
return counter
