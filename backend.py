from scipy import signal
import matplotlib.pyplot as plt

class filter:
    G = 0
    Hs = ((0,0,1),(0,0,1))    # (num,den)
    sys = signal.TransferFunction(Hs[0], Hs[1])
    w, Hdb, phi = (0,0,0)  

    def __init__(self):
        self.sys = signal.TransferFunction(self.Hs[0], self.Hs[1])
        self.w, self.Hdb, self.phi = signal.bode(self.sys)

    def num(self, newNum):
        self.Hs = (newNum, self.Hs[1])
        self.update()
        return

    def den(self, newDen):
        self.Hs = (self.Hs[0], newDen)
        self.update()
        return
    
    def update(self):
        self.sys = signal.TransferFunction(self.Hs[0],self.Hs[1])
        self.w, self.Hdb, self.phi = signal.bode(self.sys)
        return
    
    def set (self, tipoFiltro):
        if tipoFiltro == 'PAPO' : # First order - High Pass
            self.
        elif  tipoFiltro == 'PBPO': # First order - Low Pass 
        elif  tipoFiltro == 'PTPO': # First order - All Pass
        elif  tipoFiltro == 'PASO': # Second order - High Pass
        elif  tipoFiltro == 'PBSO': # Second order - Low Pass
        elif  tipoFiltro == 'PTSO': # Second order - All Pass
        elif  tipoFiltro == 'PBSO': # Second order - Band Pass
        elif  tipoFiltro == 'NSO' : # Second order - Notch
        return

    def plot(self):
        plt.semilogx(self.w, self.Hdb)
        plt.grid()
        plt.tight_layout()
        #plt.xlim(0,1000)
        plt.show()
        return


highPass = filter()

print(highPass.Hs)

highPass.num((0,1,0))
highPass.den((0,1/1000,1))
highPass.plot()