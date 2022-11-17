import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("2_1.jpg")
img2 = cv2.imread("2_3.jpg")

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

max_im1 = img1.max()
max_im2 = img2.max()
min_im1 = img1.min()
min_im2 = img2.min()

streching_image1 = (img1 - min_im1) * ((255 - 0) / (max_im1 - min_im1)) + 0
streching_image1 = np.uint8(streching_image1)

streching_image2 = (img2 - min_im2) * ((255 - 0) / (max_im2 - min_im2)) + 0
streching_image2 = np.uint8(streching_image2)
print(img1.shape)
cv2.imshow("original image", img1)
cv2.imshow("streching", streching_image1)
cv2.imshow("orginalim2", img2)
cv2.imshow("streching_img2", streching_image2)
# plt.hist(streching_image1)
plt.show()
cv2.waitKey(0)

# 4b
# img1 = np.ravel(img1)
# plt.hist(img1, bins=1)
# plt.show()

# 4c
# img1 = np.ravel(img1)
# hist, bins = np.histogram(img1)
# cdf = np.cumsum(hist)
# print("cdf=",cdf)
# plt.plot(cdf)
# plt.show()
