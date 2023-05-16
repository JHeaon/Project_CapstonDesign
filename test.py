import cv2


img = cv2.imread("./test.jpg")
img = cv2.resize(img, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imwrite('test2.png', img)


    
