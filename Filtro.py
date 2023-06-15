import numpy as np
from scipy import signal
import re

class filtro:

    def __init__(self):
        self.filterOrder = 1
        self.filterType = 0
        self.gain = 1
        self.gainType = 2
        self.fo = 1
        self.fp = 1
        self.xio = 0
        self.xip = 0

        self.numSuperior = ''
        self.denSuperior = ''

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
            #self.numSuperior == ''
            #self.denSuperior == ''
        elif self.filterOrder == 2:
            self.set_SO()
            #self.numSuperior == ''
            #self.denSuperior == ''
        else:
            self.set_sup()
        self.updateTF()
        self.realZeros = np.real(self.zeros)
        self.imagZeros = np.imag(self.zeros)
        self.realPoles = np.real(self.poles)
        self.imagPoles = np.imag(self.poles)

        return True             #TODO: devolver flag si hay error
    
    def updateTF(self):
        self.sys = signal.TransferFunction(self.Hs[0],self.Hs[1])
        self.w, self.Hdb, self.phi = signal.bode(self.sys)
        self.zeros, self.poles, _ = signal.tf2zpk(self.Hs[0], self.Hs[1])
    
    def set_PO (self):
        f = self.fp
        if f != 0:
            if self.filterType == 0 : # First order - High Pass
                self.num((0,1,0))
                self.den((0, 1/f, 1))
            elif self.filterType == 1 : # First order - Low Pass 
                self.num((0,0,1))
                self.den((0, 1/f, 1))
            elif self.filterType == 2: # First order - All Pass
                self.num((0, 1/f, -1))
                self.den((0, 1/f, 1))   
            elif self.filterType == 'CeroPO': # First order - Arbitrario - Zero
                self.num((0, 1, f))
                self.den((0, 0, 1))
            elif self.filterType == 'PoloPO': # First order - Arbitrario - Pole
                self.num((0, 0, 1))
                self.den((0, 1, f))
    
    def set_SO (self):
        xi = self.xip
        xiz = self.xio
        f = self.fp
        fz = self.fo
        if f!=0:
            if self.filterType == 0: # Second order - High Pass
                self.num((1, 0, 0))
                self.den((1/f**2, 2*xi/f, 1))
            elif self.filterType == 1: # Second order - Low Pass
                self.num((0, 0, 1))
                self.den((1/f**2, 2*xi/f, 1))
            elif self.filterType == 2: # Second order - All Pass
                self.num((1/f**2, -2*xi/f, 1))
                self.den((1/f**2, 2*xi/f, 1))
            elif self.filterType == 3: # Second order - Band Pass
                self.num((0, 1, 0))
                self.den((1/f**2, 2*xi/f, 1))
            elif self.filterType == 4 : # Second order - Notch
                self.num((1/f**2, 0, 1))
                self.den((1/f**2, 2*xi/f, 1))
            elif self.filterType == 5 : # Second order - Low Pass Notch
                self.num((1/f**2, 0, 1))
                self.den((1/f**2, 2*xi/f, 1))
            elif self.filterType == 6 and fz != 0: # Second order - High Pass Notch
                self.num((1/fz**2, 2*(xiz/fz), 1))
                self.den((1/f**2, 2*(xi/f), 1))
    
    def set_SO_arbitrario(self):
        return                          #TODO: Basicamente la funcion entera :)
    
    def set_sup(self):
        if self.numSuperior != '':
            self.num(self.poly_to_tuple(self.numSuperior))
        
        if self.denSuperior != '':
            self.den(self.poly_to_tuple(self.denSuperior))

    def poly_to_tuple(self, string):
        substring = string.replace('^', '**')
        degree = self.match(substring)
        coeffs = []

        if len(coeffs) != degree+1:
            power = degree
            for i in range(degree):
                power = self.match(substring)
                if power + i != degree:
                    coeffs.insert(i, 0)                
                else:
                    if substring[0] == '0':
                        coeffs.insert(i, 0)
                    else:
                        coeffs.insert(i, float(substring.split("*", 1)[0].strip()))
                    substring = substring.split("+", 1)[1].strip() if '+' in substring else ''        
        if substring:
            coeffs.append(float(substring))
        else:
            coeffs.append(0)
        return tuple(coeffs)


    def match(self, string):
        match = re.search(r'\*\*(\w+)', string) 
        if match:
            return int(match.group(1))
        else:
            match = re.search(r'(\d+(?:\.\d+)?)\s*\*\s*x', string)  
            if match:
                return 1
            else:
                return 0