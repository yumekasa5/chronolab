# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import tkinter as tk

class SharedValibleBase:
    def __init__(self):
        self.mode = "user"
        self.width = 1920
        self.height = 1080
        self.svPath = tk.StringVar()
        self.comPort = tk.StringVar()
        self.comPort.set("3")
        self.x_scale = 45.0
        self.y_scale = 600.0
        self.title = "Random Number Plot"
        self.x_label = "X-axis"
        self.y_label = "Y-axis"
        self.is_gui_mode = True
        self.args = []
        self.path = ""
        self.mode = "user"
        self.is_gui_mode = True
        self.root = None
        self.modeSelectDialog = None
        self.app = None
        self.fileSelectButton = None
    
    @property
    def x_scale(self):
        return self.__x_scale
    
    @x_scale.setter
    def x_scale(self, value):
        self.__x_scale = value
        
    @property
    def y_scale(self):
        return self.__y_scale
    
    @y_scale.setter
    def y_scale(self, value):
        self.__y_scale = value