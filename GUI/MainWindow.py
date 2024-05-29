# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog

from GUI.SettingDialog import SettingDialog
from GUI.FigureCanvas import FigureCanvasFrame
from GUI.FigureSettingFrame import FigureSettingFrame
from GUI.SharedValible import SharedValibleBase

class MainWindow(tk.Frame):
    def __init__(self, master=None, mode="user"):
        """Condtructor"""
        super().__init__(master)
        self.master = master
        self.mode = mode
        self.pack()

        # Opearation mode
        self.mode = mode
        print("Operation mode: " + mode)

        self.width = 1920
        self.height = 1080
        master.geometry(str(self.width) + "x" + str(self.height))
        self.master.title("ChronoLab")
        self.svPath = tk.StringVar()
        
        self.sharedValible = SharedValibleBase()
        
        self.create_widgets()

    def create_widgets(self):
        """Initialize widgets"""
        
        # File Select Button
        self.fileSelectButton = tk.Button(text="Select", width=15, height=2, font=("Meyrio", 12))
        self.fileSelectButton.place(x=0, y=300)
        self.fileSelectButton.bind("<ButtonPress>", self.openFileDialog)
        
        # COM Port Select Spinbox
        self.validate_com_port = self.master.register(self.validate_com_port)
        self.comPortLabel = tk.Label(text="COM Port :", width=10, height=2, font=("Meyrio", 12))
        self.comPortLabel.place(x=20, y=10)
        self.comPortSpinbox = tk.Spinbox(from_=1, to=10, validate="key", width=3, validatecommand=(self.validate_com_port, '%P'), font=("Meyrio", 12))
        self.comPortSpinbox.setvar(name="COM Port", value="3")
        self.comPortSpinbox.place(x=125, y=20)
        
        # Figure Setting Frame
        self.figureSettingFrame = FigureSettingFrame(master=self.master, sharedValible=self.sharedValible)
        self.figureSettingFrame.place(x=500, y=100)
        

        # Table
        self.treeViewStyle = ttk.Style()
        self.treeViewStyle.configure("Treeview", font=("Meiryo", 15), rowheight=30, fieldbackground="white")
        self.treeViewStyle.configure("Treeview.Heading", font=("Meiryo", 15))
        self.treeView = ttk.Treeview(self.master, columns=["BK", "PP", "Horse", "A&S", "Wgt(kg)", "Jockey"], style="Treeview", height=18, show="headings")
        self.treeView.column("#0", width=0, stretch="no")
        self.treeView.column("BK", anchor="center", width=60)
        self.treeView.column("PP", anchor="center", width=60)
        self.treeView.column("Horse", anchor="w", width=250)
        self.treeView.column("A&S", anchor="center", width=80)
        self.treeView.column("Wgt(kg)", anchor="center", width=100)
        self.treeView.column("Jockey", anchor="w", width=210)
        self.treeView.heading("#0", text="")
        self.treeView.heading("BK", text="BK", anchor="center")
        self.treeView.heading("PP", text="PP", anchor="center")
        self.treeView.heading("Horse", text="Horse", anchor="w")
        self.treeView.heading("A&S", text="A&S", anchor="center")
        self.treeView.heading("Wgt(kg)", text="Wgt(kg)", anchor="center")
        self.treeView.heading("Jockey", text="Jockey", anchor="w")
        self.treeView.insert("", "end", values=("1", "1", "パンサラッサ", "1.1", "55.0", "Yutaka Yoshida"))
        self.treeView.insert("", "end", values=("1", "2", "スワーヴリチャード", "1.2", "55.0", "O.Murphy"))
        self.treeView.insert("", "end", values=("2", "3", "クロノジェネシス", "1.3", "55.0", "Yuuichi Kitamura"))
        self.treeView.insert("", "end", values=("2", "4", "エフフォーリア", "1.4", "55.0", "Takeshi Yokoyama"))
        self.treeView.insert("", "end", values=("3", "5", "アーモンドアイ", "1.5", "55.0", "C.Lemaire"))
        self.treeView.insert("", "end", values=("4", "6", "ダンビュライト", "1.6", "55.0", "M.Demuro"))
        self.treeView.insert("", "end", values=("4", "7", "コントレイル", "1.7", "55.0", "Yuichi Fukunaga"))
        self.treeView.insert("", "end", values=("4", "8", "ディープインパクト", "1.8", "55.0", "Yutaka Take"))
        self.treeView.insert("", "end", values=("5", "9", "スタニングローズ", "1.9", "55.0", "Ryusei Sakai"))
        self.treeView.insert("", "end", values=("5", "10", "フィエールマン", "1.10", "55.0", "Kenichi Ikezoe"))
        self.treeView.insert("", "end", values=("6", "11", "サラキア", "1.11", "55.0", "Kohei Matsuyama"))
        self.treeView.insert("", "end", values=("6", "12", "グランアレグリア", "1.12", "55.0", "J.Moreira"))
        self.treeView.insert("", "end", values=("7", "13", "アエロリット", "1.13", "55.0", "Keita Tosaki"))
        self.treeView.insert("", "end", values=("7", "14", "サンレイポケット", "1.14", "55.0", "Katsuma Samejima"))
        self.treeView.insert("", "end", values=("8", "15", "リスグラシュー", "1.15", "55.0", "D.lane"))
        self.treeView.insert("", "end", values=("8", "16", "シュバルグラン", "1.16", "55.0", "R.Moore"))
        self.treeView.insert("", "end", values=("8", "17", "スターズオンアース", "1.17", "55.0", "Yuga Kawada"))
        self.treeView.insert("", "end", values=("8", "18", "スティッフェリオ", "1.18", "55.0", "Norihiro Yokoyama"))
        self.treeView.place(x=10, y=450)
        
        # self.treeView.bind("<<TreeviewSelect>>", self.toggle_checkbox)

        # ListBox
        color_list = ["red", "blue", "green"]
        color_v = tkinter.StringVar(self.master, value=color_list)
        self.sampleListBox = tk.Listbox(self.master, width=10, height=5, listvariable=color_v, font=("Meyrio", 12))
        self.sampleListBox.place(x=200, y=300)

        # Check ListBox status button
        self.checkBtn = tk.Button(text="Check", width=15, height=2, font=("Meyrio", 12))
        
        # Update Canvas Button
        self.updateCanvasButton = tk.Button(text="Update", width=15, height=2, font=("Meyrio", 12), command=self.update_canvas)
        self.updateCanvasButton.place(x=1000, y=700)
        
        # Open Setting Dialog Button
        self.settingButton = tk.Button(text="Setting", width=15, height=2, font=("Meyrio", 12))
        self.settingButton.place(x=0, y=400)
        self.settingButton.bind("<ButtonPress>", self.openSettingDialog)
        self.settingButton.place(x=0, y=400)
        
        # ComboBox for selecting specified x value
        self.specified_x_value_IntVar = tk.IntVar()
        self.specified_previous_x_value_IntVar = tk.IntVar()
        self.specifiedXComboBox = ttk.Combobox(self.master, textvariable=self.specified_x_value_IntVar, width=5, font=("Meyrio", 12))
        self.specifiedXComboBox["values"] = [str(i) for i in range(100)]
        self.specifiedXComboBox.place(x=1000, y=1000)
        self.specifiedXComboBox.bind("<<ComboboxSelected>>", self.comboBoxSelected)
        self.specifiedXComboBox.set("0")
        self.specified_x_value_IntVar.set(0)
        self.specified_previous_x_value_IntVar.set(0)
        
        # FigureCanvas
        self.canvas_frame = tk.Frame(self.master)
        self.canvas_frame.place(x=1000, y=10)
        self.canvas = FigureCanvasFrame(master=self.canvas_frame, sharedValible=self.sharedValible)
        self.update_canvas()

    def validate_com_port(self, value):
        if value == "":
            return True
        try:
            int(value)
        except ValueError:
            return False
        return True
    
    def checkListBoxStatus(self, event):
        print(f"ListBox(ACTIVE):{self.sampleListBox.get(tk.ACTIVE)}")
        print(f"ListBox(CurSelect):{self.sampleListBox.curselection()}")

    def deleteDataFromListBox(self, event):
        index = self.sampleListBox.curselection()
        self.sampleListBox.delete(index)

    def openFileDialog(self, event):
        """Open File Dialog and return string of file path"""
        print("File Dialog open.")
        path = ""
        path = tkinter.filedialog.askopenfilename()
        print(f"Selected file path: {path}")
        return "break"

    def openSettingDialog(self, event):
        """Open Setting Dialog"""
        print("Setting Dialog open.")
        setting_dialog = SettingDialog(self)
        return "break"

    check_str = {"uncheck": "☐", "checked": "☑"}  # ☐☑☒ Checkbox characters
    def toggle_checkbox(self, event):
        row_id = self.treeView.focus()
        row_vals = self.treeView.item(row_id, "values")
        if row_vals[0] == self.check_str["uncheck"]:
            self.treeView.item(row_id, values=(self.check_str["checked"], row_vals[1], row_vals[2], row_vals[3]))
        else:
            self.treeView.item(row_id, values=(self.check_str["uncheck"], row_vals[1], row_vals[2], row_vals[3]))

    # Function to add IDs of rows with ☑ in the first column of Treeview to the ListBox
    def add_checked_ids_to_listbox(self):
        checked_ids = []
        for item in self.treeView.get_children():
            values = self.treeView.item(item, "values")
            if values[0] == self.check_str["checked"]:
                checked_ids.append(values[1])
        self.sampleListBox.delete(0, tk.END)
        for id in checked_ids:
            self.sampleListBox.insert(tk.END, id)
    
    def comboBoxSelected(self, event):
        print(self.specifiedXComboBox.get())
        self.canvas.plotvline(int(self.specifiedXComboBox.get()), previouslabel=str(self.specified_previous_x_value_IntVar.get()), currentlabel=str(self.specifiedXComboBox.get()))
        self.specified_previous_x_value_IntVar.set(int(self.specifiedXComboBox.get()))
            
    def update_canvas(self):
        self.canvas.update()
        
    # Spinbox event
    def setXSpinBoxScaleValue(self, new_scale):
        self.canvas.ax.set_xlim(0, new_scale)
        self.update_canvas()
        
    # selectd item event
    def selected_item(self, event):
        global selected_item
        selected_item = self.treeView.focus()
        print(selected_item)
        selected_item = self.treeView.item(selected_item, "values")
    
