from scipy import signal
import numpy as np
from Filtro import filtro

def mult_prefix(val):
    multiplier = 1
    prefix = ''
    if(val > 1e10):
        multiplier = 1e9
        prefix = 'G'
    elif(val > 1e9):
        multiplier = 1e6
        prefix = 'M'
    elif(val > 1e4):
        multiplier = 1e3
        prefix = 'k'
    elif(val > 1e1):
        multiplier = 1
        prefix = ''
    elif(val > 1e-2):
        multiplier = 1e-3
        prefix = 'm'
    elif(val > 1e-5):
        multiplier = 1e-6
        prefix = 'μ'
    else:
        multiplier = 1e-9
        prefix = 'n'
    return (multiplier, prefix)

class salida:
    def __init__(self):
        # PARAMETERS
        self.amp = 1
        self.f = 2*np.pi
        self.period = 1/self.f

        # INPUT_OUTPUT SIGNALS
        self.t = np.linspace(0, 2*self.period, 500)
        self.input = np.zeros(len(self.t))
        self.output = 0 * self.t
        self.tout = self.t
        self.signalType = 0
        self.prefix = ''

    def frecuency(self, f):
        if f != 0:
            self.f = f 

    def amplitude(self, amp):
        if amp != 0:
            self.amp = amp

    def update(self, filtro):
        self.period = 1/self.f
        if self.signalType == 0:
            self.t = np.linspace(0, 2*self.period, 500)
            self.sine()
        elif self.signalType == 1:
            period = 0
            singularities = np.append(np.abs(filtro.zeros), np.abs(filtro.poles))
            singularitiesNoZeros = singularities[singularities!=0]
            if(len(singularitiesNoZeros) == 0):
                period = 20*np.pi
                self.t = np.linspace(0, period, 500)
            else:
                period = 20*np.pi/min(singularitiesNoZeros)
                self.t = np.linspace(0, period, 500)
            self.pulse(period)
        elif self.signalType == 2:
            self.t = np.linspace(0, 2*self.period, 500)
            self.periodic_pulse()
        elif self.signalType == 3:
            self.t = np.linspace(0, 2*self.period, 500)
            self.periodic_triangular()
        (multiplier, prefix) = mult_prefix(self.t[int(len(self.t)/2)])
        self.tout, self.output, _ = signal.lsim(filtro.sys, U=self.input, T=self.t)
        self.t = self.t/multiplier
        self.tout = self.tout/multiplier
        self.prefix = prefix

    def sine(self):
        self.input = self.amp * np.sin(2*np.pi*self.f*self.t)
    
    def pulse(self, period):
        self.input = self.amp * (1 + signal.square(self.t-period/10, 0.5)) / 2

    def periodic_pulse(self):
        self.input = self.amp * signal.square(2*np.pi*self.f*self.t, 0.5)
    
    def periodic_triangular(self):
        self.input = self.amp * signal.sawtooth(2*np.pi*self.f*self.t, 0.5)