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
        