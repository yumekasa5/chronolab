# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon

import MainWindowUI


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowIcon(QIcon("./data/icon/ChronoLab.ico"))
    ui = MainWindowUI.Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())