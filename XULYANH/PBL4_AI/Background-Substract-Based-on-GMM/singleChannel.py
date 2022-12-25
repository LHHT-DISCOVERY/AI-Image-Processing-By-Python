import cv2
import os
import numpy as np
import pickle
import matplotlib.pyplot as plt
import time

# Giá trị càng lớn, khả năng tiền cảnh được sử dụng làm nền càng lớn
# Giá trị càng nhỏ, khả năng nền được coi là triển vọng càng lớn
SIGMA = 30  
WEIGHT = 0.1  


# Định nghĩa mô hình GMM hình ảnh
class GmmModel:
    def __init__(self, sample_image):
        #  số pixel (kích thước ảnh)
        self.img_size = sample_image.shape[0] * sample_image.shape[1]
        # Số lượng mô hình của mỗi điểm ảnh (khởi tạo thành 0)
        self.model_count = np.zeros([1, self.img_size], int)
        # Số K của mô hình GMM Gaussuss (ở đây cố định
        # , một số phương pháp có thể thích ứng với mỗi điểm ảnh để chọn một số K của mô hình)
        self.k = 3  # Các tham số có thể điều chỉnh
        # tỷ lệ học tập  Alpha
        self.alpha = 0.005  # Các tham số có thể điều chỉnh
        # SumOfWeight Threshold T
        self.t = 0.75  # Các tham số có thể điều chỉnh
        # Hệ số trọng lượng của mỗi mô hình (khởi tạo thành 0)
        self.w = np.zeros([self.k, self.img_size])
        # Giá trị trung bình của mỗi mô hình Gaussuss (khởi tạo thành 0)
        self.u = np.zeros([self.k, self.img_size])
        # Độ lệch chuẩn của mỗi mô hình Gaussuss (khởi tạo thành mặc định)
        self.sigma = np.full([self.k, self.img_size], SIGMA)


# Đọc bộ sưu tập ảnh và trả về biểu đồ thang độ xám
def load_data_set(path):
    image_set = []
    file_names = os.listdir(path)
    for filename in file_names:
        file_path = os.path.join(path, filename)
        # Đọc dưới dạng biểu đồ thang độ xám
        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        image_set.append(img)
    return image_set


# Khởi tạo mô hình gmm
def gmm_model_create():
    # Đọc khung hình ảnh đầu tiên
    first_frame = cv2.imread('WavingTrees/background_train/b00000.bmp', cv2.IMREAD_GRAYSCALE)
    return GmmModel(first_frame)


