from PyQt5 import QtCore, QtGui, QtWidgets
from filterFolder_ui import Ui_filterFolderWindow

class Ui_OpenWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ParentWindow = None
        self.setupUi()

    def setupUi(self):
        self.setObjectName("OpenWindow")
        self.resize(823, 607)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(200, 182, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.setPalette(palette)
        self.setAutoFillBackground(False)
        self.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        print(self.frameGeometry().width())
        self.title.setGeometry(QtCore.QRect(self.frameGeometry().width()/2 - 611/2, 10, 611, 141))

        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(48)
        self.title.setFont(font)
        self.title.setTextFormat(QtCore.Qt.RichText)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.title.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding 
        )
        self.filterFolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.filterFolderButton.setGeometry(QtCore.QRect(280, 210, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(24)
        self.filterFolderButton.setFont(font)
        self.filterFolderButton.setAutoFillBackground(False)
        self.filterFolderButton.setObjectName("filterFolderButton")
        self.filterFolderButton.clicked.connect(self.filterFolder)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("OpenWindow", "Similar Image Filter"))
        self.title.setText(_translate("OpenWindow", "Similar Image Filter"))
        self.filterFolderButton.setText(_translate("OpenWindow", "Filter A Folder"))
        print('in here')
    
    def filterFolder(self):
        self.filterFolderWin = Ui_filterFolderWindow(self)
        self.filterFolderWin.show()
        self.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_OpenWindow()
    ui.show()
    sys.exit(app.exec_())
