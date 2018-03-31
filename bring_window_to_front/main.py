import sys
from sys import stderr
from PyQt4.QtGui import QApplication, QWidget, QPushButton
from PyQt4.QtGui import QHBoxLayout, QVBoxLayout
from PyQt4.QtGui import QMainWindow, QDialog
from PyQt4.QtCore import Qt


def showWindow(window):
  window.show()
  new_state = (window.windowState() & ~Qt.WindowMinimized) | Qt.WindowActive
  window.setWindowState(new_state)
  window.activateWindow()


class Application(QApplication):
  def __init__(self,argv):
    QApplication.__init__(self,argv)

  def create(self):
    main_window = QMainWindow()
    self.main_window = main_window
    self.window1 = QDialog()
    self.window1.setWindowTitle('Window 1')
    self.window2 = QDialog()
    self.window2.setWindowTitle('Window 2')
    main_window.setWindowTitle('Bring To Front Test')
    central_widget = QWidget()
    layout = QVBoxLayout()
    window1_button = QPushButton('Window1')
    window2_button = QPushButton('Window2')
    layout.addWidget(window1_button)
    layout.addWidget(window2_button)
    window1_button.clicked.connect(self.openWindow1)
    window2_button.clicked.connect(self.openWindow2)
    central_widget.setLayout(layout)
    main_window.setCentralWidget(central_widget)
    main_window.show()

  def openWindow1(self):
    showWindow(self.window1)

  def openWindow2(self):
    showWindow(self.window2)

def main(argv):
  app = Application(argv)
  app.create()
  app.exec_()

main(sys.argv)
