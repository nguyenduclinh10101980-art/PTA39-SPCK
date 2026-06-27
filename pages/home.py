from PyQt6.QtWidgets import QMainWindow, QMessageBox
import sys
from PyQt6 import uic
import os
import re


class HomePage(QMainWindow):
    def __init__(self, main_window, root_dir, cur_acc):
        super().__init__()
        self.main_window = main_window
        self.root_dir = root_dir
        self.cur_acc = cur_acc

        # load file ui
        ui_path = self.root_dir + "/ui/home.ui"
        uic.loadUi(ui_path, self)

        # bat su kien cho cac nut bam
        self.trangchu.clicked.connect(self.goto_trangchu_p)
        self.timkiem.clicked.connect(self.goto_timkiem_p)
        self.taikhoan.clicked.connect(self.goto_taikhoan_p)
        self.stackedWidget.setCurrentWidget(self.trangchu_p)
        self.setup_account()
        self.logout.clicked.connect(self.goto_logout)

        # hien thi giao dien
        self.show()

    # ------------------ xu ly su kien ------------------
    def goto_trangchu_p(self):
        self.stackedWidget.setCurrentWidget(self.trangchu_p)
    def goto_timkiem_p(self):
        self.stackedWidget.setCurrentWidget(self.timkiem_p)
    def goto_taikhoan_p(self):
        self.stackedWidget.setCurrentWidget(self.taikhoan_p)
    def setup_account(self):
        self.ten.setText(self.cur_acc['fullname'])
        self.email.setText(self.cur_acc['email'])
    def goto_logout(self):
        from pages.login import LoginPage
        self.loginpage=LoginPage(main_window=self.main_window, root_dir=self.root_dir
        )
        self.close()
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
        