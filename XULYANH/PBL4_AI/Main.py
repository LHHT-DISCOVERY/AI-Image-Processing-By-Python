from Human_Detection_and_Tracking import Detect_Tracking
from night_deetection_tracking import phat_hien_trom
if __name__ == '__main__':
    try:
        while 1:
            print("|--------------------------------------------- |")
            print("| --- Mời bạn chọn video để thực hiện demo --- | ")
            print("| 1. video đối tượng chuyển động trên đường    | ")
            print("| 2. video chuyển động vào trời tối            | ")
            print("| 0. thoát lựa chọn                            | ")
            print("|--------------------------------------------- |")
            case = int(input(" Nhập vào lựa chọn của bạn : "))
            if case == 1:
                # 2466089733293369890
                Detect_Tracking("data_video_test/test15.mp4")
                break
            elif case == 2:
                phat_hien_trom()
                break
            else:
                print("Nhập không đúng lựa chọn")
    except:
        print("END")
