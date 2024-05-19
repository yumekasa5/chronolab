# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import tkinter as tk
from PIL import Image, ImageTk

from Common._AppVersion import APP_VERSION

class ModeSelectDialog(tk.Frame):
    """Mode Select Dialog"""
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(sticky='nsew')
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.mode_String = tk.StringVar()
        self.mode_String.set("unknown")
        self.create_widgets()
        self.master.geometry("350x150")  # Set the size of the dialog window
        self.master.title("Select Mode")  # Set the title of the dialog window

    def create_widgets(self):
        """Initialize widgets"""
        
        self.appname_label = tk.Label(text="ChronoLab ver." + APP_VERSION, font=("Meiryo", 16))
        self.appname_label.place(x=80, y=10)
        self.img = ImageTk.PhotoImage(Image.open("./data/icon/ChronoLab.ico"))
        self.label_img = tk.Label(image=self.img)
        self.label_img.place(x=10, y=10)
        
        self.label = tk.Label(text="Select operation mode", font=("Meiryo", 12))
        self.label.place(x=80, y=50)
        self.button_admin = tk.Button(text="Admin", command=lambda: self.set_admin("admin"), width=10, font=("Meiryo", 10))
        self.button_admin.place(x=30, y=100)
        self.button_develop = tk.Button(text="Develop", command=lambda: self.set_develop("develop"), width=10, font=("Meiryo", 10))
        self.button_develop.place(x=130, y=100)
        self.button_user = tk.Button(text="User", command=lambda: self.set_user("user"), width=10, font=("Meiryo", 10))
        self.button_user.place(x=230, y=100)

    def set_admin(self, mode):
        """Select the Admin mode and close the window"""
        self.mode_String.set(mode)
        self.master.destroy()

    def set_develop(self, mode):
        """Select the Develop mode and close the window"""
        self.mode_String.set(mode)
        self.master.destroy()

    def set_user(self, mode):
        """Select the User mode and close the window"""
        self.mode_String.set(mode)
        self.master.destroy()
