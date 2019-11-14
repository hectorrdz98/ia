import cv2
import re
import matplotlib.pyplot as plt
import values as v
import sys

img = cv2.imread('Examples/example0.png', 1) if len(sys.argv) < 2 else cv2.imread(' '.join(sys.argv[1:]))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lineMax = 120
maxWhites = 10
lineMaxTones = [100, 245]
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

# print('FirstLine: {}'.format(firstLine))

startScan = [firstLine[0][0], int((firstLine[1][1] + firstLine[1][0]) / 2)]

minL = None
scan = [ startScan[0], startScan[1] ]
temp = 0
act = 0

while scan[0] < len(img[scan[1]]):
    #print('\nScan {} -> {}'.format(scan, img[scan[1]][scan[0]]))
    #print('act = {}\ntemp = {}, minL = {}'.format(act,temp,minL))
    if img[scan[1]][scan[0]] <= lineMaxTones[0]:
        if act != 0:
            temp += 1
        else:
            act = 1
            if (minL == None or minL > temp) and temp > 0:
                minL = temp
            temp = 1
    else:
        if act == 0:
            temp += 1
        else:
            act = 0
            if (minL == None or minL > temp) and temp > 0:
                minL = temp
            temp = 1
    scan[0] += 1

maxWhites = maxWhites * minL
# print('minL:', minL)

cont = 0
scan = [ startScan[0], startScan[1] ]
output = ''
while scan[0] < len(img[scan[1]]):
    # print('scan: {} -> {}'.format(scan, img[scan[1]][scan[0]]))
    if img[scan[1]][scan[0]] <= lineMaxTones[0]:
        if output != '' and output[len(output)-1] != '1': cont = 0
        output += '1'
    else:
        if output != '' and output[len(output)-1] != '0': cont = 0
        output += '0'
    cont += 1
    scan[0] += 1
    if cont >= lineMax or re.findall(r'0{'+str(maxWhites)+',}$', output) != []:
        break

if (output != ''):
    output = re.findall(r'[10]+1', output)[0]
    patterns = re.findall(r'0+|1+', output)

    outputFixed = ''

    for pattern in patterns:
        # print(0 if pattern[0] == '0' else 1, ':',len(pattern), ' -> ', len(pattern)/minL, ' -> ', int(len(pattern)/minL))
        outputFixed += ''.join([ '0' if pattern[0] == '0' else '1' for n in range(int(len(pattern)/minL)) ])
    
    # print(outputFixed)

    print('I see a {}'.format(v.codes[outputFixed])) if outputFixed in v.codes else print('Sorry, no match')
    print(outputFixed)
    cv2.imwrite('output.jpg', img)
    #plt.imshow(img, cmap='gray', interpolation='bicubic')
    #plt.show()

