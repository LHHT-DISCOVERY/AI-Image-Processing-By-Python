import cv2 as cv
import math

img = cv.imread("BT1.png")
cv.imshow("Ảnh gốc", img)

cen1 = [1, 5]
cen2 = [4, 1]

A = [1.1, 1.2]
B = [2, 3]
C = [6.3, 1.5]

dA1 = math.sqrt((1.1 - 1) ** 2 + (1.2 - 5) ** 2);
dB1 = math.sqrt((2 - 1) ** 2 + (3 - 5) ** 2);
dC1 = math.sqrt((6.3 - 1) ** 2 + (1.5 - 5) ** 2);

dA2 = math.sqrt((1.1 - 4) ** 2 + (1.2 - 1) ** 2);
dB2 = math.sqrt((2 - 4) ** 2 + (3 - 1) ** 2);
dC2 = math.sqrt((6.3 - 4) ** 2 + (1.5 - 1) ** 2);

if dA1 > dA2:
    print('A gan cen2')
else:
    print('A gan cen1')

if dB1 > dB2:
    print('B gan cen2')
else:
    print('B gan cen1')

if dC1 > dC2:
    print('C gan cen2')
else:
    print('C gan cen1')

cv.waitKey()
cv.destroyAllWindows()
