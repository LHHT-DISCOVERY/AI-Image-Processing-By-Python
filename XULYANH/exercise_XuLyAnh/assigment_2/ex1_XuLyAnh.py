import cv2
import matplotlib.pyplot as plt


def negative(img):
    r, c = img.shape[:2]
    new_img = img * 0
    for i in range(0, r):
        for j in range(0, c):
            pixel = img[i, j]
            pixel_new = new_img[i, j]
            pixel_new[0] = 255 - pixel[0]  # pixel Red
            pixel_new[1] = 255 - pixel[1]  # pixel Green
            pixel_new[2] = 255 - pixel[2]  # pixel Blue
            new_img[i, j] = pixel_new
    return new_img


def result(image, new_img):
    rows = 2
    columns = 1
    fig = plt.figure(figsize=(10, 10))

    fig.add_subplot(rows, columns, 1)
    plt.imshow(image)
    plt.title("Ảnh gốc ")

    fig.add_subplot(rows, columns, 2)
    plt.imshow(new_img)
    plt.title("Ảnh negative ")
    plt.show()


if __name__ == '__main__':
    image = cv2.imread("2_2.bmp", 1)
    result(image, negative(image))
