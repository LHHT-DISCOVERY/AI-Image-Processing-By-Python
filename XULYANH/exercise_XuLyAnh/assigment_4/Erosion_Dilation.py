import np as np
import numpy as np
import cv2

kernelOp = np.ones((3, 3), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
