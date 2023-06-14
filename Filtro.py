import numpy as np
from scipy import signal

class filtro:

    def __init__(self):
        self.filterOrder = 1
        self.filterType = 0
        self.gain = 1
        self.fo = 1
        self.fp = 1
        self.xio = 0
        self.xip = 0

        # Bode 
        self.Hs = ((0,0,1),(0,0,1))    # (num,den)
        self.sys = signal.TransferFunction(self.Hs[0], self.Hs[1])
        self.w, self.Hdb, self.phi = (0,0,0)

        # Input Signal
        self.t = np.linspace(0, 10, 1000)
        self.Vin = np.sin(2* np.pi * self.t)
        self.Vout = 0
        _, self.Vout, _ = signal.lsim(self.sys, U=self.Vin, T=self.t)

        # Zeros & Poles
        self.zeros = []
        self.poles = []
        self.realZeros = np.real(self.zeros)
        self.imagZeros = np.imag(self.zeros)
        self.realPoles = np.real(self.poles)
        self.imagPoles = np.imag(self.poles)

    def num(self, newNum):
        self.Hs = (newNum, self.Hs[1])
        return

    def den(self, newDen):
        self.Hs = (self.Hs[0], newDen)
        return
    
    def update (self):
        if self.filterOrder == 1:
            self.set_PO()
        elif self.filterOrder == 2:
            self.set_SO()
        #elif self.filterOrder == 3:     # Sup Order
        self.updateTF()
        self.realZeros = np.real(self.zeros)
        self.imagZeros = np.imag(self.zeros)
        self.realPoles = np.real(self.poles)
        self.imagPoles = np.imag(self.poles)
    
    def updateTF(self):
        self.sys = signal.TransferFunction(self.Hs[0],self.Hs[1])
        self.w, self.Hdb, self.phi = signal.bode(self.sys)
    
    def set_PO (self):
        wo = 2*np.pi*self.fp
        if wo != 0:
            if self.filterType == 0 : # First order - High Pass
                self.num((0,1,0))
                self.den((0, 1/wo, 1))
            elif self.filterType == 1 : # First order - Low Pass 
                self.num((0,0,1))
                self.den((0, 1/wo, 1))
            elif self.filterType == 2: # First order - All Pass
                self.num((0, 1/wo, -1))
                self.den((0, 1/wo, 1))   
            elif self.filterType == 'CeroPO': # First order - Arbitrario - Zero
                self.num((0, 1, wo))
                self.den((0, 0, 1))
            elif self.filterType == 'PoloPO': # First order - Arbitrario - Pole
                self.num((0, 0, 1))
                self.den((0, 1, wo))
        self.zeros, self.poles, _ = signal.tf2zpk(self.Hs[0], self.Hs[1])
    
    def set_SO (self):
        xi = self.xip
        wo = 2*np.pi*self.fp
        if wo != 0:
            if self.filterType == 0: # Second order - High Pass
                self.num((1, 0, 0))
                self.den((1/wo**2, 2*xi/wo, 1))
            elif self.filterType == 1: # Second order - Low Pass
                self.num((0, 0, 1))
                self.den((1/wo**2, 2*xi/wo, 1))
            elif self.filterType == 2: # Second order - All Pass
                self.num((1/wo**2, -2*xi/wo, 1))
                self.den((1/wo**2, 2*xi/wo, 1))
            elif self.filterType == 3: # Second order - Band Pass
                self.num((0, 1, 0))
                self.den((1/wo**2, 2*xi/wo, 1))
            elif self.filterType == 4 : # Second order - Notch
                self.num((1/wo**2, 0, 1))
                self.den((1/wo**2, 2*xi/wo, 1))
        self.zeros, self.poles, _ = signal.tf2zpk(self.Hs[0], self.Hs[1])
    
    def set_SO_arbitrario(self):
        return                          #TODO: Basicamente la funcion entera :)
    
    def set_sup(self, num, den):
        return

    
####################   TEST   ####################
   
#def plot(filtro):
#    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))
#
#    axes[0, 0].semilogx(filtro.w, filtro.Hdb)
#    axes[0, 0].grid(True)
#    #plt.xlim(0,1000)
#    axes[1, 0].semilogx(filtro.w, filtro.phi)
#    axes[1, 0].grid(True)
#    
#    axes[0, 1].scatter(np.real(filtro.zeros), np.imag(filtro.zeros), marker = 'o', color = 'blue', label = 'Ceros')
#    axes[0, 1].scatter(np.real(filtro.poles), np.imag(filtro.poles), marker = 'x', color = 'red', label = 'Polos')
#    axes[0, 1].set_xlabel('σ')
#    axes[0, 1].set_ylabel('jω')
#    axes[0, 1].axhline(0, color='black', linewidth=1)
#    axes[0, 1].axvline(0, color='black', linewidth=1)
#    axes[0, 1].grid(True)
#    
#    axes[1, 1].plot(filtro.t, filtro.Vin, label='Entrada', color='red')
#    axes[1, 1].plot(filtro.t, filtro.Vout, label='Salida', color='blue')
#    axes[1, 1].grid(True)
#
#    fig.tight_layout()
#    plt.show()
#    return

#meme = filtro()
#
#wo = 100
#fo = wo/(2*np.pi)
#xi = 0.5
#
#meme.set_PO('CeroPO', fo)
#
#plot(meme)
