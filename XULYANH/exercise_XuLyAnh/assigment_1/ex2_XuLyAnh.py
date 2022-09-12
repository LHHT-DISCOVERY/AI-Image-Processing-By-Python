import cv2;
import imutils

# Bài 2


# câu a
# đọc ảnh đầu vào và chỉnh sửa kích thước ảnh lên size 400*400
X = cv2.resize(cv2.imread("../Image/1_2.tif"), dsize=(400, 400))


# Câu B  chuyển thành màu xám và xoay theo chiều kim đồng hồ
Y = imutils.rotate((cv2.cvtColor(X, cv2.COLOR_BGR2GRAY)), -45)

# câu c hiển thị
cv2.imshow("Anh goc ", X)
cv2.imshow("Anh moi", Y)

cv2.waitKey()
cv2.destroyAllWindows()
