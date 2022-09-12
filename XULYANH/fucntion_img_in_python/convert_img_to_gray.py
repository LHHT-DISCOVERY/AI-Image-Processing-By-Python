import cv2

# read img
img = cv2.imread("bai1.jpg")

# convert img to gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# show img gray

cv2.imshow("Anh goc", img)

cv2.imshow("Img gray", imgGray)

cv2.waitKey()
cv2.destroyAllWindows()