# Đào tạo các thông số mô hình
def gmm_model_train(gmm_model, single_frame):
    # start_time = time.time()
    img_rows = single_frame.shape[0]
    img_cols = single_frame.shape[1]
    for m in range(img_rows):
        for n in range(img_cols):
            # Được sử dụng để xác định xem có một mô hình phân phối phù hợp với điểm ảnh (m, n).
            matched = False
            for k in range(gmm_model.model_count[0, m * img_cols + n]):
                # Tính toán sự khác biệt giữa điểm ảnh và giá trị trung bình của phân phối Gaussian
                difference = abs(single_frame[m, n] - gmm_model.u[k, m * img_cols + n])
                distance = difference * difference
                # Điểm ảnh hiện tại đáp ứng phân phối Gaussian hiện tại
                if difference <= 2.5 * gmm_model.sigma[k, m * img_cols + n]:
                    matched = True
                    # Cập nhật các thông số của mô hình phân phối Gaussian k
                    # Tính toán mật độ xác suất của Gaussine k được phân phối trên điểm pixel đó
                    prob = (1 / (2 * np.pi * gmm_model.sigma[k, m * img_cols + n] ** 2) ** 0.5) * np.exp(
                        -(single_frame[m, n] - gmm_model.u[k, m * img_cols + n]) ** 2 / (
                                2 * (gmm_model.sigma[k, m * img_cols + n] ** 2)))
                    p = gmm_model.alpha * prob
                    # update weight
                    gmm_model.w[k, m * img_cols + n] = (1 - gmm_model.alpha) * gmm_model.w[
                        k, m * img_cols + n] + gmm_model.alpha
                    # update mean
                    gmm_model.u[k, m * img_cols + n] = (1 - p) * gmm_model.u[k, m * img_cols + n] + p * single_frame[
                        m, n]
                    # update standard deviation
                    if gmm_model.sigma[k, m * img_cols + n] < SIGMA / 2:
                        gmm_model.sigma[k, m * img_cols + n] = SIGMA / 2
                    else:
                        gmm_model.sigma[k, m * img_cols + n] = ((1 - p) * gmm_model.sigma[
                            k, m * img_cols + n] ** 2 + p * distance) ** 0.5
                    break
                else:
                    # Điểm ảnh hiện tại không đáp ứng phân phối Gaussian hiện tại
                    # Chỉ cập nhật weight
                    gmm_model.w[k, m * img_cols + n] = (1 - gmm_model.alpha) * gmm_model.w[k, m * img_cols + n]
                # Sắp xếp k gmm_model để dễ dàng thay thế và cập nhật mô hình phân phối Gaussian phía sau
                gmm_model_sort(gmm_model, m, n, img_cols)
            '''
            # Điểm ảnh hiện tại không khớp với bất kỳ phân phối Gaussian nào và cần phải tạo phân phối Gaussian mới
            # Có hai tình huống cần xem xét ở đây
            # 1. Sự có mặt của phân phối Gaussian không được khởi tạo: một phân phối Gaussian mới có thể được tạo ra tại thời điểm này
            # 2. k Phân phối Gaussian đã được khởi tạo: tại thời điểm này thay thế mô hình phân phối thấp nhất order_weight
            '''
            if not matched:
                # print('(', m, ',', n, ')', 'no matching distribution')
                # condition 1
                model_count = gmm_model.model_count[0, m * img_cols + n]
                if model_count < gmm_model.k:
                    # Khởi tạo weight
                    gmm_model.w[model_count, m * img_cols + n] = WEIGHT
                    # Khởi tạo mean
                    gmm_model.u[model_count, m * img_cols + n] = single_frame[m, n]
                    # khởi tạo độ lệch chuẩn
                    gmm_model.sigma[model_count, m * img_cols + n] = SIGMA
                    gmm_model.model_count[0, m * img_cols + n] = model_count + 1
                # condition 2
                else:
                    # update weight
                    gmm_model.w[gmm_model.k - 1, m * img_cols + n] = WEIGHT
                    # update mean
                    gmm_model.u[gmm_model.k - 1, m * img_cols + n] = single_frame[m, n]
                    # update standard deviation
                    gmm_model.sigma[gmm_model.k - 1, m * img_cols + n] = SIGMA
            if sum(gmm_model.w[:, m * img_cols + n]) != 0:
                gmm_model.w[:, m * img_cols + n] = gmm_model.w[:, m * img_cols + n] / sum(
                    gmm_model.w[:, m * img_cols + n])
    # end_time = time.time()
    # print(end_time - start_time)


# Sắp xếp k gmm_model điểm ảnh được chỉ định (dựa trên: w/sigma)
def gmm_model_sort(gmm_model, m, n, img_cols):
    # Xây dựng dựa trên sắp xếp
    order_weight = gmm_model.w[:, m * img_cols + n] / gmm_model.sigma[:, m * img_cols + n]
    # Đóng gói order_weight và trọng lượng
    zip_ow_weight = zip(order_weight, gmm_model.w[:, m * img_cols + n])
    # Order_weight đóng gói và trung bình
    zip_ow_mean = zip(order_weight, gmm_model.u[:, m * img_cols + n])
    # Order_weight đóng gói và độ lệch chuẩn
    zip_ow_standard_deviation = zip(order_weight, gmm_model.sigma[:, m * img_cols + n])
    zip_ow_weight = sorted(zip_ow_weight, reverse=True)
    zip_ow_mean = sorted(zip_ow_mean, reverse=True)
    zip_ow_standard_deviation = sorted(zip_ow_standard_deviation, reverse=True)
    temp, gmm_model.w[:, m * img_cols + n] = zip(*zip_ow_weight)
    temp, gmm_model.u[:, m * img_cols + n] = zip(*zip_ow_mean)
    temp, gmm_model.sigma[:, m * img_cols + n] = zip(*zip_ow_standard_deviation)


