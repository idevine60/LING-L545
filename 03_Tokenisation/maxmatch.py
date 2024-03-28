import sys


f = open(sys.argv[1], "r") # the dictionary

dictt = []
out = []
for line in f:
    dictt.append(line.strip())

def maxMatch(sentence, dictionary):
    if sentence is None or sentence == "":
        return []
    i = len(sentence)
    # print(i)
    while i > 0:
        firstword = sentence[:i]
        # print(firstword)
        remainder = sentence[i:]
        # print(remainder)
        if firstword in dictionary:
            return [firstword] + maxMatch(remainder, dictionary)
        i -= 1
        
    firstword =  sentence[0]
    remainder = sentence[1:]
    return [firstword] + maxMatch(remainder, dictionary)

# print(dictt)
sent = sys.stdin.readline() # the hypothesis sentences
while sent:
    # print(sent)
    words = maxMatch(sent, dictt)
    print(' '.join(words))
    sent = sys.stdin.readline() # the hypothesis sentences

    # print("Dict item!:" + line)


