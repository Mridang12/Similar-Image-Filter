from PyQt5 import QtCore, QtGui, QtWidgets
import file_io

##remember to remove
imgpath = "2.jpg"

class Ui_PhotoSelector(QtWidgets.QMainWindow):
    def __init__(self, sim_list, ParentWindow = None):
        super().__init__()
        self.ParentWindow = ParentWindow
        self.sim_list = sim_list
        self.index = 0
        self.total = len(self.sim_list.keys())
        self.deletePreference = []
        for k in self.sim_list.keys():
            self.deletePreference.append([])
            for img in self.sim_list[k]:
                self.deletePreference[-1].append(True)
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
        self.netLabel.setText(f"{self.total} Similar Images")

        self.mainImage = QtWidgets.QLabel(self.centralwidget)
        self.mainImage.setGeometry(QtCore.QRect(20, 220,
            self.frameGeometry().width()*0.5,  570-220))
        print((self.sim_list[list(self.sim_list.keys())[self.index]]))
        self.loadImage(self.mainImage, list(self.sim_list.keys())[self.index].path)
        
        self.posLabel = QtWidgets.QLabel(self.centralwidget)
        self.posLabel.setGeometry(QtCore.QRect(160, 570, 250, 40))
        self.posLabel.setFont(font)
        self.posLabel.setTextFormat(QtCore.Qt.RichText)
        self.posLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.posLabel.setText(f"{self.index+1} / {self.total}")

        xAlign = 200
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QtCore.QRect(xAlign, 620, 70, 40))
        self.prevButton.setFont(font)
        self.prevButton.setText("Prev")
        self.prevButton.clicked.connect(self.showPrevImage)
        self.prevButton.setEnabled(False)

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
        self.show()

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
        self.reInitScrollArea()
        print('-----------')
        print(self.scrollWidget.layout())
        print(self.verticalBox)

    def reInitScrollArea(self):
        sim_imgs = self.sim_list[list(self.sim_list.keys())[self.index]]
        for i in range(len(sim_imgs)):
            wid = QtWidgets.QWidget()
            layout = QtWidgets.QVBoxLayout()
            layout.addStretch(1)
            wid.setLayout(layout)
            obj = QtWidgets.QLabel("imgLabel")
            obj.setGeometry(QtCore.QRect(0, 0,450, 450))
            self.loadImage(obj, sim_imgs[i].path)
            layout.addWidget(obj)

            checkBox = QtWidgets.QCheckBox()
            checkBox.setChecked(self.deletePreference[self.index][i])
            checkboxwidget = QtWidgets.QWidget()
            checkboxlayout = QtWidgets.QHBoxLayout()
            checkboxlayout.addStretch(1)
            checkboxwidget.setLayout(checkboxlayout)
            checkBoxLabel = QtWidgets.QLabel("textlabel")
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light SemiCondensed")
            font.setPointSize(12)
            checkBoxLabel.setFont(font)
            checkBoxLabel.setTextFormat(QtCore.Qt.RichText)
            checkBoxLabel.setAlignment(QtCore.Qt.AlignCenter)
            checkBoxLabel.setText("Delete")
            checkBoxLabel.setGeometry(QtCore.QRect(0, 0, 100, 40))
            checkboxlayout.addWidget(checkBox)
            checkboxlayout.addWidget(checkBoxLabel)
            #obj2.setText("adasdasd")



            layout.addWidget(checkboxwidget)
            #wid.setGeometry(QtCore.QRect(0, 0, 40, 40))
            self.verticalBox.addWidget(wid)

    def backToMain(self):
        if self.ParentWindow is not None:
            self.hide()
            self.ParentWindow.show()

    def showPrevImage(self):
        self.updateDecision()
        self.index -= 1
        self.posLabel.setText(f"{self.index+1} / {self.total}")
        self.loadImage(self.mainImage, list(self.sim_list.keys())[self.index].path)
        if self.index - 1 < 0:
            self.prevButton.setEnabled(False)
        for i in reversed(range(self.verticalBox.count())):
            if self.verticalBox.itemAt(i).widget() is not None:
                self.verticalBox.itemAt(i).widget().setParent(None)

        self.nextButton.setEnabled(True)
        self.reInitScrollArea()
        pass

    def showNextImage(self):
        self.updateDecision()
        self.index += 1
        self.posLabel.setText(f"{self.index+1} / {self.total}")
        self.loadImage(self.mainImage, list(self.sim_list.keys())[self.index].path)
        if self.index + 1 >= self.total:
            self.nextButton.setEnabled(False)
        k = list(self.sim_list.keys())[self.index - 1]
        j = len(self.sim_list[k]) - 1
        for i in reversed(range(self.verticalBox.count())):
            if self.verticalBox.itemAt(i).widget() is not None:
                self.verticalBox.itemAt(i).widget().setParent(None)
        self.prevButton.setEnabled(True)
        self.reInitScrollArea()
        pass
    
    def updateDecision(self):
        k = list(self.sim_list.keys())[self.index]
        j = len(self.sim_list[k]) - 1
        for i in reversed(range(self.verticalBox.count())):
            if self.verticalBox.itemAt(i).widget() is not None:
                self.deletePreference[self.index][j] = ((lambda x : True if x == 2 else False)(self.verticalBox.itemAt(i).widget().layout().itemAt(2).widget().layout().itemAt(1).widget().checkState()))
                j-=1

    def confirmEvent(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("The selected images will be deleted...")
        msg.setWindowTitle("Confirm Deletion")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        self.updateDecision()
        if msg.exec_() == 1024:
            print('pressed ok')
            self.proceedToDeletion()
        pass

    def proceedToDeletion(self):
        del_list = []
        i = 0
        for k in self.sim_list.keys():
            for j in range(len(self.sim_list[k])):
                if self.deletePreference[i][j]:
                    del_list.append(self.sim_list[k][j])
            i+=1
        file_io.deleteImageList(del_list)
        img = QtGui.QImage("done.jpg")
        msg = QtWidgets.QMessageBox()
        msg.setIconPixmap(QtGui.QPixmap.fromImage(img))
        msg.setWindowTitle("Success")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        window = self
        while window.ParentWindow is not None:
            window.ParentWindow.show()
            window.hide()
            window = window.ParentWindow

        pass

    def delAllEvent(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("All Similar Images will be deleted...")
        msg.setWindowTitle("Confirm Deletion")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        if msg.exec_() == 1024:
            print('pressed ok')
            for l in self.deletePreference:
                for i in range(len(l)):
                    l[i] = True
            self.proceedToDeletion()
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_PhotoSelector()
    ui.show()
    
    sys.exit(app.exec_())
