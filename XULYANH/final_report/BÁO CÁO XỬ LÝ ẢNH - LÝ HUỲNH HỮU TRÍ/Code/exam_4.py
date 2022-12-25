# ------------------------------------------------#
# Author: Huu Tri                                 #
# Update: 12/12/2022                              #
# Phương pháp: Chuyển sang ảnh xám                #
# và lấy ngưỡng chuyển sang nhị phân		      #
# dùng phép hình thái học để lọc bỏ nhiễu         #
# sau đó dùng Canny tìm đường bao           	  #
# ------------------------------------------------#

import cv2
import numpy as np

image = cv2.imread('final4.jpg')
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# Lấy ngưỡng
ret, edges = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3, 3), np.uint8)

#  thực hiện giãn nở (Dilation) sau đó Co Erosion (Closing)
mask2 = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

#  Canny
edges = cv2.Canny(image, 40, 170)

cv2.imshow('edges', edges)

cv2.imshow('image', image)

cv2.waitKey(0)
