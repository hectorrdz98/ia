import cv2
import matplotlib.pyplot as plt

limits = {
    'tapa' : {
        'pos' : 30,
        'maxB': 35
    },
    'etiqueta' : {
        'pos' : 200,
        'maxB': 110
    },
    'cantidad' : {
        'pos' : 125,
        'minW': 100
    },
}

alpha = 2

img = cv2.imread('Examples/fea.jpg', 0)

ret,thresh = cv2.threshold(img,220,255, cv2.THRESH_BINARY)
height, width = thresh.shape



# Tapa
results = {
    'fill' : [0,0]
}

for i in range(width):
    if thresh[limits['tapa']['pos']][i] == 0: results['fill'][0] += 1
    else: results['fill'][1] += 1
    thresh[limits['tapa']['pos']][i] = 0

if abs(results['fill'][0] - limits['tapa']['maxB']) <= alpha:
    print('Tapa correcta')
else:
    print('Tapa incorrecta')



# Etiqueta
results = {
    'fill' : [0,0]
}

for i in range(width):
    if thresh[limits['etiqueta']['pos']][i] == 0: results['fill'][0] += 1
    else: results['fill'][1] += 1
    thresh[limits['etiqueta']['pos']][i] = 0

if results['fill'][0] < limits['etiqueta']['maxB']:
    print('Etiqueta correcta')
else:
    print('Etiqueta incorrecta')



# Tapa
results = {
    'fill' : [0,0]
}

for i in range(width):
    if thresh[limits['cantidad']['pos']][i] == 0: results['fill'][0] += 1
    else: results['fill'][1] += 1
    thresh[limits['cantidad']['pos']][i] = 0

if abs(results['fill'][0] - limits['cantidad']['minW']) <= alpha:
    print('Cantidad de líquido correcta')
else:
    print('Cantidad de líquido incorrecta')




cv2.imwrite('output.jpg', thresh)