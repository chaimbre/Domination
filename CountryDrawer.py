from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPen, QColor, QBrush, QPainter

import pyproj
import random

class CountryDrawerWidget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self._pen = QPen( QColor(255,0,0) )                  
        self._pen.setWidth(3)
        self._xmin = self._ymin =  1e10
        self._xmax = self._ymax = -1e10
        self._polygons = []
        
    def LLH_to_ECEF(self, lat, lon, alt):
        ecef, llh = pyproj.Proj(proj='geocent'), pyproj.Proj(proj='latlong')
        x, y, z = pyproj.transform(llh, ecef, lon, lat, alt, radians=False)
        return x, y, z
     
    def setPolygons( self, polys ):
        self._polygons = []
        polsizes =[]
        self._xmin = self._ymin =  1e10
        self._xmax = self._ymax = -1e10
        for pol in polys:
            polygon = QtGui.QPolygonF()
            for lon, lat in pol.exterior.coords:
                y, x, z = self.LLH_to_ECEF(lat, lon, 0)
                self._xmax = max( self._xmax, x )
                self._xmin = min( self._xmin, x )
                self._ymax = max( self._ymax, y )
                self._ymin = min( self._ymin, y )
                polygon.append ( QtCore.QPoint( x, y ) )
            self._polygons.append( polygon )
            polsizes.append( polygon.size() )
        print( "Size of polygons to draw ", *polsizes, sep='/' )    

    def paintEvent(self, event):
        if not self._polygons: return 
        painter = QPainter(self)
        painter.setWindow(QtCore.QRect(self._xmin,self._ymin,
                                       self._xmax-self._xmin,
                                       self._ymax-self._ymin))
        for pol in self._polygons:
            ri = random.randint( 0, 255 )
            painter.setBrush( QBrush( QColor( ri,ri,0,255) )  )    
            painter.drawPolygon(pol)
