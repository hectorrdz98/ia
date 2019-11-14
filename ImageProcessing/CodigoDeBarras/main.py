import cv2
import re
import matplotlib.pyplot as plt
import values as v

img = cv2.imread('Examples/example1.png', 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lineMax = 120
lineMaxTones = [20, 245]
firstLine = [ [0, 0], [0, 0] ]

finish = False

for i in range(len(img)):
    for j in range(len(img[i])):
        if img[i][j] <= lineMaxTones[0]:
            firstLine[0][0] = j
            firstLine[0][1] = i
            finish = True
            break
    if finish: break

coords = [ firstLine[0][0], firstLine[0][1] ]
while img[coords[1]][coords[0]] <= lineMaxTones[0]:
    firstLine[1][0] = coords[0]
    firstLine[1][1] = coords[1]
    coords[1] += 1

startScan = [firstLine[0][0], int((firstLine[1][1] + firstLine[1][0]) / 2)]

cont = 0
scan = [ startScan[0], startScan[1] ]
output = ''
while True:
    if img[scan[1]][scan[0]] <= lineMaxTones[0]:
        if output != '' and output[len(output)-1] != '1': cont = 0
        output += '1'
    elif img[scan[1]][scan[0]] >= lineMaxTones[1]:
        if output != '' and output[len(output)-1] != '0': cont = 0
        output += '0'
    cont += 1
    scan[0] += 1
    if cont >= lineMax or re.findall(r'0{5,}$', output) != []:
        break

if (output != ''):
    output = re.findall(r'[10]+1', output)[0]
    print('I see a {}'.format(v.codes[output])) if output in v.codes else print('Sorry, no match')
    print(output)
    #cv2.imwrite('output.jpg', img)
    #plt.imshow(img, cmap='gray', interpolation='bicubic')
    #plt.show()

