from PyQt6.QtWidgets import QMainWindow, QMessageBox
import sys
from PyQt6 import uic
import os
import re

# mock data
account = {"fullname": "", "email": "", "password": ""}


class SignupPage(QMainWindow):
    def __init__(self, main_window, root_dir):
        super().__init__()  # ke thua cac code init cua lop cha
        self.main_window = main_window  # luu tham so
        self.root_dir = root_dir

        # load file ui
        ui_path = self.root_dir + "/ui/signup.ui"
        uic.loadUi(ui_path, self)

        # bat su kien cho cac nut bam
        # 1. nut login
        self.signupbutton.clicked.connect(
            self.handle_register
        )  # click vao nut login -> goi ham handle_register
        # 2. nut chuyen register
        self.login.clicked.connect(
            self.goto_login
        )  # click vao nut chuyen register -> goi ham goto_login

        # chay app
        self.show()

    # ------------------ xu ly su kien ------------------
    def handle_register(self):
        # lay du lieu tu input form
        email_input = (
            self.email1.text().strip()
        )  # lay du lieu tu email input, xoa khoang trang 2 dau
        password_input = self.password.text()
        fullname_input = self.full_name.text()

        # kiem tra fullname
        if fullname_input.strip() == "":
            self.show_message("Vui lòng nhập đầy đủ họ tên!")
            return  # bao loi -> ket thuc

        # validate du lieu
        if self.__validate_input(email_input, password_input) is not None:
            print(self.__validate_input(email_input, password_input))
            # co loi -> bao loi
            self.show_message(self.__validate_input(email_input, password_input))
            return  # khong lam gi nua
        else:
            # luu tai khoan
            account["fullname"] = fullname_input
            account["email"] = email_input
            account["password"] = password_input
            # thanh cong -> chuyen sang home
            self.__goto_home()

    def goto_login(self):
        from pages.login import LoginPage

        self.login_page = LoginPage(
            main_window=self.main_window, root_dir=self.root_dir
        )
        self.close()  # ✅ đóng cửa sổ
    # ------------------ ham ho tro ------------------
    def __show_message(self, message):
        # Khởi tạo hộp thoại thông báo
        msg = QMessageBox()
        msg.setWindowTitle("Thông báo")
        msg.setText(message)
        msg.setIcon(
            QMessageBox.Icon.Information
        )  # Các icon mặc định: Information, Warning, Critical, Question
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Nút bấm OK
        # Hiển thị hộp thoại
        msg.exec()