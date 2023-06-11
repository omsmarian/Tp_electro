import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

class filter:
    gain = 1
    zeros = []
    poles = []
    f0 = 0
    xi = 0

    Hs = ((0,0,1),(0,0,1))    # (num,den)
    sys = signal.TransferFunction(Hs[0], Hs[1])
    w, Hdb, phi = (0,0,0)

    t = np.linspace(0, 10, 1000)
    Vin = np.sin(2* np.pi * t)
    Vout = 0

    def __init__(self):
        self.sys = signal.TransferFunction(self.Hs[0], self.Hs[1])
        #self.w, self.Hdb, self.phi = signal.bode(self.sys)
        _, self.Vout, _ = signal.lsim(self.sys, U=self.Vin, T=self.t)

    def num(self, newNum):
        self.Hs = (newNum, self.Hs[1])
        return

    def den(self, newDen):
        self.Hs = (self.Hs[0], newDen)
        return
    
    def update(self):
        self.sys = signal.TransferFunction(self.Hs[0],self.Hs[1])
        self.w, self.Hdb, self.phi = signal.bode(self.sys)
        return
    
    def set_PO (self, tipoFiltro, f):
        self.f0 = f
        wo = 2*np.pi*f
        if tipoFiltro == 'PAPO' : # First order - High Pass
            self.num((0,1,0))
            self.den((0, 1/wo, 1))
            self.zeros.append(0)
            self.poles.append(-wo)
            self.gain = self.gain * 1/wo            #TODO
        elif tipoFiltro == 'PBPO': # First order - Low Pass 
            self.num((0,0,1))
            self.den((0, 1/wo, 1))
            self.poles.append(-wo)
            self.gain = self.gain * 1/wo
        elif tipoFiltro == 'PTPO': # First order - All Pass
            self.num((0, 1/wo, -1))
            self.den((0, 1/wo, 1))
            self.zeros.append(-wo)
            self.poles.append(-wo)
        #elif tipoFiltro == 'APO': # First order - Arbitrario
        self.update()
        return
    
    def set_SO (self, tipoFiltro, f, xi):
        self.xi = xi
        self.f0 = f
        wo = 2*np.pi*f
        if tipoFiltro == 'PASO': # Second order - High Pass
            self.num((1, 0, 0))
            self.den((1/wo**2, 2*xi/wo, 1))
        elif tipoFiltro == 'PBSO': # Second order - Low Pass
            self.num((0, 0, 1))
            self.den((1/wo**2, 2*xi/wo, 1))
        elif tipoFiltro == 'PTSO': # Second order - All Pass
            self.num((1/wo**2, -2*xi/wo, 1))
            self.den((1/wo**2, 2*xi/wo, 1))
        elif tipoFiltro == 'PBSO': # Second order - Band Pass
            self.num((0, 1, 0))
            self.den((1/wo**2, 2*xi/wo, 1))
        elif tipoFiltro == 'NSO' : # Second order - Notch
            self.num((1/wo**2, 0, 1))
            self.den((1/wo**2, 2*xi/wo, 1))
        self.zeros, self.poles, _ = signal.tf2zpk(self.Hs[0], self.Hs[1])
        self.update()
        return
    
def plot(filter):
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))

    axes[0, 0].semilogx(filter.w, filter.Hdb)
    axes[0, 0].grid(True)
    #plt.xlim(0,1000)
    axes[1, 0].semilogx(filter.w, filter.phi)
    axes[1, 0].grid(True)
    
    axes[0, 1].scatter(np.real(filter.zeros), np.imag(filter.zeros), marker = 'o', color = 'blue', label = 'Ceros')
    axes[0, 1].scatter(np.real(filter.poles), np.imag(filter.poles), marker = 'x', color = 'red', label = 'Polos')
    axes[0, 1].set_xlabel('σ')
    axes[0, 1].set_ylabel('jω')
    axes[0, 1].axhline(0, color='black', linewidth=1)
    axes[0, 1].axvline(0, color='black', linewidth=1)
    axes[0, 1].grid(True)
    
    axes[1, 1].plot(filter.t, filter.Vin, label='Entrada', color='red')
    axes[1, 1].plot(filter.t, filter.Vout, label='Salida', color='blue')
    axes[1, 1].grid(True)

    fig.tight_layout()
    plt.show()
    return


meme = filter()

meme.set_SO('PASO', 100/(2*np.pi), 0.5)
plot(meme)