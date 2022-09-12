import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.signal import convolve2d


def Convolution(image, kernel):
    conv_bucket = []
    for d in range(image.ndim):
        conv_channel = convolve2d(image[:, :, d], kernel,
                                  mode="same", boundary="symm")
        conv_bucket.append(conv_channel)
    return np.stack(conv_bucket, axis=2).astype("uint8")


kernel_sizes = [9, 15, 30, 60]
fig, axs = plt.subplots(nrows=1, ncols=len(kernel_sizes), figsize=(15, 15));

pic = cv2.imread('../../Image/1_2.tif')

for k, ax in zip(kernel_sizes, axs):
    kernel = np.ones((k, k))
    kernel /= np.sum(kernel)
    ax.imshow(Convolution(pic, kernel));
    ax.set_title("Convolved By Kernel: {}".format(k));
    ax.set_axis_off();