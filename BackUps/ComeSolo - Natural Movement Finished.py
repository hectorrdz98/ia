
game = [
    [ '*' ],
    [ '*', '*' ],
    [ '*', '*', '*' ],
    [ '*', '*', '*', '*' ],
    [ '*', '*', '*', '*', '*' ]
]

goal = [ 3, 3 ]
actPos = [ 0, 0 ]

def getNextPos(x, y):
    newY = actPos[1] + y + 1 if actPos[1] + y + 1 < len(game[actPos[0] + x]) else 0
    newX = actPos[0] + x     if actPos[1] + y + 1 < len(game[actPos[0] + x]) else actPos[0] + x + 1
    if newX < len(game):
        return [ newX, newY ]
    else:
        return None

def naturalMovement(x, y):
    printGame()
    print('Pos: ({}, {})'.format(actPos[0] + x, actPos[1] + y))
    actChar = game[actPos[0] + x][actPos[1] + y]
    print('actChar = {}'.format(actChar))

    if actChar == '*':
        print('Valid * at ({}, {})'.format(actPos[0] + x, actPos[1] + y))
    else:
        print('Valid " " at ({}, {})'.format(actPos[0] + x, actPos[1] + y))

    nextPos = getNextPos(x, y)
    if nextPos != None:
        naturalMovement(nextPos[0], nextPos[1])
    else:
        print('\n#############')
        print(' End of game')
        print('#############\n')
        return 0

def printGame():
    print('\n----------------------------------\n')
    for row in game:
        for char in row:
            print(char, end='\t')
        print()
    print('\n----------------------------------\n')

def start():
    # print('Ingresa el white space: ', end='')
    print('White space en ({}, {}) '.format(1, 0))
    # try:
        #coords = [ int(coord) for coord in input().split(',') ]
    coords = [1,0]
    game[coords[0]][coords[1]] = ' '
    naturalMovement(0, 0)
    # except:
        # print('Coordenadas invalidas')

if __name__ == "__main__":
    start()