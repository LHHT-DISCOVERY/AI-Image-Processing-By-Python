from Human_Detection_and_Tracking import Detect_Tracking
from night_deetection_tracking import phat_hien_trom
if __name__ == '__main__':
    try:
        while 1:
            print("|--------------------------------------------- |")
            print("| --- Mời bạn chọn video để thực hiện demo --- | ")
            print("| 1. video đối tượng chuyển động trên đường    | ")
            print("| 2. video chuyển động trong ánh sáng nhiễu    | ")
            print("| 3. video chuyển động vào trời tối            | ")
            print("| 0. thoát lựa chọn                            | ")
            print("|--------------------------------------------- |")
            case = int(input(" Nhập vào lựa chọn của bạn : "))
            if case == 1:
                Detect_Tracking("2466089733293369890.mp4")
            elif case == 2:
                Detect_Tracking("anhsangnhieu.mp4")
            elif case == 3:
                phat_hien_trom()
            elif case == 0:
                print("end")
                break
            else:
                print("Nhập không đúng lựa chọn")
    except:
        print("END")
