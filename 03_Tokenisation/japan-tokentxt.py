import sys

percen = 0
ttokens = []
body = ""
fulltxt = ""
test = ""
train = ""

tokens = sys.stdin.read()
fileLength = 0

ttokens.append(tokens.strip())

# print(ttokens)

# for t in tokens:
#     ttokens.append(t.strip().split("\n"))

ttokens = " ".join(ttokens)
# print(ttokens)

for t in ttokens:

        body += t

body = body.replace("\n", " ") # paragraph of full text
# print(body)



for token in body: # make a line for each sentence
    # if not token:
    #     continue
    # print(token)
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

# print(fulltxt)
print(fulltxt.split("\n"))

for x in fulltxt.split("\n"): # split files 80 and 20
    print(x)
    percen += 1
    if percen <= (0.8 * fileLength):
        train += x
        train += "\n"
    else:
        test += x
        test += "\n"



with open('tokenized.txt', 'w') as sys.stdout:
                print(fulltxt)
with open('tokenized.test.txt', 'w') as sys.stdout:
                print(test)
with open('tokenized.train.txt', 'w') as sys.stdout:
                print(train)               
# print(percen)



