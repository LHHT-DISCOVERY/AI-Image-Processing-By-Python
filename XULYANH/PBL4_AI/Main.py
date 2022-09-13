from Human_Detection_and_Tracking import Detec_Tracking

if __name__ == '__main__':
    try:
        while 1:
            print("|--------------------------------------------- |")
            print("| --- Mời bạn chọn video để thực hiện demo --- | ")
            print("| 1. video đối tượng chuyển động trên đường    | ")
            print("| 2. video chuyển động trong ánh sáng nhiễu    | ")
            print("| 3. video chuyển động vào trời tối            | ")
            print("| 4. video nhiều đối tượng chuyển chuyển động  | ")
            print("| 0. thoát lựa chọn                            | ")
            print("|--------------------------------------------- |")
            case = int(input(" Nhập vào lựa chọn của bạn : "))
            if case == 1:
                Detec_Tracking("giaothongtrenduong.mp4")
            elif case == 2:
                Detec_Tracking("anhsangnhieu.mp4")
            elif case == 3:
                Detec_Tracking("videobongtoi.mp4")
            elif case == 4:
                Detec_Tracking("nhieudoituong.mp4")
                break
            elif case == 0:
                print("end")
                break
            else:
                print("Nhập không đúng lựa chọn")
    except:
        print("Nhập ko đúng yêu cầu ")
