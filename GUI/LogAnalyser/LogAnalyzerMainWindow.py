# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog

from DataHandler.load_csv_data import load_csv

class LogAnalyzerMainWindowDialog(tk.Toplevel):
    """Mainwwindow dialog for log analyzer"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Log Analyzer")
        self.geometry("1200x600")
        
        self.create_widgets()
        
    def create_widgets(self):
        """Create widgets"""
        self.openFileDialogButton = tk.Button(self, text="Open...", width=10, height=2, font=("Meiryo", 9))
        self.openFileDialogButton.bind("<ButtonPress>", self.openFileDialog)
        self.openFileDialogButton.place(x=10, y=10)
        
        self.treeView = ttk.Treeview(self, columns=("col1", "col2", "col3", "col4", "col5", "col6"), show='headings')
        self.treeView.heading("col1", text="Column 1")
        self.treeView.heading("col2", text="Column 2")
        self.treeView.heading("col3", text="Column 3")
        self.treeView.heading("col4", text="Column 4")
        self.treeView.heading("col5", text="Column 5")
        self.treeView.heading("col6", text="Column 6")
        self.treeView.place(x=10, y=60)
        
        
    def openFileDialog(self, event):
        """Open file dialog"""
        self.filepath = tk.filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if self.filepath:
            print(self.filepath)
            df = load_csv(self.filepath)
            self.displauDataFrame(df)
        return "break"
    
    def displauDataFrame(self, df):
        """Display DataFrame"""
        for row in self.treeView.get_children():
            self.treeView.delete(row)
            
        for i, row in df.iterrows():
            self.treeView.insert("", "end", values=list(row))
        
        