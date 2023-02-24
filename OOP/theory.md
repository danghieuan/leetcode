# Lý thuyết lập trình hướng đối tượng

### 1. Lập trình hướng đối tượng là gì ?
Là kỹ thuật lập trình hướng tới việc xây dựng mô hình cấu trúc dữ liệu cho một lớp các đối tượng trong tự nhiên hoặc phát sinh trong tư duy trừu tượng của con người.

### 2. Cấu trúc của lớp đối tượng (class)
Mô hình cấu trúc dữ liệu cho lớp các đối tượng thường có 2 phần như sau:
1. Thuộc tính: là cơ sở dữ liệu cho các thông số của đối tượng (Ví dụ: chiều dài, chiều rộng,...)
2. Phương thức: là những thao tác thực hiện trên chính lớp đối tượng đó (Ví dụ: tính chu vi, tính diện tích,...)


### 3. Lập trình xây dựng lớp đối tượng (class)
class Tên_lớp:
    def __init__(self, các tham số ứng với ác thuộc tính):
        self.thuộc_tính 1 = tham số 1
        self.thuộc_tính 2 = tham số 2
        ...
    def phương_thức_1(self):
        các lệnh của phương thức
    def phương_thức_2(self):
        các lệnh của phương thức
Kết thúc class