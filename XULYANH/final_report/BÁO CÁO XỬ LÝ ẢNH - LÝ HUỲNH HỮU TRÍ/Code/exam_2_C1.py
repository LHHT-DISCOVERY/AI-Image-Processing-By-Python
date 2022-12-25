# ------------------------------------------------#
# Author: Huu Tri                                 #
# Update: 11/12/2022                              #
# Phương pháp: Chuyển sang ảnh xám                #
# và chuyển sang nhị phân		                  #
# dùng phép hình thái học để lọc bỏ nhiễu         #
# sau đó dùng tích chập với ma trận Kernel        #
# để phát hiện vết nứt trong hình                 #
# ------------------------------------------------#

import cv2
import numpy as np

img_gray = cv2.imread("final2.jpg")

ret, thresh = cv2.threshold(img_gray, 160, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("image_binary", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Kernel phầ tử cấu trúc => Khử nhiễu
kernel = np.ones((5, 5), np.uint8)
mask2 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernel)

cv2.imshow("image_remove_noise", mask2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Kernel tìm cạnh
kernel2 = np.array([[-1, -1, -1],
                    [-1, 8, -1],
                    [-1, -1, -1]])


# Applying the filter2D()
img = cv2.filter2D(src=mask2, ddepth=-1, kernel=kernel2)

cv2.imshow('Result_Kernel', img)

cv2.waitKey()
cv2.destroyAllWindows()
