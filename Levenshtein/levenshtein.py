def printM():
    print()
    for row in matrix:
        print('[', end='')
        for elem in row:
            print('{}, '.format(elem), end='')
        print(']')
    print()

s1 = 'casa'
s2 = 'cama'

matrix = [ [ ' ' for m in range(len(s2)) ] for n in range(len(s1)) ]
printM()

colsFinished = []

for i in range(len(s1)):
    for j in range(len(s2)):
        if j in colsFinished:
            matrix[i][j] = 0
        if s1[i] == s2[j] and matrix[i][j] == ' ':
            if j not in colsFinished:
                colsFinished.append(j)
                matrix[i][j] = 0
                break

printM()
