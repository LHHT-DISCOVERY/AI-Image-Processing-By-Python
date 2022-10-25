import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def Mean_filter(img, ksize):
    rows, cols = img.shape
    filter_img = np.zeros([cols,rows])
    h = (ksize - 1) // 2
    padded_img = np.pad(img, (h,h), mode = 'reflect')
    for i in range (rows):
        for j in range(cols):
            ksize_img = padded_img[i:i+ksize, j:j+ksize]
            filter_img[i,j] = np.mean(ksize_img)
    return filter_img

def Median_filter(img, ksize):
    rows, cols = img.shape
    filter_img = np.zeros([cols,rows])
    h = (ksize - 1) // 2
    padded_img = np.pad(img, (h,h), mode = 'reflect')
    for i in range (rows):
        for j in range(cols):
            ksize_img = padded_img[i:i+ksize, j:j+ksize]
            filter_img[i,j] = np.median(ksize_img)
    return filter_img

img = np.loadtxt('4_1.asc')
ksize = 5
img1 = Mean_filter(img, ksize)
fig = plt.figure(figsize=(16,9))
(ax1, ax2) = fig.subplots(1, 2)
ax1.imshow(img1, cmap = 'gray')
ax1.set_title("Mean Filter")
ax1.axis("off")

img2 = Median_filter(img, ksize)
ax2.imshow(img2, cmap = 'gray')
ax2.set_title("Median Filter")
ax2.axis("off")


plt.show()