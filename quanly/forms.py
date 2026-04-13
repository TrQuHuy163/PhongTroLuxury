from django import forms
from .models import PhongTro

class PhongTroForm(forms.ModelForm):
    class Meta:
        model = PhongTro
        # Liệt kê các cột trong bảng PhongTro mà bạn muốn người dùng nhập
        fields = ['tieu_de', 'mo_ta', 'gia_thue', 'dien_tich','dia_chi' ,'so_dien_thoai','hinh_anh'] 
        
        # Tùy chỉnh chữ hiển thị cho đẹp
        labels = {
            'tieu_de': 'Tiêu đề bài đăng',
            'mo_ta' : 'Mô tả',
            'gia_thue': 'Giá thuê (VNĐ/tháng)',
            'dien_tich': 'Diện tích (m²)',
            'dia_chi': 'Địa chỉ chi tiết',
            'so_dien_thoai' : 'sô điện thoại liên hệ',
            'hinh_anh': 'Hình ảnh phòng',
        }