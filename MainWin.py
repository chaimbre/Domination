from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QMainWindow, QPushButton, QHBoxLayout
from CountryDrawer import CountryDrawerWidget
from Country import CountryProvider

class DominMainWin(QMainWindow):
    def __init__(self):
        super(DominMainWin, self).__init__()

        self.cp = CountryProvider()
           
        drawer = CountryDrawerWidget( self )
        drawer.show()
        drawer.setPolygons( self.cp.getPolygon( "France" ) )#"RANDOM" ) )
        drawer.fitToScreen( 400.0, 400.0 )

        quitbut = QPushButton("Exit",self)
        quitbut.resize(100,30)
        quitbut.move( 400, 470 )
        quitbut.show()
        quitbut.clicked.connect( self.on_exit )

        cntry_name = self.cp.getSelName()
        self.setWindowTitle( cntry_name )

    def on_exit(self):
         print("Program exited")
         self.close()
        
      

        
