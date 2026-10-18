# ==========================================================
# service.py - Class DichVu: lưu thông tin MỘT dịch vụ
# ==========================================================
# Các thuộc tính lấy theo thẻ dịch vụ (service_card.ui):
#   ma, ten, so_sao, so_luot_danh_gia, mo_ta, gia, don_vi


class DichVu:
    def __init__(self, ma, ten, so_sao, so_luot_danh_gia, mo_ta, gia, don_vi):
        self.__ma = ma                                # mã dịch vụ (số, không trùng)
        self.__ten = ten                              # tên dịch vụ
        self.__so_sao = so_sao                        # số sao đánh giá (1 - 5)
        self.__so_luot_danh_gia = so_luot_danh_gia    # số lượt đánh giá
        self.__mo_ta = mo_ta                          # mô tả dịch vụ
        self.__gia = gia                              # giá (VND), ví dụ 180000
        self.__don_vi = don_vi                        # tính tiền theo: "ngày" / "lần"

    def __str__(self):
        return f"DichVu(ma={self.__ma}, ten={self.__ten})"

    # ------------------ HÀM LẤY (lay_...) ------------------
    def lay_ma(self):
        return self.__ma

    def lay_ten(self):
        return self.__ten

    def lay_so_sao(self):
        return self.__so_sao

    def lay_so_luot_danh_gia(self):
        return self.__so_luot_danh_gia

    def lay_mo_ta(self):
        return self.__mo_ta

    def lay_gia(self):
        return self.__gia

    def lay_don_vi(self):
        return self.__don_vi

    # ------------------ HÀM SỬA (sua_...) ------------------
    def sua_ten(self, ten_moi):
        self.__ten = ten_moi

    def sua_so_sao(self, so_sao_moi):
        self.__so_sao = so_sao_moi

    def sua_so_luot_danh_gia(self, so_luot_danh_gia_moi):
        self.__so_luot_danh_gia = so_luot_danh_gia_moi

    def sua_mo_ta(self, mo_ta_moi):
        self.__mo_ta = mo_ta_moi

    def sua_gia(self, gia_moi):
        self.__gia = gia_moi

    def sua_don_vi(self, don_vi_moi):
        self.__don_vi = don_vi_moi

    # ------------------ HÀM TIỆN ÍCH ------------------
    # Giá dạng chữ, ví dụ 180000 -> "180.000 VNĐ/ngày"
    def lay_gia_hien_thi(self):
        return f"{self.__gia:,}".replace(",", ".") + f" VNĐ/{self.__don_vi}"

    # Sao dạng hình, ví dụ 5 -> "⭐ ⭐ ⭐ ⭐ ⭐ (32 lượt)"
    def lay_danh_gia_hien_thi(self):
        return "⭐ " * self.__so_sao + f"({self.__so_luot_danh_gia} lượt)"

    # ------------------ CHUYỂN ĐỔI object <-> dict ------------------
    # object -> dict (để lưu vào file json)
    def chuyen_thanh_dict(self):
        return {
            "ma": self.__ma,
            "ten": self.__ten,
            "so_sao": self.__so_sao,
            "so_luot_danh_gia": self.__so_luot_danh_gia,
            "mo_ta": self.__mo_ta,
            "gia": self.__gia,
            "don_vi": self.__don_vi,
        }

    # dict -> object (khi đọc từ file json)
    @classmethod
    def tao_tu_dict(cls, du_lieu):
        return cls(
            ma=du_lieu.get("ma"),
            ten=du_lieu.get("ten", ""),
            so_sao=du_lieu.get("so_sao", 5),
            so_luot_danh_gia=du_lieu.get("so_luot_danh_gia", 0),
            mo_ta=du_lieu.get("mo_ta", ""),
            gia=du_lieu.get("gia", 0),
            don_vi=du_lieu.get("don_vi", "ngày"),
        )
