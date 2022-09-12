import cv2
import numpy as np

# Bài 1

# câu a
# đọc và hiển thị ảnh
img = cv2.imread("../Image/1_4.bmp")
cv2.imshow("Anh goc", img)
print(img)

# câu c
# ép sang kiểu double và hiển thị ảnh bằng imshow
img2 = np.array(img, dtype=float)
print(img2)
cv2.imshow("anh ep sang kieu double", img2/256)

#  câu d
#  => kết quả từ khi ép kiểu từ câu C  giống với ảnh ban đầu


cv2.waitKey()
cv2.destroyAllWindows()
