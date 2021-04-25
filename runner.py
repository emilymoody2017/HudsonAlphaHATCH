# -*- coding: utf-8 -*-

import sys
import mainWindow_class as mw
from PyQt5.QtWidgets import QApplication


################################################################################
# Test run the gui
app    = QApplication(sys.argv)
app.setStyle('Fusion')
window = mw.MainWindow()
window.show()
app.exec_() 

"""

To-Do
add heritable cancer
make scoring system

"""