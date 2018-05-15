
import sys
from MainWin import DominMainWin 
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

win = DominMainWin()
win.resize(500,500)
win.show()

sys.exit(app.exec_())

