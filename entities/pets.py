# ==========================================================
# pets.py - Class QuanLyThuCung: quản lý DANH SÁCH thú cưng
# ==========================================================
# Chức năng: lấy / tìm / thêm / sửa / xóa
# Dữ liệu lưu trong data/pets.json

import os
from data.data_io import DataIO
from entities.pet import ThuCung

THU_MUC_GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_DU_LIEU = os.path.join(THU_MUC_GOC, "data", "pets.json")


class QuanLyThuCung:
    def __init__(self):
        self.__danh_sach_thu_cung = []  # list chứa các object ThuCung
        self.doc_file()  # tạo xong là đọc dữ liệu từ file json luôn

    # ------------------ ĐỌC / GHI FILE JSON ------------------
    def doc_file(self):
        # Chưa có file -> danh sách rỗng
        if not os.path.exists(FILE_DU_LIEU):
            self.__danh_sach_thu_cung = []
            return
        danh_sach_dict = DataIO.read_json(FILE_DU_LIEU)  # json -> list dict
        # dùng vòng for đổi từng dict thành object ThuCung
        self.__danh_sach_thu_cung = []
        for du_lieu in danh_sach_dict:
            self.__danh_sach_thu_cung.append(ThuCung.tao_tu_dict(du_lieu))

    def luu_file(self):
        # đổi từng object ThuCung thành dict rồi ghi ra file
        danh_sach_dict = []
        for thu_cung in self.__danh_sach_thu_cung:
            danh_sach_dict.append(thu_cung.chuyen_thanh_dict())
        DataIO.write_json(FILE_DU_LIEU, danh_sach_dict)

    # ------------------ LẤY / TÌM ------------------
    def lay_tat_ca(self):
        return self.__danh_sach_thu_cung

    def tim_thu_cung(self, ma):
        # Tìm theo mã, không thấy -> trả về None
        for thu_cung in self.__danh_sach_thu_cung:
            if thu_cung.lay_ma() == ma:
                return thu_cung
        return None

    # Lấy các thú cưng của 1 tài khoản
    def lay_theo_chu(self, gia_tri):
        ket_qua = []
        for thu_cung in self.__danh_sach_thu_cung:
            if thu_cung.lay_email_chu() == gia_tri:
                ket_qua.append(thu_cung)
        return ket_qua

    # Mã mới = mã lớn nhất + 1
    def tao_ma_moi(self):
        ma_lon_nhat = 0
        for thu_cung in self.__danh_sach_thu_cung:
            if thu_cung.lay_ma() > ma_lon_nhat:
                ma_lon_nhat = thu_cung.lay_ma()
        return ma_lon_nhat + 1

    # ------------------ THÊM ------------------
    def them_thu_cung(self, thu_cung_moi):
        self.__danh_sach_thu_cung.append(thu_cung_moi)
        self.luu_file()

    # ------------------ SỬA ------------------
    def sua_thu_cung(self, thu_cung_da_sua):
        # tìm vị trí có cùng mã rồi thay bằng bản đã sửa
        for vi_tri in range(len(self.__danh_sach_thu_cung)):
            if self.__danh_sach_thu_cung[vi_tri].lay_ma() == thu_cung_da_sua.lay_ma():
                self.__danh_sach_thu_cung[vi_tri] = thu_cung_da_sua
                self.luu_file()
                return True
        return False

    # ------------------ XÓA ------------------
    def xoa_thu_cung(self, ma):
        thu_cung = self.tim_thu_cung(ma)
        if thu_cung is None:
            return False
        self.__danh_sach_thu_cung.remove(thu_cung)
        self.luu_file()
        return True
