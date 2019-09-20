
def isValidPos(pos):
    return True

def step(game, x, y):
    movements = [
        [ x-1, y-1 ],
        [ x-1, y ],
        [ x, y+1 ],
        [ x+1, y+1 ],
        [ x+1, y ],
        [ x, y-1 ]
    ]

    for move in movements:
        if isValidPos(move):
            pass

def getRemain(game):
    total = 0
    for row in game:
        for char in row:
            if char == '*':
                total += 1
    return total

def getNextPos(game, actPos, x, y):
    newY = actPos[1] + y + 1 if actPos[1] + y + 1 < len(game[actPos[0] + x]) else 0
    newX = actPos[0] + x     if actPos[1] + y + 1 < len(game[actPos[0] + x]) else actPos[0] + x + 1
    if newX < len(game):
        return [ newX, newY ]
    else:
        return None

def naturalMovement(game, actPos, x, y):
    print('Pos: ({}, {})'.format(actPos[0] + x, actPos[1] + y))
    actChar = game[actPos[0] + x][actPos[1] + y]
    print('actChar = {}'.format(actChar))
    print('Remain = {}'.format(getRemain(game)))
    printGame(game)

    if actChar == '*':
        print('Valid * at ({}, {})'.format(actPos[0] + x, actPos[1] + y))
        step(game, actPos[0] + x, actPos[1] + y)
    else:
        print('Valid " " at ({}, {})'.format(actPos[0] + x, actPos[1] + y))

    nextPos = getNextPos(game, actPos, x, y)
    if nextPos != None:
        naturalMovement(game, actPos, nextPos[0], nextPos[1])
    else:
        print('\n#############')
        print(' End of game')
        print('#############\n')
        return 0
    
def startNewSet(game):
    actPos = [ 0, 0 ]
    naturalMovement(game, actPos, 0, 0)

def printGame(game):
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
    game = [
        [ '*' ],
        [ '*', '*' ],
        [ '*', '*', '*' ],
        [ '*', '*', '*', '*' ],
        [ '*', '*', '*', '*', '*' ]
    ]
    game[coords[0]][coords[1]] = ' '
    startNewSet(game)
    # except:
        # print('Coordenadas invalidas')

if __name__ == "__main__":
    start()