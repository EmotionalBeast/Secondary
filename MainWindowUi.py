# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 640)
        MainWindow.setFixedSize(1000, 640)
        MainWindow.setWindowIcon(QtGui.QIcon("./resources/icons/tool.png"))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #素材组
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(45,10,100,30))
        self.label_1.setObjectName("label_1")
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setGeometry(QtCore.QRect(155, 10, 300, 30))
        self.comBox_1.addItems(self.groupList())
        self.comBox_1.activated.connect(lambda: self.templateList(self.comBox_1.currentText()))
        self.comBox_1.setCurrentIndex(-1)
        self.comboBox_1.setObjectName("comboBox_1")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(545,10,100,30))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(645, 10, 300, 30))
        self.comBox_2.activated.connect(lambda: self.showTemplateDate())
        self.comboBox_2.setObjectName("comboBox_2")

        #第二行，json选项
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(20, 60, 100, 30))
        self.checkBox_1.setObjectName("checkBox_1")

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(140, 60, 100, 30))
        self.checkBox_2.setObjectName("checkBox_2")

        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(260, 60, 50, 30))
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(330, 60, 70, 30))
        self.checkBox_4.setObjectName("checkBox_4")

        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(420, 60, 100, 30))
        self.checkBox_5.setObjectName("checkBox_5")

        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(540, 60, 100, 30))
        self.checkBox_6.setObjectName("checkBox_6")

        #数组box
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(660, 60, 60, 30))
        self.label_3.setObjectName("label_3")

        self.spinBox_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_1.setGeometry(QtCore.QRect(730, 60, 40, 30))
        self.spinBox_1.setObjectName("spinBox_1")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(790, 60, 60, 30))
        self.label_4.setObjectName("label_4")

        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(860, 60, 40, 30))
        self.spinBox_2.setObjectName("spinBox_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(920, 60, 80, 30))
        self.pushButton.setObjectName("pushButton")

        #主体表格
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 110, 1000, 530))
        self.tabWidget.setObjectName("tabWidget")

        
        MainWindow.setCentralWidget(self.centralwidget)

        #菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)

        #状态栏
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #toolbar
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.new = QtWidgets.QAction(QtGui.QIcon("./resources/icons/new.png"), "&new", self)
        self.edit = QtWidgets.QAction(QtGui.QIcon("./resources/icons/edit.png"), "&edit", self)
        self.save = QtWidgets.QAction(QtGui.QIcon("./resources/icons/save.png"), "&save", self)
        self.refresh = QtWidgets.QAction(QtGui.QIcon("./resources/icons/refresh.png"), "&refresh", self)
        self.open = QtWidgets.QAction(QtGui.QIcon("./resources/icons/open.png"), "&open", self)
        self.toolBar.addAction(self.new)
        self.toolBar.addAction(self.edit)
        self.toolBar.addAction(self.save)
        self.toolBar.addAction(self.refresh)
        self.toolBar.addAction(self.open)

        #define action
        self.actionNew = QtWidgets.QAction(QtGui.QIcon('./resources/images/new.png'), '&New', self)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(QtGui.QIcon('./resources/images/save_as.png'), '&Save', self)
        self.actionSave.setObjectName("actionSave")
        self.actionSetting = QtWidgets.QAction(QtGui.QIcon('./resources/images/setting.png'), '&Setting', self)
        self.actionSetting.setObjectName("actionSetting")
        self.actionQuit = QtWidgets.QAction(QtGui.QIcon('./resources/images/quit.png'), '&Quit', self)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPaint = QtWidgets.QAction(QtGui.QIcon('./resources/images/paint.png'), '&Paint', self)
        self.actionPaint.setObjectName("actionPaint")
        self.actionEnCom = QtWidgets.QAction(QtGui.QIcon('./resources/images/EnCom.png'), '&EnCom', self)
        self.actionEnCom.setObjectName("actionEnCom")

        #menu add action
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSetting)
        self.menuFile.addAction(self.actionQuit)
        self.menuTools.addAction(self.actionPaint)
        self.menuTools.addAction(self.actionEnCom)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        #The function defined in menu linking
        self.actionNew.triggered.connect(self.openFileWindow)
        self.actionSave.triggered.connect(self.saveTable)
        self.actionSetting.triggered.connect(self.openDirWindow)
        self.actionQuit.triggered.connect(QtWidgets.qApp.quit)
        self.actionPaint.triggered.connect(self.openPaintWindow)
        self.actionEnCom.triggered.connect(self.EnCom)

        #ToolBar Function linking
        self.new.triggered.connect(self.openFileWindow)
        self.edit.triggered.connect(self.editable)
        self.save.triggered.connect(self.saveTable)
        self.refresh.triggered.connect(self.setRefresh)
        self.open.triggered.connect(self.openOrigin)

        #pushButton
        self.pushButton.clicked.connect(self.createTable)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.checkBox_1.setText(_translate("MainWindow", "background"))
        self.checkBox_2.setText(_translate("MainWindow", "underArrow"))
        self.checkBox_3.setText(_translate("MainWindow", "text"))
        self.checkBox_4.setText(_translate("MainWindow", "cutout"))
        self.checkBox_5.setText(_translate("MainWindow", "aboveArrow"))
        self.checkBox_6.setText(_translate("MainWindow", "foreground"))
        self.pushButton.setText(_translate("MainWindow", "生成"))

        self.label_1.setText(_translate("MainWindow", "素材组："))
        self.label_2.setText(_translate("MainWindow", "json文件："))
        self.label_3.setText(_translate("MainWindow", "sticker："))
        self.label_4.setText(_translate("MainWindow", "elements："))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))


