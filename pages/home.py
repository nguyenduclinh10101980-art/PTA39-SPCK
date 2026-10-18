# ==========================================================
# home.py - Trang CHỦ (ui/home.ui)
# ==========================================================
# Gồm 3 trang con (QStackedWidget - mỗi lúc hiện 1 trang):
#   1. Trang chủ  : lời chào + giới thiệu
#   2. Dịch vụ    : danh sách dịch vụ -> bấm "Đặt dịch vụ" để đặt lịch
#   3. Tài khoản  : thông tin, thú cưng (thêm/sửa/xóa), lịch hẹn (huỷ)
# Mọi danh sách đều hiển thị bằng VÒNG FOR + thẻ (component).

from PyQt6.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem
from PyQt6 import uic
import os

from entities.services import QuanLyDichVu
from entities.pet import ThuCung
from entities.pets import QuanLyThuCung
from entities.booking import LichHen
from entities.bookings import QuanLyLichHen
from components.service_card import TheDichVu
from components.pet_card import TheThuCung
from components.booking_card import TheLichHen
from components.pet_form import FormThuCung
from components.booking_form import FormDatLich

SO_COT = 3  # số thẻ dịch vụ trên 1 hàng


class TrangChu(QMainWindow):
    def __init__(self, cua_so_chinh, thu_muc_goc, tai_khoan):
        super().__init__()
        self.cua_so_chinh = cua_so_chinh
        self.thu_muc_goc = thu_muc_goc
        self.tai_khoan = tai_khoan  # người dùng đang đăng nhập (object NguoiDung)
        self.quan_ly_thu_cung = QuanLyThuCung()
        self.quan_ly_lich_hen = QuanLyLichHen()

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "home.ui")
        uic.loadUi(duong_dan_ui, self)

        # ---- nút điều hướng ----
        self.nut_trang_chu.clicked.connect(self.hien_trang_chu)
        self.nut_dich_vu.clicked.connect(self.hien_trang_dich_vu)
        self.nut_tai_khoan.clicked.connect(self.hien_trang_tai_khoan)
        self.nut_dang_xuat.clicked.connect(self.dang_xuat)
        self.nut_them_thu_cung.clicked.connect(self.them_thu_cung)

        # ---- hiển thị dữ liệu ----
        self.hien_thi_thong_tin_tai_khoan()
        self.hien_thi_dich_vu()
        self.hien_thi_thu_cung()
        self.hien_thi_lich_hen()

        self.hien_trang_chu()  # mặc định mở trang chủ
        self.show()

    # ==================== CHUYỂN TRANG CON ====================
    def hien_trang_chu(self):
        self.cac_trang.setCurrentWidget(self.trang_chu)

    def hien_trang_dich_vu(self):
        self.cac_trang.setCurrentWidget(self.trang_dich_vu)

    def hien_trang_tai_khoan(self):
        self.cac_trang.setCurrentWidget(self.trang_tai_khoan)

    def dang_xuat(self):
        from pages.login import LoginPage

        self.trang_dang_nhap = LoginPage(main_window=self.cua_so_chinh, root_dir=self.thu_muc_goc)
        self.close()

    # ==================== HIỂN THỊ (vòng for) ====================
    def hien_thi_thong_tin_tai_khoan(self):
        self.ten_nguoi_dung.setText(self.tai_khoan.lay_ho_ten())  # lời chào ở trang chủ
        self.ho_ten.setText(f"Họ tên: {self.tai_khoan.lay_ho_ten()}")
        self.email.setText(f"Email: {self.tai_khoan.lay_email()}")

    def hien_thi_dich_vu(self):
        luoi = self.danh_sach_dich_vu.layout()
        # VÒNG FOR: mỗi dịch vụ -> 1 thẻ -> đặt vào lưới
        for vi_tri, dich_vu in enumerate(QuanLyDichVu().lay_tat_ca()):
            the = TheDichVu(thu_muc_goc=self.thu_muc_goc, dich_vu=dich_vu, trang_cha=self)
            luoi.addWidget(the, vi_tri // SO_COT, vi_tri % SO_COT)  # (hàng, cột)
        # thêm 1 hàng trống co giãn ở cuối -> các thẻ không bị kéo dài
        luoi.setRowStretch(luoi.rowCount(), 1)

    def hien_thi_thu_cung(self):
        self.danh_sach_thu_cung.clear()
        danh_sach = self.quan_ly_thu_cung.lay_theo_chu(self.tai_khoan.lay_email())
        if len(danh_sach) == 0:
            self.danh_sach_thu_cung.addItem("Bạn chưa có thú cưng nào.")
            return
        for thu_cung in danh_sach:
            the = TheThuCung(thu_muc_goc=self.thu_muc_goc, thu_cung=thu_cung, trang_cha=self)
            self.them_the_vao_list(self.danh_sach_thu_cung, the)

    def hien_thi_lich_hen(self):
        self.danh_sach_lich_hen.clear()
        danh_sach = self.quan_ly_lich_hen.lay_theo_chu(self.tai_khoan.lay_email())
        if len(danh_sach) == 0:
            self.danh_sach_lich_hen.addItem("Bạn chưa đặt lịch hẹn nào.")
            return
        for lich_hen in danh_sach:
            the = TheLichHen(thu_muc_goc=self.thu_muc_goc, lich_hen=lich_hen, trang_cha=self)
            self.them_the_vao_list(self.danh_sach_lich_hen, the)

    def them_the_vao_list(self, danh_sach_widget, the):
        dong = QListWidgetItem()           # tạo 1 dòng trống
        dong.setSizeHint(the.sizeHint())   # dòng cao bằng thẻ
        danh_sach_widget.addItem(dong)
        danh_sach_widget.setItemWidget(dong, the)  # đặt thẻ vào dòng

    # ==================== THÚ CƯNG: thêm / sửa / xóa ====================
    def them_thu_cung(self):
        form = FormThuCung(thu_muc_goc=self.thu_muc_goc, cha=self)
        if form.exec():  # True nếu bấm Thêm
            thu_cung_moi = ThuCung(
                ma=self.quan_ly_thu_cung.tao_ma_moi(),
                email_chu=self.tai_khoan.lay_email(),
                ten=form.ket_qua["ten"],
                ngay_sinh=form.ket_qua["ngay_sinh"],
                loai=form.ket_qua["loai"],
                ghi_chu=form.ket_qua["ghi_chu"],
            )
            self.quan_ly_thu_cung.them_thu_cung(thu_cung_moi)  # tự lưu pets.json
            self.hien_thi_thu_cung()

    # thẻ thú cưng gọi khi bấm nút Sửa
    def sua_thu_cung(self, ma):
        thu_cung = self.quan_ly_thu_cung.tim_thu_cung(ma)
        form = FormThuCung(thu_muc_goc=self.thu_muc_goc, thu_cung=thu_cung, cha=self)
        if form.exec():
            thu_cung.sua_ten(form.ket_qua["ten"])
            thu_cung.sua_ngay_sinh(form.ket_qua["ngay_sinh"])
            thu_cung.sua_loai(form.ket_qua["loai"])
            thu_cung.sua_ghi_chu(form.ket_qua["ghi_chu"])
            self.quan_ly_thu_cung.sua_thu_cung(thu_cung)  # tự lưu pets.json
            self.hien_thi_thu_cung()

    # thẻ thú cưng gọi khi bấm nút Xoá
    def xoa_thu_cung(self, ma):
        if self.hoi_xac_nhan("Bạn có chắc muốn xóa thú cưng này?"):
            self.quan_ly_thu_cung.xoa_thu_cung(ma)
            self.hien_thi_thu_cung()

    # ==================== LỊCH HẸN: đặt / huỷ ====================
    # thẻ dịch vụ gọi khi bấm nút "Đặt dịch vụ"
    def dat_dich_vu(self, dich_vu):
        danh_sach_thu_cung = self.quan_ly_thu_cung.lay_theo_chu(self.tai_khoan.lay_email())
        if len(danh_sach_thu_cung) == 0:
            self.hien_thong_bao("Bạn cần thêm thú cưng ở trang Tài khoản trước khi đặt lịch!")
            return

        form = FormDatLich(thu_muc_goc=self.thu_muc_goc, dich_vu=dich_vu,
                           danh_sach_thu_cung=danh_sach_thu_cung, cha=self)
        if form.exec():
            lich_hen_moi = LichHen(
                ma=self.quan_ly_lich_hen.tao_ma_moi(),
                email_chu=self.tai_khoan.lay_email(),
                ten_thu_cung=form.ket_qua["ten_thu_cung"],
                ten_dich_vu=dich_vu.lay_ten(),
                ngay_gio=form.ket_qua["ngay_gio"],
                ghi_chu=form.ket_qua["ghi_chu"],
            )
            self.quan_ly_lich_hen.them_lich_hen(lich_hen_moi)  # tự lưu bookings.json
            self.hien_thi_lich_hen()
            self.hien_thong_bao("Đặt lịch thành công! Xem lại ở trang Tài khoản.")

    # thẻ lịch hẹn gọi khi bấm nút Huỷ
    def huy_lich_hen(self, ma):
        if self.hoi_xac_nhan("Bạn có chắc muốn huỷ lịch hẹn này?"):
            self.quan_ly_lich_hen.xoa_lich_hen(ma)
            self.hien_thi_lich_hen()

    # ==================== HÀM HỖ TRỢ ====================
    def hoi_xac_nhan(self, noi_dung):
        # hộp thoại Yes / No, trả về True nếu bấm Yes
        tra_loi = QMessageBox.question(
            self, "Xác nhận", noi_dung,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        return tra_loi == QMessageBox.StandardButton.Yes

    def hien_thong_bao(self, noi_dung):
        hop_thoai = QMessageBox()
        hop_thoai.setWindowTitle("Thông báo")
        hop_thoai.setText(noi_dung)
        hop_thoai.setIcon(QMessageBox.Icon.Information)
        hop_thoai.setStandardButtons(QMessageBox.StandardButton.Ok)
        hop_thoai.exec()
