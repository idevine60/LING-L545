import sys

percen = 0
dictionary = ""
for line in sys.stdin:
    line = line.strip()
    percen += 1
    if line not in dictionary:
        dictionary += line
        dictionary += '\n'
   

with open('dictionary.txt', 'w') as sys.stdout:
                print(dictionary)
             
# print(percen)





