from django.db import models
from django.contrib.auth.models import User

class PhongTro(models.Model):
    # Người đăng bài (liên kết với tài khoản người dùng)
    chu_tro = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    # Các thông tin cơ bản của phòng trọ
    tieu_de = models.CharField(max_length=200)       # Chữ ngắn
    mo_ta = models.TextField()                       # Chữ dài (nhiều dòng)
    gia_thue = models.IntegerField()                 # Số nguyên (Ví dụ: 3000000)
    dien_tich = models.FloatField()                  # Số thập phân (Ví dụ: 25.5 m2)
    dia_chi = models.CharField(max_length=255)       # Chữ ngắn
    so_dien_thoai = models.CharField(max_length=15)  # Số điện thoại
    hinh_anh = models.ImageField(upload_to='phongtro/', null=True, blank=True) #hinh anh
    
    # Tự động lấy ngày giờ lúc đăng bài
    ngay_dang = models.DateTimeField(auto_now_add=True)

    # Hàm này giúp hiển thị tên phòng trọ thay vì các chữ Object khó hiểu
    def __str__(self):
        return self.tieu_de
    
#Khác hàng liên hệ 
class KhachLienHe(models.Model):
    phong = models.ForeignKey(PhongTro, on_delete=models.CASCADE) # Biết là nhắn cho phòng nào
    ten_khach = models.CharField(max_length=100)
    so_dien_thoai = models.CharField(max_length=15)
    noi_dung = models.TextField()
    ngay_gui = models.DateTimeField(auto_now_add=True) # Tự động lưu thời gian gửi

    def __str__(self):
        return f"{self.ten_khach} nhắn hỏi phòng: {self.phong.tieu_de}"