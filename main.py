import shutil
import sys
import os
import time
from PyQt6 import QtWidgets, uic, QtCore, QtGui
from PyQt6.QtWidgets import QLineEdit, QDialog, QApplication, QPushButton, QSplashScreen
from Window import Ui_MainWindow
from MatterWidget import Ui_MatterWidget
from launchframe import Ui_launchframe
import subprocess



class LaunchFrame(QSplashScreen,Ui_launchframe):
    def __init__(self, *args, obj=None, **kwargs):
        super(LaunchFrame, self).__init__(*args, **kwargs)
        self.setupUi(self)


#///////////////////////////////////////////////////////////////////////////////////////
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.searchButton.clicked.connect(self.doSearch)
        self.refrechApp()
        self.actionRefresh_app.triggered.connect(self.refrechApp)
        self.back2listButton.clicked.connect(self.back2list)
        self.openfolderbutton.clicked.connect(self.openThingsFolder)
        self.openFolderButton.clicked.connect(self.openOBJFolder)
        self.SortAZ.toggled.connect(lambda checked, factor=0: self.sortlist(factor))
        self.SortZA.toggled.connect(lambda checked, factor=1: self.sortlist(factor))
        self.delOBJButton.clicked.connect(self.delOBJ)



    def back2list(self):
        self.tablist.setCurrentIndex(0)
        print("Button pressed: Back to list")

    def openThingsFolder(self):
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, "things"])

    def delOBJ(self):
        thingsQuantity = -1
        matterNamesList = []
        CurrentOBJ = open("variables/currentOBJ.txt")
        index = CurrentOBJ.read()
        CurrentOBJ.close()

        for root, _, files in os.walk("things"):
            thingsQuantity += 1
            ncutname = root
            cutname = ncutname.split("/")
            matterName = cutname[-1]
            matterNamesList.append(matterName)
        path = str(f"things/{matterNamesList[int(index)]}")
        shutil.rmtree(path)
        print(f'Folder {path} and its content removed')
    def openOBJFolder(self):
        thingsQuantity = -1
        matterNamesList = []
        CurrentOBJ = open("variables/currentOBJ.txt")
        index = CurrentOBJ.read()
        CurrentOBJ.close()

        for root, _, files in os.walk("things"):
            thingsQuantity += 1
            ncutname = root
            cutname = ncutname.split("/")
            matterName = cutname[-1]
            matterNamesList.append(matterName)


        path = str(f"things/{matterNamesList[int(index)]}")
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        print("path for OPENOBJ:",path)
        subprocess.call([opener, path])

    def refrechApp(self):
        print("--Start app refresh--")
        

        self.tagBox.clear()
        self.tagBox.addItem("All")
        tagListFile = open("tags/tags.txt")
        tagListRaw = tagListFile.read()
        tagListCool = tagListRaw.split(";")
        tagListCool.sort()
        for i in tagListCool:
            self.tagBox.addItem(i)
            print("New tag loaded ↓",i)

        self.SearchBar.setText("")
        #clear list:
        layout = self.scrollAreaWidgetContents.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()

        thingsQuantity = -1
        matterNamesList = []
        imagePathList = []
        contentList = []
        for root, _, files in os.walk("things"):
            thingsQuantity += 1
            ncutname = root
            cutname = ncutname.split("/")
            matterName = cutname[-1]
            matterNamesList.append(matterName)
            print("Material found → ", matterName)

            ImageList = os.listdir(root)
            ImageList.sort()
            path = str(f"things/{matterName}/{ImageList[1]}")
            imagePathList.append(path)
            contentList.append(len(ImageList))

        print(thingsQuantity,"materials have been found")
        print("List of path:",imagePathList)


        del matterNamesList [0]

        WidgetCycles = 1
        for matterName in matterNamesList:
            matterWidget = QtWidgets.QWidget()
            ui_matterWidget = Ui_MatterWidget()
            ui_matterWidget.setupUi(matterWidget)
            ui_matterWidget.matterName.setText(matterName)
            ui_matterWidget.matterFrame.setStyleSheet(f"QFrame #matterFrame\u007b background-image: url({imagePathList[WidgetCycles]});\u007d")
            ui_matterWidget.matterDescription.setText(f"Contains {contentList[WidgetCycles]} items")
            ui_matterWidget.openMatterButton.setText("Open →")
            ui_matterWidget.openMatterButton.setObjectName(f"openMatterButton{WidgetCycles}")
            ui_matterWidget.openMatterButton.clicked.connect(lambda checked, index=WidgetCycles: self.openObject(index))
            self.scrollAreaWidgetContents.layout().addWidget(matterWidget)
            WidgetCycles += 1
           # print(f"QFrame \u007b background-image: url({imagePathList[WidgetCycles]});\u007d")

        getstartinfo = open("variables/startinfo.txt")
        startinfo = getstartinfo.read()
        getstartinfo.close()
        print("startinfo=",str(startinfo))
        getstartinfo = open("variables/startinfo.txt", "w")
        getstartinfo.write(str(1))
        getstartinfo.close()
        print("--Successful app refresh--")

    def openObject(self, index):
        self.progressBar.setValue(0)
        #set the current obj for "openobj" fonction.
        setCurrentOBJ = open("variables/currentOBJ.txt", "w")
        setCurrentOBJ.write(str(index))
        setCurrentOBJ.close()

        thingsQuantity = -1
        matterNamesList = []
        imagePathList = []
        contentList = []
        for root, _, files in os.walk("things"):
            thingsQuantity += 1
            ncutname = root
            cutname = ncutname.split("/")
            matterName = cutname[-1]
            matterNamesList.append(matterName)

            ImageList = os.listdir(root)
            ImageList.sort()
            path = str(f"things/{matterName}/{ImageList[1]}")
            imagePathList.append(path)
            contentList.append(len(ImageList))
            #///////////////////

        self.progressBar.setValue(30)
        self.tablist.setCurrentIndex(1)
        print("Button pressed: openMatterButton", index)
        self.OBJObjectName.setText(matterNamesList[index])
        self.OBJObjectDesc.setText(f"Contains {contentList[index]} items")
        pathList = []
        imagePathList2 = []
        for root, _, files in os.walk("things"):
            pathList.append(root)
        imagesList = os.listdir(pathList[index])
