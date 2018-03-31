""" test bringing a window to the front """
import sys
from PyQt4.QtGui import QApplication, QWidget, QPushButton
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QMainWindow, QDialog
from PyQt4.QtCore import Qt


def _show_window(window):
    window.show()
    new_state = (window.windowState() & ~Qt.WindowMinimized) | Qt.WindowActive
    window.setWindowState(new_state)
    window.activateWindow()


def _create_window(title):
    window = QDialog()
    window.setWindowTitle(title)
    return window


def _create_window_button(layout, text, callback):
    window_button = QPushButton(text)
    layout.addWidget(window_button)
    window_button.clicked.connect(callback)
    return window_button


def _create_central_widget(main_window):
    central_widget = QWidget()
    main_window.setCentralWidget(central_widget)
    return central_widget


def _create_vbox_layout(widget):
    layout = QVBoxLayout()
    widget.setLayout(layout)
    return layout


class _Application(QApplication): # pylint: disable=too-few-public-methods
    def __init__(self, argv):
        QApplication.__init__(self, argv)

        main_window = QMainWindow()
        self.main_window = main_window
        main_window.setWindowTitle('Bring To Front Test')
        central_widget = _create_central_widget(main_window)
        layout = _create_vbox_layout(central_widget)

        self._window1 = _create_window('Window 1')
        self._window2 = _create_window('Window 2')

        _create_window_button(layout, 'Window1', self._open_window_1)
        _create_window_button(layout, 'Window2', self._open_window_2)

        main_window.show()

    def _open_window_1(self):
        _show_window(self._window1)

    def _open_window_2(self):
        _show_window(self._window2)


def _main(argv):
    app = _Application(argv)
    app.exec_()


_main(sys.argv)
