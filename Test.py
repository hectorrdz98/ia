
import re

def rec(game, num=0):
    newGame = []
    for row in game:
        splitted = re.findall(r'.', ''.join(row))
        newGame.append(splitted)
    # print(newGame)
    printGame(newGame)
    if num > 0:
        newGame[1][1] = ' '
        printGame(newGame)
        return 0
    else:
        rec(newGame, num + 1)
    print('Final: ')
    printGame(newGame)

def printGame(game):
    print(' {}'.format(game[0][0]))
    print('{}{}{}'.format(game[1][0], game[1][1], game[1][2]))

if __name__ == "__main__":
    game = [
        ['*'],
        ['*', '*', '*']
    ]
    rec(game)