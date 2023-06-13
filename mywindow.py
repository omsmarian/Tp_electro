from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Ploter
import ploter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

class mywindow(QMainWindow, Ui_Ploter):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.initplots()
        self.update()
    
    #extrae el número ingresado
    def getnum(self, lineedit):
        try:
            return float((lineedit.text()).replace(',','.'))
        except:
            return 0
            
    #extrae indice
    def getindex(self, combobox):
        return combobox.currentIndex()
    
    #cambia el nombre
    def changename(self, flag):
        if flag:
            self.psiolabel.setText("ξz:")
            self.fo2label.setText("fz:")
        else:
            self.fo2label.setText("fo:")
            self.psiolabel.setText("ξo:")
    
    #deja escribir o no en base al index
    def lineeditcheck(self, combobox):
        ifcondition = (combobox.currentIndex() == 3 or combobox.currentIndex() == 5 or 
            combobox.currentIndex() == 6 or combobox.currentIndex() == 7)
        self.clearall()
        if ifcondition:
            self.fo1.setReadOnly(False)
            self.fo2.setReadOnly(False)
            self.psio.setReadOnly(False)
            self.fp2.setReadOnly(False)
            self.changename(True)
            if combobox.currentIndex() == 3:
                self.fp2.setReadOnly(True)
                self.psip.setReadOnly(True)
                self.changename(False)
            elif combobox.currentIndex() == 7:
                self.changename(False)
        else:
            self.changename(False)
            self.psio.setReadOnly(True)
            self.fo1.setReadOnly(True)
            self.fo2.setReadOnly(True)
            self.fp2.setReadOnly(False)
            self.psip.setReadOnly(False)

    #recibe flag y guarda todos los datos
    def updateparams(self, orden):
        #flags 1, primer orden, 2 segundo, 3 superior
        if orden == 1:
            fo = self.getnum(self.fo1) * self.get_multiplier(self.unitfo1)
            fp = self.getnum(self.fp1) * self.get_multiplier(self.unitfp1)      #Eze hace lo q quieras acá lo puse asi para tenerlo
            ganancia = self.getnum(self.ganancia1)          
            gananciatype = self.getganancia(orden)
            filtertype = self.getindex(self.filtro1)
        elif orden == 2:
            fo = self.getnum(self.fo2) * self.get_multiplier(self.unitfo2)
            fp = self.getnum(self.fp2) * self.get_multiplier(self.unitfp2)      #Eze acá tmb
            ganancia = self.getnum(self.ganancia2)          
            gananciatype = self.getganancia(orden)
            filtertype = self.getindex(self.filtro2)
        #else: #filtro de tercer orden
            #NO TOCAMOS ACÁ TODAVIA PQ ME VA A DAR ALGO
            #es un update no deberia returnear nada,
            # calculo q solo sube los datos a la clase filter
    
    #returns multiplier
    def get_multiplier(self, combobox):
        comboboxindex = combobox.currentIndex()
        if comboboxindex == 0:
            multiplier = 1
        elif comboboxindex == 1:
            multiplier = 1000
        elif comboboxindex == 2:
            multiplier = 1e6
        else:
            multiplier = 1e9
        return multiplier

    #returns ganancia type
    def getganancia(self, ordenflag):
        if ordenflag == 1:
            # 1 banda pasante, 2 maxima
            if self.bandapa1.isChecked():
                gananciatype = 1
            else:
                gananciatype = 2
        else:
            # 1 banda pasante, 2 maxima
            if self.bandapa2.isChecked():
                gananciatype = 1
            else:
                gananciatype = 2
        return gananciatype
    
    # Funcion *aesthetic* solo para no tener un bloque gigante
    # corre el update si tocas algo de la funcion transferencia
    def checkforparamupdates(self):
        #primer orden
        self.filtro1.activated.connect(lambda: self.lineeditcheck(self.filtro1))
        self.fo1.editingFinished.connect(lambda: self.updateparams(1))  
        self.fp1.editingFinished.connect(lambda: self.updateparams(1))  
        self.ganancia1.editingFinished.connect(lambda: self.updateparams(1))
        self.bandapa1.toggled.connect(lambda: self.updateparams(1))
        self.max1.toggled.connect(lambda: self.updateparams(1))
        self.unitfo1.activated.connect(lambda: self.updateparams(1))
        self.unitfp1.activated.connect(lambda: self.updateparams(1))
        #segundo orden
        self.filtro2.activated.connect(lambda: self.lineeditcheck(self.filtro2))
        self.fo2.editingFinished.connect(lambda: self.updateparams(2))
        self.fp2.editingFinished.connect(lambda: self.updateparams(2))
        self.psio.editingFinished.connect(lambda: self.updateparams(2))
        self.psip.editingFinished.connect(lambda: self.updateparams(2))
        self.ganancia2.editingFinished.connect(lambda: self.updateparams(2))
        self.bandapa2.toggled.connect(lambda: self.updateparams(2))
        self.max2.toggled.connect(lambda: self.updateparams(2))
        self.unitfo2.activated.connect(lambda: self.updateparams(2))
        self.unitfp2.activated.connect(lambda: self.updateparams(2))
        #orden sup
        self.numerador.editingFinished.connect(lambda: self.updateparams(3))
        self.denominador.editingFinished.connect(lambda: self.updateparams(3))
    
    #limpia todas las cajas de texto
    def clearall(self):
        self.fo1.clear()
        self.fp1.clear()
        self.fo2.clear()
        self.fp2.clear()
        self.psio.clear()
        self.psip.clear()
        self.ganancia1.clear()
        self.ganancia2.clear()
    
    #updatea los datos de entrada
    def updateinput(self):
        frec = self.getnum(self.frecent) * self.get_multiplier(self.unitfrecent)
        amp = self.getnum(self.ampent) * self.get_multiplier(self.unitampent)
        entradatype = self.getindex(self.entradabox)
        # acá lo subimos a filter tmb
    
    #chequea si se modifico algo de la entrada
    def checkforinputupdates(self):
        self.entradabox.activated.connect(lambda: self.updateinput())
        self.frecent.editingFinished.connect(lambda: self.updateinput())
        self.ampent.editingFinished.connect(lambda: self.updateinput())
    
    #update *aesthetic* para q se vea lindo
    def update(self):
        self.checkforinputupdates()
        self.checkforparamupdates()
        
    def initplots(self):
        #creo horizontal layouts
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.bodemod)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.bodefase)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.entrada)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.cerospolos)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        
        #creo los plots y los canvas
        #self.bodemodplt = plt.figure()
        #self.axes_module = self.bodemodplt.add_subplot()
        #self.bodefaseplt = plt.figure()
        #self.axes_fase = self.bodefaseplt.add_subplot()
        #self.entradaplt = plt.figure()
        #self.axes_entrada = self.entradaplt.add_subplot()
        #self.cerospolosplt = plt.figure()
        #self.axes_cerospolos = self.cerospolosplt.add_subplot()
        #self.canvas1 = FigureCanvas(self.bodemodplt)
        #self.canvas2 = FigureCanvas(self.bodefaseplt)
        #self.canvas3 = FigureCanvas(self.entradaplt)
        #self.canvas4 = FigureCanvas(self.cerospolosplt)
        self.bodemodplt = ploter.PlotBodeMod()
        self.bodefaseplt = ploter.PlotBodeFase()
        self.entradaplt = ploter.PlotEntrada()
        self.cerospolosplt = ploter.PlotCerosPolos()
        
        #agrego canvas a horizontal layouts
        self.horizontalLayout_18.addWidget(self.bodemodplt)
        self.horizontalLayout_19.addWidget(self.bodefaseplt)
        self.horizontalLayout_20.addWidget(self.entradaplt)
        self.horizontalLayout_21.addWidget(self.cerospolosplt)