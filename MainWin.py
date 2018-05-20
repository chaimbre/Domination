from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from CountryDrawer import CountryDrawerWidget
from Country import CountryProvider
import random

class DominMainWin(QMainWindow):
    def __init__(self):
        super(DominMainWin, self).__init__()

        self._cp = CountryProvider()
        self._selcountrybox = QComboBox( self )
           
        self._drawer = CountryDrawerWidget( self )
        self._drawer.resize( 400.0, 400.0 )
        self._drawer.show()
        
        self.addFields()
        self.onSelCountryChanged()
        
    def addFields(self):
        selcountrylbl = QLabel( "Select country", self )
        selcountrylbl.resize( 100, 30 )
        selcountrylbl.move( 20, 470 )
        
        self._selcountrybox.resize( 200, 30 )
        self._selcountrybox.move( 100, 470 )
        countrynames = self._cp.getAllNames()
        self._selcountrybox.addItems( countrynames )
        self._selcountrybox.setCurrentText( random.choice(countrynames) )
        self._selcountrybox.currentIndexChanged.connect(self.onSelCountryChanged)
        
        quitbut = QPushButton("Exit",self)
        quitbut.resize(100,30)
        quitbut.move( 380, 470 )
        quitbut.show()
        quitbut.clicked.connect( self.onExit )

    def onSelCountryChanged(self):
        name = self._selcountrybox.currentText()
        self.setWindowTitle( name )
        self._drawer.setPolygons( self._cp.getPolygon( name) )
        self._drawer.update()

    def onExit(self):
         print("Program exited")
         self.close()
        
      

        
