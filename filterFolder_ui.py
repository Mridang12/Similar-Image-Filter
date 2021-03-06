from PyQt5 import QtCore, QtGui, QtWidgets
from processFolder_ui import Ui_processFolder

class Ui_filterFolderWindow(QtWidgets.QMainWindow):
    def __init__(self, ParentWindow = None):
        super().__init__()
        self.ParentWindow = ParentWindow
        self.setupUi()

    def setupUi(self):
        self.setObjectName("filterFolderWindow")
        self.resize(800, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
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
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(100, 20, 611, 141))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(48)
        self.title.setFont(font)
        self.title.setTextFormat(QtCore.Qt.RichText)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.selectFolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectFolderButton.setEnabled(True)
        self.selectFolderButton.setGeometry(QtCore.QRect(280, 280, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(24)
        self.selectFolderButton.setFont(font)
        self.selectFolderButton.setAutoFillBackground(False)
        self.selectFolderButton.setObjectName("selectFolderButton")
        self.selectFolderButton.clicked.connect(self.selectFolderEvent)
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setEnabled(False)
        self.confirmButton.setGeometry(QtCore.QRect(280, 360, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(24)
        self.confirmButton.setFont(font)
        self.confirmButton.setAutoFillBackground(False)
        self.confirmButton.setObjectName("confirmButton")
        self.confirmButton.clicked.connect(self.confirmFolderEvent)
        self.folderPathLabel = QtWidgets.QLabel(self.centralwidget)
        self.folderPathLabel.setGeometry(QtCore.QRect(270, 180, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(18)
        self.folderPathLabel.setFont(font)
        self.folderPathLabel.setObjectName("folderPathLabel")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setEnabled(True)
        self.backButton.setGeometry(QtCore.QRect(20, 20, 40, 40))
        self.backButton.setObjectName("backButton")
        self.backButton.setStyleSheet("background-image : url(back.png);") 
        self.backButton.clicked.connect(self.backToMain)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("filterFolderWindow", "Filter Folder"))
        self.title.setText(_translate("filterFolderWindow", "Similar Image Filter"))
        self.selectFolderButton.setText(_translate("filterFolderWindow", "Select Folder"))
        self.confirmButton.setText(_translate("filterFolderWindow", "Confirm"))
        self.folderPathLabel.setText(_translate("filterFolderWindow", "Selected Folder : None"))

    def backToMain(self):
        if self.ParentWindow is not None:
            self.hide()
            self.ParentWindow.show()

    def selectFolderEvent(self):
        self.folderPath = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        print(f'path = {self.folderPath}')
        print(self.folderPath)
        if self.folderPath != "":
            x1, y1, w1, h1 = self.folderPathLabel.frameGeometry().getRect()
            self.folderPathLabel.setText(self.folderPath)
            self.folderPathLabel.adjustSize()
            x2, y2, w2, h2 = self.folderPathLabel.frameGeometry().getRect()
            print(x1, y1, w1, h1)
            x2 = x1 - (w2 - w1)/2
            self.folderPathLabel.setGeometry(QtCore.QRect(x2, y2, w2, h2))
            self.confirmButton.setEnabled(True)
        else:
            self.confirmButton.setEnabled(False)
            self.folderPathLabel.setText("Selected Folder : None")
            self.folderPathLabel.setGeometry(QtCore.QRect(270, 180, 251, 41))

    
    def confirmFolderEvent(self):
        self.hide()
        self.processFolderWin = Ui_processFolder(self.folderPath, self)
        pass