import numpy as np
from scipy import signal
import re

class filtro:

    def __init__(self):
        self.setUp()
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
        self.gain()
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
    
    def set_SO (self):
        xi = self.xip
        xiz = self.xio
        f = self.fp
        fz = self.fo
        
        if self.filterType == 0 and f!=0: # Second order - High Pass
            self.num((1, 0, 0))
            self.den((1/f**2, 2*xi/f, 1))
        elif self.filterType == 1 and f!=0: # Second order - Low Pass
            self.num((0, 0, 1))
            self.den((1/f**2, 2*xi/f, 1))
        elif self.filterType == 2 and f!=0: # Second order - All Pass
            self.num((1/f**2, -2*xi/f, 1))
            self.den((1/f**2, 2*xi/f, 1))
        elif self.filterType == 3 and fz != 0: # Second order - Band Pass
            self.num((0, 1, 0))
            self.den((1/fz**2, 2*xiz/fz, 1))
        elif self.filterType == 4 and f!=0: # Second order - Notch
            self.num((1/f**2, 0, 1))
            self.den((1/f**2, 2*xi/f, 1))
        elif self.filterType == 5 and f!=0: # Second order - Low Pass Notch
            self.num((1/f**2, 0, 1))
            self.den((1/f**2, 2*xi/f, 1))
        elif self.filterType == 6 and fz != 0 and f!=0: # Second order - High Pass Notch
            self.num((1/fz**2, 2*(xiz/fz), 1))
            self.den((1/f**2, 2*(xi/f), 1))
    
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
            match = re.search(r'(\d+(?:\.\d+)?)\s*\*\s*s', string)  
            if match:
                return 1
            else:
                return 0
            
    def setUp(self):
        self.filterOrder = 1
        self.filterType = 0
        self.gainBW = 0
        self.gainMax = 0
        self.gainType = 0
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

        # Zeros & Poles
        self.zeros = []
        self.poles = []
        self.realZeros = np.real(self.zeros)
        self.imagZeros = np.imag(self.zeros)
        self.realPoles = np.real(self.poles)
        self.imagPoles = np.imag(self.poles)
        
    def gain(self):
        if self.gainType == 1:
            k = 10 ** (self.gainBW/20)
            self.num(tuple(k * element for element in self.Hs[0]))
        elif self.gainType == 2:
            maxValue = max(self.Hdb)
            k = 10 ** ((self.gainMax-maxValue)/20)     
            self.num(tuple(k * element for element in self.Hs[0]))   