# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Graficador.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Ui_Ploter(object):
    def setupUi(self, Ploter):
        Ploter.setObjectName("Ploter")
        Ploter.resize(996, 854)
        Ploter.setMinimumSize(QtCore.QSize(996, 854))
        Ploter.setMaximumSize(QtCore.QSize(996, 854))
        self.centralwidget = QtWidgets.QWidget(Ploter)
        self.centralwidget.setObjectName("centralwidget")
        self.TabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.TabWidget.setGeometry(QtCore.QRect(0, 0, 391, 210))
        self.TabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.TabWidget.setObjectName("TabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.filtro1 = QtWidgets.QComboBox(self.tab)
        self.filtro1.setGeometry(QtCore.QRect(10, 50, 92, 22))
        self.filtro1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.filtro1.setEditable(False)
        self.filtro1.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.filtro1.setObjectName("filtro1")
        self.filtro1.addItem("")
        self.filtro1.addItem("")
        self.filtro1.addItem("")
        self.filtro1.addItem("")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(11, 11, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(195, 78, 179, 92))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ganancia1label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ganancia1label.setFont(font)
        self.ganancia1label.setObjectName("ganancia1label")
        self.horizontalLayout_3.addWidget(self.ganancia1label)
        self.ganancia1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.ganancia1.setObjectName("ganancia1")
        self.horizontalLayout_3.addWidget(self.ganancia1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.bandapa1 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bandapa1.setFont(font)
        self.bandapa1.setObjectName("bandapa1")
        self.verticalLayout.addWidget(self.bandapa1)
        self.max1 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.max1.setFont(font)
        self.max1.setObjectName("max1")
        self.verticalLayout.addWidget(self.max1)
        self.splitter_5 = QtWidgets.QSplitter(self.tab)
        self.splitter_5.setGeometry(QtCore.QRect(10, 140, 177, 21))
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setHandleWidth(8)
        self.splitter_5.setObjectName("splitter_5")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_5)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.fp1label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fp1label.setFont(font)
        self.fp1label.setObjectName("fp1label")
        self.horizontalLayout_17.addWidget(self.fp1label)
        self.fp1 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.fp1.setText("")
        self.fp1.setObjectName("fp1")
        self.horizontalLayout_17.addWidget(self.fp1)
        self.unitfp1 = QtWidgets.QComboBox(self.splitter_5)
        self.unitfp1.setObjectName("unitfp1")
        self.unitfp1.addItem("")
        self.unitfp1.addItem("")
        self.unitfp1.addItem("")
        self.unitfp1.addItem("")
        self.splitter_4 = QtWidgets.QSplitter(self.tab)
        self.splitter_4.setGeometry(QtCore.QRect(10, 100, 177, 21))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setHandleWidth(8)
        self.splitter_4.setObjectName("splitter_4")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fo1label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fo1label.setFont(font)
        self.fo1label.setObjectName("fo1label")
        self.horizontalLayout.addWidget(self.fo1label)
        self.fo1 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.fo1.setText("")
        self.fo1.setObjectName("fo1")
        self.horizontalLayout.addWidget(self.fo1)
        self.fo1.setReadOnly(True)
        self.unitfo1 = QtWidgets.QComboBox(self.splitter_4)
        self.unitfo1.setObjectName("unitfo1")
        self.unitfo1.addItem("")
        self.unitfo1.addItem("")
        self.unitfo1.addItem("")
        self.unitfo1.addItem("")
        self.TabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget_8 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_8.setGeometry(QtCore.QRect(195, 78, 179, 92))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.ganancia2label = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ganancia2label.setFont(font)
        self.ganancia2label.setObjectName("ganancia2label")
        self.horizontalLayout_12.addWidget(self.ganancia2label)
        self.ganancia2 = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.ganancia2.setObjectName("ganancia2")
        self.horizontalLayout_12.addWidget(self.ganancia2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.bandapa2 = QtWidgets.QRadioButton(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bandapa2.setFont(font)
        self.bandapa2.setObjectName("bandapa2")
        self.verticalLayout_3.addWidget(self.bandapa2)
        self.max2 = QtWidgets.QRadioButton(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.max2.setFont(font)
        self.max2.setObjectName("max2")
        self.verticalLayout_3.addWidget(self.max2)
        self.filtro2 = QtWidgets.QComboBox(self.tab_2)
        self.filtro2.setGeometry(QtCore.QRect(10, 50, 121, 22))
        self.filtro2.setEditable(False)
        self.filtro2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.filtro2.setObjectName("filtro2")
        self.filtro2.addItem("")
        self.filtro2.addItem("")
        self.filtro2.addItem("")
        self.filtro2.addItem("")
        self.filtro2.addItem("")
        self.filtro2.addItem("")
        self.filtro2.addItem("")
        self.filtro2.addItem("")
        self.layoutWidget_10 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_10.setGeometry(QtCore.QRect(195, 45, 141, 26))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(15)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.psiplabel = QtWidgets.QLabel(self.layoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.psiplabel.setFont(font)
        self.psiplabel.setObjectName("psiplabel")
        self.horizontalLayout_14.addWidget(self.psiplabel)
        self.psip = QtWidgets.QLineEdit(self.layoutWidget_10)
        self.psip.setText("")
        self.psip.setObjectName("psip")
        self.horizontalLayout_14.addWidget(self.psip)
        self.layoutWidget_9 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_9.setGeometry(QtCore.QRect(195, 11, 141, 31))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.psiolabel = QtWidgets.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.psiolabel.setFont(font)
        self.psiolabel.setObjectName("psiolabel")
        self.horizontalLayout_13.addWidget(self.psiolabel)
        self.psio = QtWidgets.QLineEdit(self.layoutWidget_9)
        self.psio.setText("")
        self.psio.setObjectName("psio")
        self.horizontalLayout_13.addWidget(self.psio)
        self.psio.setReadOnly(True)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(11, 11, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.splitter_6 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_6.setGeometry(QtCore.QRect(10, 100, 177, 21))
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setHandleWidth(8)
        self.splitter_6.setObjectName("splitter_6")
        self.layoutWidget_13 = QtWidgets.QWidget(self.splitter_6)
        self.layoutWidget_13.setObjectName("layoutWidget_13")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_13)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fo2label = QtWidgets.QLabel(self.layoutWidget_13)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fo2label.setFont(font)
        self.fo2label.setObjectName("fo2label")
        self.horizontalLayout_2.addWidget(self.fo2label)
        self.fo2 = QtWidgets.QLineEdit(self.layoutWidget_13)
        self.fo2.setText("")
        self.fo2.setObjectName("fo2")
        self.horizontalLayout_2.addWidget(self.fo2)
        self.fo2.setReadOnly(True)
        self.unitfo2 = QtWidgets.QComboBox(self.splitter_6)
        self.unitfo2.setObjectName("unitfo2")
        self.unitfo2.addItem("")
        self.unitfo2.addItem("")
        self.unitfo2.addItem("")
        self.unitfo2.addItem("")
        self.splitter_7 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_7.setGeometry(QtCore.QRect(10, 140, 177, 21))
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setHandleWidth(8)
        self.splitter_7.setObjectName("splitter_7")
        self.layoutWidget_6 = QtWidgets.QWidget(self.splitter_7)
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.fp2label = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fp2label.setFont(font)
        self.fp2label.setObjectName("fp2label")
        self.horizontalLayout_10.addWidget(self.fp2label)
        self.fp2 = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.fp2.setText("")
        self.fp2.setObjectName("fp2")
        self.horizontalLayout_10.addWidget(self.fp2)
        self.unitfp2 = QtWidgets.QComboBox(self.splitter_7)
        self.unitfp2.setObjectName("unitfp2")
        self.unitfp2.addItem("")
        self.unitfp2.addItem("")
        self.unitfp2.addItem("")
        self.unitfp2.addItem("")
        self.TabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.numlabel = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.numlabel.setFont(font)
        self.numlabel.setObjectName("numlabel")
        self.horizontalLayout_15.addWidget(self.numlabel)
        self.numerador = QtWidgets.QLineEdit(self.tab_3)
        self.numerador.setText("")
        self.numerador.setObjectName("numerador")
        self.horizontalLayout_15.addWidget(self.numerador)
        self.gridLayout_3.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.denlabel = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.denlabel.setFont(font)
        self.denlabel.setObjectName("denlabel")
        self.horizontalLayout_16.addWidget(self.denlabel)
        self.denominador = QtWidgets.QLineEdit(self.tab_3)
        self.denominador.setText("")
        self.denominador.setObjectName("denominador")
        self.horizontalLayout_16.addWidget(self.denominador)
        self.gridLayout_3.addLayout(self.horizontalLayout_16, 1, 0, 1, 1)
        self.TabWidget.addTab(self.tab_3, "")
        self.bodemod = QtWidgets.QFrame(self.centralwidget)
        self.bodemod.setGeometry(QtCore.QRect(400, 10, 591, 271))
        self.bodemod.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.bodemod.setFrameShape(QtWidgets.QFrame.Panel)
        self.bodemod.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bodemod.setLineWidth(3)
        self.bodemod.setObjectName("bodemod")
        self.bodefase = QtWidgets.QFrame(self.centralwidget)
        self.bodefase.setGeometry(QtCore.QRect(400, 290, 591, 261))
        self.bodefase.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.bodefase.setFrameShape(QtWidgets.QFrame.Panel)
        self.bodefase.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bodefase.setLineWidth(3)
        self.bodefase.setObjectName("bodefase")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 220, 301, 156))
        self.frame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(3)
        self.frame_3.setObjectName("frame_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(13, 13, 173, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName("label_6")
        self.entradabox = QtWidgets.QComboBox(self.frame_3)
        self.entradabox.setGeometry(QtCore.QRect(10, 50, 152, 22))
        self.entradabox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.entradabox.setEditable(False)
        self.entradabox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.entradabox.setObjectName("entradabox")
        self.entradabox.addItem("")
        self.entradabox.addItem("")
        self.entradabox.addItem("")
        self.entradabox.addItem("")
        self.splitter = QtWidgets.QSplitter(self.frame_3)
        self.splitter.setGeometry(QtCore.QRect(11, 80, 271, 26))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(13)
        self.splitter.setObjectName("splitter")
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frecentlabel = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frecentlabel.setFont(font)
        self.frecentlabel.setObjectName("frecentlabel")
        self.horizontalLayout_4.addWidget(self.frecentlabel)
        self.frecent = QtWidgets.QLineEdit(self.layoutWidget3)
        self.frecent.setText("")
        self.frecent.setObjectName("frecent")
        self.horizontalLayout_4.addWidget(self.frecent)
        self.unitfrecent = QtWidgets.QComboBox(self.splitter)
        self.unitfrecent.setObjectName("unitfrecent")
        self.unitfrecent.addItem("")
        self.unitfrecent.addItem("")
        self.unitfrecent.addItem("")
        self.unitfrecent.addItem("")
        self.splitter_2 = QtWidgets.QSplitter(self.frame_3)
        self.splitter_2.setGeometry(QtCore.QRect(13, 117, 271, 26))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(14)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ampentlabel = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ampentlabel.setFont(font)
        self.ampentlabel.setObjectName("ampentlabel")
        self.horizontalLayout_5.addWidget(self.ampentlabel)
        self.ampent = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.ampent.setText("")
        self.ampent.setObjectName("ampent")
        self.horizontalLayout_5.addWidget(self.ampent)
        self.unitampent = QtWidgets.QComboBox(self.splitter_2)
        self.unitampent.setObjectName("unitampent")
        self.unitampent.addItem("")
        self.unitampent.addItem("")
        self.unitampent.addItem("")
        self.cerospolos = QtWidgets.QFrame(self.centralwidget)
        self.cerospolos.setGeometry(QtCore.QRect(10, 390, 381, 461))
        self.cerospolos.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.cerospolos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cerospolos.setFrameShape(QtWidgets.QFrame.Panel)
        self.cerospolos.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cerospolos.setLineWidth(3)
        self.cerospolos.setObjectName("cerospolos")
        self.entrada = QtWidgets.QFrame(self.centralwidget)
        self.entrada.setGeometry(QtCore.QRect(400, 560, 591, 291))
        self.entrada.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.entrada.setFrameShape(QtWidgets.QFrame.Panel)
        self.entrada.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.entrada.setLineWidth(3)
        self.entrada.setObjectName("entrada")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        Ploter.setCentralWidget(self.centralwidget)
        #creo horizontalLayout
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.bodemod)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        #creo canvas
        self.bodemodplt = plt.figure()
        self.canvas1 = FigureCanvas(self.bodemodplt)
        #agrego canvas
        self.horizontalLayout_18.addWidget(self.canvas1)
        #creo horizontalLayout
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.bodefase)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        #creo canvas
        self.bodefaseplt = plt.figure()
        self.canvas2 = FigureCanvas(self.bodefaseplt)
        #agrego canvas
        self.horizontalLayout_19.addWidget(self.canvas2)
         #creo horizontalLayout
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.entrada)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        #creo canvas
        self.entradaplt = plt.figure()
        self.canvas3 = FigureCanvas(self.entradaplt)
        #agrego canvas
        self.horizontalLayout_20.addWidget(self.canvas3)
        #creo horizontalLayout
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.cerospolos)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        #creo canvas
        self.cerospolosplt = plt.figure()
        self.canvas4 = FigureCanvas(self.cerospolosplt)
        #agrego canvas
        self.horizontalLayout_21.addWidget(self.canvas4)

        self.retranslateUi(Ploter)
        self.TabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Ploter)

    def retranslateUi(self, Ploter):
        _translate = QtCore.QCoreApplication.translate
        Ploter.setWindowTitle(_translate("Ploter", "Plot Tool"))
        self.filtro1.setItemText(0, _translate("Ploter", "Pasa altos"))
        self.filtro1.setItemText(1, _translate("Ploter", "Pasa bajos"))
        self.filtro1.setItemText(2, _translate("Ploter", "Pasa todo"))
        self.filtro1.setItemText(3, _translate("Ploter", "Arbritario"))
        self.label_5.setText(_translate("Ploter", "Tipo de Filtro:"))
        self.ganancia1label.setText(_translate("Ploter", "Ganancia:"))
        self.bandapa1.setText(_translate("Ploter", "Banda Pasante"))
        self.max1.setText(_translate("Ploter", "Máxima"))
        self.fp1label.setText(_translate("Ploter", "fp:"))
        self.unitfp1.setItemText(0, _translate("Ploter", "Hz"))
        self.unitfp1.setItemText(1, _translate("Ploter", "KHz"))
        self.unitfp1.setItemText(2, _translate("Ploter", "MHz"))
        self.unitfp1.setItemText(3, _translate("Ploter", "GHz"))
        self.fo1label.setText(_translate("Ploter", "fo:"))
        self.unitfo1.setItemText(0, _translate("Ploter", "Hz"))
        self.unitfo1.setItemText(1, _translate("Ploter", "KHz"))
        self.unitfo1.setItemText(2, _translate("Ploter", "MHz"))
        self.unitfo1.setItemText(3, _translate("Ploter", "GHz"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab), _translate("Ploter", "Primer Orden"))
        self.ganancia2label.setText(_translate("Ploter", "Ganancia:"))
        self.bandapa2.setText(_translate("Ploter", "Banda Pasante"))
        self.max2.setText(_translate("Ploter", "Máxima"))
        self.filtro2.setItemText(0, _translate("Ploter", "Pasa altos"))
        self.filtro2.setItemText(1, _translate("Ploter", "Pasa bajos"))
        self.filtro2.setItemText(2, _translate("Ploter", "Pasa todo"))
        self.filtro2.setItemText(3, _translate("Ploter", "Pasa Banda"))
        self.filtro2.setItemText(4, _translate("Ploter", "Notch"))
        self.filtro2.setItemText(5, _translate("Ploter", "Low-pass notch"))
        self.filtro2.setItemText(6, _translate("Ploter", "High-pass notch"))
        self.filtro2.setItemText(7, _translate("Ploter", "Arbitrarios"))
        self.psiplabel.setText(_translate("Ploter", " ξp:"))
        self.psiolabel.setText(_translate("Ploter", " ξo:"))
        self.label.setText(_translate("Ploter", "Tipo de Filtro:"))
        self.fo2label.setText(_translate("Ploter", "fo:"))
        self.unitfo2.setItemText(0, _translate("Ploter", "Hz"))
        self.unitfo2.setItemText(1, _translate("Ploter", "KHz"))
        self.unitfo2.setItemText(2, _translate("Ploter", "MHz"))
        self.unitfo2.setItemText(3, _translate("Ploter", "GHz"))
        self.fp2label.setText(_translate("Ploter", "fp:"))
        self.unitfp2.setItemText(0, _translate("Ploter", "Hz"))
        self.unitfp2.setItemText(1, _translate("Ploter", "KHz"))
        self.unitfp2.setItemText(2, _translate("Ploter", "MHz"))
        self.unitfp2.setItemText(3, _translate("Ploter", "GHz"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_2), _translate("Ploter", "Segundo Orden"))
        self.numlabel.setText(_translate("Ploter", "Numerador:"))
        self.denlabel.setText(_translate("Ploter", "Denominador:"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_3), _translate("Ploter", "Orden Superior"))
        self.label_6.setText(_translate("Ploter", "Señal de Entrada"))
        self.entradabox.setItemText(0, _translate("Ploter", "Senoide"))
        self.entradabox.setItemText(1, _translate("Ploter", "Pulso Unitario"))
        self.entradabox.setItemText(2, _translate("Ploter", "Pulso Periódico"))
        self.entradabox.setItemText(3, _translate("Ploter", "Triangular Perdiódica"))
        self.frecentlabel.setText(_translate("Ploter", "Frecuencia:"))
        self.unitfrecent.setItemText(0, _translate("Ploter", "Hz"))
        self.unitfrecent.setItemText(1, _translate("Ploter", "KHz"))
        self.unitfrecent.setItemText(2, _translate("Ploter", "MHz"))
        self.unitfrecent.setItemText(3, _translate("Ploter", "GHz"))
        self.ampentlabel.setText(_translate("Ploter", "Amplitud:"))
        self.unitampent.setItemText(0, _translate("Ploter", "V"))
        self.unitampent.setItemText(1, _translate("Ploter", "KV"))
        self.unitampent.setItemText(2, _translate("Ploter", "MV"))

        self.filtro1.activated.connect(lambda: self.lineeditcheck(self.filtro1))
        self.filtro2.activated.connect(lambda: self.lineeditcheck(self.filtro2))
        #primer orden
        self.fo1.editingFinished.connect(lambda: self.getnum(self.fo1))  
        self.fp1.editingFinished.connect(lambda: self.getnum(self.fp1))  
        self.ganancia1.editingFinished.connect(lambda: self.getnum(self.ganancia1))
        self.bandapa1.toggled.connect(lambda: print(self.getindex(self.filtro1)))
        self.plot
        #segundo orden
        self.fo2.editingFinished.connect(lambda: self.getnum(self.fo2))
        self.fp2.editingFinished.connect(lambda: self.getnum(self.fp2))
        self.psio.editingFinished.connect(lambda: self.getnum(self.psio))
        self.psip.editingFinished.connect(lambda: self.getnum(self.psip))
        self.ganancia2.editingFinished.connect(lambda: self.getnum(self.ganancia2))
        #orden sup
        self.numerador.editingFinished.connect(lambda: self.getnum(self.numerador))
        self.denominador.editingFinished.connect(lambda: self.getnum(self.denominador))
        
    
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
        if combobox.currentIndex() == 3 or combobox.currentIndex() == 5 or combobox.currentIndex() == 6 or combobox.currentIndex() == 7:
            self.fo1.setReadOnly(False)
            self.fo2.setReadOnly(False)
            self.psio.setReadOnly(False)
            self.fp2.clear()
            self.fp2.setReadOnly(False)
            self.changename(True)
            if combobox.currentIndex() == 3:
                self.fp2.clear()
                self.fp2.setReadOnly(True)
                self.changename(False)
            elif combobox.currentIndex() == 7:
                self.changename(False)
        else:
            self.changename(False)
            self.psio.setReadOnly(True)
            self.psio.clear()
            self.fo1.setReadOnly(True)
            self.fo1.clear()
            self.fo2.setReadOnly(True)
            self.fo2.clear()
            self.fp2.setReadOnly(False)

    def plot (self):
        #fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))

        self.bodemodplt.clear()
        self.bodefaseplt.clear()
        self.cerospolosplt.clear()
        self.entradaplt.clear()

        # Module
        plt.semilogx(filter.w, filter.Hdb)
        plt.grid(True)
        self.canvas1.draw()
        
        # Phase
        plt.semilogx(filter.w, filter.phi)
        plt.grid(True)
        self.canvas2.draw()
        
        # Poles & zeros
        plt.scatter(np.real(filter.zeros), np.imag(filter.zeros), marker = 'o', color = 'blue', label = 'Ceros')
        plt.scatter(np.real(filter.poles), np.imag(filter.poles), marker = 'x', color = 'red', label = 'Polos')
        plt.set_xlabel('σ')
        plt.set_ylabel('jω')
        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)
        plt.grid(True)
        self.canvas4.draw()

        # Out        
        plt.plot(filter.t, filter.Vin, label='Entrada', color='red')
        plt.plot(filter.t, filter.Vout, label='Salida', color='blue')
        plt.grid(True)
        self.canvas3.draw()
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ploter = QtWidgets.QMainWindow()
    ui = Ui_Ploter()
    ui.setupUi(Ploter)
    Ploter.show()
    sys.exit(app.exec_())
