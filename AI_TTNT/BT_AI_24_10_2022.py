# import matplotlib.pyplot as plt  # thư viện vẽ đồ thị
# import pandas as pd  # thư  viện đọc file exel
# from sklearn import linear_model
#
# data_frame = pd.read_csv("moneybonus.csv")
# # in danh sách tuef exel
# print(data_frame)
# # this input (feature)
# data_frame["area"]  # in ra area trong ypyter
# # this output(lable)
# data_frame["price"]  # in ra price trong ypyter
# # ve đồ thị cac diem
# plt.scatter(data_frame["area"], data_frame["price"], color="black", marker="+")
# # tao doi tuong bang model neu o tren
# linear_regresstion = linear_model.LinearRegression()
# # huan luyen cho model , bang hàm fit
# linear_regresstion.fit(data_frame[["area"]], data_frame["price"]) \
#     # du doan 3700
# n = linear_regresstiona.predict([[3700]])
# print("với area 3700 tương ứng với price là : ", n)
# # y = m*X + b
# # y = coef * X + intercept_ , m = coef -> độ dốc , b = inrtercept_ giao điểm của trục tung x = 0 , đứng
# m = linear_regresstion.coef_
# print('độ dốc m =  ', m)
# b = linear_regresstion.intercept_
# print("b = ", b)
# # vd :
# print(" nhập area bạn mong muốn , chúng tôi sẽ đề xuất giá cho bạn !")
# x = int(input())
# print('bạn đã nhập area : ', x)
# y_predict = m * x + b
# print('kết quả price của ', x, "là : ", y_predict)
# print('xin cảm ơn!')
# # tên đồ thị
# plt.xlabel("house's area", fontsize=20)
# plt.ylabel("price", fontsize=20)
# # gọi lại đồ thị khi nãy
# plt.scatter(data_frame["area"], data_frame["price"], color="blue", marker="+")
# # vẽ đè lên đồ thị phía trên
# plt.plot(data_frame["area"], m * data_frame["area"] + b, color="red")


a = [106, 97, 108, 96, 112, 111, 97, 99, 87, 91]
b = [115, 104, 98, 101, 98, 106, 95, 98, 87, 86]
kq = 0
kq2 = 0
for i in range(0, len(a)):
    kq += (a[i] - 100.4 * (b[i] - 98.8))
    kq2 = ((a[i] - 100.4) ** 2) + kq2
    result = kq / kq2 ;
    print(result)

