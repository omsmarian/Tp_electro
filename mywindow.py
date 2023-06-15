from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Ploter
import ploter
from Filtro import filtro
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigatorTool

class mywindow(QMainWindow, Ui_Ploter):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('descarga.jpg'))
        self.datos = filtro()
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
        if combobox.currentIndex() == 3:
            self.fo1.setReadOnly(False)
            self.fp2.clear()
            self.psip.clear()
            self.fp2.setReadOnly(True)
            self.psip.setReadOnly(True)
            self.fo2.setReadOnly(False)
            self.psio.setReadOnly(False)
            self.changename(False)
        elif combobox.currentIndex() == 7:
            self.fp2.setReadOnly(False)
            self.psip.setReadOnly(False)
            self.fo2.setReadOnly(False)
            self.psio.setReadOnly(False)
            self.changename(False)
        elif combobox.currentIndex() == 5 or combobox.currentIndex() == 6:
            self.clearall2()
            self.fp2.setReadOnly(False)
            self.psip.setReadOnly(False)
            self.fo2.setReadOnly(False)
            self.psio.setReadOnly(False)
            self.changename(True)
        else:
            self.changename(False)
            self.fo1.clear()
            self.fo2.clear()
            self.psio.clear()
            self.psio.setReadOnly(True)
            self.fo1.setReadOnly(True)
            self.fo2.setReadOnly(True)
            self.fp2.setReadOnly(False)
            self.psip.setReadOnly(False)
        self.updateparams(self.getTabindex())

    #recibe flag y guarda todos los datos
    def updateparams(self, orden):
        #flags 0, primer orden, 1 segundo, 2 superior
        if orden == 0:
            self.datos.fo = self.getnum(self.fo1) * self.get_multiplier(self.unitfo1)
            self.datos.fp = self.getnum(self.fp1) * self.get_multiplier(self.unitfp1)    
            self.datos.gain = self.getnum(self.ganancia1)          
            self.datos.gainType = self.getganancia(orden)
            self.datos.filterType = self.getindex(self.filtro1)
        elif orden == 1:
            self.datos.fo = self.getnum(self.fo2) * self.get_multiplier(self.unitfo2)
            self.datos.fp = self.getnum(self.fp2) * self.get_multiplier(self.unitfp2)     
            self.datos.xio = self.getnum(self.psio)
            self.datos.xip = self.getnum(self.psip)
            self.datos.gain = self.getnum(self.ganancia2)          
            self.datos.gainType = self.getganancia(orden)
            self.datos.filterType = self.getindex(self.filtro2)
        else: 
            self.datos.numSuperior = self.numerador.text()
            self.datos.denSuperior = self.denominador.text()
            
        self.datos.filterOrder = self.getTabindex() + 1
        if self.datos.update():
            self.updateplots()
        else:
            print("ERROR")
    
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
        self.TabWidget.currentChanged.connect(lambda: self.TabUpdate(self.getTabindex()))
        #primer orden
        self.filtro1.activated.connect(lambda: self.lineeditcheck(self.filtro1))
        self.fo1.editingFinished.connect(lambda: self.updateparams(self.getTabindex()))
        self.fp1.editingFinished.connect(lambda: self.updateparams(self.getTabindex()))
        self.ganancia1.editingFinished.connect(lambda: self.updateparams(self.getTabindex()))
        self.bandapa1.toggled.connect(lambda: self.updateparams(self.getTabindex()))
        self.max1.toggled.connect(lambda: self.updateparams(self.getTabindex()))
        self.unitfo1.activated.connect(lambda: self.updateparams(self.getTabindex()))
        self.unitfp1.activated.connect(lambda: self.updateparams(self.getTabindex()))
        #segundo orden
        self.filtro2.activated.connect(lambda: self.lineeditcheck(self.filtro2))
        self.fo2.editingFinished.connect(lambda: self.updateparams(self.getTabindex()))
        self.fp2.editingFinished.connect(lambda: self.updateparams(self.getTabindex()))
        self.psio.editingFinished.connect(lambda: self.updateparams(self.getTabindex()))
        self.psip.editingFinished.connect(lambda: self.updateparams(self.getTabindex()))
        self.ganancia2.editingFinished.connect(lambda: self.updateparams(self.getTabindex()))
        self.bandapa2.toggled.connect(lambda: self.updateparams(self.getTabindex()))
        self.max2.toggled.connect(lambda: self.updateparams(self.getTabindex()))
        self.unitfo2.activated.connect(lambda: self.updateparams(self.getTabindex()))
        self.unitfp2.activated.connect(lambda: self.updateparams(self.getTabindex()))
        #orden sup
        self.numerador.editingFinished.connect(lambda: self.updateparams(self.getTabindex()))
        self.denominador.editingFinished.connect(lambda: self.updateparams(self.getTabindex()))
    
    #limpia todas las cajas de texto de segundo orden
    def clearall2(self):
        self.fo2.clear()
        self.fp2.clear()
        self.psio.clear()
        self.psip.clear()
        self.ganancia2.clear()
        
    #limpia todas las cajas de texto de segundo orden
    def clearall1(self):
        self.fo1.clear()
        self.fp1.clear()
        self.ganancia1.clear()
    
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
        self.horizontalLayout_18 = QtWidgets.QVBoxLayout(self.bodemod)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_19 = QtWidgets.QVBoxLayout(self.bodefase)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_20 = QtWidgets.QVBoxLayout(self.entrada)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.horizontalLayout_21 = QtWidgets.QVBoxLayout(self.cerospolos)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        
        #creo los plots y los canvas
        self.bodemodplt = ploter.PlotBodeMod()
        self.bodefaseplt = ploter.PlotBodeFase()
        self.entradaplt = ploter.PlotEntrada()
        self.cerospolosplt = ploter.PlotCerosPolos()
        
        #agrego toolbars
        self.horizontalLayout_18.addWidget(NavigatorTool(self.bodemodplt, self))
        self.horizontalLayout_19.addWidget(NavigatorTool(self.bodefaseplt, self))
        self.horizontalLayout_20.addWidget(NavigatorTool(self.entradaplt, self))
        self.horizontalLayout_21.addWidget(NavigatorTool(self.cerospolosplt, self))
        
        #agrego canvas a horizontal layouts
        self.horizontalLayout_18.addWidget(self.bodemodplt)
        self.horizontalLayout_19.addWidget(self.bodefaseplt)
        self.horizontalLayout_20.addWidget(self.entradaplt)
        self.horizontalLayout_21.addWidget(self.cerospolosplt)

    #actualiza los plots
    def updateplots(self):
        self.bodemodplt.plot(self.datos.w, self.datos.Hdb)
        self.bodefaseplt.plot(self.datos.w, self.datos.phi)
        self.cerospolosplt.plot(self.datos.realZeros, self.datos.imagZeros,
                                self.datos.realPoles, self.datos.imagPoles)
    
    #devuelve el tab en el cual estas
    def getTabindex(self):
        return self.TabWidget.currentIndex()

    #chequea los LineEdits para cambiar de tab 
    def TabUpdate(self, index):
        if index == 0:
            self.lineeditcheck(self.filtro1)
            self.clearall2()
        elif index == 1:
            self.lineeditcheck(self.filtro2)
            self.clearall1()
        self.datos.setUp()
        self.clearplots()


    def clearplots(self):
        self.bodemodplt.setUp()
        self.bodefaseplt.setUp()
        self.cerospolosplt.setUp()
        self.entradaplt.setUp()