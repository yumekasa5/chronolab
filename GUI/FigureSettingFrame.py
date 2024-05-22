# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import tkinter as tk
import tkinter.ttk as ttk

class FigureSettingFrame(tk.Frame):
    """Frame for setting the figure"""
    def __init__(self, master=None, sharedValible=None):
        super().__init__(master)
        self.master = master
        self.shared_var = sharedValible
        self.create_widgets()

    def create_widgets(self):
        """Initialize widgets"""
        self.label_title = tk.Label(text="Figure Setting", font=("Meiryo", 12))
        self.label_title.place(x=300, y=10)
        self.label_title = tk.Label(text="Title", font=("Meiryo", 10))
        self.label_title.place(x=300, y=40)
        self.entry_title = tk.Entry(width=20, font=("Meiryo", 10))
        self.entry_title.place(x=360, y=40)
        
        # Spinbox for scale x-axis
        self.label_scale_x = tk.Label(text="X-axis Scale", font=("Meiryo", 10))
        self.label_scale_x.place(x=300, y=80)
        
        self.scaleXSpingBox = tk.Spinbox(from_=0, to=100, increment=0.1, width=5, font=("Meiryo", 10), command=self.on_SpinBoxXScaleChange)
        # スピンボックスの初期値を設定
        self.scaleXSpingBox.delete(0, tk.END)
        self.scaleXSpingBox.insert(0, "5.0")
        self.scaleXSpingBox.place(x=480, y=80)
        
        # Spinbox for scale y-axis
        self.label_scale = tk.Label(text="Y-axis Scale", font=("Meiryo", 10))
        self.label_scale.place(x=300, y=110)
        
        self.scaleYSpingBox = tk.Spinbox(from_=0, to=100, increment=0.1, width=5, font=("Meiryo", 10), command=self.on_SpinBoxYScaleChange)
        # スピンボックスの初期値を設定
        self.scaleYSpingBox.delete(0, tk.END)
        self.scaleYSpingBox.insert(0, "10.0")
        self.scaleYSpingBox.place(x=480, y=110)
        
    # X Spinbox event
    def on_SpinBoxXScaleChange(self):
        # X軸スピンボックスの値を取得
        self.x_scale = float(self.scaleXSpingBox.get())
        print(self.x_scale)
        self.shared_var.x_scale = self.x_scale
    
    # Y Spinbox event
    def on_SpinBoxYScaleChange(self):
        # Y軸スピンボックスの値を取得
        self.y_scale = float(self.scaleYSpingBox.get())
        print(self.y_scale)
        self.shared_var.y_scale = self.y_scale
        
        