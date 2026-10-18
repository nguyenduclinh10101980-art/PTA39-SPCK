# ==========================================================
# booking.py - Class LichHen: lưu thông tin MỘT lịch hẹn
# ==========================================================
# Các thuộc tính lấy theo form đặt lịch (booking_form.ui):
#   ma, email_chu, ten_thu_cung, ten_dich_vu, ngay_gio, ghi_chu


class LichHen:
    def __init__(self, ma, email_chu, ten_thu_cung, ten_dich_vu, ngay_gio, ghi_chu):
        self.__ma = ma                        # mã lịch hẹn (số, không trùng)
        self.__email_chu = email_chu          # email người đặt
        self.__ten_thu_cung = ten_thu_cung    # tên thú cưng
        self.__ten_dich_vu = ten_dich_vu      # tên dịch vụ
        self.__ngay_gio = ngay_gio            # ngày giờ hẹn, ví dụ "20/10/2026 09:00"
        self.__ghi_chu = ghi_chu              # ghi chú thêm

    def __str__(self):
        return f"LichHen(ma={self.__ma}, ten_dich_vu={self.__ten_dich_vu})"

    # ------------------ HÀM LẤY (lay_...) ------------------
    def lay_ma(self):
        return self.__ma

    def lay_email_chu(self):
        return self.__email_chu

    def lay_ten_thu_cung(self):
        return self.__ten_thu_cung

    def lay_ten_dich_vu(self):
        return self.__ten_dich_vu

    def lay_ngay_gio(self):
        return self.__ngay_gio

    def lay_ghi_chu(self):
        return self.__ghi_chu

    # ------------------ HÀM SỬA (sua_...) ------------------
    def sua_ten_thu_cung(self, ten_thu_cung_moi):
        self.__ten_thu_cung = ten_thu_cung_moi

    def sua_ten_dich_vu(self, ten_dich_vu_moi):
        self.__ten_dich_vu = ten_dich_vu_moi

    def sua_ngay_gio(self, ngay_gio_moi):
        self.__ngay_gio = ngay_gio_moi

    def sua_ghi_chu(self, ghi_chu_moi):
        self.__ghi_chu = ghi_chu_moi

    # ------------------ CHUYỂN ĐỔI object <-> dict ------------------
    # object -> dict (để lưu vào file json)
    def chuyen_thanh_dict(self):
        return {
            "ma": self.__ma,
            "email_chu": self.__email_chu,
            "ten_thu_cung": self.__ten_thu_cung,
            "ten_dich_vu": self.__ten_dich_vu,
            "ngay_gio": self.__ngay_gio,
            "ghi_chu": self.__ghi_chu,
        }

    # dict -> object (khi đọc từ file json)
    @classmethod
    def tao_tu_dict(cls, du_lieu):
        return cls(
            ma=du_lieu.get("ma"),
            email_chu=du_lieu.get("email_chu", ""),
            ten_thu_cung=du_lieu.get("ten_thu_cung", ""),
            ten_dich_vu=du_lieu.get("ten_dich_vu", ""),
            ngay_gio=du_lieu.get("ngay_gio", ""),
            ghi_chu=du_lieu.get("ghi_chu", ""),
        )
