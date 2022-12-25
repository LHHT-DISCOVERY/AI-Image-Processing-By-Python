import time

import cv2
import numpy as np

import Object


# argument parsing
def Detect_Tracking(vd):
    cap = cv2.VideoCapture(vd)
    # Print the capture properties to console, height, width and FPS
    print('Height: ', cap.get(4))
    print('Width: ', cap.get(3))
    print('Frame per Seconds: ', cap.get(5))

    cnt_up = 0
    cnt_down = 0
    w = cap.get(3)
    h = cap.get(4)

    # Entry / exit lines
    # line_up = int((h / 2))
    line_down = int((h / 2))

    # pt3 = [0, line_up]
    # pt4 = [w, line_up]
    # pts_L2 = np.array([pt3, pt4], np.int32)
    # pts_L2 = pts_L2.reshape((-1, 1, 2))

    pt1 = [0, line_down]
    pt2 = [w, line_down]
    pts_L1 = np.array([pt1, pt2], np.int32)
    pts_L1 = pts_L1.reshape((-1, 1, 2))

    up_limit = int(1 * (h / 5))
    down_limit = int(4 * (h / 5))

    line_down_color = (255, 0, 255)
    # line_up_color = (0, 0, 255)

    # background subtraction
    fgbg = cv2.createBackgroundSubtractorMOG2(200, 16, True)

    # Structuring elements for morphographic filters
    kernelOp = np.ones((6, 6), np.uint8)
    kernelOp2 = np.ones((5, 5), np.uint8)
    kernel_cl = np.ones((22, 22), np.uint8)

    # Variables
    font = cv2.FONT_HERSHEY_SIMPLEX
    object = []
    pid = 1

    # lấy fps
    prev_frame_time = 0
    # new_frame_time = 0

    while cap.isOpened():
        # đọc hình ảnh từ video
        ret, frame = cap.read()
        new_frame_time = time.time()
        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time
        FPS = fps
        # FPS = cv2.VideoCapture.get(5)
        # top_left, bottom_right = (0, 100), (460, 0)
        for i in object:
            i.age_one()

        # áp dụng background subtraction

        fgmask2 = fgbg.apply(frame)
        try:
            ret, imBin2 = cv2.threshold(fgmask2, 254, 255, cv2.THRESH_BINARY)
            mask2 = cv2.morphologyEx(imBin2, cv2.MORPH_OPEN, kernelOp)
            mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernel_cl)
            mask2 = cv2.erode(mask2, kernelOp2)
        except:
            print("tổng xe trong video là : " + str(cnt_down + cnt_up))
            print('END of File')
            break

        #  Contours
        contours0, _ = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours0:
            area = cv2.contourArea(cnt)
            if area > 900:
                M = cv2.moments(cnt)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                x, y, w, h = cv2.boundingRect(cnt)
                new = True
                if cy in range(up_limit, down_limit):
                    for i in object:
                        if abs(cx - i.getX()) <= w and abs(cy - i.getY()) <= h:
                            #  đối tượng gần với đối tượng đã được phát hiện trước đó
                            new = False
                            i.updateCoords(cx, cy)  # cập nhật tọa độ trong đối tượng
                            # if i.going_UP(line_down, line_up):
                            #     cnt_up += 1
                            #     a = str(cnt_up)
                            #     b = time.strftime("%c")
                            #     with open("Data.txt", 'a') as f:
                            #         f.write("ID : " + a + "--UP-->" + str(b) + "\n")

                            if i.going_DOWN(line_down):
                                cnt_down += 1
                                a = str(cnt_down)
                                b = time.strftime("%c")
                                with open("Data.txt", 'a') as f:
                                    f.write("ID: " + a + "--DOWN-->" + str(b) + "\n")
                            break
                        if i.getState() == '1':
                            if i.getDir() == 'down' and i.getY() > down_limit:
                                i.setDone()
                            elif i.getDir() == 'up' and i.getY() < up_limit:
                                i.setDone()
                        if i.timedOut():
                            # xóa người khỏi danh sách
                            index = object.index(i)
                            object.pop(index)
                            del i  # giải phóng bộ nhớ
                    if new:
                        p = Object.Object(pid, cx, cy, 5)
                        object.append(p)
                        pid += 1
                    # vẽ contour
                    for i in object:
                        color_contour = i.getRGB()
                        cv2.circle(frame, (cx, cy), 5, color_contour, -2)
                        img = cv2.rectangle(frame, (x, y), (x + w, y + h), color_contour, 2)
                        cv2.putText(img, "Moving Object", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                                    (0, 255, 0),
                                    2, cv2.LINE_AA)
                        # LINE_AA là giao diện như : màu sắc, độ dày, loại đường

                        # tracking code
                        for i in object:
                            if len(i.getTracks()) >= 2:
                                pts = np.array(i.getTracks(), np.int32)
                                pts = pts.reshape((-1, 1, 2))
                                frame = cv2.polylines(frame, [pts], False, color_contour, 2)
        # display info
        # str_up = ' DOI TUONG DI LEN  : ' + str(cnt_up)
        # cv2.line(frame, (10, 10), (10, 30), (255, 0, 0), 2)
        # cv2.line(frame, (10, 10), (5, 20), (255, 0, 0), 2)
        # cv2.line(frame, (10, 10), (15, 20), (255, 0, 0), 2)
        str_down = ' DOI TUONG DI XUONG: ' + str(cnt_down)
        cv2.line(frame, (10, 35), (10, 55), (0, 0, 255), 2)
        cv2.line(frame, (10, 55), (5, 45), (0, 0, 255), 2)
        cv2.line(frame, (10, 55), (15, 45), (0, 0, 255), 2)
        FPS = "FPS : " + str(FPS)

        #  ranh giới để phân biệt đối tượng đi đang đi lên hay đi xuố   ng
        # frame = cv2.polylines(frame, [pts_L1], False, up_limit, thickness=3)
        frame = cv2.polylines(frame, [pts_L1], False, down_limit, thickness=3)

        frame = cv2.polylines(frame, [pts_L1], False, line_down_color, thickness=3)
        # frame = cv2.polylines(frame, [pts_L2], False, line_up_color, thickness=3)

        cv2.putText(frame, FPS, (20, 20), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame, str_down, (20, 40), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        # cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
        #             (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 255), 1)

        cv2.imshow('Original Video', frame)  # display original video
        cv2.imshow('Masked Video', mask2)  # display B & W video
        # cv2.imshow('roi' , roi)

        # press ESC to exit
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
