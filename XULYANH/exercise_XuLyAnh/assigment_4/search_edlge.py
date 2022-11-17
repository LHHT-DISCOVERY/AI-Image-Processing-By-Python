import cv2
from  matplotlib import pyplot as plt

img1 = cv2.imread("4.png")
img2 = cv2.imread("3.png")

imgGray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
imgGray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

edges1 = cv2.Canny(imgGray1, threshold1=100, threshold2=200)
edges2 = cv2.Canny(imgGray2, threshold1=100, threshold2=200)

cv2.imshow("original image", img1)
cv2.imshow("streching", edges1)
cv2.imshow("orginalim2", img2)
cv2.imshow("streching_img2", edges2)
plt.show()


cv2.waitKey()

