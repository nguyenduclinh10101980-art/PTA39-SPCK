# ==========================================================
# booking_form.py - Cửa sổ POPUP đặt lịch hẹn
# ==========================================================
# Giao diện: ui/booking_form.ui
# Cách dùng:
#   form = FormDatLich(thu_muc_goc, dich_vu, danh_sach_thu_cung)
#   if form.exec():              # True nếu bấm Đặt lịch
#       du_lieu = form.ket_qua   # dict ten_thu_cung, ngay_gio, ghi_chu

import os
from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import QDateTime
from PyQt6 import uic


class FormDatLich(QDialog):
    def __init__(self, thu_muc_goc, dich_vu, danh_sach_thu_cung, cha=None):
        super().__init__(cha)
        self.thu_muc_goc = thu_muc_goc
        self.ket_qua = None

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "booking_form.ui")
        uic.loadUi(duong_dan_ui, self)
        self.setWindowTitle("Đặt lịch hẹn")

        # tên dịch vụ đang chọn
        self.ten_dich_vu.setText(dich_vu.lay_ten())

        # VÒNG FOR: đưa tên từng thú cưng vào ô chọn
        for thu_cung in danh_sach_thu_cung:
            self.o_thu_cung.addItem(thu_cung.lay_ten())

        # mặc định: ngày mai, cùng giờ hiện tại
        self.o_ngay_gio.setDisplayFormat("dd/MM/yyyy HH:mm")
        self.o_ngay_gio.setDateTime(QDateTime.currentDateTime().addDays(1))

        self.nut_dat_lich.clicked.connect(self.xu_ly_dat_lich)
        self.nut_huy.clicked.connect(self.reject)

    # ------------------ xử lý sự kiện ------------------
    def xu_ly_dat_lich(self):
        # không cho đặt lịch vào thời gian đã qua
        if self.o_ngay_gio.dateTime() < QDateTime.currentDateTime():
            self.hien_thong_bao("Không thể đặt lịch vào thời gian đã qua!")
            return

        self.ket_qua = {
            "ten_thu_cung": self.o_thu_cung.currentText(),
            "ngay_gio": self.o_ngay_gio.dateTime().toString("dd/MM/yyyy HH:mm"),
            "ghi_chu": self.o_ghi_chu.toPlainText().strip(),
        }
        self.accept()

    # ------------------ hàm hỗ trợ ------------------
    def hien_thong_bao(self, noi_dung):
        hop_thoai = QMessageBox()
        hop_thoai.setWindowTitle("Thông báo")
        hop_thoai.setText(noi_dung)
        hop_thoai.setIcon(QMessageBox.Icon.Warning)
        hop_thoai.setStandardButtons(QMessageBox.StandardButton.Ok)
        hop_thoai.exec()
