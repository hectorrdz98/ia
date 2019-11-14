def printM():
    print()
    for row in matrix:
        print('[', end='')
        for elem in row:
            print('{}, '.format(elem), end='')
        print(']')
    print()

s1 = 'pedro'
s2 = 'pdroo'

matrix = [ [ 0 for j in range(len(s2)+1) ] for i in range(len(s1)+1) ]

for j in range(len(s2)+1):
    matrix[0][j] = j

for i in range(len(s1)+1):
    matrix[i][0] = i

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        mod = 1
        if (s1[i-1] == s2[j-1]): mod = 0
        matrix[i][j] = min([matrix[i][j-1]+1, matrix[i-1][j]+1, matrix[i-1][j-1]+mod])

print('\nMin # of modifications: {}'.format(matrix[len(s1)][len(s2)]))

printM()