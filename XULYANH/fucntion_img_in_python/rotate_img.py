import cv2
import imutils

img = cv2.imread("../Image/1_4.bmp")
img_rotate = imutils.rotate(img , -45)

cv2.imshow("xoay -45" ,img_rotate)

cv2.waitKey()
cv2.destroyAllWindows()
