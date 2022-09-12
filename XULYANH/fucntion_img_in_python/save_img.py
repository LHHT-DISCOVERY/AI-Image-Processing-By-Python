import cv2

img = cv2.imread("bai1.jpg")

saveImgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

cv2.imwrite("img_new.jpg" ,saveImgGray)