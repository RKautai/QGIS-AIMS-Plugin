# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AimsUI/AimsClient/Gui/Ui_EditFeatureDialog.ui'
#
# Created: Fri Aug  5 09:54:53 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_EditFeatureDialog(object):
    def setupUi(self, EditFeatureDialog):
        EditFeatureDialog.setObjectName(_fromUtf8("EditFeatureDialog"))
        EditFeatureDialog.resize(480, 1087)
        self.verticalLayout = QtGui.QVBoxLayout(EditFeatureDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(EditFeatureDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_4 = QtGui.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 460, 1067))
        self.scrollAreaWidgetContents_4.setObjectName(_fromUtf8("scrollAreaWidgetContents_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_44 = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.horizontalLayout_11.addWidget(self.label_44)
        self.uFullNum = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uFullNum.setMaximumSize(QtCore.QSize(200, 16777215))
        self.uFullNum.setObjectName(_fromUtf8("uFullNum"))
        self.horizontalLayout_11.addWidget(self.uFullNum)
        self.uAddressType = QtGui.QComboBox(self.scrollAreaWidgetContents_4)
        self.uAddressType.setObjectName(_fromUtf8("uAddressType"))
        self.horizontalLayout_11.addWidget(self.uAddressType)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_41 = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout_4.addWidget(self.label_41, 0, 8, 1, 1)
        self.label_42 = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_4.addWidget(self.label_42, 0, 0, 1, 1)
        self.label_43 = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout_4.addWidget(self.label_43, 0, 6, 1, 1)
        self.uHigh = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uHigh.setMaximumSize(QtCore.QSize(65, 16777215))
        self.uHigh.setMaxLength(6)
        self.uHigh.setObjectName(_fromUtf8("uHigh"))
        self.gridLayout_4.addWidget(self.uHigh, 1, 6, 1, 1)
        self.uPrefix = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uPrefix.setMaximumSize(QtCore.QSize(65, 16777215))
        self.uPrefix.setText(_fromUtf8(""))
        self.uPrefix.setMaxLength(3)
        self.uPrefix.setObjectName(_fromUtf8("uPrefix"))
        self.gridLayout_4.addWidget(self.uPrefix, 1, 0, 1, 1)
        self.uBase = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uBase.setMaximumSize(QtCore.QSize(65, 16777215))
        self.uBase.setInputMethodHints(QtCore.Qt.ImhNone)
        self.uBase.setMaxLength(6)
        self.uBase.setObjectName(_fromUtf8("uBase"))
        self.gridLayout_4.addWidget(self.uBase, 1, 4, 1, 1)
        self.uUnit = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uUnit.setMaximumSize(QtCore.QSize(65, 16777215))
        self.uUnit.setMaxLength(6)
        self.uUnit.setObjectName(_fromUtf8("uUnit"))
        self.gridLayout_4.addWidget(self.uUnit, 1, 2, 1, 1)
        self.uAlpha = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uAlpha.setMaximumSize(QtCore.QSize(65, 16777215))
        self.uAlpha.setMaxLength(4)
        self.uAlpha.setObjectName(_fromUtf8("uAlpha"))
        self.gridLayout_4.addWidget(self.uAlpha, 1, 8, 1, 1)
        self.label_39 = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.gridLayout_4.addWidget(self.label_39, 0, 2, 1, 1)
        self.label_40 = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.gridLayout_4.addWidget(self.label_40, 0, 4, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label_45 = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_45)
        self.externalAddressIdLabel_5 = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.externalAddressIdLabel_5.setObjectName(_fromUtf8("externalAddressIdLabel_5"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.externalAddressIdLabel_5)
        self.uExternalAddId = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uExternalAddId.setText(_fromUtf8(""))
        self.uExternalAddId.setMaxLength(15)
        self.uExternalAddId.setObjectName(_fromUtf8("uExternalAddId"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.uExternalAddId)
        self.externalAddressIdSchemeLabel_5 = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.externalAddressIdSchemeLabel_5.setObjectName(_fromUtf8("externalAddressIdSchemeLabel_5"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.LabelRole, self.externalAddressIdSchemeLabel_5)
        self.uExternalAddressIdScheme = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uExternalAddressIdScheme.setText(_fromUtf8(""))
        self.uExternalAddressIdScheme.setMaxLength(100)
        self.uExternalAddressIdScheme.setObjectName(_fromUtf8("uExternalAddressIdScheme"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.FieldRole, self.uExternalAddressIdScheme)
        self.lifeCycleLabel = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.lifeCycleLabel.setObjectName(_fromUtf8("lifeCycleLabel"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.LabelRole, self.lifeCycleLabel)
        self.ulifeCycle = QtGui.QComboBox(self.scrollAreaWidgetContents_4)
        self.ulifeCycle.setObjectName(_fromUtf8("ulifeCycle"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.FieldRole, self.ulifeCycle)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_2)
        self.uUnitType = QtGui.QComboBox(self.scrollAreaWidgetContents_4)
        self.uUnitType.setObjectName(_fromUtf8("uUnitType"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.FieldRole, self.uUnitType)
        self.levelTypeLabel = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.levelTypeLabel.setObjectName(_fromUtf8("levelTypeLabel"))
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.LabelRole, self.levelTypeLabel)
        self.uLevelType = QtGui.QComboBox(self.scrollAreaWidgetContents_4)
        self.uLevelType.setObjectName(_fromUtf8("uLevelType"))
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.FieldRole, self.uLevelType)
        self.levelValueLabel = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.levelValueLabel.setObjectName(_fromUtf8("levelValueLabel"))
        self.formLayout_5.setWidget(6, QtGui.QFormLayout.LabelRole, self.levelValueLabel)
        self.uLevelValue = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uLevelValue.setMaxLength(40)
        self.uLevelValue.setObjectName(_fromUtf8("uLevelValue"))
        self.formLayout_5.setWidget(6, QtGui.QFormLayout.FieldRole, self.uLevelValue)
        self.line_14 = QtGui.QFrame(self.scrollAreaWidgetContents_4)
        self.line_14.setFrameShape(QtGui.QFrame.HLine)
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.formLayout_5.setWidget(7, QtGui.QFormLayout.SpanningRole, self.line_14)
        self.label_46 = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.formLayout_5.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_46)
        self.roadCentrelineIdLabel = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.roadCentrelineIdLabel.setFont(font)
        self.roadCentrelineIdLabel.setObjectName(_fromUtf8("roadCentrelineIdLabel"))
        self.formLayout_5.setWidget(9, QtGui.QFormLayout.LabelRole, self.roadCentrelineIdLabel)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.uRclId = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uRclId.setReadOnly(True)
        self.uRclId.setObjectName(_fromUtf8("uRclId"))
        self.horizontalLayout_12.addWidget(self.uRclId)
        self.uPersistRcl = QtGui.QCheckBox(self.scrollAreaWidgetContents_4)
        self.uPersistRcl.setText(_fromUtf8(""))
        self.uPersistRcl.setObjectName(_fromUtf8("uPersistRcl"))
        self.horizontalLayout_12.addWidget(self.uPersistRcl)
        self.uGetRclToolButton = QtGui.QToolButton(self.scrollAreaWidgetContents_4)
        self.uGetRclToolButton.setMinimumSize(QtCore.QSize(24, 0))
        self.uGetRclToolButton.setMaximumSize(QtCore.QSize(24, 16777215))
        self.uGetRclToolButton.setText(_fromUtf8(""))
        self.uGetRclToolButton.setObjectName(_fromUtf8("uGetRclToolButton"))
        self.horizontalLayout_12.addWidget(self.uGetRclToolButton)
        self.formLayout_5.setLayout(9, QtGui.QFormLayout.FieldRole, self.horizontalLayout_12)
        self.roadPrefixLabel = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.roadPrefixLabel.setObjectName(_fromUtf8("roadPrefixLabel"))
        self.formLayout_5.setWidget(10, QtGui.QFormLayout.LabelRole, self.roadPrefixLabel)
        self.uRoadPrefix = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uRoadPrefix.setMaxLength(20)
        self.uRoadPrefix.setObjectName(_fromUtf8("uRoadPrefix"))
        self.formLayout_5.setWidget(10, QtGui.QFormLayout.FieldRole, self.uRoadPrefix)
        self.roadNameLabel = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.roadNameLabel.setFont(font)
        self.roadNameLabel.setObjectName(_fromUtf8("roadNameLabel"))
        self.formLayout_5.setWidget(11, QtGui.QFormLayout.LabelRole, self.roadNameLabel)
        self.uRoadName = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uRoadName.setMaxLength(150)
        self.uRoadName.setObjectName(_fromUtf8("uRoadName"))
        self.formLayout_5.setWidget(11, QtGui.QFormLayout.FieldRole, self.uRoadName)
        self.roadTypeNameLabel = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.roadTypeNameLabel.setFont(font)
        self.roadTypeNameLabel.setObjectName(_fromUtf8("roadTypeNameLabel"))
        self.formLayout_5.setWidget(12, QtGui.QFormLayout.LabelRole, self.roadTypeNameLabel)
        self.uRoadTypeName = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uRoadTypeName.setMaxLength(40)
        self.uRoadTypeName.setObjectName(_fromUtf8("uRoadTypeName"))
        self.formLayout_5.setWidget(12, QtGui.QFormLayout.FieldRole, self.uRoadTypeName)
        self.roadSuffixLabel = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.roadSuffixLabel.setFont(font)
        self.roadSuffixLabel.setObjectName(_fromUtf8("roadSuffixLabel"))
        self.formLayout_5.setWidget(13, QtGui.QFormLayout.LabelRole, self.roadSuffixLabel)
        self.uRoadSuffix = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uRoadSuffix.setMaxLength(40)
        self.uRoadSuffix.setReadOnly(False)
        self.uRoadSuffix.setObjectName(_fromUtf8("uRoadSuffix"))
        self.formLayout_5.setWidget(13, QtGui.QFormLayout.FieldRole, self.uRoadSuffix)
        self.waterRouteNameLabel = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.waterRouteNameLabel.setObjectName(_fromUtf8("waterRouteNameLabel"))
        self.formLayout_5.setWidget(14, QtGui.QFormLayout.LabelRole, self.waterRouteNameLabel)
        self.uWaterRouteName = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uWaterRouteName.setMaxLength(100)
        self.uWaterRouteName.setReadOnly(False)
        self.uWaterRouteName.setObjectName(_fromUtf8("uWaterRouteName"))
        self.formLayout_5.setWidget(14, QtGui.QFormLayout.FieldRole, self.uWaterRouteName)
        self.waterNameLabel = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.waterNameLabel.setObjectName(_fromUtf8("waterNameLabel"))
        self.formLayout_5.setWidget(15, QtGui.QFormLayout.LabelRole, self.waterNameLabel)
        self.uWaterName = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.uWaterName.setMaxLength(100)
        self.uWaterName.setReadOnly(False)
        self.uWaterName.setObjectName(_fromUtf8("uWaterName"))
        self.formLayout_5.setWidget(15, QtGui.QFormLayout.FieldRole, self.uWaterName)
        self.line_16 = QtGui.QFrame(self.scrollAreaWidgetContents_4)
        self.line_16.setFrameShape(QtGui.QFrame.HLine)
        self.line_16.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_16.setObjectName(_fromUtf8("line_16"))
        self.formLayout_5.setWidget(17, QtGui.QFormLayout.SpanningRole, self.line_16)
        self.verticalLayout_3.addLayout(self.formLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_47 = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.horizontalLayout_2.addWidget(self.label_47)
        self.buttonAO = QtGui.QPushButton(self.scrollAreaWidgetContents_4)
        self.buttonAO.setMaximumSize(QtCore.QSize(22, 16777215))
        self.buttonAO.setObjectName(_fromUtf8("buttonAO"))
        self.horizontalLayout_2.addWidget(self.buttonAO)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.wAddObj = QtGui.QWidget(self.scrollAreaWidgetContents_4)
        self.wAddObj.setObjectName(_fromUtf8("wAddObj"))
        self.formLayout_2 = QtGui.QFormLayout(self.wAddObj)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.objectTypeLabel = QtGui.QLabel(self.wAddObj)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.objectTypeLabel.setFont(font)
        self.objectTypeLabel.setObjectName(_fromUtf8("objectTypeLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.objectTypeLabel)
        self.uObjectType = QtGui.QComboBox(self.wAddObj)
        self.uObjectType.setObjectName(_fromUtf8("uObjectType"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.uObjectType)
        self.objectNameLabel = QtGui.QLabel(self.wAddObj)
        self.objectNameLabel.setObjectName(_fromUtf8("objectNameLabel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.objectNameLabel)
        self.uObjectName = QtGui.QLineEdit(self.wAddObj)
        self.uObjectName.setMaxLength(250)
        self.uObjectName.setObjectName(_fromUtf8("uObjectName"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.uObjectName)
        self.label_61 = QtGui.QLabel(self.wAddObj)
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_61)
        self.uPositionType = QtGui.QComboBox(self.wAddObj)
        self.uPositionType.setObjectName(_fromUtf8("uPositionType"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.uPositionType)
        self.lExternalObjectId = QtGui.QLabel(self.wAddObj)
        self.lExternalObjectId.setObjectName(_fromUtf8("lExternalObjectId"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.lExternalObjectId)
        self.uExternalObjectId = QtGui.QLineEdit(self.wAddObj)
        self.uExternalObjectId.setMaxLength(15)
        self.uExternalObjectId.setObjectName(_fromUtf8("uExternalObjectId"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.uExternalObjectId)
        self.lExtObjectIdScheme = QtGui.QLabel(self.wAddObj)
        self.lExtObjectIdScheme.setObjectName(_fromUtf8("lExtObjectIdScheme"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.lExtObjectIdScheme)
        self.uExtObjectIdScheme = QtGui.QLineEdit(self.wAddObj)
        self.uExtObjectIdScheme.setMaxLength(100)
        self.uExtObjectIdScheme.setObjectName(_fromUtf8("uExtObjectIdScheme"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.uExtObjectIdScheme)
        self.lValref = QtGui.QLabel(self.wAddObj)
        self.lValref.setObjectName(_fromUtf8("lValref"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.lValref)
        self.uValuationReference = QtGui.QLineEdit(self.wAddObj)
        self.uValuationReference.setBaseSize(QtCore.QSize(0, 50))
        self.uValuationReference.setMaxLength(30)
        self.uValuationReference.setObjectName(_fromUtf8("uValuationReference"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.uValuationReference)
        self.lCertTitle = QtGui.QLabel(self.wAddObj)
        self.lCertTitle.setObjectName(_fromUtf8("lCertTitle"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.lCertTitle)
        self.uCertificateOfTitle = QtGui.QLineEdit(self.wAddObj)
        self.uCertificateOfTitle.setMaxLength(20)
        self.uCertificateOfTitle.setObjectName(_fromUtf8("uCertificateOfTitle"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.uCertificateOfTitle)
        self.lAppellation = QtGui.QLabel(self.wAddObj)
        self.lAppellation.setObjectName(_fromUtf8("lAppellation"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.lAppellation)
        self.uAppellation = QtGui.QLineEdit(self.wAddObj)
        self.uAppellation.setMaxLength(500)
        self.uAppellation.setObjectName(_fromUtf8("uAppellation"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.uAppellation)
        self.uMblkOverride = QtGui.QLineEdit(self.wAddObj)
        self.uMblkOverride.setMaxLength(7)
        self.uMblkOverride.setObjectName(_fromUtf8("uMblkOverride"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.uMblkOverride)
        self.label = QtGui.QLabel(self.wAddObj)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.LabelRole, self.label)
        self.verticalLayout_3.addWidget(self.wAddObj)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents_4)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_48 = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_48)
        self.uNotes = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uNotes.sizePolicy().hasHeightForWidth())
        self.uNotes.setSizePolicy(sizePolicy)
        self.uNotes.setMinimumSize(QtCore.QSize(0, 20))
        self.uNotes.setMaximumSize(QtCore.QSize(16777215, 100))
        self.uNotes.setBaseSize(QtCore.QSize(0, 0))
        self.uNotes.setObjectName(_fromUtf8("uNotes"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.uNotes)
        self.verticalLayout_2.addLayout(self.formLayout_4)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.uAbort = QtGui.QPushButton(self.scrollAreaWidgetContents_4)
        self.uAbort.setObjectName(_fromUtf8("uAbort"))
        self.horizontalLayout_13.addWidget(self.uAbort)
        self.uSubmitAddressButton = QtGui.QPushButton(self.scrollAreaWidgetContents_4)
        self.uSubmitAddressButton.setObjectName(_fromUtf8("uSubmitAddressButton"))
        self.horizontalLayout_13.addWidget(self.uSubmitAddressButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(EditFeatureDialog)
        QtCore.QMetaObject.connectSlotsByName(EditFeatureDialog)
        EditFeatureDialog.setTabOrder(self.uFullNum, self.uAddressType)
        EditFeatureDialog.setTabOrder(self.uAddressType, self.uPrefix)
        EditFeatureDialog.setTabOrder(self.uPrefix, self.uUnit)
        EditFeatureDialog.setTabOrder(self.uUnit, self.uBase)
        EditFeatureDialog.setTabOrder(self.uBase, self.uHigh)
        EditFeatureDialog.setTabOrder(self.uHigh, self.uAlpha)
        EditFeatureDialog.setTabOrder(self.uAlpha, self.uAbort)
        EditFeatureDialog.setTabOrder(self.uAbort, self.uSubmitAddressButton)

    def retranslateUi(self, EditFeatureDialog):
        EditFeatureDialog.setWindowTitle(_translate("EditFeatureDialog", "Form", None))
        self.label_44.setText(_translate("EditFeatureDialog", "Number Splitter:", None))
        self.label_41.setText(_translate("EditFeatureDialog", "Alpha:", None))
        self.label_42.setText(_translate("EditFeatureDialog", "Prefix:", None))
        self.label_43.setText(_translate("EditFeatureDialog", "High:", None))
        self.label_39.setText(_translate("EditFeatureDialog", "Unit:", None))
        self.label_40.setText(_translate("EditFeatureDialog", "Base:", None))
        self.label_45.setText(_translate("EditFeatureDialog", "Address Extras:", None))
        self.externalAddressIdLabel_5.setText(_translate("EditFeatureDialog", "External Address Id:", None))
        self.externalAddressIdSchemeLabel_5.setText(_translate("EditFeatureDialog", "Ext Address Id Scheme:", None))
        self.lifeCycleLabel.setText(_translate("EditFeatureDialog", "Life Cycle:", None))
        self.label_2.setText(_translate("EditFeatureDialog", "Unit Type:", None))
        self.levelTypeLabel.setText(_translate("EditFeatureDialog", "Level Type:", None))
        self.levelValueLabel.setText(_translate("EditFeatureDialog", "Level Value:", None))
        self.label_46.setText(_translate("EditFeatureDialog", "Road:", None))
        self.roadCentrelineIdLabel.setText(_translate("EditFeatureDialog", "Road Centreline Id:", None))
        self.roadPrefixLabel.setText(_translate("EditFeatureDialog", "Road Prefix:", None))
        self.roadNameLabel.setText(_translate("EditFeatureDialog", "Road Name:", None))
        self.roadTypeNameLabel.setText(_translate("EditFeatureDialog", "Road Type:", None))
        self.roadSuffixLabel.setText(_translate("EditFeatureDialog", "Road Suffix:", None))
        self.waterRouteNameLabel.setText(_translate("EditFeatureDialog", "Water Route Name:", None))
        self.waterNameLabel.setText(_translate("EditFeatureDialog", "Water Name:", None))
        self.label_47.setText(_translate("EditFeatureDialog", "Addressable Object:", None))
        self.buttonAO.setText(_translate("EditFeatureDialog", "⇅", None))
        self.objectTypeLabel.setText(_translate("EditFeatureDialog", "Object Type:", None))
        self.objectNameLabel.setText(_translate("EditFeatureDialog", "Object Name:", None))
        self.label_61.setText(_translate("EditFeatureDialog", "Position Type:", None))
        self.lExternalObjectId.setText(_translate("EditFeatureDialog", "External Object Id:", None))
        self.lExtObjectIdScheme.setText(_translate("EditFeatureDialog", "Ext Object Id Scheme:", None))
        self.lValref.setText(_translate("EditFeatureDialog", "Valuation Reference:", None))
        self.lCertTitle.setText(_translate("EditFeatureDialog", "Certificate Of Title:", None))
        self.lAppellation.setText(_translate("EditFeatureDialog", "Appellation:", None))
        self.label.setText(_translate("EditFeatureDialog", "Meshblock Override:", None))
        self.label_48.setText(_translate("EditFeatureDialog", "Notes:", None))
        self.uAbort.setText(_translate("EditFeatureDialog", "Abort", None))
        self.uSubmitAddressButton.setText(_translate("EditFeatureDialog", "Submit", None))

