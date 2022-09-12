import cv2

img = cv2.imread("../Image/1_2.tif")
#  làm rõ
img_ro = cv2.GaussianBlur(img, ksize=(1, 1), sigmaX=0)
# làm mơf
img_mo = cv2.GaussianBlur(img, ksize=(21, 21), sigmaX=0)
cv2.imshow("Lam Ro img", img_ro)
cv2.imshow("Lam Mo img", img_mo)

cv2.waitKey()
cv2.destroyAllWindows
