import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class PlotCanvas(FigureCanvas):
    def __init__(self):
        self.fig = plt.figure()
        self.fig.set_tight_layout(True)
        self.axes = self.fig.add_subplot()
        super().__init__(self.fig)

class PlotBodeMod(PlotCanvas):
    def __init__(self):
        super().__init__()
    
    
    def plot(self, x, y, color, label):
        self.axes.clear()
        self.axes.grid(True)
        self.axes.semilogx(x, y, color, label)
        
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('|H| [dB]')
        self.fig.canvas.draw()
        
class PlotBodeFase(PlotCanvas):
    def __init__(self):
        super().__init__()
        
    def plot(self, x, y, color, label):
        self.axes.clear()
        self.axes.grid(True)
        self.axes.semilogx(x, y, color, label)
        
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('Fase [°]')
        self.fig.canvas.draw()
        
class PlotEntrada(PlotCanvas):
    def __init__(self):
        super().__init__()
    
    def plot(self, x, y, color, label):
        self.axes.clear()
        self.axes.grid(True)
        self.axes.plot(x, y, color, label)
        
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('Voltaje [V]')
        self.fig.canvas.draw()
        
class PlotCerosPolos(PlotCanvas):
    def __init__(self):
        super().__init__()
        
    def plot(self, x, y, color, label):
        self.axes.clear()
        self.axes.grid(True)
        self.axes.plot(x, y, color, label)
        
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('Fase [°]')
        self.fig.canvas.draw()