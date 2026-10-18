# ==========================================================
# bookings.py - Class QuanLyLichHen: quản lý DANH SÁCH lịch hẹn
# ==========================================================
# Chức năng: lấy / tìm / thêm / sửa / xóa
# Dữ liệu lưu trong data/bookings.json

import os
from data.data_io import DataIO
from entities.booking import LichHen

THU_MUC_GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_DU_LIEU = os.path.join(THU_MUC_GOC, "data", "bookings.json")


class QuanLyLichHen:
    def __init__(self):
        self.__danh_sach_lich_hen = []  # list chứa các object LichHen
        self.doc_file()  # tạo xong là đọc dữ liệu từ file json luôn

    # ------------------ ĐỌC / GHI FILE JSON ------------------
    def doc_file(self):
        # Chưa có file -> danh sách rỗng
        if not os.path.exists(FILE_DU_LIEU):
            self.__danh_sach_lich_hen = []
            return
        danh_sach_dict = DataIO.read_json(FILE_DU_LIEU)  # json -> list dict
        # dùng vòng for đổi từng dict thành object LichHen
        self.__danh_sach_lich_hen = []
        for du_lieu in danh_sach_dict:
            self.__danh_sach_lich_hen.append(LichHen.tao_tu_dict(du_lieu))

    def luu_file(self):
        # đổi từng object LichHen thành dict rồi ghi ra file
        danh_sach_dict = []
        for lich_hen in self.__danh_sach_lich_hen:
            danh_sach_dict.append(lich_hen.chuyen_thanh_dict())
        DataIO.write_json(FILE_DU_LIEU, danh_sach_dict)

    # ------------------ LẤY / TÌM ------------------
    def lay_tat_ca(self):
        return self.__danh_sach_lich_hen

    def tim_lich_hen(self, ma):
        # Tìm theo mã, không thấy -> trả về None
        for lich_hen in self.__danh_sach_lich_hen:
            if lich_hen.lay_ma() == ma:
                return lich_hen
        return None

    # Lấy các lịch hẹn của 1 tài khoản
    def lay_theo_chu(self, gia_tri):
        ket_qua = []
        for lich_hen in self.__danh_sach_lich_hen:
            if lich_hen.lay_email_chu() == gia_tri:
                ket_qua.append(lich_hen)
        return ket_qua

    # Mã mới = mã lớn nhất + 1
    def tao_ma_moi(self):
        ma_lon_nhat = 0
        for lich_hen in self.__danh_sach_lich_hen:
            if lich_hen.lay_ma() > ma_lon_nhat:
                ma_lon_nhat = lich_hen.lay_ma()
        return ma_lon_nhat + 1

    # ------------------ THÊM ------------------
    def them_lich_hen(self, lich_hen_moi):
        self.__danh_sach_lich_hen.append(lich_hen_moi)
        self.luu_file()

    # ------------------ SỬA ------------------
    def sua_lich_hen(self, lich_hen_da_sua):
        # tìm vị trí có cùng mã rồi thay bằng bản đã sửa
        for vi_tri in range(len(self.__danh_sach_lich_hen)):
            if self.__danh_sach_lich_hen[vi_tri].lay_ma() == lich_hen_da_sua.lay_ma():
                self.__danh_sach_lich_hen[vi_tri] = lich_hen_da_sua
                self.luu_file()
                return True
        return False

    # ------------------ XÓA ------------------
    def xoa_lich_hen(self, ma):
        lich_hen = self.tim_lich_hen(ma)
        if lich_hen is None:
            return False
        self.__danh_sach_lich_hen.remove(lich_hen)
        self.luu_file()
        return True
