# ==========================================================
# service_card.py - Thẻ (card) hiển thị MỘT dịch vụ
# ==========================================================
# Giao diện thẻ: ui/service_card.ui
# Trang chủ dùng vòng for để tạo nhiều thẻ dịch vụ.

import os
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic


class TheDichVu(QWidget):
    def __init__(self, thu_muc_goc, dich_vu, trang_cha):
        super().__init__()
        self.thu_muc_goc = thu_muc_goc
        self.dich_vu = dich_vu      # 1 object DichVu
        self.trang_cha = trang_cha  # trang chủ (để nhờ mở form đặt lịch)

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "service_card.ui")
        uic.loadUi(duong_dan_ui, self)

        self.hien_thi_thong_tin()
        self.nut_dat_dich_vu.clicked.connect(self.bam_dat_dich_vu)

    # ------------------ xử lý sự kiện ------------------
    def hien_thi_thong_tin(self):
        self.ten_dich_vu.setText(self.dich_vu.lay_ten())
        self.danh_gia.setText(self.dich_vu.lay_danh_gia_hien_thi())
        self.mo_ta.setText(self.dich_vu.lay_mo_ta())
        self.gia.setText(self.dich_vu.lay_gia_hien_thi())

    def bam_dat_dich_vu(self):
        self.trang_cha.dat_dich_vu(self.dich_vu)
