import cv2
import matplotlib.pyplot as plt
from scipy import ndimage

image = cv2.imread("../Image/coins.png")
cv2.imshow("anh tien", image)

#  chuyển ảnh gốc thành ảnh xám sau đó chuển thành nhị phân
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("anh tien binary", thresh_binary)

threshold = 100
nr_objects, bwlab = ndimage.label(img_gray > threshold)
print("so thanh phan duoc ket noi ", bwlab)
plt.imshow(nr_objects)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
