# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'processFolder.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import file_io
import image
from threading import Thread
import concurrent.futures
import traceback, sys
from photoSelector_ui import Ui_PhotoSelector

class Ui_processFolder(QtWidgets.QMainWindow):
    def __init__(self, folderPath, ParentWindow = None):
        super().__init__()
        self.folderPath = folderPath
        self.ParentWindow = ParentWindow
        self.img = None
        self.setupUi()

    def setupUi(self):
        self.setObjectName("processFolder")
        self.resize(824, 608)
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
        self.setAutoFillBackground(False)
        self.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(120, 10, 611, 141))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(48)
        self.title.setFont(font)
        self.title.setTextFormat(QtCore.Qt.RichText)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.continueButton = QtWidgets.QPushButton(self.centralwidget)
        self.continueButton.setGeometry(QtCore.QRect(280, 430, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(24)
        self.continueButton.setFont(font)
        self.continueButton.setAutoFillBackground(False)
        self.continueButton.setObjectName("continueButton")
        self.continueButton.setEnabled(False)
        self.continueButton.clicked.connect(self.photoSelectionEvent)
        self.processingLabel = QtWidgets.QLabel(self.centralwidget)
        self.processingLabel.setGeometry(QtCore.QRect(280, 150, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(18)
        self.processingLabel.setFont(font)
        self.processingLabel.setObjectName("processingLabel")
        self.loadingLabel = QtWidgets.QLabel(self.centralwidget)
        self.loadingLabel.setGeometry(QtCore.QRect(100, 50, 600, 500))
        self.loadingLabel.setObjectName("loadingLabel")
        self.loadGif(self.loadingLabel, "loading3.gif")
        
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setEnabled(True)
        self.backButton.setGeometry(QtCore.QRect(20, 20, 40, 40))
        self.backButton.setObjectName("backButton")
        self.backButton.setStyleSheet("background-image : url(back.png);") 
        self.backButton.clicked.connect(self.back)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

        # self.thread = Thread(target = file_io.processFolder, args = [self.folderPath, self.processingLabel])
        # self.thread.start()
        self.threadpool = QtCore.QThreadPool()
        worker = Worker(self.folderPath, self.processingLabel, self)
        worker.signals.result.connect(self.processingComplete)
        self.threadpool.start(worker)

        #thread.join()
        print(f'Done wit it')
        # image.processFolder(self.folderPath, self.processingLabel)

    def processingComplete(self, s):
        if s != {}:
            self.continueButton.setEnabled(True)    
            self.sim_list = s
            print(s)
    
    def photoSelectionEvent(self):
        self.hide()
        self.photoSelectorWin = Ui_PhotoSelector(self.sim_list, self)
        pass
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("processFolder", "Similar Image Filter"))
        self.title.setText(_translate("processFolder", "Similar Image Filter"))
        self.continueButton.setText(_translate("processFolder", "Continue"))
        self.processingLabel.setText(_translate("processFolder", "Processing : "))

    def back(self):
        if self.ParentWindow is not None:
            self.hide()
            self.ParentWindow.show()

    def loadGif(self, label, path):
        if self.img is not None:
            self.img.stop()
        self.img = QtGui.QMovie(path) #.scaledToWidth(label.frameGeometry().width())
        # if img.isNull():
        #     QtWidgets.QMessageBox.information(label, "Image Load Error",
        #         f"Could not load image at path {path}")
        #     return
        label.setMovie(self.img)
        print(self.img)
        self.img.setScaledSize(QtCore.QSize(label.frameGeometry().width(), label.frameGeometry().width()/(900/600)))
        self.img.start()

        print(self.img.currentFrameNumber())
        pass


class WorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(object)

class Worker(QtCore.QRunnable):
    
    def __init__(self, folderPath, label, ui):
        super(Worker, self).__init__()
        self.folderPath = folderPath
        self.label = label
        self.signals = WorkerSignals()
        self.ui = ui

    @QtCore.pyqtSlot()
    def run(self):
        try:
            print('a')
            size, img_list = file_io.processFolder(self.folderPath, self.label)
            print('b')
            self.label.setText("Comparing images ...")
            status = ""
            sim_list = {}
            if img_list == []:
                status = "No images found in the selected folder..."
            else:
                del_size, sim_list = image.processImages(img_list)
                if sim_list == {}:
                    status = "No similar images found in the selected folder..."

                else:
                    sim = 0
                    for k in sim_list.keys():
                        for img in sim_list[k]:
                            sim+=1
                    status = f"Out of {len(img_list)} images, {sim} are similar. Deleting all will save {round(del_size, 2)} MBs."

            
            
            
            x1, y1, w1, h1 = self.label.frameGeometry().getRect()
            self.label.setText(status)
            self.label.adjustSize()
            x2, y2, w2, h2 = self.label.frameGeometry().getRect()
            print(x1, y1, w1, h1)
            x2 = x1 - (w2 - w1)/2
            self.label.setGeometry(QtCore.QRect(x2, y2, w2, h2))
            self.ui.loadingLabel.setGeometry(300, 200, 200, 200)
            self.ui.loadGif(self.ui.loadingLabel, "done.jpg")
            result = sim_list

        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            print(exctype, value)
            pass
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


