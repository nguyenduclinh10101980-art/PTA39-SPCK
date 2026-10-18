# ==========================================================
# booking_card.py - Thẻ (card) hiển thị MỘT lịch hẹn
# ==========================================================
# Giao diện thẻ: ui/booking_card.ui  (có nút Huỷ lịch)

import os
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic


class TheLichHen(QWidget):
    def __init__(self, thu_muc_goc, lich_hen, trang_cha):
        super().__init__()
        self.thu_muc_goc = thu_muc_goc
        self.lich_hen = lich_hen    # 1 object LichHen
        self.trang_cha = trang_cha  # trang chủ (để nhờ huỷ lịch)

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "booking_card.ui")
        uic.loadUi(duong_dan_ui, self)

        self.hien_thi_thong_tin()
        self.nut_huy_lich.clicked.connect(self.bam_huy_lich)

    # ------------------ xử lý sự kiện ------------------
    def hien_thi_thong_tin(self):
        self.dich_vu_va_thu_cung.setText(
            f"{self.lich_hen.lay_ten_dich_vu()}  -  {self.lich_hen.lay_ten_thu_cung()}"
        )
        self.thoi_gian_va_ghi_chu.setText(
            f"{self.lich_hen.lay_ngay_gio()}  -  {self.lich_hen.lay_ghi_chu()}"
        )

    def bam_huy_lich(self):
        self.trang_cha.huy_lich_hen(self.lich_hen.lay_ma())
