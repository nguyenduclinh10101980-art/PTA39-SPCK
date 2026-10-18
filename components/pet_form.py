# ==========================================================
# pet_form.py - Cửa sổ POPUP thêm / sửa thú cưng
# ==========================================================
# Giao diện: ui/pet_form.ui
# Cách dùng:
#   form = FormThuCung(thu_muc_goc)            # thêm mới
#   form = FormThuCung(thu_muc_goc, thu_cung)  # sửa
#   if form.exec():                            # True nếu bấm Thêm/Lưu
#       du_lieu = form.ket_qua                 # dict ten, ngay_sinh, loai, ghi_chu

import os
from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import QDate
from PyQt6 import uic

CAC_LOAI = ["Chó", "Mèo", "Khác"]  # các lựa chọn cho ô "Loại"


class FormThuCung(QDialog):
    def __init__(self, thu_muc_goc, thu_cung=None, cha=None):
        super().__init__(cha)
        self.thu_muc_goc = thu_muc_goc
        self.thu_cung = thu_cung  # None -> THÊM mới, có giá trị -> SỬA
        self.ket_qua = None

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "pet_form.ui")
        uic.loadUi(duong_dan_ui, self)

        self.o_loai.addItems(CAC_LOAI)
        self.o_ngay_sinh.setDisplayFormat("dd/MM/yyyy")

        if self.thu_cung is None:
            self.setWindowTitle("Thêm thú cưng")
            self.o_ngay_sinh.setDate(QDate.currentDate())
        else:
            self.setWindowTitle("Sửa thú cưng")
            self.tieu_de.setText("Sửa thú cưng")
            self.nut_luu.setText("Lưu")
            self.dien_du_lieu_cu()

        self.nut_luu.clicked.connect(self.xu_ly_luu)
        self.nut_huy.clicked.connect(self.reject)  # reject(): đóng popup, không lưu

    # ------------------ xử lý sự kiện ------------------
    def dien_du_lieu_cu(self):
        self.o_ten.setText(self.thu_cung.lay_ten())
        self.o_ngay_sinh.setDate(QDate.fromString(self.thu_cung.lay_ngay_sinh(), "dd/MM/yyyy"))
        self.o_loai.setCurrentText(self.thu_cung.lay_loai())
        self.o_ghi_chu.setPlainText(self.thu_cung.lay_ghi_chu())

    def xu_ly_luu(self):
        ten_nhap = self.o_ten.text().strip()
        if ten_nhap == "":
            self.hien_thong_bao("Vui lòng nhập tên thú cưng!")
            return

        self.ket_qua = {
            "ten": ten_nhap,
            "ngay_sinh": self.o_ngay_sinh.date().toString("dd/MM/yyyy"),
            "loai": self.o_loai.currentText(),
            "ghi_chu": self.o_ghi_chu.toPlainText().strip(),  # QTextEdit dùng toPlainText()
        }
        self.accept()  # accept(): đóng popup + báo "đã lưu"

    # ------------------ hàm hỗ trợ ------------------
    def hien_thong_bao(self, noi_dung):
        hop_thoai = QMessageBox()
        hop_thoai.setWindowTitle("Thông báo")
        hop_thoai.setText(noi_dung)
        hop_thoai.setIcon(QMessageBox.Icon.Warning)
        hop_thoai.setStandardButtons(QMessageBox.StandardButton.Ok)
        hop_thoai.exec()
