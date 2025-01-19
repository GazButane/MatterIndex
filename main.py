import shutil
import sys
import os
import time
import json
from PyQt6 import QtWidgets, uic, QtCore, QtGui
from PyQt6.QtWidgets import QLineEdit, QDialog, QFileDialog, QApplication, QPushButton, QSplashScreen, QLabel, QDialogButtonBox, QColorDialog, \
    QVBoxLayout, QMessageBox
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt
from Window import Ui_MainWindow
from MatterWidget import Ui_MatterWidget
from launchframe import Ui_launchframe
import subprocess
from PIL import Image



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
        self.SearchBar.returnPressed.connect(self.doSearch)
        self.notifFrame.setVisible(False)
        self.refrechApp()
        self.actionRefresh_app.triggered.connect(self.manualRefreshApp)
        self.back2listButton.clicked.connect(self.back2list)
        self.back2listButton_2.clicked.connect(self.back2list)
        self.ManageTagsButton.clicked.connect(self.openManageTagsTab)
        self.openfolderbutton.clicked.connect(self.openThingsFolder)
        self.openFolderButton.clicked.connect(self.openOBJFolder)
        self.notifDelButton.clicked.connect(self.undisplayNotiframe)
        self.delOBJButton.clicked.connect(self.delOBJ)
        self.DestinationFolderButton.clicked.connect(self.setDestinationFolder)
        self.ExportButton.clicked.connect((self.exportObject))
        self.TMSaveButton.clicked.connect(lambda flag: self.updateTagManagement(True))
        self.TMTagBox.currentTextChanged.connect(self.fillTagManagementFields)
        self.TMColorSelectorButton.clicked.connect(self.PickColor)
        self.TMClearFieldsButton.clicked.connect(self.clearTagManagementFields)
        self.OBJ_AddTagToObjectButton.clicked.connect(self.addTagToObject)
        self.TMDeleteButton.clicked.connect(self.deleteTag)



    def checkTagFile(self):
        print("## Checking if tag.json file exist...")
        currentDatabase = open("variables/currentDatabase.txt", "r")
        sourceDirectory = currentDatabase.read()
        currentDatabase.close()
        filesList = os.listdir(sourceDirectory)
        if str("tags.json") in filesList:
            print("--> tags.json found, finished")
        else:
            print("--> tags.json not found, creating a new one...")
            shutil.copy("tagsJSON-template/tags.json", sourceDirectory)
            print("--> tags.json created, finished")
        print("")



    def setDestinationFolder(self):

        directory = QFileDialog.getExistingDirectory(self, "Select a Directory", "",
                                                     options=QFileDialog.Option.ShowDirsOnly)
        if directory:
            print(f"Selected directory: {directory}")
            self.displayNotif(f"Selected directory: {directory}", 1)

        else:
            self.displayNotif(f"No directory selected", 0)

        currentDestinationFolder = open("variables/currentDestinationFolder.txt", "w")
        currentDestinationFolder.write(directory)
        currentDestinationFolder.close()


    def exportObject(self):
        CurrentOBJ = open("variables/currentOBJ.txt")
        ObjPath = CurrentOBJ.read()
        CurrentOBJ.close()
        currentDestinationFolder = open("variables/currentDestinationFolder.txt")
        TargetPath = currentDestinationFolder.read()
        currentDestinationFolder.close()

        SourcePath = ObjPath

        destination_subfolder = os.path.join(TargetPath, ObjPath)

        if not os.path.exists(destination_subfolder):
            os.makedirs(destination_subfolder)

        for item in os.listdir(SourcePath):
            src = os.path.join(SourcePath, item)
            dest = os.path.join(destination_subfolder, item)
            if os.path.isdir(src):
                shutil.copytree(src, dest, dirs_exist_ok=True)
                print("All files exported with shutil.copytree")
            else:
                shutil.copy2(src, dest)
                print("All files exported with shutil.copy2")

            self.displayNotif(f"Files exported !", 1)

    def displayNotif(self, text, state):
        self.notifText.setText(text)
        if state == 1:
            self.notifIcon.setText("ⅰ")
            self.notifFrame.setStyleSheet("QFrame{\n"
                                          "    background-color: #246EDB;\n"
                                          "    padding: 2px 20px;\n"
                                          "    text-align: center;\n"
                                          "    text-decoration: none;\n"
                                          "    border-color: grey;\n"
                                          "    border-style:solid;\n"
                                          "    border-width: 0px;\n"
                                          "    border-radius: 15px;\n"
                                          "    font-family:\'Courier New\', Courier, monospace;\n"
                                          "    margin: 10px;\n"
                                          "}")
        else:
            self.notifIcon.setText("!")
            self.notifFrame.setStyleSheet("QFrame{\n"
                                          "    background-color: #CC0000;\n"
                                          "    padding: 2px 20px;\n"
                                          "    text-align: center;\n"
                                          "    text-decoration: none;\n"
                                          "    border-color: grey;\n"
                                          "    border-style:solid;\n"
                                          "    border-width: 0px;\n"
                                          "    border-radius: 15px;\n"
                                          "    font-family:\'Courier New\', Courier, monospace;\n"
                                          "    margin: 10px;\n"
                                          "}")

        self.notifFrame.setVisible(True)


    def undisplayNotiframe(self):
        self.notifFrame.setVisible(False)


    def back2list(self):
        self.tablist.setCurrentIndex(0)
        print("Button pressed: Back to list")

    def openManageTagsTab(self):
        self.tablist.setCurrentIndex(2)


    def displayTag(self, tagName):
        currentDatabase = open("variables/currentDatabase.txt", "r")
        sourceDirectory = currentDatabase.read()
        currentDatabase.close()
        try:
            with open(f"{sourceDirectory}/tags.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Tag file not found")
            return None

        for tag in data.get("tags", []):
            if tag['name'].lower() == tagName.lower():
                TagColor = tag.get('color', None)

                # add tag to TagManagementWidget
                self.TagEditButton = QtWidgets.QPushButton(parent=self.OBJWidgetContainer)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum,
                                                   QtWidgets.QSizePolicy.Policy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.TagEditButton.sizePolicy().hasHeightForWidth())
                self.TagEditButton.setSizePolicy(sizePolicy)
                self.TagEditButton.setMinimumSize(QtCore.QSize(0, 20))
                self.TagEditButton.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setFamily("Comfortaa")
                font.setPointSize(10)
                font.setBold(False)
                font.setUnderline(False)
                font.setStrikeOut(False)
                self.TagEditButton.setFont(font)
                self.TagEditButton.setText(tagName)
                self.TagEditButton.setStyleSheet(f":hover\u007b\n"
                                                 "background-color:black;\n"
                                                 "border-width: 1px;\n"
                                                 "border-color: #A40000;\n"
                                                 "\u007d\n"
                                                 "QPushButton\u007b\n"
                                                 f"background-color: {TagColor};\n"
                                                 "     padding: 0px 10px;\n"
                                                 "    text-align: center;\n"
                                                 "    text-decoration: none;\n"
                                                 "    border-color: grey;\n"
                                                 "    border-style:solid;\n"
                                                 "    border-width: 0px;\n"
                                                 "    border-radius: 5px;\n"
                                                 "    margin: 0px;\n"
                                                 "\u007d")
                self.TagEditButton.setObjectName(f"TagEditButton_{tagName}")
                self.TagEditButton.clicked.connect(lambda checked, tag = tagName: self.removeTag(tag))
                self.horizontalLayout_9.addWidget(self.TagEditButton)
                # self.horizontalLayout_7.addWidget(self.OBJWidgetContainer)

    def removeTag(self, tagName):
        CurrentOBJ = open("variables/currentOBJ.txt")
        ObjPath = CurrentOBJ.read()
        CurrentOBJ.close()
        print(tagName)

        currentDatabase = open("variables/currentDatabase.txt", "r")
        sourceDirectory = currentDatabase.read()
        currentDatabase.close()

        with open(f"{sourceDirectory}/tags.json", 'r') as file:
            data = json.load(file)

        for tag in data['tags']:
            if tag['name'] == tagName:
                if ObjPath in tag['Objects']:
                    tag['Objects'].remove(ObjPath)
                    print(f"Removed '{ObjPath}' from '{tagName}' tag.")
                else:
                    print(f"Object '{ObjPath}' not found in '{tagName}' tag.")
                break
        else:
            print(f"Tag '{tagName}' not found in the JSON file.")

        with open(f"{sourceDirectory}/tags.json", 'w') as file:
            json.dump(data, file, indent=4)

        self.openSelectedObject(ObjPath)


    def deleteTag(self):
        tagName = self.TMTagBox.currentText()

        currentDatabase = open("variables/currentDatabase.txt", "r")
        sourceDirectory = currentDatabase.read()
        currentDatabase.close()

        with open(f"{sourceDirectory}/tags.json", 'r') as file:
            data = json.load(file)

        tagFound = False
        for i, tag in enumerate(data['tags']):
            if tag['name'] == tagName:
                del data['tags'][i]
                tag_found = True
                print(f"Tag '{tagName}' has been removed.")
                break

        if not tagFound:
            print(f"Tag '{tagName}' not found in the JSON file.")

        with open(f"{sourceDirectory}/tags.json", 'w') as file:
            json.dump(data, file, indent=4)

        self.clearTagManagementFields()
        self.updateTagManagement(isManual=True)
        self.displayNotif(f"Tag <<{tagName}>> deleted", 1)


    def addTagToObject(self):
        s = self.OBJTagBox.currentText()
        CurrentOBJ = open("variables/currentOBJ.txt")
        ObjPath = CurrentOBJ.read()
        CurrentOBJ.close()

        currentDatabase = open("variables/currentDatabase.txt", "r")
        sourceDirectory = currentDatabase.read()
        currentDatabase.close()

        alreadyExist = self.OBJWidgetContainer.findChild(QPushButton, f"TagEditButton_{s}")
        print(f"Already exist ? -> {alreadyExist}")
        if alreadyExist:
            self.displayNotif("This tag is already assigned for this object", 0)
        else:
            self.displayTag(s)

            with open(f"{sourceDirectory}/tags.json", "r") as file:
                data = json.load(file)

            for tag in data["tags"]:
                if tag["name"] == s:
                    if ObjPath not in tag["Objects"]:
                        tag["Objects"].append(ObjPath)
                    else:
                        print(f"{ObjPath} already assigned to '{s}'.")
                    break
            else:
                print(f"ERR: Tag '{s}' not found")

            with open(f"{sourceDirectory}/tags.json", "w") as file:
                json.dump(data, file, indent=4)

            print("Tags.json Updated")


    def openThingsFolder(self):
        directory = QFileDialog.getExistingDirectory(self, "Select database", "",
                                                     options=QFileDialog.Option.ShowDirsOnly)
        if directory:
            print(f"Selected database: {directory}")
            self.displayNotif(f"Selected database", 1)
            currentDatabase = open("variables/currentDatabase.txt", "w")
            currentDatabase.write(directory)
            currentDatabase.close()
            self.refrechApp("")

        else:
            self.displayNotif(f"No database selected", 0)




    def delOBJ(self):
        CurrentOBJ = open("variables/currentOBJ.txt")
        ObjPath = CurrentOBJ.read()
        CurrentOBJ.close()

        shutil.rmtree(ObjPath)
        print(f'Folder {ObjPath} and its content removed')
        self.displayNotif("Deleted !", 1)
        self.back2list()
        self.refrechApp()


    def openOBJFolder(self):
        CurrentOBJ = open("variables/currentOBJ.txt")
        ObjPath = CurrentOBJ.read()
        CurrentOBJ.close()

        opener = "open" if sys.platform == "darwin" else "xdg-open"
        print("path for OPENOBJ:",ObjPath)
        subprocess.call([opener, ObjPath])


    def PickColor(self):
        color = QColorDialog.getColor()
        self.TMColorHexEditor.setText(str(color.name()))
        self.TMColorPreviewWidget.setStyleSheet(f"QWidget\u007b\n"
f"    background-color: {color.name()};\n"
"    padding: 2px 6px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-color: grey;\n"
"    border-style:solid;\n"
"    border-width: 0px;\n"
"    border-radius: 15px;\n"
"    font-family:\'Courier New\', Courier, monospace;\n"
"    margin: 10px;\n"
"\u007d")

    def updateTagManagement(self, isManual=None):
        print("## Importing tags into the UI from tag.json...")
        NewTagName = self.TMNameEditor.text()
        NewTagColor = self.TMColorHexEditor.text()

        currentDatabase = open("variables/currentDatabase.txt", "r")
        sourceDirectory = currentDatabase.read()
        currentDatabase.close()

        if NewTagName:
            try:
                with open(f"{sourceDirectory}/tags.json", 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = {"tags": []}

            for tag in data['tags']:
                if tag['name'].lower() == NewTagName.lower():
                    return

            new_tag = {
                "name": NewTagName,
                "color": NewTagColor,
                "IsDeletable": str("True"),
                "Objects": []
            }

            data['tags'].append(new_tag)

            with open(f"{sourceDirectory}/tags.json", 'w') as file:
                json.dump(data, file, indent=4)

        else:
            if isManual:
                self.displayNotif("Name field is empty",0)

        self.tagBox.clear()
        self.TMTagBox.clear()
        self.OBJTagBox.clear()

        with open(f"{sourceDirectory}/tags.json", "r") as tagListFile:
            tagData = json.load(tagListFile)

        tagList = tagData.get("tags", [])
        sortedTags = sorted(tagList, key=lambda tag: tag['name'].lower())

        print("--> Reading file...")
        for tag in sortedTags:
            name = tag['name']
            color = tag.get('color', '#2B2B2B')
            self.tagBox.addItem(name)
            self.TMTagBox.addItem(name)
            self.OBJTagBox.addItem(name)
            itemIndex = self.tagBox.count() - 1
            qColor = QColor(color)
            self.tagBox.setItemData(itemIndex, qColor, Qt.ItemDataRole.BackgroundRole)
            self.TMTagBox.setItemData(itemIndex, qColor, Qt.ItemDataRole.BackgroundRole)
            self.OBJTagBox.setItemData(itemIndex, qColor, Qt.ItemDataRole.BackgroundRole)
            print(f"-       Tag Name: {name}, Color: {color}")

        print("--> All tags are imported, finished")
        print("")

    def fillTagManagementFields(self, s):
        TagColor = "#45CE7F"

        currentDatabase = open("variables/currentDatabase.txt", "r")
        sourceDirectory = currentDatabase.read()
        currentDatabase.close()

        try:
            with open(f"{sourceDirectory}/tags.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Tag file not found")
            return None

        for tag in data.get("tags", []):
            if tag['name'].lower() == s.lower():
                TagColor = tag.get('color', None)


        print(f"Selected Tag: {s}")
        self.TMNameEditor.setText(s)
        self.TMColorHexEditor.setText(TagColor)
        self.TMColorPreviewWidget.setStyleSheet(f"QWidget\u007b\n"
f"    background-color: {TagColor};\n"
"    padding: 2px 6px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-color: grey;\n"
"    border-style:solid;\n"
"    border-width: 0px;\n"
"    border-radius: 15px;\n"
"    font-family:\'Courier New\', Courier, monospace;\n"
"    margin: 10px;\n"
"\u007d")
        print(f"background-color:{s};")

    def clearTagManagementFields(self):
        self.TMNameEditor.setText("")
        self.TMColorHexEditor.setText("")



    def refrechApp(self, filter = ""):
        print("--Start app refresh--")
        print("")
        self.checkTagFile()
        #Clear SearchBar
        self.SearchBar.setText("")
        #Clear list:
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

        currentDatabase = open("variables/currentDatabase.txt", "r")
        sourceDirectory = currentDatabase.read()
        currentDatabase.close()

        print("## Search for files...")
        for root, folders, files in os.walk(sourceDirectory):
            folders.sort(key=str.lower)
            if sourceDirectory == root:
                continue

            if not files:
                continue
            filterByName = [f for f in files if filter.lower() in f.lower()]
            if not filterByName:
                continue

            tagFilterObjects = []
            try:
                filterTag = self.tagBox.currentText()
                with open(f"{sourceDirectory}/tags.json", 'r') as file:
                    data = json.load(file)
                for i, tag in enumerate(data['tags']):
                    if tag['name'] == filterTag:
                        tagFilterObjects = tag['Objects']
            except:
                tagFilterObjects.append("allObjects")
                print("ERROR: Tags file not found")

            if not str(root) in tagFilterObjects and not str("allObjects") in tagFilterObjects:
                continue




            thingsQuantity += 1

            matterName = os.path.basename(root)
            matterNamesList.append(matterName)

            KeyWords = ["basecolor", "color", "diffuse", "albedo", "base_color", "diff"]

            ImageList = os.listdir(root)
            ImageList.sort()

            BaseColorImage = None

            for IMG in ImageList:
                if any(mot in IMG.lower() for mot in KeyWords):
                    BaseColorImage = os.path.join(root, IMG)
                    break

            if not BaseColorImage and ImageList:
                BaseColorImage = os.path.join(root, ImageList[0])

            imagePathList.append(BaseColorImage)
            contentList.append(len(ImageList))


        print(f"--> Search finished, {thingsQuantity} items found")
        print("")

        WidgetCycles = 0
        for matterName in matterNamesList:
            matterWidget = QtWidgets.QWidget()
            ui_matterWidget = Ui_MatterWidget()
            ui_matterWidget.setupUi(matterWidget)
            ui_matterWidget.matterName.setText(matterName)
            #let's create a thumbnail:
            thumbnail_filename = f'thumbnail/thumb_{matterName}.png'
            try:
                objThumbnail = Image.open(imagePathList[WidgetCycles])
            except:
                objThumbnail = Image.open("no_image.png")

            Size = (100, 100)
            objThumbnail.thumbnail(Size)
            objThumbnail.save(thumbnail_filename)
            #full image:
            #ui_matterWidget.matterFrame.setStyleSheet(f"QFrame #matterFrame\u007b background-image: url({imagePathList[WidgetCycles]});\u007d")
            #compressed:
            ui_matterWidget.matterFrame.setStyleSheet(f"QFrame #matterFrame\u007b background-image: url({thumbnail_filename});\u007d")

            ui_matterWidget.matterDescription.setText(f"Contains {contentList[WidgetCycles]} items")
            ui_matterWidget.openMatterButton.setText("Open")
            ui_matterWidget.openMatterButton.setObjectName(f"openMatterButton{WidgetCycles}")
            #ui_matterWidget.openMatterButton.clicked.connect(lambda checked, index=WidgetCycles+1: self.openObject(index))
            ui_matterWidget.openMatterButton.clicked.connect(lambda checked, OBJPath = str(f"{sourceDirectory}/{matterName}"): self.openSelectedObject(OBJPath))
            self.scrollAreaWidgetContents.layout().addWidget(matterWidget)
            WidgetCycles += 1

        getstartinfo = open("variables/startinfo.txt")
        startinfo = getstartinfo.read()
        getstartinfo.close()
        getstartinfo = open("variables/startinfo.txt", "w")
        getstartinfo.write(str(1))
        getstartinfo.close()
        # Update tag combobox
        try:
            self.updateTagManagement(False)
        except:
            print("Tag Manager Error")


        print("--Successful app refresh--")
        print("")



    def manualRefreshApp(self):
        self.refrechApp()
        self.displayNotif("Refreshed !", 1)


    def openSelectedObject(self, ObjPath):
        self.progressBar.setValue(0)
        setCurrentOBJ = open("variables/currentOBJ.txt", "w")
        setCurrentOBJ.write(ObjPath)
        setCurrentOBJ.close()
        #clear image container
        layout = self.OBJPicturesContainer.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()

        # clear Tag container
        layout = self.OBJWidgetContainer.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()

        #Open Object Tab
        self.tablist.setCurrentIndex(1)

        #Get Object infos and apply to text widgets
        SplittedPath = ObjPath.split("/")
        objectName = SplittedPath[-1]
        print(f"Selected Object Name ---------> {objectName}")
        self.OBJObjectName.setText(objectName)
        numberFiles = len(os.listdir(ObjPath))
        objectInfo = str(f"{numberFiles} images inside")
        print(f"Selected Object Info ---------> {objectInfo}")
        self.OBJObjectDesc.setText(objectInfo)

        #Get list of tags
        currentDatabase = open("variables/currentDatabase.txt", "r")
        sourceDirectory = currentDatabase.read()
        currentDatabase.close()

        with open(f"{sourceDirectory}/tags.json", "r") as file:
            data = json.load(file)
        listOfTags = [
            tag["name"]
            for tag in data["tags"]
            if ObjPath in tag["Objects"] or "allObjects" in tag["Objects"]
        ]

        for tag in listOfTags:
            self.displayTag(tag)

        #Get images path
        images = []
        for path in os.listdir(ObjPath):
            # check if current path is a file
            if os.path.isfile(os.path.join(ObjPath, path)):
                images.append(f"{ObjPath}/{path}")
        print(f"Images (path) --> {images}")

        self.progressBar.setValue(10)

        #Put images in OBJPicturesContainer
        tilesize = int(900 / len(images))
        progression = 10
        for image in images:
            self.OBJlabel_ = QtWidgets.QLabel(parent=self.OBJPicturesContainer)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.OBJlabel_.sizePolicy().hasHeightForWidth())
            self.OBJlabel_.setSizePolicy(sizePolicy)
            self.OBJlabel_.setMinimumSize(QtCore.QSize(tilesize, tilesize))
            self.OBJlabel_.setMaximumSize(QtCore.QSize(tilesize, tilesize))
            self.OBJlabel_.setText("")
            # self.OBJlabel_.setPixmap(QtGui.QPixmap(image))
            self.OBJlabel_.setStyleSheet(f"border-radius: 15px; background-image: url({image})")
            self.OBJlabel_.setScaledContents(True)
            self.OBJlabel_.setObjectName(f"OBJlabel_")
            self.horizontalLayout_2.addWidget(self.OBJlabel_)
            self.verticalLayout_6.addWidget(self.OBJPicturesContainer)
            progression += 80/len(images)
            self.progressBar.setValue(int(progression))

        self.progressBar.setValue(100)



    def doSearch(self):
        content = self.SearchBar.text()
        print("Search executed:", content)
        self.SearchBar.setText("")
        self.displayNotif("Search results:", 1)
        # clear list:
        layout = self.scrollAreaWidgetContents.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()
        self.refrechApp(str(content))



app = QtWidgets.QApplication(sys.argv)
splash = LaunchFrame()
splash.show()
#time.sleep(0.5)
window = MainWindow()
splash.finish(window)
window.show()
app.exec()

