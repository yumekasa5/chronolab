# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import sys
from PySide6.QtWidgets import QWidget, QTextEdit
from PySide6.QtCore import Qt 
from PySide6.QtGui import QDragEnterEvent, QDropEvent

class DraggableTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()
            
    def dropEvent(self, event: QDropEvent):
        text = event.mineData().text()
        self.insertPlaneText(text)