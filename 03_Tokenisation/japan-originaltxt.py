import sys

percen = 0
test = ""
train = ""
cleantxt = ""
fulltxt = ""

tokens = sys.stdin.read()

fileLength = 0

for t in tokens: # make a paragraph of full text
    if t != "\n" and " ":
        cleantxt += t
print(cleantxt)

for token in cleantxt: # make a line for each sentence
    if not token:
        continue
    if token[-1] in '!?':
        fulltxt += token 
        fulltxt += '\n' # adds line
        fileLength += 1
    elif token[-1] == '。':
        fulltxt += token 
        fulltxt += '\n' # adds line
        fileLength += 1
    else:
        fulltxt += token 

print(fulltxt)

for x in fulltxt.split(): # split files 80 and 20
    percen += 1
    if percen <= (0.8 * fileLength):
        train += x
        train += "\n"
    else:
        test += x
        test += "\n"


with open('original.txt', 'w') as sys.stdout:
                print(fulltxt)
with open('original.test.txt', 'w') as sys.stdout:
                print(test)
with open('original.train.txt', 'w') as sys.stdout:
                print(train)               

                





