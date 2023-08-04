# Form implementation generated from reading ui file 'matterWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MatterWidget(object):
    def setupUi(self, MatterWidget):
        MatterWidget.setObjectName("MatterWidget")
        MatterWidget.resize(761, 126)
        MatterWidget.setMinimumSize(QtCore.QSize(0, 120))
        MatterWidget.setMaximumSize(QtCore.QSize(16777215, 128))
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
        brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
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
        brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
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
        brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        MatterWidget.setPalette(palette)
        MatterWidget.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(MatterWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.matterFrame = QtWidgets.QFrame(parent=MatterWidget)
        self.matterFrame.setMinimumSize(QtCore.QSize(0, 110))
        self.matterFrame.setMaximumSize(QtCore.QSize(16777215, 110))
        self.matterFrame.setAutoFillBackground(False)
        self.matterFrame.setStyleSheet("QFrame #matterFrame {\n"
"    color: rgb(218, 218, 218);\n"
"    background-color: rgba(0, 0, 0, 0.37);\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    background-image: url(\"no_image.svg\");\n"
"    background-size: 10%;\n"
"    border-color: grey;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-radius: 15px;\n"
"\n"
"}")
        self.matterFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.matterFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.matterFrame.setObjectName("matterFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.matterFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.matterName = QtWidgets.QLabel(parent=self.matterFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matterName.sizePolicy().hasHeightForWidth())
        self.matterName.setSizePolicy(sizePolicy)
        self.matterName.setMinimumSize(QtCore.QSize(300, 0))
        self.matterName.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Thin")
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.matterName.setFont(font)
        self.matterName.setStyleSheet("color: rgb(218, 218, 218);\n"
"    text-decoration: none;\n"
"   border-color: grey;\n"
"    border-radius: 15px;\n"
"margin-left: 10px;\n"
" background-color: rgba(0, 0, 0, 0.37);")
        self.matterName.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.matterName.setObjectName("matterName")
        self.verticalLayout_4.addWidget(self.matterName)
        self.matterDescription = QtWidgets.QLabel(parent=self.matterFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matterDescription.sizePolicy().hasHeightForWidth())
        self.matterDescription.setSizePolicy(sizePolicy)
        self.matterDescription.setMinimumSize(QtCore.QSize(300, 0))
        self.matterDescription.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(13)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.matterDescription.setFont(font)
        self.matterDescription.setStyleSheet("color: rgb(218, 218, 218);\n"
"    text-decoration: none;\n"
"   border-color: grey;\n"
"    border-radius: 15px;\n"
"margin-left: 10px;\n"
" background-color: rgba(0, 0, 0, 0.37);\n"
"")
        self.matterDescription.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.matterDescription.setObjectName("matterDescription")
        self.verticalLayout_4.addWidget(self.matterDescription)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.openMatterButton = QtWidgets.QPushButton(parent=self.matterFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openMatterButton.sizePolicy().hasHeightForWidth())
        self.openMatterButton.setSizePolicy(sizePolicy)
        self.openMatterButton.setMinimumSize(QtCore.QSize(100, 0))
        self.openMatterButton.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(15)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.openMatterButton.setFont(font)
        self.openMatterButton.setStyleSheet("QPushButton{\n"
"font-family:\'Courier New\', Courier, monospace;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"   border-color: grey;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-radius: 15px;\n"
"     background-color: rgba(0, 0, 0, 0.37);\n"
"\n"
"}\n"
"\n"
":hover{\n"
"background-color:black;\n"
"}")
        self.openMatterButton.setObjectName("openMatterButton")
        self.horizontalLayout_4.addWidget(self.openMatterButton)
        self.horizontalLayout.addWidget(self.matterFrame)

        self.retranslateUi(MatterWidget)
        QtCore.QMetaObject.connectSlotsByName(MatterWidget)

    def retranslateUi(self, MatterWidget):
        _translate = QtCore.QCoreApplication.translate
        MatterWidget.setWindowTitle(_translate("MatterWidget", "Form"))
        self.matterName.setText(_translate("MatterWidget", "Matter Name:"))
        self.matterDescription.setText(_translate("MatterWidget", "Matter description:"))
        self.openMatterButton.setText(_translate("MatterWidget", "Open"))
