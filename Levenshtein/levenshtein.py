def printM():
    print()
    for row in matrix:
        print('[', end='')
        for elem in row:
            print('{}, '.format(elem), end='')
        print(']')
    print()

s1 = 'casas'
s2 = 'cama'

matrix = [ [ 0 for m in range(len(s2)+1) ] for n in range(len(s1)+1) ]
printM()

for j in range(len(s2)+1):
    matrix[0][j] = j

for i in range(len(s1)+1):
    matrix[i][0] = i

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] != s2[j-1]: 
            matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1])+1
        else:
            matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])

print('\nMin # of modifications: {}'.format(matrix[len(s1)][len(s2)]-1 if matrix[len(s1)][len(s2)] != 0 else 0))
            

printM()
