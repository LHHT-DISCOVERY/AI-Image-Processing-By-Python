import matplotlib.pyplot as plt
import numpy as np
#  Bài 4
# câu a Đọc ảnh và hiển thị ảnh và giảm độ phân giải
Y1 = np.loadtxt('../../Image/1_3.asc', np.int32)
print("Kích thước ảnh gốc : ", Y1.shape)
plt.title("kích thước ảnh vban đầu")
plt.imshow(Y1, cmap="gray")
plt.show()
# Giảm độ phan giải hình ảnh theo he 4
# cách 1 :
Y2 = Y1[::4, ::4]
#  hiển thị kích thước ảnh sau khi giảm độ phân giải
print("Kích thước hình ảnh  sau khi giảm 4 cách 1 : ", Y2.shape)
plt.title("kích thước Y4 sau khi giảm bằng cách 1")
plt.imshow(Y2, cmap="gray")
plt.show()
# cách 2 :
Y3 = Y1
Y4 = Y2 * 0
for i in range(0, Y2.shape[0]):
    for j in range(0, Y2.shape[1]):
        a = np.sum(Y3[4 * i:4 * (i + 1), 4 * j:4 * (j + 1)]) / 16
        Y4[i, j] = a
print("kích thước Y4 sau khi giảm bằng cách 2 là : ", Y4.shape)
plt.title("kích thước Y4 sau khi giảm bằng cách 2 ")
plt.imshow(Y4, cmap="gray")
plt.show()

# tăng độ phân giải lên 4

