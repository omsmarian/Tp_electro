import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

#clase padre
class PlotCanvas(FigureCanvas):
    def __init__(self):
        self.fig = plt.figure()
        self.fig.set_tight_layout(True)
        self.axes = self.fig.add_subplot()
        self.axes.grid(True)
        super().__init__(self.fig)

#calse para plotear modulo de bode
class PlotBodeMod(PlotCanvas):
    def __init__(self):
        super().__init__()
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('|H| [dB]')
    
    def plot(self, w, Hdb):
        self.axes.clear()
        self.axes.grid(True)
        self.axes.semilogx(w, Hdb)
        
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('|H| [dB]')
        self.fig.canvas.draw()

#calse para plotear la fase del bode    
class PlotBodeFase(PlotCanvas):
    def __init__(self):
        super().__init__()
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('Fase [°]')
        
    def plot(self, w, phi):
        self.axes.clear()
        self.axes.grid(True)
        self.axes.semilogx(w, phi)
        
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('Fase [°]')
        self.fig.canvas.draw()

#clase para plotear la entrada
class PlotEntrada(PlotCanvas):
    def __init__(self):
        super().__init__()
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('Voltaje [V]')
    
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
        self.axes.set_xlabel('σ')
        self.axes.set_ylabel('jω')
        
    def plot(self, realCeros, imagCeros, realPolos, imagPolos):
        self.axes.clear()
        self.axes.grid(True)
        self.axes.scatter(realCeros, imagCeros, marker = 'o', color = 'blue', label = 'Ceros')
        self.axes.scatter(realPolos, imagPolos, marker = 'x', color = 'red', label = 'Polos')
        
        self.axes.axhline(0, color='black', linewidth=1)
        self.axes.axvline(0, color='black', linewidth=1)
        self.axes.set_xlabel('σ')
        self.axes.set_ylabel('jω')
        self.fig.canvas.draw()