# ------------------------------------------------#
# Author: Huu Tri                                 #
# Update: 10/12/2022                              #
# Phương pháp: Chuyển sang ảnh xám                #
# và chuyển sang nhị phân		                  #
# dùng phép hình thái học để lọc bỏ nhiễu         #
# sau đó dùng Canny tìm cạnh           	          #
# để phát hiện vết nứt trong hình                 #
# ------------------------------------------------#

import cv2
import numpy as np

# Đọc ảnh chuyển sang ảnh xám
img_gray = cv2.imread("final2.jpg", cv2.IMREAD_GRAYSCALE)

# Lấy ngưỡng
ret, thresh = cv2.threshold(img_gray, 160, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("gray", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Phần tử cấu trúc
kernel = np.ones((5, 5), np.uint8)

# Phép toám hình thái (Opening , Closing)
mask2 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernel)

cv2.imshow("gray", mask2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Canny
edges = cv2.Canny(mask2, threshold1=50, threshold2=600)

cv2.imshow("result", edges)
cv2.imwrite("result_ex_2.jpg", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
