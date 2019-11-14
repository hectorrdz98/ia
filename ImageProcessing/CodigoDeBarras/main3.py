import cv2
import re
import matplotlib.pyplot as plt
import values as v
import sys
import numpy as np

def detect(img):
    cv2.imwrite('output.jpg', img)
    lineMax = 120
    maxWhites = 10
    lineMaxTones = [30, 245]
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

    print(firstLine)

    startScan = [firstLine[0][0], int((firstLine[1][1] + firstLine[1][0]) / 2)]

    minL = None
    scan = [ startScan[0], startScan[1] ]
    temp = 0
    act = 0

    while scan[0] < len(img[scan[1]]):
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

    cont = 0
    scan = [ startScan[0], startScan[1] ]
    output = ''
    while scan[0] < len(img[scan[1]]):
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
            outputFixed += ''.join([ '0' if pattern[0] == '0' else '1' for n in range(int(len(pattern)/minL)) ])

        return [ v.codes[outputFixed] if outputFixed in v.codes else None, outputFixed ]


def detectNew(img, height, width):
    global limitsScanner
    output = ''
    for i in range(limitsScanner[0]):
        value = img[int(height/2)][int(width/2) - int(limitsScanner[0]/2) + i]

    maxWhites = 10
    lineMaxTones = [50, 245]
    minL = None
    scan = [ int(height/2), int(width/2) - int(limitsScanner[0]/2) ]
    temp = 0
    act = 0
    pixelsRead = 0

    while scan[1] < int(width/2) + int(limitsScanner[0]/2):
        # print(img[scan[0]][scan[1]], end=' ')
        pixelsRead += 1
        if img[scan[0]][scan[1]] <= lineMaxTones[0]:
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
        scan[1] += 1

    scan = [ int(height/2), int(width/2) - int(limitsScanner[0]/2) ]
    while scan[1] < int(width/2) + int(limitsScanner[0]/2):
        if img[scan[0]][scan[1]] <= lineMaxTones[0]:
            output += '1'
        else:
            output += '0'
        scan[1] += 1
    
    return [ v.codes[output] if output in v.codes else None, output ]


    if minL:
        maxWhites = maxWhites * minL

        #print('\nmiL:', minL)
        #print('maxWhites:', maxWhites)
        #print('pixelsRead:', pixelsRead)

        scan = [ int(height/2), int(width/2) - int(limitsScanner[0]/2) ]
        while scan[1] < int(width/2) + int(limitsScanner[0]/2):
            if img[scan[0]][scan[1]] <= lineMaxTones[0]:
                output += '1'
            else:
                output += '0'
            scan[1] += 1
        
        return [ '', len(output) ]



        
        output = re.findall(r'1[10]+1', output)
        if output != []: 
            output = output[0]
            patterns = re.findall(r'0+|1+', output)

            outputFixed = ''

            for pattern in patterns:
                outputFixed += ''.join([ '0' if pattern[0] == '0' else '1' for n in range(int(len(pattern)/minL)) ])

            return [ v.codes[outputFixed] if outputFixed in v.codes else None, outputFixed ]
        return [ 'Error', output ]    
    else:
        return [ 'Error', output ]
        



cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

limitsScanner = [ 250, 2 ]

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape

    if cv2.waitKey(1) & 0xFF == ord('q'): break

    """
    if cv2.waitKey(33) == ord('a'):
        datas = detectNew(gray, height, width)
        print('I see a {}'.format(datas[0])) if datas[0] else print('Sorry, no match')
        print(datas[1])
    """
    datas = detectNew(gray, height, width)
    if datas[0] and datas[0] != 'Error': print('I see a {}'.format(datas[0]))
    print('\n{}\n'.format(datas[1]))
    
    color_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # Print scaner
    for i in range(limitsScanner[0]):
        for j in range(limitsScanner[1]):
            color_img[int(height/2) - int(limitsScanner[1]/2) + j][int(width/2) - int(limitsScanner[0]/2) + i] = [ 0, 0, 204 ]
    
    cv2.imshow('Gray', color_img)

    

cap.release()
cv2.destroyAllWindows()