# 🐶 Home Pet Care - Trung Hiếu

Ứng dụng đặt dịch vụ chăm sóc thú cưng viết bằng **Python + PyQt6**, giao diện thiết kế bằng **Qt Designer**, dữ liệu lưu trong **file JSON**.

## Chức năng
- Đăng ký / đăng nhập (tài khoản lưu trong `data/users.json`)
- Trang chủ: lời chào + giới thiệu
- Dịch vụ: danh sách dịch vụ (`data/services.json`), bấm "Đặt dịch vụ" để đặt lịch hẹn
- Tài khoản:
  - Thêm / sửa / xóa thú cưng (`data/pets.json`)
  - Xem và huỷ lịch hẹn (`data/bookings.json`)

## Cấu trúc thư mục
```
assets/       hình ảnh (imgs), biểu tượng (icons) và style.qss (giao diện chung)
pages/        các trang: login, signup, home
ui/           file .ui thiết kế bằng Qt Designer
components/   thẻ: TheDichVu, TheThuCung, TheLichHen + popup: FormThuCung, FormDatLich
entities/     class dữ liệu: NguoiDung, DichVu, ThuCung, LichHen + class quản lý QuanLy...
data/         file JSON lưu dữ liệu + data_io.py (đọc/ghi JSON)
app.py        file chạy chương trình
```

## Cài đặt và chạy (Windows)
1. Cài Python 3.10 trở lên.
2. Mở Terminal tại thư mục dự án, cài thư viện:
   ```
   pip install -r Requirements.txt
   ```
3. Chạy app:
   ```
   python app.py
   ```

## Tài khoản dùng thử
- Email: `nguyenductrunghieu6@gmail.com`
- Mật khẩu: `123456`
