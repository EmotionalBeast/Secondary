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
import tools



class MyMainWindow(QMainWindow, Ui_MainWindow):

	def __init__(self):
		super(MyMainWindow,self).__init__()
		self.variableInit()
		self.setupUi(self)
		self.index = 0
		
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
		if self.comboBox_2.currentText() != "":
			self.myPaintWindow = MyPaintWindow(self.comboBox_1.currentText(), self.comboBox_2.currentText())
			self.myPaintWindow.setWindowModality(Qt.ApplicationModal)
			self.myPaintWindow.show()
		else:
			QMessageBox.information(self,"提示","请选择json文件!")

	def openOrigin(self):
		if self.comboBox_1.currentText() != "":
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
		self.background_list = []
		self.underArrow_list = []
		self.text_list = []
		self.cutout_list = []
		self.aboveArrow_list = []
		self.foreground_list = []
		self.layers_list = []

		self.checkBox_1.setChecked(False)
		self.dic = self.readJson()

		if self.dic == 0:
			self.spinBox_1.setValue(0)
			self.spinBox_2.setValue(0)
			self.spinBox_3.setValue(0)
			self.spinBox_4.setValue(0)
			self.spinBox_5.setValue(0)
			self.spinBox_6.setValue(0)
			self.spinBox_7.setValue(0)
			self.spinBox_8.setValue(0)
			self.spinBox_9.setValue(0)
		else:
			self.checkBox_1.setChecked(True)
			self.elements_list = self.dic["elements"]
			self.spinBox_1.setValue(len(self.elements_list))
			
			self.sticker_list = self.dic["sticker"]
			self.spinBox_8.setValue(len(self.sticker_list))
			temp_dic = {"mediaId":"","id":""}
			temp_dic1 = {"mediaId":""}
			for k in range(len(self.elements_list)):	
				temp_dic["mediaId"] = self.elements_list[k]["id"]
				temp_dic1["mediaId"] = self.elements_list[k]["id"]
				self.cutSeparate_list = self.elements_list[k]["cutSeparate"]
				for i in range(len(self.cutSeparate_list)):
					temp_dic["id"] = self.cutSeparate_list[i]["id"]
					temp1 = self.cutSeparate_list[i]
					temp1.update(temp_dic1)
					if self.cutSeparate_list[i]["resourceDirectory"][1:] == "background":						
						self.background_list.append(temp1)
						temp = self.cutSeparate_list[i]["layers"]
						for j in range(len(temp)):
							temp[j].update(temp_dic)
							self.layers_list.append(temp[j])

					if self.cutSeparate_list[i]["resourceDirectory"][1:] == "underArrow":
						self.underArrow_list.append(temp1)
						temp = self.cutSeparate_list[i]["layers"]
						for j in range(len(temp)):
							temp[j].update(temp_dic)
							self.layers_list.append(temp[j])

					if self.cutSeparate_list[i]["resourceDirectory"][1:] == "text":
						self.text_list.append(temp1)
						temp = self.cutSeparate_list[i]["layers"]
						for j in range(len(temp)):
							temp[j].update(temp_dic)
							self.layers_list.append(temp[j])

					if self.cutSeparate_list[i]["resourceDirectory"][1:] == "cutout":
						self.cutout_list.append(temp1)
						temp = self.cutSeparate_list[i]["layers"]
						for j in range(len(temp)):
							temp[j].update(temp_dic)
							self.layers_list.append(temp[j])

					if self.cutSeparate_list[i]["resourceDirectory"][1:] == "aboveArrow":
						self.aboveArrow_list.append(temp1)
						temp = self.cutSeparate_list[i]["layers"]
						for j in range(len(temp)):
							temp[j].update(temp_dic)
							self.layers_list.append(temp[j])
							
					if self.cutSeparate_list[i]["resourceDirectory"][1:] == "foreground":
						self.foreground_list.append(temp1)
						temp = self.cutSeparate_list[i]["layers"]
						for j in range(len(temp)):
							temp[j].update(temp_dic)
							self.layers_list.append(temp[j])

			self.spinBox_2.setValue(len(self.background_list))
			self.spinBox_3.setValue(len(self.underArrow_list))
			self.spinBox_4.setValue(len(self.text_list))
			self.spinBox_5.setValue(len(self.cutout_list))
			self.spinBox_6.setValue(len(self.aboveArrow_list))
			self.spinBox_7.setValue(len(self.foreground_list))
			self.spinBox_9.setValue(len(self.layers_list))


	def showTemplateData(self):
		self.resolveJson()
		self.initTable()
		if self.checkBox_1.isChecked() == True:
			# value main table
			self.tableWidget_1.setRowCount(1)
			self.tableWidget_1.setItem(0, 0, QTableWidgetItem(self.dic["version"]))
			self.tableWidget_1.setItem(0, 1, QTableWidgetItem(self.dic["music"]))
			self.tableWidget_1.setItem(0, 2, QTableWidgetItem(str(self.dic["templateId"])))

		if self.spinBox_1.value() != 0:
			#value elements
			#value media table
			self.tableWidget_2.setRowCount(self.spinBox_1.value())  
			for i in range(len(self.elements_list)):
				self.tableWidget_2.setItem(i, 0, QTableWidgetItem(self.elements_list[i]["id"]))
				self.tableWidget_2.setItem(i, 1, QTableWidgetItem(self.elements_list[i]["type"]))
				self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(self.elements_list[i]["blur"]["type"])))
				self.tableWidget_2.setItem(i, 3, QTableWidgetItem(str(self.elements_list[i]["blur"]["size"])))
				self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(self.elements_list[i]["constraints"]["left"]["constant"])))
				self.tableWidget_2.setItem(i, 5, QTableWidgetItem(str(self.elements_list[i]["constraints"]["left"]["percentage"])))
				self.tableWidget_2.setItem(i, 6, QTableWidgetItem(str(self.elements_list[i]["constraints"]["top"]["constant"])))
				self.tableWidget_2.setItem(i, 7, QTableWidgetItem(str(self.elements_list[i]["constraints"]["top"]["percentage"])))
				self.tableWidget_2.setItem(i, 8, QTableWidgetItem(str(self.elements_list[i]["constraints"]["width"]["constant"])))
				self.tableWidget_2.setItem(i, 9, QTableWidgetItem(str(self.elements_list[i]["constraints"]["width"]["percentage"])))
				self.tableWidget_2.setItem(i, 10, QTableWidgetItem(str(self.elements_list[i]["constraints"]["height"]["constant"])))
				self.tableWidget_2.setItem(i, 11, QTableWidgetItem(str(self.elements_list[i]["constraints"]["height"]["percentage"])))

		#value background table
		if self.spinBox_2.value() != 0:
			self.tableWidget_3.setRowCount(self.spinBox_2.value())
			for i in range(len(self.background_list)):
				self.tableWidget_3.setItem(i, 0, QTableWidgetItem(self.background_list[i]["mediaId"]))
				self.tableWidget_3.setItem(i, 1, QTableWidgetItem(self.background_list[i]["id"]))
				self.tableWidget_3.setItem(i, 2, QTableWidgetItem(str(self.background_list[i]["type"])))
				self.tableWidget_3.setItem(i, 3, QTableWidgetItem(self.background_list[i]["resourceDirectory"]))
				self.tableWidget_3.setItem(i, 4, QTableWidgetItem(self.background_list[i]["animation"]))
				self.tableWidget_3.setItem(i, 5, QTableWidgetItem(str(self.background_list[i]["rect"]["x"])))
				self.tableWidget_3.setItem(i, 6, QTableWidgetItem(str(self.background_list[i]["rect"]["y"])))
				self.tableWidget_3.setItem(i, 7, QTableWidgetItem(str(self.background_list[i]["rect"]["width"])))
				self.tableWidget_3.setItem(i, 8, QTableWidgetItem(str(self.background_list[i]["rect"]["height"])))
				self.tableWidget_3.setItem(i, 9, QTableWidgetItem(self.background_list[i]["keyPath"]))
				self.tableWidget_3.setItem(i, 10, QTableWidgetItem(self.background_list[i]["filter"]))

		#value underArrow table
		if self.spinBox_3.value() != 0:
			self.tableWidget_4.setRowCount(self.spinBox_3.value())
			for i in range(len(self.underArrow_list)):
				self.tableWidget_4.setItem(i, 0, QTableWidgetItem(self.underArrow_list[i]["mediaId"]))
				self.tableWidget_4.setItem(i, 1, QTableWidgetItem(self.underArrow_list[i]["id"]))
				self.tableWidget_4.setItem(i, 2, QTableWidgetItem(str(self.underArrow_list[i]["type"])))
				self.tableWidget_4.setItem(i, 3, QTableWidgetItem(str(self.underArrow_list[i]["adjust"])))
				self.tableWidget_4.setItem(i, 4, QTableWidgetItem(self.underArrow_list[i]["resourceDirectory"]))
				self.tableWidget_4.setItem(i, 5, QTableWidgetItem(self.underArrow_list[i]["animation"]))
				self.tableWidget_4.setItem(i, 6, QTableWidgetItem(str(self.underArrow_list[i]["rect"]["x"])))
				self.tableWidget_4.setItem(i, 7, QTableWidgetItem(str(self.underArrow_list[i]["rect"]["y"])))
				self.tableWidget_4.setItem(i, 8, QTableWidgetItem(str(self.underArrow_list[i]["rect"]["width"])))
				self.tableWidget_4.setItem(i, 9, QTableWidgetItem(str(self.underArrow_list[i]["rect"]["height"])))
				self.tableWidget_4.setItem(i, 10, QTableWidgetItem(self.underArrow_list[i]["keyPath"]))
			
		#value text table
		if self.spinBox_4.value() != 0:
			self.tableWidget_5.setRowCount(self.spinBox_4.value())
			for i in range(len(self.text_list)):
				self.tableWidget_5.setItem(i, 0, QTableWidgetItem(self.text_list[i]["mediaId"]))
				self.tableWidget_5.setItem(i, 1, QTableWidgetItem(self.text_list[i]["id"]))
				self.tableWidget_5.setItem(i, 2, QTableWidgetItem(str(self.text_list[i]["type"])))
				self.tableWidget_5.setItem(i, 3, QTableWidgetItem(self.text_list[i]["resourceDirectory"]))
				self.tableWidget_5.setItem(i, 4, QTableWidgetItem(self.text_list[i]["animation"]))
				self.tableWidget_5.setItem(i, 5, QTableWidgetItem(str(self.text_list[i]["fontSize"])))
				self.tableWidget_5.setItem(i, 6, QTableWidgetItem(self.text_list[i]["fontName"]))
				self.tableWidget_5.setItem(i, 7, QTableWidgetItem(self.text_list[i]["placeHolder"]))
				self.tableWidget_5.setItem(i, 8, QTableWidgetItem(str(self.text_list[i]["lineSpacing"])))
				self.tableWidget_5.setItem(i, 9, QTableWidgetItem(str(self.text_list[i]["letterSpacing"])))
				self.tableWidget_5.setItem(i, 10, QTableWidgetItem(self.text_list[i]["textAlignment"]))
				self.tableWidget_5.setItem(i, 11, QTableWidgetItem(self.text_list[i]["textColor"]))
				self.tableWidget_5.setItem(i, 12, QTableWidgetItem(str(self.text_list[i]["canvasWidth"])))
				self.tableWidget_5.setItem(i, 13, QTableWidgetItem(str(self.text_list[i]["contentSize"][0])))
				self.tableWidget_5.setItem(i, 14, QTableWidgetItem(str(self.text_list[i]["contentSize"][1])))
				self.tableWidget_5.setItem(i, 15, QTableWidgetItem(self.text_list[i]["keyPath"]))

		#value cutout table
		if self.spinBox_5.value() != 0:
			self.tableWidget_6.setRowCount(self.spinBox_5.value())
			for i in range(len(self.cutout_list)):
				self.tableWidget_6.setItem(i, 0, QTableWidgetItem(self.cutout_list[i]["mediaId"]))
				self.tableWidget_6.setItem(i, 1, QTableWidgetItem(self.cutout_list[i]["id"]))
				self.tableWidget_6.setItem(i, 2, QTableWidgetItem(str(self.cutout_list[i]["type"])))
				self.tableWidget_6.setItem(i, 3, QTableWidgetItem(self.cutout_list[i]["resourceDirectory"]))
				self.tableWidget_6.setItem(i, 4, QTableWidgetItem(self.cutout_list[i]["animation"]))
				self.tableWidget_6.setItem(i, 5, QTableWidgetItem(str(self.cutout_list[i]["rect"]["x"])))
				self.tableWidget_6.setItem(i, 6, QTableWidgetItem(str(self.cutout_list[i]["rect"]["y"])))
				self.tableWidget_6.setItem(i, 7, QTableWidgetItem(str(self.cutout_list[i]["rect"]["width"])))
				self.tableWidget_6.setItem(i, 8, QTableWidgetItem(str(self.cutout_list[i]["rect"]["height"])))
				self.tableWidget_6.setItem(i, 9, QTableWidgetItem(self.cutout_list[i]["keyPath"]))
				self.tableWidget_6.setItem(i, 10, QTableWidgetItem(self.cutout_list[i]["filter"]))

		#value aboveArrow table
		if self.spinBox_6.value() != 0:
			self.tableWidget_7.setRowCount(self.spinBox_6.value())
			for i in range(len(self.aboveArrow_list)):
				self.tableWidget_7.setItem(i, 0, QTableWidgetItem(self.aboveArrow_list[i]["mediaId"]))
				self.tableWidget_7.setItem(i, 1, QTableWidgetItem(self.aboveArrow_list[i]["id"]))
				self.tableWidget_7.setItem(i, 2, QTableWidgetItem(str(self.aboveArrow_list[i]["type"])))
				self.tableWidget_7.setItem(i, 3, QTableWidgetItem(str(self.aboveArrow_list[i]["adjust"])))
				self.tableWidget_7.setItem(i, 4, QTableWidgetItem(self.aboveArrow_list[i]["resourceDirectory"]))
				self.tableWidget_7.setItem(i, 5, QTableWidgetItem(self.aboveArrow_list[i]["animation"]))
				self.tableWidget_7.setItem(i, 6, QTableWidgetItem(str(self.aboveArrow_list[i]["rect"]["x"])))
				self.tableWidget_7.setItem(i, 7, QTableWidgetItem(str(self.aboveArrow_list[i]["rect"]["y"])))
				self.tableWidget_7.setItem(i, 8, QTableWidgetItem(str(self.aboveArrow_list[i]["rect"]["width"])))
				self.tableWidget_7.setItem(i, 9, QTableWidgetItem(str(self.aboveArrow_list[i]["rect"]["height"])))
				self.tableWidget_7.setItem(i, 10, QTableWidgetItem(self.aboveArrow_list[i]["keyPath"]))

		#value foreground table
		if self.spinBox_7.value() != 0:
			self.tableWidget_8.setRowCount(self.spinBox_7.value())
			for i in range(len(self.foreground_list)):
				self.tableWidget_8.setItem(i, 0, QTableWidgetItem(self.foreground_list[i]["mediaId"]))
				self.tableWidget_8.setItem(i, 1, QTableWidgetItem(self.foreground_list[i]["id"]))
				self.tableWidget_8.setItem(i, 2, QTableWidgetItem(str(self.foreground_list[i]["type"])))
				self.tableWidget_8.setItem(i, 3, QTableWidgetItem(self.foreground_list[i]["resourceDirectory"]))
				self.tableWidget_8.setItem(i, 4, QTableWidgetItem(self.foreground_list[i]["animation"]))
				self.tableWidget_8.setItem(i, 5, QTableWidgetItem(str(self.foreground_list[i]["rect"]["x"])))
				self.tableWidget_8.setItem(i, 6, QTableWidgetItem(str(self.foreground_list[i]["rect"]["y"])))
				self.tableWidget_8.setItem(i, 7, QTableWidgetItem(str(self.foreground_list[i]["rect"]["width"])))
				self.tableWidget_8.setItem(i, 8, QTableWidgetItem(str(self.foreground_list[i]["rect"]["height"])))
				self.tableWidget_8.setItem(i, 9, QTableWidgetItem(self.foreground_list[i]["keyPath"]))

		if self.spinBox_8.value() != 0:
			self.tableWidget_9.setRowCount(self.spinBox_8.value())
			for i in range(len(self.sticker_list)):
				self.tableWidget_9.setItem(i, 0, QTableWidgetItem(self.sticker_list[i]["id"]))
				self.tableWidget_9.setItem(i, 1, QTableWidgetItem(str(self.sticker_list[i]["resourceDirectory"])))
				self.tableWidget_9.setItem(i, 2, QTableWidgetItem(str(self.sticker_list[i]["rect"]["x"])))
				self.tableWidget_9.setItem(i, 3, QTableWidgetItem(str(self.sticker_list[i]["rect"]["y"])))
				self.tableWidget_9.setItem(i, 4, QTableWidgetItem(str(self.sticker_list[i]["rect"]["width"])))
				self.tableWidget_9.setItem(i, 5, QTableWidgetItem(str(self.sticker_list[i]["rect"]["height"])))

		if self.spinBox_9.value() != 0:
			self.tableWidget_10.setRowCount(self.spinBox_9.value())
			for i in range(len(self.layers_list)):
				self.tableWidget_10.setItem(i, 0, QTableWidgetItem(self.layers_list[i]["mediaId"]))
				self.tableWidget_10.setItem(i, 1, QTableWidgetItem(self.layers_list[i]["id"]))
				self.tableWidget_10.setItem(i, 2, QTableWidgetItem(str(self.layers_list[i]["name"])))
				self.tableWidget_10.setItem(i, 3, QTableWidgetItem(str(self.layers_list[i]["resource"])))

		self.statusbar.showMessage("NonEditable")
				
				
	def editable(self):
		if self.comboBox_2.currentText() != "":
			if self.checkBox_1.isChecked() == True:
				self.tableWidget_1.setEditTriggers(QAbstractItemView.CurrentChanged)

			if self.spinBox_1.value() != 0:
				self.tableWidget_2.setEditTriggers(QAbstractItemView.CurrentChanged)

			if self.spinBox_2.value() != 0:
				self.tableWidget_3.setEditTriggers(QAbstractItemView.CurrentChanged)

			if self.spinBox_3.value() != 0:
				self.tableWidget_4.setEditTriggers(QAbstractItemView.CurrentChanged)

			if self.spinBox_4.value() != 0:
				self.tableWidget_5.setEditTriggers(QAbstractItemView.CurrentChanged)

			if self.spinBox_5.value() != 0:
				self.tableWidget_6.setEditTriggers(QAbstractItemView.CurrentChanged)

			if self.spinBox_6.value() != 0:
				self.tableWidget_7.setEditTriggers(QAbstractItemView.CurrentChanged)

			if self.spinBox_7.value() != 0:
				self.tableWidget_8.setEditTriggers(QAbstractItemView.CurrentChanged)

			if self.spinBox_8.value() != 0:
				self.tableWidget_9.setEditTriggers(QAbstractItemView.CurrentChanged)

			if self.spinBox_9.value() != 0:
				self.tableWidget_10.setEditTriggers(QAbstractItemView.CurrentChanged)

			self.statusbar.showMessage("Editable")
		else:
			QMessageBox.information(self, "提示", "请选择json文件")

	def nonEditable(self):
		if self.comboBox_2.currentText() != "":
			if self.checkBox_1.isChecked() == True:
				self.tableWidget_1.setEditTriggers(QAbstractItemView.NoEditTriggers)

			if self.spinBox_1.value() != 0:
				self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)

			if self.spinBox_2.value() != 0:
				self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)

			if self.spinBox_3.value() != 0:
				self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)

			if self.spinBox_4.value() != 0:
				self.tableWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)

			if self.spinBox_5.value() != 0:
				self.tableWidget_6.setEditTriggers(QAbstractItemView.NoEditTriggers)

			if self.spinBox_6.value() != 0:
				self.tableWidget_7.setEditTriggers(QAbstractItemView.NoEditTriggers)

			if self.spinBox_7.value() != 0:
				self.tableWidget_8.setEditTriggers(QAbstractItemView.NoEditTriggers)

			if self.spinBox_8.value() != 0:
				self.tableWidget_9.setEditTriggers(QAbstractItemView.NoEditTriggers)

			if self.spinBox_9.value() != 0:
				self.tableWidget_10.setEditTriggers(QAbstractItemView.NoEditTriggers)

			self.statusbar.showMessage("Editable")
		else:
			QMessageBox.information(self, "提示", "请选择json文件")

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
		self.initTable()
		if self.checkBox_1.isChecked() == True:
			#main table
			self.tableWidget_1.setRowCount(1)
			self.tableWidget_1.setItem(0, 0, QTableWidgetItem("1.0"))
			self.tableWidget_1.setItem(0, 2, QTableWidgetItem(self.comboBox_2.currentText()[self.count:]))
			#media table
		if self.spinBox_1.value() != 0:
			self.tableWidget_2.setRowCount(self.spinBox_1.value())
			for j in range(self.spinBox_1.value()):
				self.tableWidget_2.setItem(j, 0, QTableWidgetItem(str(j)))
				self.tableWidget_2.setItem(j, 1, QTableWidgetItem("media"))
				self.tableWidget_2.setItem(j, 4, QTableWidgetItem("0"))
				self.tableWidget_2.setItem(j, 6, QTableWidgetItem("0"))
				self.tableWidget_2.setItem(j, 8, QTableWidgetItem("0"))
				self.tableWidget_2.setItem(j, 10, QTableWidgetItem("0"))

				if self.spinBox_9.value() != 0:
					self.tableWidget_10.setRowCount(self.spinBox_9.value())
					for k in range(self.spinBox_9.value()):
						self.tableWidget_10.setItem(k, 0, QTableWidgetItem(str(j)))

				count = 0
				if self.spinBox_2.value() != 0:
					#background table
					self.tableWidget_3.setRowCount(self.spinBox_2.value())
					for i in range(self.spinBox_2.value()):
						self.tableWidget_3.setItem(i, 0, QTableWidgetItem(str(j)))
						self.tableWidget_3.setItem(i, 1, QTableWidgetItem(str(count)))
						self.tableWidget_3.setItem(i, 2, QTableWidgetItem("0"))
						self.tableWidget_3.setItem(i, 3, QTableWidgetItem("/background"))
						self.tableWidget_3.setItem(i, 4, QTableWidgetItem("data.json"))
					count += 1

				if self.spinBox_3.value() != 0:
					self.tableWidget_4.setRowCount(self.spinBox_3.value())
					for i in range(self.spinBox_3.value()):
						self.tableWidget_4.setItem(i, 0, QTableWidgetItem(str(j)))
						self.tableWidget_4.setItem(i, 1, QTableWidgetItem(str(count)))
						self.tableWidget_4.setItem(i, 2, QTableWidgetItem("1"))
						self.tableWidget_4.setItem(i, 3, QTableWidgetItem("0"))
						self.tableWidget_4.setItem(i, 4, QTableWidgetItem("/underArrow"))
						self.tableWidget_4.setItem(i, 5, QTableWidgetItem("data.json"))
					count += 1

				if self.spinBox_4.value() != 0:
					self.tableWidget_5.setRowCount(self.spinBox_4.value())
					for i in range(self.spinBox_3.value()):
						self.tableWidget_5.setItem(i, 0, QTableWidgetItem(str(j)))
						self.tableWidget_5.setItem(i, 1, QTableWidgetItem(str(count)))
						self.tableWidget_5.setItem(i, 2, QTableWidgetItem("3"))
						self.tableWidget_5.setItem(i, 3, QTableWidgetItem("/text"))
						self.tableWidget_5.setItem(i, 4, QTableWidgetItem("data.json"))
					count += 1

				if self.spinBox_5.value() != 0:
					self.tableWidget_6.setRowCount(self.spinBox_5.value())
					for i in range(self.spinBox_5.value()):
						self.tableWidget_6.setItem(i, 0, QTableWidgetItem(str(j)))
						self.tableWidget_6.setItem(i, 1, QTableWidgetItem(str(count)))
						self.tableWidget_6.setItem(i, 2, QTableWidgetItem("2"))
						self.tableWidget_6.setItem(i, 3, QTableWidgetItem("/cutout"))
						self.tableWidget_6.setItem(i, 4, QTableWidgetItem("data.json"))
					count += 1

				if self.spinBox_6.value() != 0:
					self.tableWidget_7.setRowCount(self.spinBox_6.value())
					for i in range(self.spinBox_6.value()):
						self.tableWidget_7.setItem(i, 0, QTableWidgetItem(str(j)))
						self.tableWidget_7.setItem(i, 1, QTableWidgetItem(str(count)))
						self.tableWidget_7.setItem(i, 2, QTableWidgetItem("1"))
						self.tableWidget_7.setItem(i, 3, QTableWidgetItem("0"))
						self.tableWidget_7.setItem(i, 4, QTableWidgetItem("/aboveArrow"))
						self.tableWidget_7.setItem(i, 5, QTableWidgetItem("data.json"))
					count += 1

				if self.spinBox_7.value() != 0:
					self.tableWidget_8.setRowCount(self.spinBox_7.value())
					for i in range(self.spinBox_6.value()):
						self.tableWidget_8.setItem(i, 0, QTableWidgetItem(str(j)))
						self.tableWidget_8.setItem(i, 1, QTableWidgetItem(str(count)))
						self.tableWidget_8.setItem(i, 2, QTableWidgetItem("0"))
						self.tableWidget_8.setItem(i, 3, QTableWidgetItem("/foreground"))
						self.tableWidget_8.setItem(i, 0, QTableWidgetItem("data.json"))
					
		if self.spinBox_8.value() != 0:
			self.tableWidget_9.setRowCount(self.spinBox_8.value())
			for i in range(self.spinBox_8.value()):
				self.tableWidget_9.setItem(i, 0, QTableWidgetItem(str(i)))
				self.tableWidget_9.setItem(i, 1, QTableWidgetItem("/sticker"))

		path = self.workspacePath + "/" + self.comboBox_1.currentText() + "/in/" + self.comboBox_2.currentText()[self.count:]

		layers_dic = tools.getLayers(path)

		num = 0 
		index = 0
		if layers_dic["background"] != "":
			for i in range(layers_dic["background"]):
				self.tableWidget_10.setItem(index, 1, QTableWidgetItem(str(num)))
				self.tableWidget_10.setItem(index, 2, QTableWidgetItem("img_" + str(i) + ".png"))
				self.tableWidget_10.setItem(index, 3, QTableWidgetItem("image/img_" + str(i) + ".png"))
				index += 1
			num += 1
		if layers_dic["underArrow"] != "":
			for i in range(layers_dic["underArrow"]):
				self.tableWidget_10.setItem(index, 1, QTableWidgetItem(str(num)))
				self.tableWidget_10.setItem(index, 2, QTableWidgetItem("img_" + str(i) + ".png"))
				self.tableWidget_10.setItem(index, 3, QTableWidgetItem("image/img_" + str(i) + ".png"))
				index += 1
			num += 1
		if layers_dic["text"] != "":
			for i in range(layers_dic["text"]):
				self.tableWidget_10.setItem(index, 1, QTableWidgetItem(str(num)))
				self.tableWidget_10.setItem(index, 2, QTableWidgetItem("text"))
				self.tableWidget_10.setItem(index, 3, QTableWidgetItem("image/img_" + str(i) + ".png"))
				index += 1
			num += 1
		if layers_dic["cutout"] != "":
			for i in range(layers_dic["cutout"]):
				self.tableWidget_10.setItem(index, 1, QTableWidgetItem(str(num)))
				self.tableWidget_10.setItem(index, 2, QTableWidgetItem("img_" + str(i) + ".png"))
				self.tableWidget_10.setItem(index, 3, QTableWidgetItem("image/img_" + str(i) + ".png"))
				index += 1
			num += 1
		if layers_dic["aboveArrow"] != "":
			for i in range(layers_dic["aboveArrow"]):
				self.tableWidget_10.setItem(index, 1, QTableWidgetItem(str(num)))
				self.tableWidget_10.setItem(index, 2, QTableWidgetItem("img_" + str(i) + ".png"))
				self.tableWidget_10.setItem(index, 3, QTableWidgetItem("image/img_" + str(i) + ".png"))
				index += 1
			num += 1
		if layers_dic["foreground"] != "":
			for i in range(layers_dic["foreground"]):
				self.tableWidget_10.setItem(index, 1, QTableWidgetItem(str(num)))
				self.tableWidget_10.setItem(index, 2, QTableWidgetItem("img_" + str(i) + ".png"))
				self.tableWidget_10.setItem(index, 3, QTableWidgetItem("image/img_" + str(i) + ".png"))
				index += 1
			num += 1


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
		if self.comboBox_1.currentText() != "":
			self.encryption()
			self.compressing()
		else:
			QMessageBox.information(self, "提示", "请选择素材组！")

	def layers(self):
    		pass

    			
    				
    			
		
	



	
