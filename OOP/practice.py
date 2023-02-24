"""
Tạo lớp Hình chữ nhật gồm các thuộc tính chiều dài, chiều rộng.
Các phương thức bao gồm tính chu vi, tính diện tích, tính độ dài đường chéo.
"""
import math

class HCN:
    def __init__(self, dai, rong):
        self.chieu_dai = dai
        self.chieu_rong = rong

    def tinhChuVi(self):
        s = (self.chieu_dai + self.chieu_rong)*2
        return s

    def tinhDienTich(self):
        c = self.chieu_dai*self.chieu_rong
        return c

    def tinhDoDaiDuongCheo(self):
        d = math.sqrt(self.chieu_dai**2 + self.chieu_rong**2)
        return d


h1 = HCN(5,5)   # khai báo đối tượng h1 thuộc lớp HCN

print(h1.tinhDienTich()) # gọi tên đối tượng h1.gọi_tên_phương_thức của nó
print(h1.tinhChuVi()) # tương tự
print(h1.tinhDoDaiDuongCheo()) # tương tự