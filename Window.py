# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1248, 595)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(66, 66, 66))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 101, 150))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 66, 66))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 101, 150))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 66, 66))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logoMI.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(66, 66, 66))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 101, 150))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 66, 66))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 101, 150))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 66, 66))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cantarell Light")
        font.setPointSize(12)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.SearchBar = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.SearchBar.setStyleSheet("color: rgb(218, 218, 218);\n"
"    background-color: rgba(0, 0, 0, 0.37);\n"
"    padding: 6px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-color: grey;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-radius: 15px;\n"
"    font-family:\'Courier New\', Courier, monospace;\n"
"    margin: 10px;")
        self.SearchBar.setFrame(True)
        self.SearchBar.setObjectName("SearchBar")
        self.verticalLayout.addWidget(self.SearchBar)
        self.searchButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.searchButton.setEnabled(True)
        self.searchButton.setStyleSheet("QPushButton{\n"
"\n"
"color: rgb(218, 218, 218);\n"
"    background-color: rgba(0, 0, 0, 0.37);\n"
"    padding: 7px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-color: grey;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-radius: 15px;\n"
"    font-family:\'Courier New\', Courier, monospace;\n"
"    margin: 10px;\n"
"}\n"
"\n"
":hover{\n"
"background-color:black;\n"
"}")
        self.searchButton.setAutoDefault(False)
        self.searchButton.setDefault(False)
        self.searchButton.setFlat(False)
        self.searchButton.setObjectName("searchButton")
        self.verticalLayout.addWidget(self.searchButton)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cantarell Light")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.tagBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.tagBox.setStyleSheet("color: rgb(218, 218, 218);\n"
