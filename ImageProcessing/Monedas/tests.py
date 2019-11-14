import cv2

img1 = cv2.imread('circulo.png', 1)
img2 = img1.copy()
img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

#--- Blur the gray scale image
img = cv2.GaussianBlur(img,(5, 5),0)

#--- Perform Canny edge detection (in my case lower = 84 and upper = 255, because I resized the image, may vary in your case)
edges = cv2.Canny(img, 192, 200)
cv2.imshow('Edges', edges )