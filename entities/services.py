# ==========================================================
# services.py - Class QuanLyDichVu: quản lý DANH SÁCH dịch vụ
# ==========================================================
# Chức năng: lấy / tìm / thêm / sửa / xóa
# Dữ liệu lưu trong data/services.json

import os
from data.data_io import DataIO
from entities.service import DichVu

THU_MUC_GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_DU_LIEU = os.path.join(THU_MUC_GOC, "data", "services.json")


class QuanLyDichVu:
    def __init__(self):
        self.__danh_sach_dich_vu = []  # list chứa các object DichVu
        self.doc_file()  # tạo xong là đọc dữ liệu từ file json luôn

    # ------------------ ĐỌC / GHI FILE JSON ------------------
    def doc_file(self):
        # Chưa có file -> danh sách rỗng
        if not os.path.exists(FILE_DU_LIEU):
            self.__danh_sach_dich_vu = []
            return
        danh_sach_dict = DataIO.read_json(FILE_DU_LIEU)  # json -> list dict
        # dùng vòng for đổi từng dict thành object DichVu
        self.__danh_sach_dich_vu = []
        for du_lieu in danh_sach_dict:
            self.__danh_sach_dich_vu.append(DichVu.tao_tu_dict(du_lieu))

    def luu_file(self):
        # đổi từng object DichVu thành dict rồi ghi ra file
        danh_sach_dict = []
        for dich_vu in self.__danh_sach_dich_vu:
            danh_sach_dict.append(dich_vu.chuyen_thanh_dict())
        DataIO.write_json(FILE_DU_LIEU, danh_sach_dict)

    # ------------------ LẤY / TÌM ------------------
    def lay_tat_ca(self):
        return self.__danh_sach_dich_vu

    def tim_dich_vu(self, ma):
        # Tìm theo mã, không thấy -> trả về None
        for dich_vu in self.__danh_sach_dich_vu:
            if dich_vu.lay_ma() == ma:
                return dich_vu
        return None

    # Mã mới = mã lớn nhất + 1
    def tao_ma_moi(self):
        ma_lon_nhat = 0
        for dich_vu in self.__danh_sach_dich_vu:
            if dich_vu.lay_ma() > ma_lon_nhat:
                ma_lon_nhat = dich_vu.lay_ma()
        return ma_lon_nhat + 1

    # ------------------ THÊM ------------------
    def them_dich_vu(self, dich_vu_moi):
        self.__danh_sach_dich_vu.append(dich_vu_moi)
        self.luu_file()

    # ------------------ SỬA ------------------
    def sua_dich_vu(self, dich_vu_da_sua):
        # tìm vị trí có cùng mã rồi thay bằng bản đã sửa
        for vi_tri in range(len(self.__danh_sach_dich_vu)):
            if self.__danh_sach_dich_vu[vi_tri].lay_ma() == dich_vu_da_sua.lay_ma():
                self.__danh_sach_dich_vu[vi_tri] = dich_vu_da_sua
                self.luu_file()
                return True
        return False

    # ------------------ XÓA ------------------
    def xoa_dich_vu(self, ma):
        dich_vu = self.tim_dich_vu(ma)
        if dich_vu is None:
            return False
        self.__danh_sach_dich_vu.remove(dich_vu)
        self.luu_file()
        return True
