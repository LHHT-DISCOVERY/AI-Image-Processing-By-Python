import matplotlib.pyplot as plt
import numpy as np

img = np.loadtxt('../../Image/1_3.asc')
n_initial = 8
n_reduced6bits = 6
n_reduced3bits = 3
s6bits = pow(2, n_initial) / pow(2, n_reduced6bits)
s3bits = pow(2, n_initial) / pow(2, n_reduced3bits)
# QuantizedImage6bits = pow(2, 2)
QuantizedImage6bits = np.floor(img / s6bits) * s6bits + s6bits / 2
QuantizedImage3bits = np.floor(img / s3bits) * s3bits + s3bits / 2
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.subplot(1, 3, 2)
plt.imshow(QuantizedImage6bits, cmap='gray')
plt.subplot(1, 3, 3)
plt.imshow(QuantizedImage3bits, cmap='gray')
plt.show()
