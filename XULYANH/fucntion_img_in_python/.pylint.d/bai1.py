import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import cv2

# =============================================================================
# # Đọc và hiển thị ảnh 
# # Hiển thị ra kích thước của ảnh
# =============================================================================
img  = plt.imread("bai1.jpg")
print("read img")
print(img)

plt.imshow(img)
plt.show()
print("Img.shape")
print(img.shape)

# =============================================================================
# Tạo ảnh mới bằng thoật toán KMeas
# =============================================================================
width = img.shape[0];
height = img.shape[1];

img = img.reshape(width*height ,3)
print("Img.reshape")
print(img.shape)
kmeans  = KMeans(n_clusters = 4).fit(img) 
labels = kmeans.predict(img)

# màu trung bình
cluster = kmeans.cluster_centers_

print("cluster")
print(cluster)
print("Label")
print(labels)

img2 = np.zeros_like(img)
for i in range(len(img)):
    img2[i] = cluster[labels[i]]

img2 = img2.reshape(width,height,3)   
plt.imshow(img2)
plt.show()
plt.imsave("ảnh mới.jpg",img2)

# =============================================================================
# # đọc và hiển thị kích thước ủa ảnh bằng cv2
# =============================================================================

img = cv2.imread("bai1.jpg")
print("shape from cv2 : " ,img.shape)

# =============================================================================
#  đọc và hiển thị ảnh gốc và ảnh trắng đen bằng cv2
# =============================================================================

cv2.imshow("img root : ", img)


img = cv2.imread("bai1.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("img gray : " , img)



# =============================================================================
# lưu ảnh trắng đen đc tạo ở trên
# =============================================================================

cv2.imwrite("gray.png", img)

# =============================================================================
# xoay ảnh 45 độ
# =============================================================================
import imutils
imgRotate = imutils.rotate(img, 45)
cv2.imshow("ảnh xoay 45 độ", imgRotate)

# =============================================================================
# Hàm convert sang ảnh xám
# =============================================================================

imgGray = cv2.cvtColor(cv2.imread("bai1.jpg"), cv2.COLOR_BRG2GRAY)
cv2.imshow(imgGray)
cv2.waitKey()
cv2.destroyAllWindows()