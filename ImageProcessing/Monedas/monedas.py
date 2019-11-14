import cv2
import matplotlib.pyplot as plt

img = cv2.imread('monedasmx.jpg', 0)

ret,thresh = cv2.threshold(img,150,255, cv2.THRESH_BINARY_INV)

cv2.imwrite('output2.jpg', thresh)


thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

cv2.imwrite('output.jpg', thresh)