##

        layout = self.OBJPicturesContainer.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()
##

        self.progressBar.setValue(60)
        tilesize = int(900 / len(imagesList))
        for image in imagesList:
            self.OBJlabel_ = QtWidgets.QLabel(parent=self.OBJPicturesContainer)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.OBJlabel_.sizePolicy().hasHeightForWidth())
            self.OBJlabel_.setSizePolicy(sizePolicy)
            self.OBJlabel_.setMinimumSize(QtCore.QSize(tilesize, tilesize))
            self.OBJlabel_.setMaximumSize(QtCore.QSize(tilesize, tilesize))
            self.OBJlabel_.setText("")
            url = str(f"{pathList[index]}/{image}")
            print(url)
            self.OBJlabel_.setPixmap(QtGui.QPixmap(url))
            self.OBJlabel_.setScaledContents(True)
            self.OBJlabel_.setObjectName(f"OBJlabel_")
            self.horizontalLayout_2.addWidget(self.OBJlabel_)
            self.verticalLayout_6.addWidget(self.OBJPicturesContainer)

        self.progressBar.setValue(100)

    def doSearch(self):
        content = self.SearchBar.text()
        print("Search executed:", content)
        self.SearchBar.setText("")
        # clear list:
        layout = self.scrollAreaWidgetContents.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()


    def sortlist(self, factor):
        self.progressBar.setValue(0)
        # clear list:
        layout = self.scrollAreaWidgetContents.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()

        self.progressBar.setValue(5)
        thingsQuantity = -1
        matterNamesList = []
        imagePathList = []
        contentList = []
        for root, _, files in os.walk("things"):
            thingsQuantity += 1
            ncutname = root
            cutname = ncutname.split("/")
            matterName = cutname[-1]
            matterNamesList.append(matterName)
            print("Material found → ", matterName)

            ImageList = os.listdir(root)
            ImageList.sort()
            path = str(f"things/{matterName}/{ImageList[1]}")
            imagePathList.append(path)
            contentList.append(len(ImageList))


        self.progressBar.setValue(50)
        del matterNamesList[0]
        if factor == 1:
            matterNamesList.reverse()
            imagePathList.reverse()


        WidgetCycles = 1
        for matterName in matterNamesList:
            matterWidget = QtWidgets.QWidget()
            ui_matterWidget = Ui_MatterWidget()
            ui_matterWidget.setupUi(matterWidget)
            ui_matterWidget.matterName.setText(matterName)
            ui_matterWidget.matterFrame.setStyleSheet(
                f"QFrame #matterFrame\u007b background-image: url({imagePathList[WidgetCycles]});\u007d")
            ui_matterWidget.matterDescription.setText(f"Contains {contentList[WidgetCycles]} items")
            ui_matterWidget.openMatterButton.setText(f"Open{WidgetCycles}")
            ui_matterWidget.openMatterButton.setObjectName(f"openMatterButton{WidgetCycles}")
            ui_matterWidget.openMatterButton.clicked.connect(lambda checked, index=WidgetCycles: self.openObject(index))
            self.scrollAreaWidgetContents.layout().addWidget(matterWidget)
            WidgetCycles += 1

        self.progressBar.setValue(100)





app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
splash = LaunchFrame()
splash.show()
window.show()
splash.finish(window)
app.exec()


