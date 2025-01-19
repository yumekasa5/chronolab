# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width = 5, height = 4, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.updateGeometry()