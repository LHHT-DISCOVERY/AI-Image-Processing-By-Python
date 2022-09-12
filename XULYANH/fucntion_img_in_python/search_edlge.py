import cv2 

img = cv2.imread("bai1.jpg")

imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(imgGray, threshold1 = 100 , threshold2 = 200)

cv2.imshow("Canny" , edges)

cv2.waitKey()
cv2.destroyAllWindows