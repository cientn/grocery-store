import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Tạo kết nối tới cơ sở dữ liệu
conn = sqlite3.connect('quan_ly_ban_hang.db')
c = conn.cursor()

# Tạo bảng sản phẩm
c.execute('''CREATE TABLE IF NOT EXISTS san_pham (
            barcode TEXT PRIMARY KEY,
            ten_san_pham TEXT,
            gia_tien REAL,
            so_luong INTEGER,
            han_su_dung TEXT)''')

# Tạo bảng hóa đơn
c.execute('''CREATE TABLE IF NOT EXISTS hoa_don (
            ma_hoa_don INTEGER PRIMARY KEY AUTOINCREMENT,
            ngay_in DATE,
            tong_tien REAL)''')

# Tạo bảng chi tiết hóa đơn
c.execute('''CREATE TABLE IF NOT EXISTS chi_tiet_hoa_don (
            ma_hoa_don INTEGER,
            barcode TEXT,
            so_luong INTEGER,
            FOREIGN KEY (ma_hoa_don) REFERENCES hoa_don (ma_hoa_don),
            FOREIGN KEY (barcode) REFERENCES san_pham (barcode))''')

conn.commit()

def tinh_tien():
    # Logic xử lý tính tiền và cập nhật cơ sở dữ liệu
    pass

def tong_ket_ngay():
    # Logic xử lý tổng kết ngày
    pass

def xem_kho():
    # Logic hiển thị danh sách sản phẩm trong kho
    pass

def nhap_kho():
    # Logic nhập hàng vào kho
    pass

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng dụng Quản lý Bán Hàng")

# Tạo các thẻ (tab)
tab_control = ttk.Notebook(root)
tab_home = ttk.Frame(tab_control)
tab_tinh_tien = ttk.Frame(tab_control)
tab_tong_ket_ngay = ttk.Frame(tab_control)
tab_xem_kho = ttk.Frame(tab_control)
tab_nhap_kho = ttk.Frame(tab_control)

tab_control.add(tab_home, text='Trang Chủ')
tab_control.add(tab_tinh_tien, text='Tính Tiền')
tab_control.add(tab_tong_ket_ngay, text='Tổng Kết Ngày')
tab_control.add(tab_xem_kho, text='Xem Kho')
tab_control.add(tab_nhap_kho, text='Nhập Kho')

tab_control.pack(expand=1, fill='both')

# Trang Chủ
btn_tinh_tien = tk.Button(tab_home, text="Tính Tiền", command=lambda: tab_control.select(tab_tinh_tien))
btn_tinh_tien.pack(pady=10)

btn_tong_ket_ngay = tk.Button(tab_home, text="Tổng Kết Ngày", command=lambda: tab_control.select(tab_tong_ket_ngay))
btn_tong_ket_ngay.pack(pady=10)

btn_xem_kho = tk.Button(tab_home, text="Xem Kho", command=lambda: tab_control.select(tab_xem_kho))
btn_xem_kho.pack(pady=10)

btn_nhap_kho = tk.Button(tab_home, text="Nhập Kho", command=lambda: tab_control.select(tab_nhap_kho))
btn_nhap_kho.pack(pady=10)

# Các chức năng cụ thể cần được hoàn thiện thêm
# ...

# Chạy ứng dụng
root.mainloop()

# Đóng kết nối cơ sở dữ liệu khi thoát ứng dụng
conn.close()
