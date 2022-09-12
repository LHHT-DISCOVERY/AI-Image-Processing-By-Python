import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def histogram(img):
    r, c = img.shape[:2]
    h = np.zeros(256, np.uint64)
    x = np.arange(0, 256)
    for i in range(0, r):
        for j in range(0, c):
            h[img[i, j]] = h[img[i, j]] + 1

    plt.bar(x, h, color="red", align="center")
    plt.title("Histogram of gray scare image")
    plt.show()

    p = h / (r * c)
    plt.bar(x, p, color="blue", align="center")
    plt.title("Normal histogram")
    plt.show()

    count, _ = np.histogram(img, bins=10)
    pdf = count / sum(count)
    plt.plot(pdf, color="red", label="pdf")
    plt.title("PDF")
    plt.legend()
    plt.show()

    cdf = np.cumsum(p)
    plt.plot(cdf, color="red", label="cdf")
    plt.title("CDF")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    img = cv.imread("2_2.bmp")
    histogram(img)
