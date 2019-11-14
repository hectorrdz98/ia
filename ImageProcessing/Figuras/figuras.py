import cv2
import matplotlib.pyplot as plt
import math

alpha4Circle = 4

def getShape(val):
    if (len(val['borders']) == 4):
        lenghts = [
            val['borders'][1][1] - val['borders'][0][1],
            val['borders'][3][0] - val['borders'][1][0],
            val['borders'][3][1] - val['borders'][2][1],
            val['borders'][3][0] - val['borders'][0][0]
        ]
        if len(set(lenghts)) == 1:
            return 'Square'
        return 'Rectangle'
    else:
        centroid = getCentroid(val)
        minR = None
        maxR = None

        for coords in val['perimeter']:
            tempR = math.sqrt(
                pow(abs(centroid[0] - coords[0]), 2) + 
                pow(abs(centroid[1] - coords[1]), 2)
            )

            if not minR: 
                minR = tempR
                maxR = tempR
            else:
                if tempR < minR: minR = tempR
                if tempR > maxR: maxR = tempR
        
        if maxR - minR <= alpha4Circle:
            return 'Circle'

        return 'Unidentified'

def getCentroid(val):
    promX = sum([ x[0] for x in val['pixels'] ]) / len(val['pixels'])
    promY = sum([ x[1] for x in val['pixels'] ]) / len(val['pixels'])
    return [ promX, promY ]


img = cv2.imread('figurasHD.png', 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

figures = {}

for n in range(len(img)):
    for i in range(len(img[n])):

        actPix = img[n][i]
        # print('[{}, {}]: {}'.format(n, i, actPix))
        flag = 0

        if (actPix != 255):
            
            if (img[n-1][i] == actPix or img[n-1][i] == 0): flag += 1
            if (img[n+1][i] == actPix or img[n+1][i] == 0): flag += 1
            if (img[n][i-1] == actPix or img[n][i-1] == 0): flag += 1
            if (img[n][i+1] == actPix or img[n][i+1] == 0): flag += 1

            if (flag > 0):
                if actPix in figures:
                    figures[actPix]['pixels'].append([n, i])
                else:
                    figures[actPix] = {'perimeter': [], 'pixels': [ [n,i] ] }
            else:
                figures[actPix] = {'perimeter': [], 'pixels': [ [n,i] ] }
            
            preColor = actPix

            if (1 <= flag <= 2):
                if 'borders' in figures[actPix]:
                    figures[actPix]['borders'].append([n,i])
                else:
                    figures[actPix]['borders'] = [ [n,i] ]

            if (flag > 0 and flag < 4):
                img[n][i] = 0
                actPix = img[n][i]
                figures[preColor]['perimeter'].append([n,i])

cont = 1
for key,val in figures.items():
    print('\nFig #{}\nColor: {}\nPerimeter: {}\nArea: {}'.format(cont, key, len(val['perimeter']), len(val['pixels'])))
    print('Borders: {}'.format(len(val['borders'])))
    print('Centroid: {}'.format(getCentroid(val)))
    print('Shape: {}'.format(getShape(val)))
    cont += 1


cv2.imwrite('figurasHD.jpg', img)