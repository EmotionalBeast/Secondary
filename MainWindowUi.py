# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import tools


class Ui_MainWindow(object):

    #初始化界面控件
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 740)
        MainWindow.setFixedSize(1000, 740)
        MainWindow.setWindowIcon(QtGui.QIcon("./resources/icons/tool.png"))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 140, 1000, 600))
        self.tabWidget.setObjectName("tabWidget")

        #素材组
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(45,10,100,30))
        self.label_1.setObjectName("label_1")
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setGeometry(QtCore.QRect(155, 10, 300, 30))
        self.comboBox_1.addItems(self.groupList())
        self.comboBox_1.activated.connect(lambda: self.templateList(self.comboBox_1.currentText()))
        self.comboBox_1.setCurrentIndex(-1)
        self.comboBox_1.setObjectName("comboBox_1")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(545,10,100,30))
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(645, 10, 300, 30))
        self.comboBox_2.activated.connect(lambda: self.showTemplateData())
        self.comboBox_2.setObjectName("comboBox_2")

        #数组box
        #meida table
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(712, 60, 78, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

        self.spinBox_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_1.setGeometry(QtCore.QRect(800, 60, 40, 30))
        self.spinBox_1.setObjectName("spinBox_1")

        #background table
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(198, 60, 88, 30))
        self.label_4.setObjectName("label_4")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(296, 60, 40, 30))
        self.spinBox_2.setObjectName("spinBox_2")

        #underFloating table
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 98, 30))
        self.label_5.setObjectName("label_5")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(128, 60, 40, 30))
        self.spinBox_3.setObjectName("spinBox_3")

        #text table
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(376, 100, 78, 30))
        self.label_6.setObjectName("label_6")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(464, 100, 40, 30))
        self.spinBox_4.setObjectName("spinBox_4")

        #cutout table
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(356, 60, 98, 30))
        self.label_7.setObjectName("label_7")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

        self.spinBox_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_5.setGeometry(QtCore.QRect(464, 60, 40, 30))
        self.spinBox_5.setObjectName("spinBox_5")

        #aboveFloating table
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 100, 98, 30))
        self.label_8.setObjectName("label_8")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

        self.spinBox_6 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_6.setGeometry(QtCore.QRect(128, 100, 40, 30))
        self.spinBox_6.setObjectName("spinBox_6")

        #foreground table
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(198, 100, 88, 30))
        self.label_9.setObjectName("label_9")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

        self.spinBox_7 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_7.setGeometry(QtCore.QRect(296, 100, 40, 30))
        self.spinBox_7.setObjectName("spinBox_7")

        #sticker table
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(544, 60, 78, 30))
        self.label_10.setObjectName("label_10")
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

        self.spinBox_8 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_8.setGeometry(QtCore.QRect(632, 60, 40, 30))
        self.spinBox_8.setObjectName("spinBox_8")

        #layers table
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(544, 100, 78, 30))
        self.label_11.setObjectName("label_11")
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

        self.spinBox_9 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_9.setGeometry(QtCore.QRect(632, 100, 40, 30))
        self.spinBox_9.setObjectName("spinBox_9")

        #第二行，json选项
        #main table
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(762, 100, 100, 30))
        self.checkBox_1.setObjectName("checkBox_1")

        #生成按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(902, 100, 80, 30))
        self.pushButton.setObjectName("pushButton")

        
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

        #tabWidget index init
        self.tabWidget.setCurrentIndex(0)

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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.checkBox_1.setText(_translate("MainWindow", "main"))
        self.pushButton.setText(_translate("MainWindow", "生成"))

        self.label_1.setText(_translate("MainWindow", "素材组："))
        self.label_2.setText(_translate("MainWindow", "json文件："))
        self.label_3.setText(_translate("MainWindow", "media："))
        self.label_4.setText(_translate("MainWindow", "background："))
        self.label_5.setText(_translate("MainWindow", "underFloating："))
        self.label_6.setText(_translate("MainWindow", "text："))
        self.label_7.setText(_translate("MainWindow", "cutout："))
        self.label_8.setText(_translate("MainWindow", "aboveFloating："))
        self.label_9.setText(_translate("MainWindow", "foreground："))
        self.label_10.setText(_translate("MainWindow", "sticker："))
        self.label_11.setText(_translate("MainWindow", "layers："))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        #设置菜单栏的属性
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))

        #设置工具栏的属性
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

        #设置动作属性
        self.actionNew.setText(_translate("MainWindow", "新建"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "保存"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSetting.setText(_translate("MainWindow", "设置"))
        self.actionSetting.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionQuit.setText(_translate("MainWindow", "退出"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPaint.setText(_translate("MainWindow", "展示"))
        self.actionPaint.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionEnCom.setText(_translate("MainWindow", "加密压缩"))
        self.actionEnCom.setShortcut(_translate("MainWindow", "Ctrl+K"))

    #setting table
    def mainTable(self):
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tableWidget_1 = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget_1.setColumnCount(3)
        self.tableWidget_1.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.tableWidget_1.setObjectName("tableWidget_1") 

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabWidget.addTab(self.tab_1, "")

        self.tableWidget_1.setColumnWidth(1,120)


        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget_1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "version"))
        item = self.tableWidget_1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "music"))
        item = self.tableWidget_1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "templateId"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "main"))
        self.tableWidget_1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def mediaTable(self):
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setColumnCount(12)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.tableWidget_2.setObjectName("tableWidget_2") 

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(11, item)
        self.tabWidget.addTab(self.tab_2, "")

        self.tableWidget_2.setColumnWidth(9,120)
        self.tableWidget_2.setColumnWidth(10,120)
        self.tableWidget_2.setColumnWidth(11,120)


        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "blur_type"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "blur_size"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "left_constant"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "left_percentage"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "top_constant"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "top_percentage"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "width_constant"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "width_percentage"))
        item = self.tableWidget_2.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "height_constant"))
        item = self.tableWidget_2.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "height_percentage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "media"))
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def backgroundTable(self):
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setColumnCount(11)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.tableWidget_3.setObjectName("tableWidget_3") 

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabWidget.addTab(self.tab_3, "")

        self.tableWidget_3.setColumnWidth(4,180)

        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "mediaId"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "resourceDirectory"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "animation"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "rect_x"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "rect_y"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "rect_width"))
        item = self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "rect_height"))
        item = self.tableWidget_3.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "keyPath"))
        item = self.tableWidget_3.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "filter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "background"))
        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def underFloatingTable(self):
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setColumnCount(11)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.tableWidget_4.setObjectName("tableWidget_4") 

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabWidget.addTab(self.tab_4, "")

        self.tableWidget_4.setColumnWidth(4,150)

        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "mediaId"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "adjust"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "resourceDirectory"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "animation"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "rect_x"))
        item = self.tableWidget_4.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "rect_y"))
        item = self.tableWidget_4.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "rect_width"))
        item = self.tableWidget_4.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "rect_height"))
        item = self.tableWidget_4.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "keyPath"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "underFloating"))
        self.tableWidget_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def textTable(self):
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_5.setColumnCount(24)
        self.tableWidget_5.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.tableWidget_5.setObjectName("tableWidget_5") 

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()

        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabWidget.addTab(self.tab_5, "")

        self.tableWidget_5.setColumnWidth(3,150)
        self.tableWidget_5.setColumnWidth(6,300)
        self.tableWidget_5.setColumnWidth(7,400)
        self.tableWidget_5.setColumnWidth(16,120)
        self.tableWidget_5.setColumnWidth(17,120)
        self.tableWidget_5.setColumnWidth(18,120)
        self.tableWidget_5.setColumnWidth(19,120)
        self.tableWidget_5.setColumnWidth(20,120)
        self.tableWidget_5.setColumnWidth(21,120)
        self.tableWidget_5.setColumnWidth(22,120)
        self.tableWidget_5.setColumnWidth(23,120)


        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "meidaId"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "resourceDirectory"))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "animation"))
        item = self.tableWidget_5.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "fontSize"))
        item = self.tableWidget_5.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "fontName"))
        item = self.tableWidget_5.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "placeHolder"))
        item = self.tableWidget_5.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "lineSpacing"))
        item = self.tableWidget_5.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "letterSpacing"))
        item = self.tableWidget_5.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "textAlignment"))
        item = self.tableWidget_5.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "textColor"))
        item = self.tableWidget_5.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "canvasWidth"))
        item = self.tableWidget_5.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "contentSize_w"))
        item = self.tableWidget_5.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "contentSize_h"))
        item = self.tableWidget_5.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "keypath"))
        item = self.tableWidget_5.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "left_constant"))
        item = self.tableWidget_5.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "left_percentage"))
        item = self.tableWidget_5.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "right_constant"))
        item = self.tableWidget_5.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "right_percentage"))
        item = self.tableWidget_5.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "top_constant"))
        item = self.tableWidget_5.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "top_percentage"))
        item = self.tableWidget_5.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "height_constant"))
        item = self.tableWidget_5.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "height_percentage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "text"))
        self.tableWidget_5.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def cutoutTable(self):
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_6.setColumnCount(11)
        self.tableWidget_6.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.tableWidget_6.setObjectName("tableWidget_6") 

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabWidget.addTab(self.tab_6, "")

        self.tableWidget_6.setColumnWidth(3,150)

        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "mediaId"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "resourceDirectory"))
        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "animation"))
        item = self.tableWidget_6.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "rect_x"))
        item = self.tableWidget_6.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "rect_y"))
        item = self.tableWidget_6.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "rect_width"))
        item = self.tableWidget_6.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "rect_height"))
        item = self.tableWidget_6.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "keyPath"))
        item = self.tableWidget_6.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "filter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "cutout"))
        self.tableWidget_6.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def aboveFloatingTable(self):
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tableWidget_7 = QtWidgets.QTableWidget(self.tab_7)
        self.tableWidget_7.setColumnCount(11)
        self.tableWidget_7.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.tableWidget_7.setObjectName("tableWidget_7") 

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabWidget.addTab(self.tab_7, "")

        self.tableWidget_7.setColumnWidth(4,150)

        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "mediaId"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "adjust"))
        item = self.tableWidget_7.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "resourceDirectory"))
        item = self.tableWidget_7.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "animation"))
        item = self.tableWidget_7.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "rect_x"))
        item = self.tableWidget_7.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "rect_y"))
        item = self.tableWidget_7.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "rect_width"))
        item = self.tableWidget_7.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "rect_height"))
        item = self.tableWidget_7.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "keyPath"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "aboveFloating"))
        self.tableWidget_7.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
    def foregroundTable(self):
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tableWidget_8 = QtWidgets.QTableWidget(self.tab_8)
        self.tableWidget_8.setColumnCount(10)
        self.tableWidget_8.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.tableWidget_8.setObjectName("tableWidget_8") 

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabWidget.addTab(self.tab_8, "")

        self.tableWidget_8.setColumnWidth(3,150)

        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget_8.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "mediaId"))
        item = self.tableWidget_8.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_8.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidget_8.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "resourceDirectory"))
        item = self.tableWidget_8.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "animation"))
        item = self.tableWidget_8.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "rect_x"))
        item = self.tableWidget_8.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "rect_y"))
        item = self.tableWidget_8.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "rect_width"))
        item = self.tableWidget_8.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "rect_height"))
        item = self.tableWidget_8.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "keyPath"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "foreground"))
        self.tableWidget_8.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def stickerTable(self):
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tableWidget_9 = QtWidgets.QTableWidget(self.tab_9)
        self.tableWidget_9.setColumnCount(6)
        self.tableWidget_9.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.tableWidget_9.setObjectName("tableWidget_9") 

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(5, item)
        self.tabWidget.addTab(self.tab_9, "")

        self.tableWidget_9.setColumnWidth(1,150)

        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget_9.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_9.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "resourceDirectory"))
        item = self.tableWidget_9.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "rect_x"))
        item = self.tableWidget_9.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "rect_y"))
        item = self.tableWidget_9.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "rect_width"))
        item = self.tableWidget_9.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "rect_height"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "sticker"))
        self.tableWidget_9.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def layersTable(self):
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tableWidget_10 = QtWidgets.QTableWidget(self.tab_10)
        self.tableWidget_10.setColumnCount(4)
        self.tableWidget_10.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.tableWidget_10.setObjectName("tableWidget_10") 

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab_10, "")

        self.tableWidget_10.setColumnWidth(3,150)


        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget_10.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "mediaId"))
        item = self.tableWidget_10.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_10.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "name"))
        item = self.tableWidget_10.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "resource"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "layers"))
        self.tableWidget_10.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def initTable(self):
        if self.index > 0:
            self.tabWidget.close()
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 140, 1000, 600))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setCurrentIndex(0)

        if self.checkBox_1.isChecked() == True and self.spinBox_1.value() != 0:
            self.mainTable()
            self.mediaTable()

        if self.spinBox_2.value() != 0:
            self.backgroundTable()

        if self.spinBox_3.value() != 0:
            self.underFloatingTable()

        if self.spinBox_4.value() != 0:
            self.textTable()

        if self.spinBox_5.value() != 0:
            self.cutoutTable()

        if self.spinBox_6.value() != 0:
            self.aboveFloatingTable()

        if self.spinBox_7.value() != 0:
            self.foregroundTable()

        if self.spinBox_8.value() != 0:
            self.stickerTable()
            
        if self.spinBox_9.value() != 0:
            self.layersTable()

        self.tabWidget.show()
        self.index +=1

    def initComBox(self):
        #定义type的comBox
        self.comBox_05 = QtWidgets.QComboBox()
        self.comBox_05.addItems(tools.getFonts())
        self.comBox_05.setEditable(True)
        self.comBox_05.setCurrentIndex(-1)

        self.comBox_15 = QtWidgets.QComboBox()
        self.comBox_15.addItems(tools.getFonts())
        self.comBox_15.setEditable(True)
        self.comBox_15.setCurrentIndex(-1)

        self.comBox_25 = QtWidgets.QComboBox()
        self.comBox_25.addItems(tools.getFonts())
        self.comBox_25.setEditable(True)
        self.comBox_25.setCurrentIndex(-1)

        self.comBox_35 = QtWidgets.QComboBox()
        self.comBox_35.addItems(tools.getFonts())
        self.comBox_35.setEditable(True)
        self.comBox_35.setCurrentIndex(-1)

        self.comBox_45 = QtWidgets.QComboBox()
        self.comBox_45.addItems(tools.getFonts())
        self.comBox_45.setEditable(True)
        self.comBox_45.setCurrentIndex(-1)

        self.comBox_55 = QtWidgets.QComboBox()
        self.comBox_55.addItems(tools.getFonts())
        self.comBox_55.setEditable(True)
        self.comBox_55.setCurrentIndex(-1)

        self.comBox_65 = QtWidgets.QComboBox()
        self.comBox_65.addItems(tools.getFonts())
        self.comBox_65.setEditable(True)
        self.comBox_65.setCurrentIndex(-1)

        self.comBox_75 = QtWidgets.QComboBox()
        self.comBox_75.addItems(tools.getFonts())
        self.comBox_75.setEditable(True)
        self.comBox_75.setCurrentIndex(-1)

        #在table中添加comBox
        self.tableWidget_5.setCellWidget(0, 6, self.comBox_05)
        self.tableWidget_5.setCellWidget(1, 6, self.comBox_15)
        self.tableWidget_5.setCellWidget(2, 6, self.comBox_25)
        self.tableWidget_5.setCellWidget(3, 6, self.comBox_35)
        self.tableWidget_5.setCellWidget(4, 6, self.comBox_45)
        self.tableWidget_5.setCellWidget(5, 6, self.comBox_55)
        self.tableWidget_5.setCellWidget(6, 6, self.comBox_65)
        self.tableWidget_5.setCellWidget(7, 6, self.comBox_75)






