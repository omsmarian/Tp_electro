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
        self. w = 2*np.pi
        self.period = 1/self.w
        self.phase = 0

        # INPUT_OUTPUT SIGNALS
        self.t = np.linspace(0, 2*self.period, 500)
        self.sine()
        self.output = 0 * self.t
        self.signalType = 0
        self.prefix = ''

    def frecuency(self, w, filtro):
        if w != 0:
            self.w = w # Tirar error si hay frecuencia 0
        self.update(filtro)

    def amplitude(self, amp, filtro):
        if amp != 0:
            self.amp = amp
        self.update(filtro)

    def update(self, filtro):
        self.period = 1/self.w
        self.t = np.linspace(0, 2*self.period, 500)
        if self.signalType == 0:
            self.sine()
        elif self.signalType == 1:
            self.pulse()
        elif self.signalType == 2:
            self.periodic_pulse()
        elif self.signalType == 3:
            print('triangular')
            self.periodic_triangular()
        (multiplier, prefix) = mult_prefix(self.t[int(len(self.t)/2)])
        self.t=self.t/multiplier
        self.prefix = prefix
        _, self.output, _ = signal.lsim((list(filtro.Hs[0]), 
                                         list(filtro.Hs[1])), self.input, self.t)
                        #TODO: Ver bien que es _, creo que ahi va de vuelta Vin

    def sine(self):
        self.input = self.amp * np.sin(self.w * self.t + self.phase)
    
    def pulse(self):
        self.input = self.amp * signal.square(self.t, duty=1)

    def periodic_pulse(self):
        return
    
    def periodic_triangular(self):
        self.input = self.amp * signal.sawtooth(self.t, 0.5)