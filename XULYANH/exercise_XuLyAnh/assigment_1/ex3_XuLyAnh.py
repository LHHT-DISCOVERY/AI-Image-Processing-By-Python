import cv2
import matplotlib.pyplot as plt
import os


def imgcrop(input, xPieces, yPieces):
    filename, file_extension = os.path.splitext(input)
    im = cv2.imread(input)
    imgwidth, imgheight = im.size
    height = imgheight // yPieces
    width = imgwidth // xPieces
    for i in range(0, yPieces):
        for j in range(0, xPieces):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = im.crop(box)
            try:
                a.save("bai3/" + filename + "-" + str(i) + str(j) + file_extension)
            except:
                pass


imgcrop("../Image/1_1.jpg", 4, 4)

path = '../bai3'
images = os.listdir(path)
type(images)
len(images)

img_data = []
for img in images:
    img_arr = cv2.imread(os.path.join(path, img))
    img_data.append(img_arr)
plt.figure(figsize=(10, 10))

print("in binh thường")
for i in range(len(img_data)):
    plt.subplot(4, 4, i + 1)
    plt.imshow(img_data[i])
