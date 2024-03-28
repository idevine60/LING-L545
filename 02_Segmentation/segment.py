import sys 

abbrevs = ['Б-то.', 'б.', 'г.', 'м.', 'у.', 'без доп.', 'д.-в.-н.', 'д.-в.-нем.', 'и.о.', 'И.О.', 'м.б.', 'п. г. т.', 'п.т.ч.', 'ст.', 'д.п.', 'и.', 'тс.', 'я.']
line = sys.stdin.readline()

while line:
    for token in line.strip().split():
        if not token:
            continue
        if token[-1] in '!?':
            sys.stdout.write(token + '\n') # adds line
        elif token[-1] == '.':
            if token in abbrevs:
                    sys.stdout.write(token + ' ' ) # doesn't add line
            else:
                    sys.stdout.write(token + '\n') # adds line
        else:
            sys.stdout.write(token + ' ') # doesn't add line
    line = sys.stdin.readline()
