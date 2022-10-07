import time

import cv2
import numpy as np
from pygame import mixer


def phat_hien_trom():
    mixer.init()
    mixer.music.load('Tieng-coi-xe-canh-sat-www_tiengdong_com.mp3')
    backSub = cv2.createBackgroundSubtractorMOG2()

    top_left, bottom_right = (200, 100), (700, 680)

    cap = cv2.VideoCapture('9014172086922407300.mp4')
    kernelOp = np.ones((6, 6), np.uint8)
    kernelOp2 = np.ones((5, 5), np.uint8)
    kernel_cl = np.ones((22, 22), np.uint8)

    while True:
        ret, frame = cap.read()
        fgMask = backSub.apply(frame)

        # Khu nhieu
        ret, imBin2 = cv2.threshold(fgMask, 254, 255, cv2.THRESH_BINARY)
        fgMask = cv2.morphologyEx(imBin2, cv2.MORPH_OPEN, kernelOp)
        fgMask = cv2.morphologyEx(fgMask, cv2.MORPH_CLOSE, kernel_cl)
        fgMask = cv2.erode(fgMask, kernelOp2)

        contours, ret = cv2.findContours(fgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # khu vực cấm
        # cv2.rectangle(frame, top_left, bottom_right, (255, 255, 0), 2)
        object = []
        for i in range(len(contours)):
            # x là điểm cuối cùng bên trái
            # y là điểm cuối cùng bên phải
            # x + với rộng , y + với cao

            (x, y, w, h) = cv2.boundingRect(contours[i])
            cx = x + w / 2
            cy = y + h / 2

            trong_vong_canh_bao = top_left[0] < cx < bottom_right[0] and top_left[1] < cy < bottom_right[1]
            area = cv2.contourArea(contours[i])
            if area < 600:
                continue
            if trong_vong_canh_bao:
                img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
                mixer.music.play()
                object.append([(x, y), (x + w, y + h)])
                cv2.putText(frame, "WARNING !!!", (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
                cv2.putText(img, "TROM DI CHUYEN", (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, .5,
                            (0, 255, 0),
                            2, cv2.LINE_AA)
                with open("Data_trom.txt", 'a') as f:
                    b = time.strftime("%c")
                    f.write("DOI_TUONG_VAO_NHA_LUC : " + b + "\n")
                    print(object)

        cv2.imshow('Camera', frame)
        cv2.imshow('Masked Video', fgMask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
