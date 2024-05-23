# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class FigureCanvasFrame(tk.Frame):
    """Canvas Frame for drawing figures"""
    def __init__(self, master=None, sharedValible=None):
        super().__init__(master, width=800, height=800)  # Set the size of the frame
        self.master = master
        self.shared_var = sharedValible
        self.create_figure()

    def create_figure(self):
        """Set the figure"""
        # Setting of the matplotlib figure
        self.fig = Figure(figsize=(6, 6), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("Random Number Plot")
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")
        self.ax.set_xlim(0, self.shared_var.x_scale)
        self.ax.set_ylim(0, self.shared_var.y_scale)
        
        # Create a canvas to draw the figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
    def update(self):
        """"Update the figure"""
        self.ax.clear()
        self.ax.set_title("Random Number Plot")
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")
        self.ax.set_xlim(0, self.shared_var.x_scale)
        self.ax.set_ylim(0, self.shared_var.y_scale)
        self.ax.plot(np.random.rand(10))
        self.canvas.draw()