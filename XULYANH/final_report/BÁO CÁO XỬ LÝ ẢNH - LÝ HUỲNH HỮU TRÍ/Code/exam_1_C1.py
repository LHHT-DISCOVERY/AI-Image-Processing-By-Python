# -------------------------------------#
# Author: Huu Tri 			           #
# Update: 10/12/2022 			       #
# Median Filter And convolution Kernel #
# -------------------------------------#
import cv2
import numpy as np

img = cv2.imread('final1.bmp', 0)
new_img = cv2.imread('final1.bmp', 0)

prop = new_img.shape
# Lọc trung vị
for i in range(1, prop[0] - 1):
    for j in range(1, prop[1] - 1):

        win = []
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                win.append(img[x][y])
        win.sort()

        new_img[i][j] = win[4]

# Kernel làm nét
sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]],
                          dtype=np.float32)

sharpen_image = cv2.filter2D(src=new_img,
                             ddepth=-1,
                             kernel=sharpen_kernel)
cv2.imshow('image_root', img)
cv2.imshow('image_remove_salt_pepper', new_img)
cv2.imshow('image_improve', sharpen_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
