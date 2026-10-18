# ==========================================================
# user.py - Class NguoiDung: lưu thông tin MỘT người dùng
# ==========================================================
# Mỗi NguoiDung gồm:
#   - ho_ten   : họ tên
#   - email    : email (dùng để đăng nhập, không được trùng)
#   - mat_khau : mật khẩu


class NguoiDung:
    def __init__(self, ho_ten, email, mat_khau):
        # dấu __ ở đầu: thuộc tính "riêng tư", chỉ đọc/sửa qua hàm lay_... / sua_...
        self.__ho_ten = ho_ten
        self.__email = email
        self.__mat_khau = mat_khau

    def __str__(self):
        return f"NguoiDung(ho_ten={self.__ho_ten}, email={self.__email})"

    # ------------------ HÀM LẤY (lay_...) ------------------
    def lay_ho_ten(self):
        return self.__ho_ten

    def lay_email(self):
        return self.__email

    def lay_mat_khau(self):
        return self.__mat_khau

    # ------------------ HÀM SỬA (sua_..., có kiểm tra) ------------------
    def sua_ho_ten(self, ho_ten):
        if ho_ten.strip() != "":
            self.__ho_ten = ho_ten
        else:
            print("Họ tên không được để trống!")

    def sua_email(self, email):
        if "@" in email:
            self.__email = email
        else:
            print("Email không hợp lệ!")

    def sua_mat_khau(self, mat_khau):
        if len(mat_khau) >= 6:
            self.__mat_khau = mat_khau
        else:
            print("Mật khẩu phải từ 6 ký tự trở lên!")

    # ------------------ CHUYỂN ĐỔI object <-> dict ------------------
    # object -> dict (để lưu vào file json)
    def chuyen_thanh_dict(self):
        return {
            "ho_ten": self.__ho_ten,
            "email": self.__email,
            "mat_khau": self.__mat_khau,
        }

    # dict -> object (khi đọc từ file json)
    @classmethod
    def tao_tu_dict(cls, du_lieu):
        return cls(
            ho_ten=du_lieu.get("ho_ten", ""),
            email=du_lieu.get("email", ""),
            mat_khau=du_lieu.get("mat_khau", ""),
        )
