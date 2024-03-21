import nltk
from collections import defaultdict
import sys
import unicodedata
import string
import collections

lines = open("wiki.txt", "r", encoding="utf-8")
corpa = lines.readlines()

# All valid characters
cv_alphabet = "aeiouаăеёĕийоуÿыэюябвгджзйклмнпрсçтфхцчшщъь"
cv_alphabet += cv_alphabet.upper() 
punct = string.punctuation

tlist = cv_alphabet.split()
valid_list = []
nonvalid_list = []

space_count = 0
format_sym_count = 0

for line in corpa:
    for word in line:
        for l in word:
            if l in cv_alphabet:
                valid_list.append(l)
            elif l in punct:
                valid_list.append(l)
            elif unicodedata.category(l) == "Zs":
                space_count +=1
                nonvalid_list.append(l)
            elif unicodedata.category(l) == "Cf":
                format_sym_count +=1
                nonvalid_list.append(l)
            else: 
                nonvalid_list.append(l)

cleanCharCount = collections.Counter(valid_list)
cleanCvChars = cleanCharCount.most_common()
print(cleanCvChars, file=sys.stdout)

print('\n''\n''\n''\n''\n')

uncleanCharCount = collections.Counter(nonvalid_list)
uncleanCvChars = uncleanCharCount.most_common()
print(uncleanCvChars, file=sys.stderr)

print(space_count, file=sys.stderr)
print(format_sym_count, file=sys.stderr)

unicodedata.normalize("NFKD", str(valid_list))
# with open('myfile.txt', 'w') as f:
#     print(charCount, file=f)