"    background-color: rgba(0, 0, 0, 0.37);\n"
"    padding: 6px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"   border-color: grey;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-radius: 15px;\n"
"    font-family:\'Courier New\', Courier, monospace;\n"
"    margin: 10px;")
        self.tagBox.setObjectName("tagBox")
        self.tagBox.addItem("")
        self.verticalLayout.addWidget(self.tagBox)
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cantarell Light")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.radioFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.radioFrame.setStyleSheet("QFrame #radioFrame{\n"
"    color: rgb(218, 218, 218);\n"
"    background-color: rgba(0, 0, 0, 0.37);\n"
"    padding: 6px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"   border-color: grey;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-radius: 15px;\n"
"    font-family:\'Courier New\', Courier, monospace;\n"
"    margin: 10px;\n"
"}")
        self.radioFrame.setObjectName("radioFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.radioFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.SortAZ = QtWidgets.QRadioButton(parent=self.radioFrame)
        self.SortAZ.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.SortAZ.setStyleSheet("")
        self.SortAZ.setChecked(True)
        self.SortAZ.setObjectName("SortAZ")
        self.verticalLayout_4.addWidget(self.SortAZ)
        self.SortZA = QtWidgets.QRadioButton(parent=self.radioFrame)
        self.SortZA.setObjectName("SortZA")
        self.verticalLayout_4.addWidget(self.SortZA)
        self.verticalLayout.addWidget(self.radioFrame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.notifFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.notifFrame.setStyleSheet("QFrame{\n"
"    background-color: #246EDB;\n"
"    padding: 2px 6px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-color: grey;\n"
"    border-style:solid;\n"
"    border-width: 0px;\n"
"    border-radius: 15px;\n"
"    font-family:\'Courier New\', Courier, monospace;\n"
"    margin: 10px;\n"
"}")
        self.notifFrame.setObjectName("notifFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.notifFrame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.notifIcon = QtWidgets.QLabel(parent=self.notifFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notifIcon.sizePolicy().hasHeightForWidth())
        self.notifIcon.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.notifIcon.setFont(font)
        self.notifIcon.setStyleSheet("  padding: 0px 0px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-width: 0px;\n"
"    font-family:\'Georgia\';\n"
"    margin: 0px;")
        self.notifIcon.setObjectName("notifIcon")
        self.horizontalLayout_5.addWidget(self.notifIcon)
        self.notifText = QtWidgets.QLabel(parent=self.notifFrame)
        self.notifText.setStyleSheet("\n"
"    padding: 0px 0px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-width: 0px;\n"
"    font-family:\'Courier New\', Courier, monospace;\n"
"    margin: 5px;")
        self.notifText.setObjectName("notifText")
        self.horizontalLayout_5.addWidget(self.notifText)
        self.notifDelButton = QtWidgets.QPushButton(parent=self.notifFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notifDelButton.sizePolicy().hasHeightForWidth())
        self.notifDelButton.setSizePolicy(sizePolicy)
        self.notifDelButton.setMaximumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.notifDelButton.setFont(font)
        self.notifDelButton.setStyleSheet("    background-color: #246EDB;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-color: grey;\n"
"    border-style:solid;\n"
"    border-width: 0px;\n"
"    border-radius: 15px;\n"
"")
        self.notifDelButton.setObjectName("notifDelButton")
        self.horizontalLayout_5.addWidget(self.notifDelButton)
        self.verticalLayout.addWidget(self.notifFrame)
        self.openfolderbutton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.openfolderbutton.setStyleSheet("QPushButton{\n"
"color: rgb(218, 218, 218);\n"
"    background-color: rgba(0, 0, 0, 0.37);\n"
"    padding: 7px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-color: grey;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-radius: 15px;\n"
"    font-family:\'Courier New\', Courier, monospace;\n"
"    margin: 10px;\n"
"}\n"
"\n"
":hover{\n"
"background-color:black;\n"
"}")
        self.openfolderbutton.setObjectName("openfolderbutton")
        self.verticalLayout.addWidget(self.openfolderbutton)
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setStyleSheet("color: rgb(218, 218, 218);\n"
"    background-color: rgba(0, 0, 0, 0.37);\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-family:\'Courier New\', Courier, monospace;\n"
"    margin: 10px;\n"
"height: 5px;")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tablist = QtWidgets.QTabWidget(parent=self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.tablist.setPalette(palette)
        self.tablist.setStyleSheet("    color: white;\n"
"    background-color: #242424;\n"
"border-radius: 15px;\n"
"\n"
"")
        self.tablist.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.tablist.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tablist.setElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.tablist.setObjectName("tablist")
        self.List = QtWidgets.QWidget()
        self.List.setStyleSheet("")
        self.List.setObjectName("List")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.List)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.List)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 976, 504))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        spacerItem2 = QtWidgets.QSpacerItem(3000, 5, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.tablist.addTab(self.List, "")
        self.Object = QtWidgets.QWidget()
        self.Object.setStyleSheet("")
        self.Object.setObjectName("Object")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Object)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.OBJObjectName = QtWidgets.QLabel(parent=self.Object)
        self.OBJObjectName.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(24)
        font.setBold(True)
        self.OBJObjectName.setFont(font)
        self.OBJObjectName.setObjectName("OBJObjectName")
        self.verticalLayout_5.addWidget(self.OBJObjectName)
        self.OBJObjectDesc = QtWidgets.QLabel(parent=self.Object)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OBJObjectDesc.sizePolicy().hasHeightForWidth())
        self.OBJObjectDesc.setSizePolicy(sizePolicy)
        self.OBJObjectDesc.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        font.setBold(False)
        self.OBJObjectDesc.setFont(font)
        self.OBJObjectDesc.setObjectName("OBJObjectDesc")
        self.verticalLayout_5.addWidget(self.OBJObjectDesc)
        self.horizontalWidget = QtWidgets.QWidget(parent=self.Object)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setMinimumSize(QtCore.QSize(0, 50))
        self.horizontalWidget.setStyleSheet("QPushButton{\n"
"color: rgb(218, 218, 218);\n"
"    background-color: rgba(0, 0, 0, 0.37);\n"
"    padding: 7px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-color: grey;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-radius: 15px;\n"
"    font-family:\'Courier New\', Courier, monospace;\n"
"    margin: 10px;\n"
"}")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.openFolderButton = QtWidgets.QPushButton(parent=self.horizontalWidget)
        self.openFolderButton.setStyleSheet(":hover{\n"
"background-color:black;\n"
"}")
        self.openFolderButton.setObjectName("openFolderButton")
        self.horizontalLayout_3.addWidget(self.openFolderButton)
        self.delOBJButton = QtWidgets.QPushButton(parent=self.horizontalWidget)
        self.delOBJButton.setStyleSheet(":hover{\n"
"background-color:black;\n"
"border-color:#A40000;\n"
"}")
        self.delOBJButton.setObjectName("delOBJButton")
        self.horizontalLayout_3.addWidget(self.delOBJButton)
        self.copyAllButton = QtWidgets.QPushButton(parent=self.horizontalWidget)
        self.copyAllButton.setStyleSheet(":hover{\n"
"background-color:black;\n"
"}")
        self.copyAllButton.setObjectName("copyAllButton")
        self.horizontalLayout_3.addWidget(self.copyAllButton)
        self.back2listButton = QtWidgets.QPushButton(parent=self.horizontalWidget)
        self.back2listButton.setStyleSheet(":hover{\n"
"background-color:black;\n"
"}")
        self.back2listButton.setObjectName("back2listButton")
        self.horizontalLayout_3.addWidget(self.back2listButton)
        self.verticalLayout_5.addWidget(self.horizontalWidget)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.label_8 = QtWidgets.QLabel(parent=self.Object)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_8.setStyleSheet("\n"
"color: rgb(218, 218, 218);\n"
"    background-color: rgba(0, 0, 0, 0.37);\n"
"    padding: 7px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-color: grey;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-radius: 15px;\n"
"    font-family:\'Courier New\', Courier, monospace;\n"
"    margin: 10px;\n"
"")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.OBJPicturesContainer = QtWidgets.QWidget(parent=self.Object)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OBJPicturesContainer.sizePolicy().hasHeightForWidth())
        self.OBJPicturesContainer.setSizePolicy(sizePolicy)
        self.OBJPicturesContainer.setMaximumSize(QtCore.QSize(16777215, 200))
        self.OBJPicturesContainer.setStyleSheet("#OBJPicturesContainer{\n"
"color: rgb(218, 218, 218);\n"
"    background-color: rgba(0, 0, 0, 0.37);\n"
"    padding: 20px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-color: grey;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-radius: 15px;\n"
"    font-family:\'Courier New\', Courier, monospace;\n"
"    margin: 10px;\n"
"}")
        self.OBJPicturesContainer.setObjectName("OBJPicturesContainer")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.OBJPicturesContainer)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.OBJlabel_1 = QtWidgets.QLabel(parent=self.OBJPicturesContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OBJlabel_1.sizePolicy().hasHeightForWidth())
        self.OBJlabel_1.setSizePolicy(sizePolicy)
        self.OBJlabel_1.setMinimumSize(QtCore.QSize(150, 150))
        self.OBJlabel_1.setMaximumSize(QtCore.QSize(150, 150))
        self.OBJlabel_1.setText("")
        self.OBJlabel_1.setPixmap(QtGui.QPixmap("no_image.svg"))
        self.OBJlabel_1.setScaledContents(True)
        self.OBJlabel_1.setObjectName("OBJlabel_1")
        self.horizontalLayout_2.addWidget(self.OBJlabel_1)
        self.verticalLayout_6.addWidget(self.OBJPicturesContainer)
        self.tablist.addTab(self.Object, "")
        self.horizontalLayout.addWidget(self.tablist)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1248, 20))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(parent=self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuedit = QtWidgets.QMenu(parent=self.menubar)
        self.menuedit.setObjectName("menuedit")
        self.menutool = QtWidgets.QMenu(parent=self.menubar)
        self.menutool.setObjectName("menutool")
        self.menuhelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionimport = QtGui.QAction(parent=MainWindow)
        self.actionimport.setObjectName("actionimport")
        self.actionopen_folder = QtGui.QAction(parent=MainWindow)
        self.actionopen_folder.setObjectName("actionopen_folder")
        self.actionsearch = QtGui.QAction(parent=MainWindow)
        self.actionsearch.setObjectName("actionsearch")
        self.actionwebsite = QtGui.QAction(parent=MainWindow)
        self.actionwebsite.setObjectName("actionwebsite")
        self.actionabout = QtGui.QAction(parent=MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionconfigure = QtGui.QAction(parent=MainWindow)
        self.actionconfigure.setObjectName("actionconfigure")
        self.actionexit = QtGui.QAction(parent=MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionRefresh_app = QtGui.QAction(parent=MainWindow)
        self.actionRefresh_app.setObjectName("actionRefresh_app")
        self.menufile.addAction(self.actionimport)
        self.menufile.addAction(self.actionopen_folder)
        self.menuedit.addAction(self.actionconfigure)
        self.menutool.addAction(self.actionsearch)
        self.menutool.addAction(self.actionRefresh_app)
        self.menuhelp.addAction(self.actionwebsite)
        self.menuhelp.addAction(self.actionabout)
        self.menuhelp.addAction(self.actionexit)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())
        self.menubar.addAction(self.menutool.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tablist.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MatterIndex"))
        self.label_2.setText(_translate("MainWindow", "Find by name:"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.label_3.setText(_translate("MainWindow", "Tags:"))
        self.tagBox.setItemText(0, _translate("MainWindow", "All"))
        self.label_13.setText(_translate("MainWindow", "Sort:"))
        self.SortAZ.setText(_translate("MainWindow", "→ A/Z"))
        self.SortZA.setText(_translate("MainWindow", "← Z/A"))
        self.notifIcon.setText(_translate("MainWindow", "ⅰ"))
        self.notifText.setText(_translate("MainWindow", "Notification"))
        self.notifDelButton.setText(_translate("MainWindow", "✕"))
        self.openfolderbutton.setText(_translate("MainWindow", "Open folder"))
        self.tablist.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.tablist.setTabText(self.tablist.indexOf(self.List), _translate("MainWindow", "List"))
        self.OBJObjectName.setText(_translate("MainWindow", "Object Name"))
        self.OBJObjectDesc.setText(_translate("MainWindow", "Object desc"))
        self.openFolderButton.setText(_translate("MainWindow", "Open folder"))
        self.delOBJButton.setText(_translate("MainWindow", "Delete Object"))
        self.copyAllButton.setText(_translate("MainWindow", "Copy All"))
        self.back2listButton.setText(_translate("MainWindow", "← Back to list"))
        self.label_8.setText(_translate("MainWindow", "Pictures available:"))
        self.tablist.setTabText(self.tablist.indexOf(self.Object), _translate("MainWindow", "Objet"))
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.menuedit.setTitle(_translate("MainWindow", "Edit"))
        self.menutool.setTitle(_translate("MainWindow", "Tool"))
        self.menuhelp.setTitle(_translate("MainWindow", "Help"))
        self.actionimport.setText(_translate("MainWindow", "import"))
        self.actionopen_folder.setText(_translate("MainWindow", "open folder"))
        self.actionsearch.setText(_translate("MainWindow", "search"))
        self.actionwebsite.setText(_translate("MainWindow", "website"))
        self.actionabout.setText(_translate("MainWindow", "about"))
        self.actionconfigure.setText(_translate("MainWindow", "configure"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionRefresh_app.setText(_translate("MainWindow", "Refresh app"))
