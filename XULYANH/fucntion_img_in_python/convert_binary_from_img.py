import cv2

img = cv2.imread("bai1.jpg")

imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)


# 127 là ngưỡng , > 127 cho bằng 255; else = 0
ret , thresh_binary = cv2.threshold(imgGray , 50 , 255 , cv2.THRESH_BINARY)
cv2.imshow("img then threshold" , thresh_binary)

cv2.waitKey()
cv2.destroyAllWindows