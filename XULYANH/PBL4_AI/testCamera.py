import datetime
import time

import cv2
import numpy as np

import Object

cnt_up = 0
cnt_down = 0
w = 1280
h = 720
frameArea = h * w
areaTH = frameArea / 250
print('Area Threshold: ', areaTH)

# background subtraction
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

# Structuring elements for morphographic filters
kernelOp = np.ones((3, 3), np.uint8)
kernelOp2 = np.ones((5, 5), np.uint8)
kernelCl = np.ones((11, 11), np.uint8)

# Variables
font = cv2.FONT_HERSHEY_SIMPLEX
persons = []
max_p_age = 5
pid = 1

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    for i in persons:
        i.age_one()

    # Apply background subtraction
    fgmask2 = fgbg.apply(frame)
    # eliminate shadows
    try:
        ret, imBin2 = cv2.threshold(fgmask2, 200, 255, cv2.THRESH_BINARY)
        mask2 = cv2.morphologyEx(imBin2, cv2.MORPH_OPEN, kernelOp)
        mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernelCl)
    except:
        break

    #  Contours
    contours0, hierarchy = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours0:
        area = cv2.contourArea(cnt)
        if area > areaTH:

            #  Tracking

            M = cv2.moments(cnt)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            x, y, w, h = cv2.boundingRect(cnt)
               
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 255), 1)

    cv2.imshow('Live Streaming', frame)  # display Live Streaming
    cv2.imshow('Masked Video', mask2)  # display B & W video

    # press ESC to exit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# End of while(cap.isOpened())

# close all windows
cv2.destroyAllWindows()
