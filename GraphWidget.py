# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import sys
from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout
from PySide6.QtCore import Qt 
# from PySide6.QtGui import QDragEnterEvent, QDropEvent


from MatplotlibCanvas import MplCanvas

class GraphWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        mplCanvas = MplCanvas(self)
        mplCanvas.ax.plot([0, 1, 2, 3], [10, 2, 20, 40])
        layout = QVBoxLayout(self)
        layout.addWidget(mplCanvas)
        self.setLayout(layout)
