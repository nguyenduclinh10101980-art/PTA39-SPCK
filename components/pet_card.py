# ==========================================================
# pet_card.py - Thẻ (card) hiển thị MỘT thú cưng
# ==========================================================
# Giao diện thẻ: ui/pet_card.ui  (có nút Sửa, Xoá)

import os
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic


class TheThuCung(QWidget):
    def __init__(self, thu_muc_goc, thu_cung, trang_cha):
        super().__init__()
        self.thu_muc_goc = thu_muc_goc
        self.thu_cung = thu_cung    # 1 object ThuCung
        self.trang_cha = trang_cha  # trang chủ (để nhờ sửa / xóa)

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "pet_card.ui")
        uic.loadUi(duong_dan_ui, self)

        self.hien_thi_thong_tin()
        self.nut_sua.clicked.connect(self.bam_sua)
        self.nut_xoa.clicked.connect(self.bam_xoa)

    # ------------------ xử lý sự kiện ------------------
    def hien_thi_thong_tin(self):
        self.ten_va_loai.setText(f"{self.thu_cung.lay_ten()} ({self.thu_cung.lay_loai()})")
        self.thong_tin_them.setText(
            f"Ngày sinh: {self.thu_cung.lay_ngay_sinh()}  -  {self.thu_cung.lay_ghi_chu()}"
        )

    def bam_sua(self):
        self.trang_cha.sua_thu_cung(self.thu_cung.lay_ma())

    def bam_xoa(self):
        self.trang_cha.xoa_thu_cung(self.thu_cung.lay_ma())
