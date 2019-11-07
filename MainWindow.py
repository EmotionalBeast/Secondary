#coding: utf-8

import json, os, sys, subprocess
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, 
													QTableWidgetItem, QAbstractItemView, QComboBox)
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5 import QtWidgets, QtCore

from MainWindowUi import Ui_MainWindow
from PaintWindow import MyPaintWindow
from DirWindow import MyDirWindow
from FileWindow import MyFileWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):

	def __init__(self):
		super(MyMainWindow,self).__init__()
		self.variableInit()
		self.setupUi(self)
		

	def variableInit(self):
		with open("./resources/json/setting.json", "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr, strict = False)
		self.workspacePath = dic["directory"]


	def openFileWindow(self):
		self.myFileWindow = MyFileWindow()
		self.myFileWindow.setWindowModality(Qt.ApplicationModal)
		self.myFileWindow.show()

	def openDirWindow(self):
		self.myDirWindow = MyDirWindow()
		self.myDirWindow.setWindowModality(Qt.ApplicationModal)
		self.myDirWindow.show()

	def openPaintWindow(self):
		if self.comboBox_2.currentText() != null:
			self.myPaintWindow = MyPaintWindow(self.comboBox_1.currentText(), self.comboBox_2.currentText())
			self.myPaintWindow.setWindowModality(Qt.ApplicationModal)
			self.myPaintWindow.show()
		else:
			QMessageBox.information(self,"提示","请选择json文件!")

	def openOrigin(self):
		if self.comboBox_1.currentText() != null:
			pathOrigin ="file:///" + self.workspacePath + "/" + self.comboBox_1.currentText() + "/origin/"
			QDesktopServices.openUrl(QUrl(pathOrigin))
		else:
			QMessageBox.information(self, "提示", "请选择素材组！")
		

	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Message', 'You sure to quit?',
									 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	#comboBox checked operation	
	#get material group exist in workspace directory and show them in comboBox_1 
	def groupList(self):
		tempList = []
		for root,dirs,files in os.walk(self.workspacePath):
			for dir in dirs:
				if root == self.workspacePath:
					tempList.append(dir)
		return tempList

	#get template json in group checked and show them in comboBox_2
	def templateList(self, comboBoxText):
		if self.comboBox_2.count() != 0:
			self.comboBox_2.clear()
		tempList = []
		path = self.workspacePath + "/" + comboBoxText + "/in"
		for root,dirs,files in os.walk(path):
			for dir in dirs:
				if path == root:
					self.count = len(dir) * (-1)
			for file in files:
				if file == "template.json":
					name = file + "-" + root[self.count:]
					tempList.append(name)
					tempList.sort()

		self.comboBox_2.addItems(tempList)
		self.comboBox_2.setCurrentIndex(-1)

	#show template json data in table
	def readJson(self):
		temp_1 = self.comboBox_1.currentText()
		temp_2 = self.comboBox_2.currentText()
		path = self.workspacePath + "/" + temp_1 + "/in/" + temp_2[self.count:] + "/template.json" 
		with open(path, "r") as lf:
			size = os.path.getsize(path)
			if size != 0:
				jsonStr = lf.read()
				dic = json.loads(jsonStr, strict = False)
				return dic
			else:
				return 0

	def resolveJson(self):
		self.elements_list = []
		self.cutSeparate_list = []
		self.sticker_list = []

		self.checkBox_1.setChecked(False)
		self.checkBox_1.setChecked(False)
		self.checkBox_1.setChecked(False)
		self.checkBox_1.setChecked(False)
		self.checkBox_1.setChecked(False)
		self.checkBox_1.setChecked(False)
		self.dic = self.readJson()

		if self.dic == 0:
			self.spinBox_1.setValue(0)
			self.spinBox_2.setValue(0)
		else:
			self.elements_list = self.dic["elements"]
			self.cutSeparate_list = self.elements_list[0]["cutSeparate"]
			self.sticker_list = self.dic["sticker"]
			self.templateId = self.dic['templateId']

			self.spinBox_1.setValue(len(self.sticker_list))
			self.spinBox_2.setValue(len(self.elements_list))

			for i in range(len(self.cutSeparate_list)):
				if self.cutSeparate_list[i]["resourceDirectory"][1:] == "background":
					self.background_dic = self.cutSeparate_list[i]
					self.checkBox_1.setChecked(True)
				if self.cutSeparate_list[i]["resourceDirectory"][1:] == "underArrow":
					self.underArrow_dic = self.cutSeparate_list[i]
					self.checkBox_2.setChecked(True)
				if self.cutSeparate_list[i]["resourceDirectory"][1:] == "text":
					self.text_dic = self.cutSeparate_list[i]
					self.checkBox_3.setChecked(True)
				if self.cutSeparate_list[i]["resourceDirectory"][1:] == "cutout":
					self.cutout_dic = self.cutSeparate_list[i]
					self.checkBox_4.setChecked(True)
				if self.cutSeparate_list[i]["resourceDirectory"][1:] == "aboveArrow":
					self.aboveArrow_dic = self.cutSeparate_list[i]
					self.checkBox_5.setChecked(True)
				if self.cutSeparate_list[i]["resourceDirectory"][1:] == "foreground":
					self.foreground_dic = self.cutSeparate_list[i]
					self.checkBox_6.setChecked(True)

	def showTemplateData(self):
		self.resolveJson()
		# value main table
		self.mainTable()
		self.tableWidget_1.setRowCount(1)
		self.tableWidget_1.setItem(0, 0, QTableWidgetItem(self.dic["version"]))
		self.tableWidget_1.setItem(0, 1, QTableWidgetItem(self.dic["music"]))
		self.tableWidget_1.setItem(0, 2, QTableWidgetItem(str(self.dic["templateId"])))

		#value elements
		#value media table
		self.mediaTable()
		self.tableWidget_2.setRowCount(1)
		self.tableWidget_2.setItem(0, 0, QTableWidgetItem(self.elements_list[0]["id"]))
		self.tableWidget_2.setItem(0, 1, QTableWidgetItem(self.elements_list[0]["type"]))
		self.tableWidget_2.setItem(0, 2, QTableWidgetItem(str(self.elements_list[0]["blur"]["type"])))
		self.tableWidget_2.setItem(0, 3, QTableWidgetItem(str(self.elements_list[0]["blur"]["size"])))
		self.tableWidget_2.setItem(0, 4, QTableWidgetItem(str(self.elements_list[0]["constraints"]["left"]["constant"])))
		self.tableWidget_2.setItem(0, 5, QTableWidgetItem(str(self.elements_list[0]["constraints"]["left"]["percentage"])))
		self.tableWidget_2.setItem(0, 6, QTableWidgetItem(str(self.elements_list[0]["constraints"]["top"]["constant"])))
		self.tableWidget_2.setItem(0, 7, QTableWidgetItem(str(self.elements_list[0]["constraints"]["top"]["percentage"])))
		self.tableWidget_2.setItem(0, 8, QTableWidgetItem(str(self.elements_list[0]["constraints"]["width"]["constant"])))
		self.tableWidget_2.setItem(0, 9, QTableWidgetItem(str(self.elements_list[0]["constraints"]["width"]["percentage"])))
		self.tableWidget_2.setItem(0, 10, QTableWidgetItem(str(self.elements_list[0]["constraints"]["height"]["constant"])))
		self.tableWidget_2.setItem(0, 11, QTableWidgetItem(str(self.elements_list[0]["constraints"]["height"]["percentage"])))

		#value background table
		if self.checkBox_1.isChecked() == True:
			self.backgroundTable()
			self.tableWidget_3.setRowCount(1)
			self.tableWidget_3.setItem(0, 0, QTableWidgetItem(str(self.background_dic["id"])))
			self.tableWidget_3.setItem(0, 1, QTableWidgetItem(str(self.background_dic["type"])))
			self.tableWidget_3.setItem(0, 2, QTableWidgetItem(self.background_dic["resourceDirectory"]))
			self.tableWidget_3.setItem(0, 3, QTableWidgetItem(self.background_dic["animation"]))
			self.tableWidget_3.setItem(0, 4, QTableWidgetItem(str(self.background_dic["rect"]["x"])))
			self.tableWidget_3.setItem(0, 5, QTableWidgetItem(str(self.background_dic["rect"]["y"])))
			self.tableWidget_3.setItem(0, 6, QTableWidgetItem(str(self.background_dic["rect"]["width"])))
			self.tableWidget_3.setItem(0, 7, QTableWidgetItem(str(self.background_dic["rect"]["height"])))
			self.tableWidget_3.setItem(0, 8, QTableWidgetItem(self.background_dic["keyPath"]))
			self.tableWidget_3.setItem(0, 9, QTableWidgetItem(self.background_dic["filter"]))

		#value underArrow table
		if self.checkBox_2.isChecked() == True:
			self.underArrowTable()
			self.tableWidget_4.setRowCount(1)
			self.tableWidget_4.setItem(0, 0, QTableWidgetItem(str(self.underArrow_dic["id"])))
			self.tableWidget_4.setItem(0, 1, QTableWidgetItem(str(self.underArrow_dic["type"])))
			self.tableWidget_4.setItem(0, 2, QTableWidgetItem(str(self.underArrow_dic["adjust"])))
			self.tableWidget_4.setItem(0, 3, QTableWidgetItem(self.underArrow_dic["resourceDirectory"]))
			self.tableWidget_4.setItem(0, 4, QTableWidgetItem(self.underArrow_dic["animation"]))
			self.tableWidget_4.setItem(0, 5, QTableWidgetItem(str(self.underArrow_dic["rect"]["x"])))
			self.tableWidget_4.setItem(0, 6, QTableWidgetItem(str(self.underArrow_dic["rect"]["y"])))
			self.tableWidget_4.setItem(0, 7, QTableWidgetItem(str(self.underArrow_dic["rect"]["width"])))
			self.tableWidget_4.setItem(0, 8, QTableWidgetItem(str(self.underArrow_dic["rect"]["height"])))
			self.tableWidget_4.setItem(0, 9, QTableWidgetItem(self.underArrow_dic["keyPath"]))
			
		#value text table
		if self.checkBox_3.isChecked() == True:
			self.textTable()
			self.tableWidget_5.setRowCount(1)
			self.tableWidget_5.setItem(0, 0, QTableWidgetItem(str(self.text_dic["id"])))
			self.tableWidget_5.setItem(0, 1, QTableWidgetItem(str(self.text_dic["type"])))
			self.tableWidget_5.setItem(0, 2, QTableWidgetItem(self.text_dic["resourceDirectory"]))
			self.tableWidget_5.setItem(0, 3, QTableWidgetItem(self.text_dic["animation"]))
			self.tableWidget_5.setItem(0, 4, QTableWidgetItem(str(self.text_dic["fontSize"])))
			self.tableWidget_5.setItem(0, 5, QTableWidgetItem(self.text_dic["fontName"]))
			self.tableWidget_5.setItem(0, 6, QTableWidgetItem(self.text_dic["placeHolder"]))
			self.tableWidget_5.setItem(0, 7, QTableWidgetItem(str(self.text_dic["lineSpacing"])))
			self.tableWidget_5.setItem(0, 8, QTableWidgetItem(str(self.text_dic["letterSpacing"])))
			self.tableWidget_5.setItem(0, 9, QTableWidgetItem(self.text_dic["textAlignment"]))
			self.tableWidget_5.setItem(0, 10, QTableWidgetItem(self.text_dic["textColor"]))
			self.tableWidget_5.setItem(0, 11, QTableWidgetItem(str(self.text_dic["canvasWidth"])))
			self.tableWidget_5.setItem(0, 12, QTableWidgetItem(str(self.text_dic["contentSize"][0])))
			self.tableWidget_5.setItem(0, 13, QTableWidgetItem(str(self.text_dic["contentSize"][1])))
			self.tableWidget_5.setItem(0, 14, QTableWidgetItem(self.text_dic["keyPath"]))

		#value cutout table
		if self.checkBox_3.isChecked() == True:
			self.cutoutTable()
			self.tableWidget_6.setRowCount(1)
			self.tableWidget_6.setItem(0, 0, QTableWidgetItem(str(self.cutout_dic["id"])))
			self.tableWidget_6.setItem(0, 1, QTableWidgetItem(str(self.cutout_dic["type"])))
			self.tableWidget_6.setItem(0, 2, QTableWidgetItem(self.cutout_dic["resourceDirectory"]))
			self.tableWidget_6.setItem(0, 3, QTableWidgetItem(self.cutout_dic["animation"]))
			self.tableWidget_6.setItem(0, 4, QTableWidgetItem(str(self.cutout_dic["rect"]["x"])))
			self.tableWidget_6.setItem(0, 5, QTableWidgetItem(str(self.cutout_dic["rect"]["y"])))
			self.tableWidget_6.setItem(0, 6, QTableWidgetItem(str(self.cutout_dic["rect"]["width"])))
			self.tableWidget_6.setItem(0, 7, QTableWidgetItem(str(self.cutout_dic["rect"]["height"])))
			self.tableWidget_6.setItem(0, 8, QTableWidgetItem(self.cutout_dic["keyPath"]))
			self.tableWidget_6.setItem(0, 9, QTableWidgetItem(self.cutout_dic["filter"]))

		#value aboveArrow table
		if self.checkBox_5.isChecked() == True:
			self.aboveArrowTable()
			self.tableWidget_7.setRowCount(1)
			self.tableWidget_7.setItem(0, 0, QTableWidgetItem(str(self.aboveArrow_dic["id"])))
			self.tableWidget_7.setItem(0, 1, QTableWidgetItem(str(self.aboveArrow_dic["type"])))
			self.tableWidget_7.setItem(0, 2, QTableWidgetItem(str(self.aboveArrow_dic["adjust"])))
			self.tableWidget_7.setItem(0, 3, QTableWidgetItem(self.aboveArrow_dic["resourceDirectory"]))
			self.tableWidget_7.setItem(0, 4, QTableWidgetItem(self.aboveArrow_dic["animation"]))
			self.tableWidget_7.setItem(0, 5, QTableWidgetItem(str(self.aboveArrow_dic["rect"]["x"])))
			self.tableWidget_7.setItem(0, 6, QTableWidgetItem(str(self.aboveArrow_dic["rect"]["y"])))
			self.tableWidget_7.setItem(0, 7, QTableWidgetItem(str(self.aboveArrow_dic["rect"]["width"])))
			self.tableWidget_7.setItem(0, 8, QTableWidgetItem(str(self.aboveArrow_dic["rect"]["height"])))
			self.tableWidget_7.setItem(0, 9, QTableWidgetItem(self.aboveArrow_dic["keyPath"]))

		#value foreground table
		if self.checkBox_6.isChecked() == True:
			self.foregroundTable()
			self.tableWidget_8.setRowCount(1)
			self.tableWidget_8.setItem(0, 0, QTableWidgetItem(str(self.foreground_dic["id"])))
			self.tableWidget_8.setItem(0, 1, QTableWidgetItem(str(self.foreground_dic["type"])))
			self.tableWidget_8.setItem(0, 2, QTableWidgetItem(self.foreground_dic["resourceDirectory"]))
			self.tableWidget_8.setItem(0, 3, QTableWidgetItem(self.foreground_dic["animation"]))
			self.tableWidget_8.setItem(0, 4, QTableWidgetItem(str(self.foreground_dic["rect"]["x"])))
			self.tableWidget_8.setItem(0, 5, QTableWidgetItem(str(self.foreground_dic["rect"]["y"])))
			self.tableWidget_8.setItem(0, 6, QTableWidgetItem(str(self.foreground_dic["rect"]["width"])))
			self.tableWidget_8.setItem(0, 7, QTableWidgetItem(str(self.foreground_dic["rect"]["height"])))
			self.tableWidget_8.setItem(0, 8, QTableWidgetItem(self.foreground_dic["keyPath"]))

		if self.spinBox_1.value() != 0:
			self.stickerTable()
			self.tableWidget_9.setRowCount(self.spinBox_1.value())
			for i in range(self.spinBox_1.value()):
				self.tableWidget_9.setItem(i, 0, QTableWidgetItem(str(self.sticker_list[i]["id"])))
				self.tableWidget_9.setItem(i, 1, QTableWidgetItem(str(self.sticker_list[i]["resourceDirectory"])))
				self.tableWidget_9.setItem(i, 2, QTableWidgetItem(str(self.sticker_list[i]["constraints"]["left"]["constant"])))
				self.tableWidget_9.setItem(i, 3, QTableWidgetItem(str(self.sticker_list[i]["constraints"]["left"]["percentage"])))
				self.tableWidget_9.setItem(i, 4, QTableWidgetItem(str(self.sticker_list[i]["constraints"]["top"]["constant"])))
				self.tableWidget_9.setItem(i, 5, QTableWidgetItem(str(self.sticker_list[i]["constraints"]["top"]["percentage"])))
				self.tableWidget_9.setItem(i, 6, QTableWidgetItem(str(self.sticker_list[i]["constraints"]["width"]["constant"])))
				self.tableWidget_9.setItem(i, 7, QTableWidgetItem(str(self.sticker_list[i]["constraints"]["width"]["percentage"])))
				self.tableWidget_9.setItem(i, 8, QTableWidgetItem(str(self.sticker_list[i]["constraints"]["height"]["constant"])))
				self.tableWidget_9.setItem(i, 9, QTableWidgetItem(str(self.sticker_list[i]["constraints"]["height"]["percentage"])))

	def editable(self):
		pass


	def setRefresh(self):
		bc = self.comboBox_1.count()
		text_1 = self.comboBox_1.currentText()
		self.comboBox_1.clear()
		self.comboBox_1.addItems(self.groupList())
		ac = self.comboBox_1.count()
		if bc != ac:
			self.comboBox_1.setCurrentIndex(-1)
			self.comboBox_2.setCurrentIndex(-1)
		else:
			self.comboBox_1.setCurrentText(text_1)
	
	def createTable(self):
		pass

	def saveTable(self):
		pass

	def checkValues(self):
		pass

	def tableValues(self):
		pass
	
	def encryption(self):
		pass

	def compressing(self):
		pass

	def EnCom(self):
		if self.comboBox_1.currentText() != null:
			self.encryption()
			self.compressing()
		else:
			QMessageBox.information(self, "提示", "请选择素材组！")

	def openOrigin(self):
		pass

	def layers(self):
    		pass
    		
    	# self.backgroundLayer = []
		# self.underArrowLayer = []
		# self.textLayer = []
		# self.cutoutLayer = []
		# self.aboveArrowLayer = []
		# self.foregroundLayer = []
    				
    			
    				
    			
		
	



	
