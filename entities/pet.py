# ==========================================================
# pet.py - Class ThuCung: lưu thông tin MỘT thú cưng
# ==========================================================
# Các thuộc tính lấy theo form thêm thú cưng (pet_form.ui):
#   ma, email_chu, ten, ngay_sinh, loai, ghi_chu


class ThuCung:
    def __init__(self, ma, email_chu, ten, ngay_sinh, loai, ghi_chu):
        self.__ma = ma                  # mã thú cưng (số, không trùng)
        self.__email_chu = email_chu    # email của chủ (tài khoản)
        self.__ten = ten                # tên thú cưng
        self.__ngay_sinh = ngay_sinh    # ngày sinh, ví dụ "01/01/2024"
        self.__loai = loai              # loại: Chó / Mèo / ...
        self.__ghi_chu = ghi_chu        # ghi chú thêm

    def __str__(self):
        return f"ThuCung(ma={self.__ma}, ten={self.__ten})"

    # ------------------ HÀM LẤY (lay_...) ------------------
    def lay_ma(self):
        return self.__ma

    def lay_email_chu(self):
        return self.__email_chu

    def lay_ten(self):
        return self.__ten

    def lay_ngay_sinh(self):
        return self.__ngay_sinh

    def lay_loai(self):
        return self.__loai

    def lay_ghi_chu(self):
        return self.__ghi_chu

    # ------------------ HÀM SỬA (sua_...) ------------------
    def sua_ten(self, ten_moi):
        self.__ten = ten_moi

    def sua_ngay_sinh(self, ngay_sinh_moi):
        self.__ngay_sinh = ngay_sinh_moi

    def sua_loai(self, loai_moi):
        self.__loai = loai_moi

    def sua_ghi_chu(self, ghi_chu_moi):
        self.__ghi_chu = ghi_chu_moi

    # ------------------ CHUYỂN ĐỔI object <-> dict ------------------
    # object -> dict (để lưu vào file json)
    def chuyen_thanh_dict(self):
        return {
            "ma": self.__ma,
            "email_chu": self.__email_chu,
            "ten": self.__ten,
            "ngay_sinh": self.__ngay_sinh,
            "loai": self.__loai,
            "ghi_chu": self.__ghi_chu,
        }

    # dict -> object (khi đọc từ file json)
    @classmethod
    def tao_tu_dict(cls, du_lieu):
        return cls(
            ma=du_lieu.get("ma"),
            email_chu=du_lieu.get("email_chu", ""),
            ten=du_lieu.get("ten", ""),
            ngay_sinh=du_lieu.get("ngay_sinh", ""),
            loai=du_lieu.get("loai", ""),
            ghi_chu=du_lieu.get("ghi_chu", ""),
        )
