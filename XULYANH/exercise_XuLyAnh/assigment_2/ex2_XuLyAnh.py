import cv2
import matplotlib.pyplot as plt


def bit(imgGray):
    rows = 3
    columns = 3
    fig = plt.figure(figsize=(10, 20))
    j = 0
    imgs = [255 * ((img & (1 << i)) >> i) for i in range(9)]
    for i in range(8, -1, -1):
        j += 1
        fig.add_subplot(rows, columns, j)
        plt.imshow(imgs[i])
        plt.title(i)
    plt.show()


if __name__ == '__main__':
    img = cv2.imread("2_2.bmp")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bit(imgGray)
