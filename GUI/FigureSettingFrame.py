# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import tkinter as tk
import tkinter.ttk as ttk

class FigureSettingFrame(tk.Frame):
    """Frame for setting the figure"""
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        """Initialize widgets"""
        self.label_title = tk.Label(text="Figure Setting", font=("Meiryo", 12))
        self.label_title.place(x=300, y=10)
        self.label_title = tk.Label(text="Title", font=("Meiryo", 10))
        self.label_title.place(x=300, y=40)
        self.entry_title = tk.Entry(width=20, font=("Meiryo", 10))
        self.entry_title.place(x=360, y=40)
        self.label_xlabel = tk.Label(text="X-axis", font=("Meiryo", 10))
        self.label_xlabel.place(x=300, y=70)
        self.entry_xlabel = tk.Entry(width=20, font=("Meiryo", 10))
        self.entry_xlabel.place(x=360, y=70)
        self.label_ylabel = tk.Label(text="Y-axis", font=("Meiryo", 10))
        self.label_ylabel.place(x=300, y=100)
        self.entry_ylabel = tk.Entry(width=20, font=("Meiryo", 10))
        
        
        # Spinbox for scale x-axis
        self.label_scale_x = tk.Label(text="X-axis Scale", font=("Meiryo", 10))
        self.label_scale_x.place(x=420, y=130)
        
        self.scaleXSpingBox = tk.Spinbox(from_=0, to=100, increment=0.1, width=5, font=("Meiryo", 10))
        self.scaleXSpingBox.place(x=500, y=130)
        
        # Spinbox for scale y-axis
        self.label_scale = tk.Label(text="Scale", font=("Meiryo", 10))
        self.label_scale.place(x=300, y=130)
        
        self.scaleYSpingBox = tk.Spinbox(from_=0, to=100, increment=0.1, width=5, font=("Meiryo", 10), command=self.on_YSpinBoxChange)
        self.scaleYSpingBox.place(x=360, y=130)
        
    # X Spinbox event
    def on_XSpinBoxChange(self):
        # X軸スピンボックスの値を取得
        x = float(self.scaleXSpingBox.get())
    
    # Y Spinbox event
    def on_YSpinBoxChange(self):
        # Y軸スピンボックスの値を取得
        y = float(self.scaleYSpingBox.get())