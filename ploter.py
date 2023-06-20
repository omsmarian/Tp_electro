import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np 

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
        self.setUp()
    
    def plot(self, w, Hdb):
        self.setUp()
        self.axes.semilogx(w, Hdb)
        self.fig.canvas.draw()

    def setUp(self):
        self.axes.clear()
        self.axes.grid(True, which="both", linestyle='--')
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('|H| [dB]')
        self.fig.canvas.draw()

#calse para plotear la fase del bode    
class PlotBodeFase(PlotCanvas):
    def __init__(self):
        super().__init__()
        self.setUp()
        
    def plot(self, w, phi):
        self.setUp()
        self.axes.semilogx(w, phi)
        self.fig.canvas.draw()

    def setUp(self):
        self.axes.clear()
        self.axes.grid(True, which="both", linestyle='--')
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('Fase [°]')
        self.fig.canvas.draw()
        
#clase para plotear la entrada
class PlotEntrada(PlotCanvas):
    def __init__(self):
        super().__init__()
        self.setUp('')
    
    def plot(self, t, tout, yEntrada, ySalida, prefix):
        self.setUp(prefix)
        self.axes.plot(t, yEntrada, color = 'red', label = 'Señal de entrada')
        self.axes.plot(tout, ySalida, label = 'Señal de salida')
        self.fig.canvas.draw()

    def setUp(self, prefix):        
        self.axes.clear()
        self.axes.grid(True, linestyle='--')
        self.axes.set_xlabel(f'Tiempo [{prefix}s]')
        self.axes.set_ylabel('Voltaje [V]')
        self.fig.canvas.draw()

#clase para plotear ceros y polos        
class PlotCerosPolos(PlotCanvas):
    def __init__(self):
        super().__init__()
        self.setUp()
        
    def plot(self, realCeros, imagCeros, realPolos, imagPolos):
        self.setUp()
        self.axes.scatter(realCeros, imagCeros, marker = 'o', color = 'blue', label = 'Ceros')
        self.axes.scatter(realPolos, imagPolos, marker = 'x', color = 'red', label = 'Polos')
        self.fig.canvas.draw()

    def setUp(self):
        self.axes.clear()
        self.axes.grid(True, linestyle='--')
        self.axes.axhline(0, color='black', linewidth=1)
        self.axes.axvline(0, color='black', linewidth=1)
        self.axes.set_xlabel('σ')
        self.axes.set_ylabel('jω')
        self.fig.canvas.draw()