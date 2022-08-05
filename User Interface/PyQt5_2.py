import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QInputDialog, QLineEdit, QLabel, QWidget
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('3omar.hs')
        # self.show()
        self.textbox = QLineEdit(self)
        self.textbox.move(10, 50)
        self.textbox.resize(280, 40)
        windowExample = QWidget()
        labelA = QLabel(windowExample)
        labelA.setText('Label Example')
        labelA.move(10, 40)

        windowExample = QWidget()
        self.label = QLabel(windowExample)
        self.label.setText("lllllllllllllllllllllllllllllllllllllllabel")
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()