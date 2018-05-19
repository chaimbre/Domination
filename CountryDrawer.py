from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPen, QColor, QBrush, QPainter

import pyproj
import random

class CountryDrawerWidget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.pen = QPen( QColor(255,0,0) )                  
        self.pen.setWidth(3)
        self.brush = QBrush( QColor(255,255,0,255))
        self.xmin = self.ymin =  1e10
        self.xmax = self.ymax = -1e10

    def LLH_to_ECEF(self, lat, lon, alt):
        ecef, llh = pyproj.Proj(proj='geocent'), pyproj.Proj(proj='latlong')
        x, y, z = pyproj.transform(llh, ecef, lon, lat, alt, radians=False)
        return x, y, z
     
    def setPolygons( self, polys ):
        self.polygons = []
        polygon = QtGui.QPolygonF()
        polsizes =[]
        self.xmin = self.ymin =  1e10
        self.xmax = self.ymax = -1e10
        for pol in polys:
            for lon, lat in pol.exterior.coords:
                y, x, z = self.LLH_to_ECEF(lat, lon, 0)
                self.xmax = max( self.xmax, x )
                self.xmin = min( self.xmin, x )
                self.ymax = max( self.ymax, y )
                self.ymin = min( self.ymin, y )
                polygon.append ( QtCore.QPoint( x, y ) )
            self.polygons.append( polygon )
            polsizes.append( polygon.size() )
            polygon = QtGui.QPolygonF()
        print( "Size of polygons to draw ", *polsizes, sep='/' )    

    def paintEvent(self, event):
        if not self.polygons: return 
        painter = QPainter(self)
        painter.setWindow(QtCore.QRect(self.xmin, self.ymin, self.xmax-self.xmin, self.ymax-self.ymin))
        painter.setBrush( self.brush )
        for pol in self.polygons:
            ri = random.randint( 0, 255 )
            painter.setBrush( QBrush( QColor( ri,255,0,255) )  )    
            painter.drawPolygon(pol)

    def fitToScreen( self, xscreen_size, yscreen_size ):
        xwidth = self.xmax-self.xmin
        ywidth = self.ymax-self.ymin
        xfac = xscreen_size / xwidth
        yfac = yscreen_size / ywidth
        return self.resize( xwidth*xfac, ywidth*yfac )
