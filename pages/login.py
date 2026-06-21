from PyQt6.QtWidgets import QMainWindow, QMessageBox
import sys
from PyQt6 import uic
import os
import re

# mock data
account = {"fullname": "Trung hieu", "email": "nguyenductrunghieu6@gmail.com", "password": "123456"}


class LoginPage(QMainWindow):
    def __init__(self, main_window, root_dir):
        super().__init__()  # ke thua cac code init cua lop cha
        self.main_window = main_window  # luu tham so
        self.root_dir = root_dir

        # load file ui
        ui_path = self.root_dir + "/ui/login.ui"
        uic.loadUi(ui_path, self)

        # bat su kien cho cac nut bam
        self.loginbutton.clicked.connect(
            self.handle_login
        )
        self.register_2.clicked.connect(
            self.goto_register
        )


        # chay app
        self.show()

    # ------------------ xu ly su kien ------------------
    def handle_login(self):
        # lay du lieu tu input form
        email_input = (
            self.answer1.text().strip()
        )   
        password_input = self.answer.text()
         # validate du lieu
        if self.__validate_input(email_input, password_input) is not None:
            print(self.__validate_input(email_input, password_input))
            # co loi -> bao loi
            self.show_message(self.__validate_input(email_input, answer1_input)) # type: ignore
            return  # khong lam gi nua
        else:
            # thanh cong -> chuyen sang home
            self.__goto_home()

    def goto_register(self):
        from pages.signup import SignupPage

        self.register_page = SignupPage(
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