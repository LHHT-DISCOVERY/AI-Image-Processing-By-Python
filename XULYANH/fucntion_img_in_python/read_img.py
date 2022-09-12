import cv2 

# read img
img = cv2.imread("bai1.jpg")

# show img
cv2.imshow("anh goc" ,img)

# print size img
print(img.shape)
print(img)

cv2.waitKey()
cv2.destroyAllWindows()