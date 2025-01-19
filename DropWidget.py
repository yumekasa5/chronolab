# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt 
from PySide6.QtGui import QDragEnterEvent, QDropEvent

class DropWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.initUI()
    
    def initUI(self):
        self.label = QLabel("Please drop your text here.", self)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        
    def dragEnterEvent(self, event: QDragEnterEvent): 
        if event.mimeData().hasText():
            event.acceptProposedAction()
            
    def dropEvent(self, event: QDropEvent):
        text = event.mimeData().text()
        self.label.setText(f"Dropped text: {text}")