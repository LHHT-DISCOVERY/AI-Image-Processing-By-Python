from Human_Detection_and_Tracking import Detec_Tracking

if __name__ == '__main__':
    try:
        while 1:
            print("|--------------------------------------------- |")
            print("| --- Mời bạn chọn video để thực hiện demo --- | ")
            print("| 1. video người tham gia giao thông           | ")
            print("| 2. video người chuyển động trong trời mưa    | ")
            print("| 3. video người chuyển động vào trời tối      | ")
            print("| 0. thoát lựa chọn                            | ")
            print("|--------------------------------------------- |")
            case = int(input(" Nhập vào lựa chọn của bạn : "))
            if case == 1:
                Detec_Tracking("video.mp4")
            elif case == 2:
                Detec_Tracking("video2.mp4")
            elif case == 3:
                Detec_Tracking("output_49.gif")
            elif case == 0:
                print("end")
                break
            else:
                print("Nhập không đúng lựa chọn")
    except:
        print("Nhập ko đúng yêu cầu ")
