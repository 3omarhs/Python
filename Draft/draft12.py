import sys
import PyQt5
# from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

# pip install PyQt5


class Example(PyQt5.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):

        reply = PyQt5.QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", PyQt5.QMessageBox.Yes |
                                     PyQt5.QMessageBox.No, PyQt5.QMessageBox.No)

        if reply == PyQt5.QMessageBox.Yes:

            event.accept()
        else:

            event.ignore()


def main():
    app = PyQt5.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()