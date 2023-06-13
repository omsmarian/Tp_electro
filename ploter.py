import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

#clase padre
class PlotCanvas(FigureCanvas):
    def __init__(self):
        self.fig = plt.figure()
        self.fig.set_tight_layout(True)
        self.axes = self.fig.add_subplot()
        super().__init__(self.fig)

#calse para plotear modulo de bode
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

#calse para plotear la fase del bode    
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

#clase para plotear la entrada
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

#calse para plotear ceros y polos        
class PlotCerosPolos(PlotCanvas):
    def __init__(self):
        super().__init__()
        
    def plot(self, x, y, color, label):
        self.axes.clear()
        self.axes.grid(True)
        self.axes.plot(x, y, color, label)      #Eze arreglalo
        
        self.axhline(0, color='black', linewidth=1)
        self.axvline(0, color='black', linewidth=1)
        self.axes.set_xlabel('σ')
        self.axes.set_ylabel('jω')
        self.fig.canvas.draw()