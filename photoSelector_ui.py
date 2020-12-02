from PyQt5 import QtCore, QtGui, QtWidgets
from filterFolder_ui import Ui_filterFolderWindow


##remember to remove
imgpath = "2.jpg"

class Ui_PhotoSelector(QtWidgets.QMainWindow):
    def __init__(self, ParentWindow = None):
        super().__init__()
        self.ParentWindow = ParentWindow
        self.setupUi()

    def setupUi(self):
        self.setObjectName("PhotoSelector")
        self.desktop = QtWidgets.QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.window_ratio = 824/608
        
        self.resize(810*self.window_ratio, 810)
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
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setEnabled(True)
        self.backButton.setGeometry(QtCore.QRect(20, 20, 40, 40))
        self.backButton.setObjectName("backButton")
        self.backButton.setStyleSheet("background-image : url(back.png);") 
        self.backButton.clicked.connect(self.backToMain)

        self.netLabel = QtWidgets.QLabel(self.centralwidget)
        self.netLabel.setGeometry(QtCore.QRect(150, 170, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(20)
        self.netLabel.setFont(font)
        self.netLabel.setTextFormat(QtCore.Qt.RichText)
        self.netLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.netLabel.setText("50 Similar Images")


        self.mainImage = QtWidgets.QLabel(self.centralwidget)
        self.mainImage.setGeometry(QtCore.QRect(20, 120,
            self.frameGeometry().width()*0.5, self.frameGeometry().width()*0.5))
        self.loadImage(self.mainImage, imgpath)
        
        self.posLabel = QtWidgets.QLabel(self.centralwidget)
        self.posLabel.setGeometry(QtCore.QRect(160, 570, 250, 40))
        self.posLabel.setFont(font)
        self.posLabel.setTextFormat(QtCore.Qt.RichText)
        self.posLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.posLabel.setText("1 / 50")

        xAlign = 200
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QtCore.QRect(xAlign, 620, 70, 40))
        self.prevButton.setFont(font)
        self.prevButton.setText("Prev")
        self.prevButton.clicked.connect(self.showPrevImage)

        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(xAlign + 100, 620, 70, 40))
        self.nextButton.setFont(font)
        self.nextButton.setText("Next")
        self.nextButton.clicked.connect(self.showNextImage)

        xAlign = 100
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(xAlign + 250, 700, 130, 45))
        self.confirmButton.setFont(font)
        self.confirmButton.setText("Confirm")
        self.confirmButton.clicked.connect(self.confirmEvent)

        self.delAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.delAllButton.setGeometry(QtCore.QRect(xAlign, 700, 130, 45))
        self.delAllButton.setFont(font)
        self.delAllButton.setText("Delete All")
        self.delAllButton.clicked.connect(self.delAllEvent)

        self.initScrollableArea()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("PhotoSelector", "Similar Image Filter"))
        self.title.setText(_translate("PhotoSelector", "Similar Image Filter"))
        print('in here')
        
    
    def filterFolder(self):
        self.filterFolderWin = Ui_filterFolderWindow(self)
        self.filterFolderWin.show()
        self.hide()

    def loadImage(self, label, path):
        img = QtGui.QImage(path).scaledToWidth(label.frameGeometry().width())
        if img.isNull():
            QtWidgets.QMessageBox.information(label, "Image Load Error",
                f"Could not load image at path {path}")
            return
        label.setPixmap(QtGui.QPixmap.fromImage(img))
        pass

    def initScrollableArea(self):
        self.scrollWidget = QtWidgets.QWidget()
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.verticalBox = QtWidgets.QVBoxLayout()
        

        self.scrollWidget.setLayout(self.verticalBox)
        
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)
        (x, y, w, h) = self.mainImage.frameGeometry().getRect()
        self.scrollArea.setGeometry(QtCore.QRect(x + w + 10, 10+141,
            self.frameGeometry().width() - (x + w + 20), self.frameGeometry().height()-(141+10+20)))
        for i in range(1, 5):
            wid = QtWidgets.QWidget()
            layout = QtWidgets.QVBoxLayout()
            wid.setLayout(layout)
            obj = QtWidgets.QLabel("textlabel")
            obj.setGeometry(QtCore.QRect(0, 0,450, 450))
            self.loadImage(obj, imgpath)
            layout.addWidget(obj)
            obj2 = QtWidgets.QLabel()
            obj2.setText("adasdasd")
            layout.addWidget(obj2)
            wid.setGeometry(QtCore.QRect(0, 0, 40, 40))
            self.verticalBox.addWidget(wid)

    def backToMain(self):
        if self.ParentWindow is not None:
            self.hide()
            self.ParentWindow.show()

    def showPrevImage(self):
        pass

    def showNextImage(self):
        pass

    def confirmEvent(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("The selected images will be deleted...")
        msg.setWindowTitle("Confirm Deletion")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        if msg.exec_() == 1024:
            print('pressed ok')
        pass

    def delAllEvent(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("All Similar Images will be deleted...")
        msg.setWindowTitle("Confirm Deletion")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        if msg.exec_() == 1024:
            print('pressed ok')
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_PhotoSelector()
    ui.show()
    
    sys.exit(app.exec_())