# lọc nhiễu với các hoạt động xử lý hình thái
def optimize_frame(single_frame):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    frame_parsed = cv2.morphologyEx(single_frame, cv2.MORPH_OPEN, kernel, iterations=1)
    frame_parsed = cv2.morphologyEx(frame_parsed, cv2.MORPH_CLOSE, kernel, iterations=3)
    return frame_parsed


# Tùy thuộc vào mô hình GMM được đào tạo,
#  thao tác trừ nền của hình ảnh đầu vào được thực hiện và hình ảnh được xử lý được trả về
def background_subtract(gmm_model, single_frame):
    # ước tính mô hình nền sum(weight_i)>T
    img_rows = single_frame.shape[0]
    img_cols = single_frame.shape[1]
    for pixel_index in range(img_rows * img_cols):
        weight_sum = 0
        for k in range(gmm_model.model_count[0, pixel_index]):
            weight_sum = weight_sum + gmm_model.w[k, pixel_index]
            # Nếu mô hình K đầu tiên đã đáp ứng ngưỡng trọng số, chỉ có mô hình K trước đó được chọn
            if weight_sum > gmm_model.t:
                gmm_model.model_count[0, pixel_index] = k + 1
                break
    # Khởi tạo hình ảnh sau khi xử lý
    frame_parsed = np.full([img_rows, img_cols], 255, np.uint8)
    for m in range(img_rows):
        for n in range(img_cols):
            hit = False
            for k in range(gmm_model.model_count[0, m * img_cols + n]):
                # Tính toán sự khác biệt giữa điểm ảnh hiện tại và giá trị trung bình phân phối Gaussian
                difference = abs(single_frame[m, n] - gmm_model.u[k, m * img_cols + n])
                if difference <= 2 * gmm_model.sigma[k, m * img_cols + n]:
                    # 背景
                    hit = True
                    break
            if hit:
                # 前景
                frame_parsed[m, n] = 0
    return frame_parsed


# Lưu mô hình GMM đến path

def gmm_model_save(gmm_model, path):
    with open(path, 'wb') as f:
        pickle.dump(gmm_model, f)


# Tải mô hình GMM 
def gmm_model_load(path):
    with open(path, 'rb') as f:
        gmm_model = pickle.load(f)
    return gmm_model


if __name__ == '__main__':
    # Khởi tạo mô hình GMM
    model = gmm_model_create()
    gmm_model_path = './models_learned/gmm_model_maxK={0}_alpha={1}_T={2}_sigma={3}.pkl'.format(model.k, model.alpha,
                                                                                                model.t, SIGMA)
    # Tải trực tiếp nếu mô hình đã tồn tại
    if not os.path.exists(gmm_model_path):
        # Tải bộ data
        frames = load_data_set('WavingTrees/background_train/')
        for i in range(len(frames)):
            print('frame ' + str(i) + ' is training...')
            gmm_model_train(model, frames[i])
        print('GMM Model learning process finished')
        print('saving model...')
        gmm_model_save(model, gmm_model_path)
    else:
        print('local model already exists')
    print('loading model...\n', gmm_model_path)
    # Tải mô hình 
    model = gmm_model_load(gmm_model_path)
    frames = load_data_set('WavingTrees/person_in/')
    # Hiển thị hiệu ứng cắt trong thời gian thực
    param_str = 'maxK={0} alpha={1} T={2} SIGMA={3}'.format(model.k, model.alpha, model.t, SIGMA)
    plt.ion()
    for i in range(len(frames)):
        # Sau khi trừ nền
        frame_subtracted = background_subtract(model, frames[i])
        # Tối ưu hóa xử lý hình ảnh
        frame_optimized = optimize_frame(frame_subtracted)
        plt.suptitle('(Frame {0}) RealTime Background Subtract\n\n{1}'.format(i + 1, param_str))
        plt.subplot(131)
        plt.title('origin')
        plt.imshow(frames[i], cmap='gray')
        plt.subplot(132)
        plt.title('subtracted')
        plt.imshow(frame_subtracted, cmap='gray')
        plt.subplot(133)
        plt.title('optimized')
        plt.imshow(frame_optimized, cmap='gray')
        plt.pause(0.2)
        plt.clf()
    plt.ioff()
