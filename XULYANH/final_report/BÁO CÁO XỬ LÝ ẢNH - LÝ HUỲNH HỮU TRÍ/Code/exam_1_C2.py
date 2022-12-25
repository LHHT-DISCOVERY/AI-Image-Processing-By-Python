# -------------------------------------#
# Author: Huu Tri 			           #
# Update: 10/12/2022 			       #
# Median Filter And Cân bằng Histogram #
# -------------------------------------#
import cv2
import numpy as np

img = cv2.imread('final1.bmp', 0)
new_img = cv2.imread('final1.bmp', 0)
hist = np.zeros((256,), np.uint8)
cv2.imshow('anh goc ', img)


#  tính toán histogram
def compute_hist(img):
    hist = np.zeros((256,), np.uint8)
    h, w = img.shape[:2]
    for i in range(h):
        for j in range(w):
            hist[img[i][j]] += 1
    return hist


#  cân bằng histogram
def equal_hist(hist):
    cumulator = np.zeros_like(hist, np.float64)
    for i in range(len(cumulator)):
        cumulator[i] = hist[:i].sum()
    print(cumulator)
    new_hist = (cumulator - cumulator.min()) / (cumulator.max() - cumulator.min()) * 255
    new_hist = np.uint8(new_hist)
    return new_hist


hist = compute_hist(img).ravel()
new_hist = equal_hist(hist)

h, w = img.shape[:2]

# thay thế lại tất cả các điểm ảnh từ hàm tính cân bằng histogram trên
for i in range(h):
    for j in range(w):
        img[i, j] = new_hist[img[i, j]]

new_img = img
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

cv2.imshow('image_result', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
