
wins = 0

def isValidPos(game, pos):
    if pos[0] >= 0 and pos[1] >= 0:
        try:
            game[pos[0]][pos[1]]
            # print('Valid pos ({}, {})'.format(pos[0], pos[1]))
            return True
        except:
            pass
            # print('Invalid pos ({}, {})'.format(pos[0], pos[1]))
    else:
        pass
        # print('Invalid pos ({}, {})'.format(pos[0], pos[1]))
    return False

def step(game, actPos, x, y):
    movements = [
        [ x-1, y-1 ],
        [ x-1,   y ],
        [   x, y+1 ],
        [ x+1, y+1 ],
        [ x+1,   y ],
        [   x, y-1 ]
    ]

    eatMovements = [
        [ x-2, y-2 ],
        [ x-2,   y ],
        [   x, y+2 ],
        [ x+2, y+2 ],
        [ x+2,   y ],
        [   x, y-2 ]
    ]

    cont = 0

    for move in movements:
        if isValidPos(game, move):
            print('{} is a valid move'.format(move))
            if game[move[0]][move[1]] == '*':
                if isValidPos(game, eatMovements[cont]):
                    print('{} is a valid jump'.format(eatMovements[cont]))
                    if game[eatMovements[cont][0]][eatMovements[cont][1]] == ' ':
                        print('Is a perfect spot for jumping')
                        game[x][y] = ' '
                        game[move[0]][move[1]] = ' '
                        game[eatMovements[cont][0]][eatMovements[cont][1]] = '*'
                        startNewSet(game)
                    else:
                        print('Is not a good spot for jumping (*)')
            else:
                print('No a valid *')
        cont += 1
            

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
    global wins
    print('\n-------------------------------------------------------------------')
    print('\nPos: ({}, {})'.format(actPos[0] + x, actPos[1] + y))
    actChar = game[actPos[0] + x][actPos[1] + y]
    print('actChar = {}'.format(actChar))
    print('Remain = {}'.format(getRemain(game)))
    printGame(game)
    if getRemain(game) == 1:
        wins += 1
        return 0

    if actChar == '*':
        print('Valid * at ({}, {})'.format(actPos[0] + x, actPos[1] + y))
        step(game, actPos, actPos[0] + x, actPos[1] + y)
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
    print('\n################')
    print(' Start new set')
    print('################\n')
    actPos = [ 0, 0 ]
    naturalMovement(game, actPos, 0, 0)

def printGame(game):
    print('\n--------------\n')
    print('      {}'.format(game[0][0]))
    print('     {} {}'.format(game[1][0], game[1][1]))
    print('    {} {} {}'.format(game[2][0], game[2][1], game[2][2]))
    print('   {} {} {} {}'.format(game[3][0], game[3][1], game[3][2], game[3][3]))
    print('  {} {} {} {} {}'.format(game[4][0], game[4][1], game[4][2], game[4][3], game[4][4]))
    print('\n--------------\n')

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
    print('\n\nWins: {}'.format(wins))
    # except:
        # print('Coordenadas invalidas')

if __name__ == "__main__":
    start()