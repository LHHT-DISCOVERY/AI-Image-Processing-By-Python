import cv2

img = cv2.imread("../Image/1_4.bmp")

img_resize = cv2.resize(img , dsize = (400,400))

cv2.imshow("resize img" , img_resize)
# giảm kích thước ảnh đi một nữa

img_resize_2 = cv2.resize(img , dsize = None , fx = 1.1 , fy = 2)
cv2.imshow(" giam kich thuoc anh goc mot nua " ,img_resize_2)

cv2.waitKey()
cv2.destroyAllWindows