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

		with open("./resources/json/font.json", 'r') as lf:
			jsonStr = lf.read()
			self.dict1 = json.loads(jsonStr, strict = False)
		#反转字典，赋值给新的字典
		self.dict2 = {v:k for k,v in self.dict1.items()}

		
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
		self.background_list = []
		self.underFloating_list = []
		self.text_list = []
		self.cutout_list = []
		self.aboveFloating_list = []
		self.foreground_list = []
		self.layers_list = []

		self.checkBox_1.setChecked(False)
		self.dic = self.readJson()

		if self.dic == 0:
			path = self.workspacePath + "/" + self.comboBox_1.currentText() + "/in/" + self.comboBox_2.currentText()[self.count:]
			layers_dic, count = tools.getLayers(path)
			self.checkBox_1.setChecked(True)
			self.spinBox_1.setValue(1)
			if "background" in layers_dic.keys():
				self.spinBox_2.setValue(1) #background
			if "underFloating" in layers_dic.keys():
				self.spinBox_3.setValue(1)	#underFloating
			if "text" in layers_dic.keys():
				self.spinBox_4.setValue(1)	#text
			if "cutout" in layers_dic.keys():
				self.spinBox_5.setValue(1)	#cutout
			if "aboveFloating" in layers_dic.keys():
				self.spinBox_6.setValue(1)	#aboveFloating
			if "foreground" in layers_dic.keys():
				self.spinBox_7.setValue(1)	#foreground
			self.spinBox_8.setValue(0)	#sticker
			self.spinBox_9.setValue(count) #layers
			return False

		else:
			self.checkBox_1.setChecked(True)
			self.elements_list = self.dic["elements"]
			self.spinBox_1.setValue(len(self.elements_list))
			if "sticker" in self.dic.keys():	
				self.sticker_list = []		
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
						if "layers" in self.cutSeparate_list[i].keys():
							temp = self.cutSeparate_list[i]["layers"]
							for j in range(len(temp)):
								temp[j].update(temp_dic)
								self.layers_list.append(temp[j])

					if self.cutSeparate_list[i]["resourceDirectory"][1:] == "underFloating":
						self.underFloating_list.append(temp1)
						if "layers" in self.cutSeparate_list[i].keys():
							temp = self.cutSeparate_list[i]["layers"]
							for j in range(len(temp)):
								temp[j].update(temp_dic)
								self.layers_list.append(temp[j])

					if self.cutSeparate_list[i]["resourceDirectory"][1:] == "text":
						self.text_list.append(temp1)
						if "layers" in self.cutSeparate_list[i].keys():
							temp = self.cutSeparate_list[i]["layers"]
							for j in range(len(temp)):
								temp[j].update(temp_dic)
								self.layers_list.append(temp[j])

					if self.cutSeparate_list[i]["resourceDirectory"][1:] == "cutout":
						self.cutout_list.append(temp1)
						if "layers" in self.cutSeparate_list[i].keys():
							temp = self.cutSeparate_list[i]["layers"]
							for j in range(len(temp)):
								temp[j].update(temp_dic)
								self.layers_list.append(temp[j])

					if self.cutSeparate_list[i]["resourceDirectory"][1:] == "aboveFloating":
						self.aboveFloating_list.append(temp1)
						if "layers" in self.cutSeparate_list[i].keys():
							temp = self.cutSeparate_list[i]["layers"]
							for j in range(len(temp)):
								temp[j].update(temp_dic)
								self.layers_list.append(temp[j])
							
					if self.cutSeparate_list[i]["resourceDirectory"][1:] == "foreground":
						self.foreground_list.append(temp1)
						if "layers" in self.cutSeparate_list[i].keys():
							temp = self.cutSeparate_list[i]["layers"]
							for j in range(len(temp)):
								temp[j].update(temp_dic)
								self.layers_list.append(temp[j])

			self.spinBox_2.setValue(len(self.background_list))
			self.spinBox_3.setValue(len(self.underFloating_list))
			self.spinBox_4.setValue(len(self.text_list))
			self.spinBox_5.setValue(len(self.cutout_list))
			self.spinBox_6.setValue(len(self.aboveFloating_list))
			self.spinBox_7.setValue(len(self.foreground_list))
			self.spinBox_9.setValue(len(self.layers_list))
			return True

	def showTemplateData(self):
		self.tabWidget.clear()
		if self.resolveJson() == False:
			return 0
		self.initTable()
		if self.checkBox_1.isChecked() == True:
			# value main table
			self.tableWidget_1.setRowCount(1)
			self.tableWidget_1.setItem(0, 0, QTableWidgetItem(self.dic["version"]))
			self.tableWidget_1.setItem(0, 2, QTableWidgetItem(str(self.dic["templateId"])))
			if "music" in self.dic.keys():
				self.tableWidget_1.setItem(0, 1, QTableWidgetItem(self.dic["music"]))
			else:
				self.tableWidget_1.setItem(0, 1, QTableWidgetItem(""))

		if self.spinBox_1.value() != 0:
			#value elements
			#value media table
			self.tableWidget_2.setRowCount(self.spinBox_1.value())  
			for i in range(len(self.elements_list)):
				self.tableWidget_2.setItem(i, 0, QTableWidgetItem(self.elements_list[i]["id"]))
				self.tableWidget_2.setItem(i, 1, QTableWidgetItem(self.elements_list[i]["type"]))
				self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(self.elements_list[i]["constraints"]["left"]["constant"])))
				self.tableWidget_2.setItem(i, 5, QTableWidgetItem(str(self.elements_list[i]["constraints"]["left"]["percentage"])))
				self.tableWidget_2.setItem(i, 6, QTableWidgetItem(str(self.elements_list[i]["constraints"]["top"]["constant"])))
				self.tableWidget_2.setItem(i, 7, QTableWidgetItem(str(self.elements_list[i]["constraints"]["top"]["percentage"])))
				self.tableWidget_2.setItem(i, 8, QTableWidgetItem(str(self.elements_list[i]["constraints"]["width"]["constant"])))
				self.tableWidget_2.setItem(i, 9, QTableWidgetItem(str(self.elements_list[i]["constraints"]["width"]["percentage"])))
				self.tableWidget_2.setItem(i, 10, QTableWidgetItem(str(self.elements_list[i]["constraints"]["height"]["constant"])))
				self.tableWidget_2.setItem(i, 11, QTableWidgetItem(str(self.elements_list[i]["constraints"]["height"]["percentage"])))
				if "blur" in self.elements_list[i].keys():
					self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(self.elements_list[i]["blur"]["type"])))
					self.tableWidget_2.setItem(i, 3, QTableWidgetItem(str(self.elements_list[i]["blur"]["size"])))
				else:
					self.tableWidget_2.setItem(i, 2, QTableWidgetItem(""))
					self.tableWidget_2.setItem(i, 3, QTableWidgetItem(""))

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
				if "keyPath" in self.background_list[i].keys():
					self.tableWidget_3.setItem(i, 9, QTableWidgetItem(self.background_list[i]["keyPath"]))
				else:
					self.tableWidget_3.setItem(i, 9, QTableWidgetItem(""))
				if "filter" in self.background_list[i].keys():
					self.tableWidget_3.setItem(i, 10, QTableWidgetItem(self.background_list[i]["filter"]))
				else:
					self.tableWidget_3.setItem(i, 10, QTableWidgetItem(""))

		#value underFloating table
		if self.spinBox_3.value() != 0:
			self.tableWidget_4.setRowCount(self.spinBox_3.value())
			for i in range(len(self.underFloating_list)):
				self.tableWidget_4.setItem(i, 0, QTableWidgetItem(self.underFloating_list[i]["mediaId"]))
				self.tableWidget_4.setItem(i, 1, QTableWidgetItem(self.underFloating_list[i]["id"]))
				self.tableWidget_4.setItem(i, 2, QTableWidgetItem(str(self.underFloating_list[i]["type"])))
				self.tableWidget_4.setItem(i, 3, QTableWidgetItem(str(self.underFloating_list[i]["adjust"])))
				self.tableWidget_4.setItem(i, 4, QTableWidgetItem(self.underFloating_list[i]["resourceDirectory"]))
				self.tableWidget_4.setItem(i, 5, QTableWidgetItem(self.underFloating_list[i]["animation"]))
				self.tableWidget_4.setItem(i, 6, QTableWidgetItem(str(self.underFloating_list[i]["rect"]["x"])))
				self.tableWidget_4.setItem(i, 7, QTableWidgetItem(str(self.underFloating_list[i]["rect"]["y"])))
				self.tableWidget_4.setItem(i, 8, QTableWidgetItem(str(self.underFloating_list[i]["rect"]["width"])))
				self.tableWidget_4.setItem(i, 9, QTableWidgetItem(str(self.underFloating_list[i]["rect"]["height"])))
				if "keyPath" in self.underFloating_list[i].keys():
					self.tableWidget_4.setItem(i, 10, QTableWidgetItem(self.underFloating_list[i]["keyPath"]))
				else:
					self.tableWidget_4.setItem(i, 10, QTableWidgetItem(""))
			
		#value text table
		if self.spinBox_4.value() != 0:
			self.tableWidget_5.setRowCount(self.spinBox_4.value())
			self.initComBox()
			for i in range(len(self.text_list)):
				self.tableWidget_5.setItem(i, 0, QTableWidgetItem(self.text_list[i]["mediaId"]))
				self.tableWidget_5.setItem(i, 1, QTableWidgetItem(self.text_list[i]["id"]))
				self.tableWidget_5.setItem(i, 2, QTableWidgetItem(str(self.text_list[i]["type"])))
				self.tableWidget_5.setItem(i, 3, QTableWidgetItem(self.text_list[i]["resourceDirectory"]))
				self.tableWidget_5.setItem(i, 4, QTableWidgetItem(self.text_list[i]["animation"]))
				self.tableWidget_5.setItem(i, 5, QTableWidgetItem(str(self.text_list[i]["fontSize"])))
				self.tableWidget_5.cellWidget(i,6).setCurrentText(self.dict2[self.text_list[i]["fontName"]])
				self.tableWidget_5.setItem(i, 7, QTableWidgetItem(self.text_list[i]["placeHolder"]))
				self.tableWidget_5.setItem(i, 8, QTableWidgetItem(str(self.text_list[i]["lineSpacing"])))
				self.tableWidget_5.setItem(i, 9, QTableWidgetItem(str(self.text_list[i]["letterSpacing"])))
				self.tableWidget_5.setItem(i, 10, QTableWidgetItem(self.text_list[i]["textAlignment"]))
				self.tableWidget_5.setItem(i, 11, QTableWidgetItem(self.text_list[i]["textColor"]))
				self.tableWidget_5.setItem(i, 12, QTableWidgetItem(str(self.text_list[i]["canvasWidth"])))
				self.tableWidget_5.setItem(i, 13, QTableWidgetItem(str(self.text_list[i]["contentSize"][0])))
				self.tableWidget_5.setItem(i, 14, QTableWidgetItem(str(self.text_list[i]["contentSize"][1])))
				self.tableWidget_5.setItem(i, 16, QTableWidgetItem(str(self.text_list[i]["constraints"]["left"]["constant"])))
				self.tableWidget_5.setItem(i, 17, QTableWidgetItem(str(self.text_list[i]["constraints"]["left"]["percentage"])))
				self.tableWidget_5.setItem(i, 18, QTableWidgetItem(str(self.text_list[i]["constraints"]["right"]["constant"])))
				self.tableWidget_5.setItem(i, 19, QTableWidgetItem(str(self.text_list[i]["constraints"]["right"]["percentage"])))
				self.tableWidget_5.setItem(i, 20, QTableWidgetItem(str(self.text_list[i]["constraints"]["top"]["constant"])))
				self.tableWidget_5.setItem(i, 21, QTableWidgetItem(str(self.text_list[i]["constraints"]["top"]["percentage"])))
				self.tableWidget_5.setItem(i, 22, QTableWidgetItem(str(self.text_list[i]["constraints"]["height"]["constant"])))
				self.tableWidget_5.setItem(i, 23, QTableWidgetItem(str(self.text_list[i]["constraints"]["height"]["percentage"])))
				if "keyPath" in self.text_list[i].keys():
					self.tableWidget_5.setItem(i, 15, QTableWidgetItem(self.text_list[i]["keyPath"]))
				else:
					self.tableWidget_5.setItem(i, 15, QTableWidgetItem(""))

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
				if "keyPath" in self.cutout_list[i].keys():
					self.tableWidget_6.setItem(i, 9, QTableWidgetItem(self.cutout_list[i]["keyPath"]))
				else:
					self.tableWidget_6.setItem(i, 9, QTableWidgetItem(""))
				if "filter" in self.cutout_list[i].keys():
					self.tableWidget_6.setItem(i, 10, QTableWidgetItem(self.cutout_list[i]["filter"]))
				else:
					self.tableWidget_6.setItem(i, 10, QTableWidgetItem(""))

		#value aboveFloating table
		if self.spinBox_6.value() != 0:
			self.tableWidget_7.setRowCount(self.spinBox_6.value())
			for i in range(len(self.aboveFloating_list)):
				self.tableWidget_7.setItem(i, 0, QTableWidgetItem(self.aboveFloating_list[i]["mediaId"]))
				self.tableWidget_7.setItem(i, 1, QTableWidgetItem(self.aboveFloating_list[i]["id"]))
				self.tableWidget_7.setItem(i, 2, QTableWidgetItem(str(self.aboveFloating_list[i]["type"])))
				self.tableWidget_7.setItem(i, 3, QTableWidgetItem(str(self.aboveFloating_list[i]["adjust"])))
				self.tableWidget_7.setItem(i, 4, QTableWidgetItem(self.aboveFloating_list[i]["resourceDirectory"]))
				self.tableWidget_7.setItem(i, 5, QTableWidgetItem(self.aboveFloating_list[i]["animation"]))
				self.tableWidget_7.setItem(i, 6, QTableWidgetItem(str(self.aboveFloating_list[i]["rect"]["x"])))
				self.tableWidget_7.setItem(i, 7, QTableWidgetItem(str(self.aboveFloating_list[i]["rect"]["y"])))
				self.tableWidget_7.setItem(i, 8, QTableWidgetItem(str(self.aboveFloating_list[i]["rect"]["width"])))
				self.tableWidget_7.setItem(i, 9, QTableWidgetItem(str(self.aboveFloating_list[i]["rect"]["height"])))
				if "keyPath" in self.aboveFloating_list[i].keys():
					self.tableWidget_7.setItem(i, 10, QTableWidgetItem(self.aboveFloating_list[i]["keyPath"]))
				else:
					self.tableWidget_7.setItem(i, 10, QTableWidgetItem(""))
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
				if "keyPath" in self.foreground_list[i].keys():
					self.tableWidget_8.setItem(i, 9, QTableWidgetItem(self.foreground_list[i]["keyPath"]))
				else:
					self.tableWidget_8.setItem(i, 9, QTableWidgetItem(""))

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

			if self.spinBox_7.value() != 0:
				self.tableWidget_8.setEditTriggers(QAbstractItemView.NoEditTriggers)

			if self.spinBox_8.value() != 0:
				self.tableWidget_9.setEditTriggers(QAbstractItemView.NoEditTriggers)

			if self.spinBox_9.value() != 0:
				self.tableWidget_10.setEditTriggers(QAbstractItemView.NoEditTriggers)

			self.statusbar.showMessage("NonEditable")
		else:
			QMessageBox.information(self, "提示", "请选择json文件")

	def setRefresh(self):
		self.variableInit()
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
			self.tableWidget_1.setItem(0, 1, QTableWidgetItem(""))
			self.tableWidget_1.setItem(0, 2, QTableWidgetItem(self.comboBox_2.currentText()[self.count:]))
			#media table
		if self.spinBox_1.value() != 0:
			self.tableWidget_2.setRowCount(self.spinBox_1.value())
			for j in range(self.spinBox_1.value()):
				self.tableWidget_2.setItem(j, 0, QTableWidgetItem(str(j)))
				self.tableWidget_2.setItem(j, 1, QTableWidgetItem("media"))
				self.tableWidget_2.setItem(j, 2, QTableWidgetItem(""))
				self.tableWidget_2.setItem(j, 3, QTableWidgetItem(""))
				self.tableWidget_2.setItem(j, 4, QTableWidgetItem("0"))
				self.tableWidget_2.setItem(j, 5, QTableWidgetItem("0"))
				self.tableWidget_2.setItem(j, 6, QTableWidgetItem("0"))
				self.tableWidget_2.setItem(j, 7, QTableWidgetItem("0"))
				self.tableWidget_2.setItem(j, 8, QTableWidgetItem("0"))
				self.tableWidget_2.setItem(j, 9, QTableWidgetItem("1"))
				self.tableWidget_2.setItem(j, 10, QTableWidgetItem("0"))
				self.tableWidget_2.setItem(j, 11, QTableWidgetItem("1"))

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
						self.tableWidget_3.setItem(i, 5, QTableWidgetItem("0"))
						self.tableWidget_3.setItem(i, 6, QTableWidgetItem("0"))
						self.tableWidget_3.setItem(i, 7, QTableWidgetItem("375"))
						self.tableWidget_3.setItem(i, 8, QTableWidgetItem("667"))
						self.tableWidget_3.setItem(i, 9, QTableWidgetItem(""))
						self.tableWidget_3.setItem(i, 10, QTableWidgetItem(""))
					count += 1

				if self.spinBox_3.value() != 0:
					self.tableWidget_4.setRowCount(self.spinBox_3.value())
					for i in range(self.spinBox_3.value()):
						self.tableWidget_4.setItem(i, 0, QTableWidgetItem(str(j)))
						self.tableWidget_4.setItem(i, 1, QTableWidgetItem(str(count)))
						self.tableWidget_4.setItem(i, 2, QTableWidgetItem("1"))
						self.tableWidget_4.setItem(i, 3, QTableWidgetItem("0"))
						self.tableWidget_4.setItem(i, 4, QTableWidgetItem("/underFloating"))
						self.tableWidget_4.setItem(i, 5, QTableWidgetItem("data.json"))
						self.tableWidget_4.setItem(i, 10, QTableWidgetItem(""))
					count += 1

				if self.spinBox_5.value() != 0:
					self.tableWidget_6.setRowCount(self.spinBox_5.value())
					for i in range(self.spinBox_5.value()):
						self.tableWidget_6.setItem(i, 0, QTableWidgetItem(str(j)))
						self.tableWidget_6.setItem(i, 1, QTableWidgetItem(str(count)))
						self.tableWidget_6.setItem(i, 2, QTableWidgetItem("2"))
						self.tableWidget_6.setItem(i, 3, QTableWidgetItem("/cutout"))
						self.tableWidget_6.setItem(i, 4, QTableWidgetItem("data.json"))
						self.tableWidget_6.setItem(i, 9, QTableWidgetItem(""))
						self.tableWidget_6.setItem(i, 10, QTableWidgetItem(""))
					count += 1

				if self.spinBox_6.value() != 0:
					self.tableWidget_7.setRowCount(self.spinBox_6.value())
					for i in range(self.spinBox_6.value()):
						self.tableWidget_7.setItem(i, 0, QTableWidgetItem(str(j)))
						self.tableWidget_7.setItem(i, 1, QTableWidgetItem(str(count)))
						self.tableWidget_7.setItem(i, 2, QTableWidgetItem("1"))
						self.tableWidget_7.setItem(i, 3, QTableWidgetItem("0"))
						self.tableWidget_7.setItem(i, 4, QTableWidgetItem("/aboveFloating"))
						self.tableWidget_7.setItem(i, 5, QTableWidgetItem("data.json"))
						self.tableWidget_7.setItem(i, 10, QTableWidgetItem(""))
					count += 1

				if self.spinBox_7.value() != 0:
					self.tableWidget_8.setRowCount(self.spinBox_7.value())
					for i in range(self.spinBox_7.value()):
						self.tableWidget_8.setItem(i, 0, QTableWidgetItem(str(j)))
						self.tableWidget_8.setItem(i, 1, QTableWidgetItem(str(count)))
						self.tableWidget_8.setItem(i, 2, QTableWidgetItem("0"))
						self.tableWidget_8.setItem(i, 3, QTableWidgetItem("/foreground"))
						self.tableWidget_8.setItem(i, 0, QTableWidgetItem("data.json"))
						self.tableWidget_8.setItem(i, 9, QTableWidgetItem(""))
					count += 1

				if self.spinBox_4.value() != 0:
					self.tableWidget_5.setRowCount(self.spinBox_4.value())
					self.initComBox()
					for i in range(self.spinBox_4.value()):
						self.tableWidget_5.setItem(i, 0, QTableWidgetItem(str(j)))
						self.tableWidget_5.setItem(i, 1, QTableWidgetItem(str(count)))
						self.tableWidget_5.setItem(i, 2, QTableWidgetItem("3"))
						self.tableWidget_5.setItem(i, 3, QTableWidgetItem("/text"))
						self.tableWidget_5.setItem(i, 4, QTableWidgetItem("data.json"))
						self.tableWidget_5.setItem(i, 8, QTableWidgetItem("0"))
						self.tableWidget_5.setItem(i, 9, QTableWidgetItem("0"))
						self.tableWidget_5.setItem(i, 12, QTableWidgetItem("375"))
						self.tableWidget_5.setItem(i, 15, QTableWidgetItem(""))
						self.tableWidget_5.setItem(i, 16, QTableWidgetItem("0"))
						self.tableWidget_5.setItem(i, 18, QTableWidgetItem("0"))
						self.tableWidget_5.setItem(i, 20, QTableWidgetItem("0"))
						self.tableWidget_5.setItem(i, 22, QTableWidgetItem("0"))

					
		if self.spinBox_8.value() != 0:
			self.tableWidget_9.setRowCount(self.spinBox_8.value())
			for i in range(self.spinBox_8.value()):
				self.tableWidget_9.setItem(i, 0, QTableWidgetItem(str(i)))
				self.tableWidget_9.setItem(i, 1, QTableWidgetItem("/sticker"))

		path = self.workspacePath + "/" + self.comboBox_1.currentText() + "/in/" + self.comboBox_2.currentText()[self.count:]

		layers_dic, _ = tools.getLayers(path)
		num = 0
		index = 0
		if "background" in layers_dic.keys():
			for i in range(layers_dic["background"]):
				self.tableWidget_10.setItem(index, 1, QTableWidgetItem(str(num)))
				self.tableWidget_10.setItem(index, 2, QTableWidgetItem("img_" + str(i) + ".png"))
				self.tableWidget_10.setItem(index, 3, QTableWidgetItem("images/img_" + str(i) + ".png"))
				index += 1
			num += 1
		if "underFloating" in layers_dic.keys():
			for i in range(layers_dic["underFloating"]):
				self.tableWidget_10.setItem(index, 1, QTableWidgetItem(str(num)))
				self.tableWidget_10.setItem(index, 2, QTableWidgetItem("img_" + str(i) + ".png"))
				self.tableWidget_10.setItem(index, 3, QTableWidgetItem("images/img_" + str(i) + ".png"))
				index += 1
			num += 1
		if "text" in layers_dic.keys():
			for i in range(layers_dic["text"]):
				self.tableWidget_10.setItem(index, 1, QTableWidgetItem(str(num)))
				self.tableWidget_10.setItem(index, 2, QTableWidgetItem("text"))
				self.tableWidget_10.setItem(index, 3, QTableWidgetItem("images/img_" + str(i) + ".png"))
				index += 1
			num += 1
		if "cutout" in layers_dic.keys():
			for i in range(layers_dic["cutout"]):
				self.tableWidget_10.setItem(index, 1, QTableWidgetItem(str(num)))
				self.tableWidget_10.setItem(index, 2, QTableWidgetItem("img_" + str(i) + ".png"))
				self.tableWidget_10.setItem(index, 3, QTableWidgetItem("images/img_" + str(i) + ".png"))
				index += 1
			num += 1
		if "aboveFloating" in layers_dic.keys():
			for i in range(layers_dic["aboveFloating"]):
				self.tableWidget_10.setItem(index, 1, QTableWidgetItem(str(num)))
				self.tableWidget_10.setItem(index, 2, QTableWidgetItem("img_" + str(i) + ".png"))
				self.tableWidget_10.setItem(index, 3, QTableWidgetItem("images/img_" + str(i) + ".png"))
				index += 1
			num += 1
		if "foreground" in layers_dic.keys():
			for i in range(layers_dic["foreground"]):
				self.tableWidget_10.setItem(index, 1, QTableWidgetItem(str(num)))
				self.tableWidget_10.setItem(index, 2, QTableWidgetItem("img_" + str(i) + ".png"))
				self.tableWidget_10.setItem(index, 3, QTableWidgetItem("images/img_" + str(i) + ".png"))
				index += 1
			num += 1

	def saveTable(self):
		if self.comboBox_2.currentText() != "":
			self.nonEditable()
			if self.checkTableItem():
				self.getTableValues()
				name = self.comboBox_2.currentText()
				path = self.workspacePath + "/" + self.comboBox_1.currentText() + "/in/" + name[self.count:] + "/" + name[:13]
				tools.writeJson(path, self.dic)
				QMessageBox.information(self, "提示", "保存成功！")
			else:
				QMessageBox.information(self, "提示", self.message)
		else:
			QMessageBox.information(self, "提示", "请选择保存模版！")
		
	def getTableValues(self):
		if self.spinBox_1.value() != 0:
			media_list = []
			for k in range(self.spinBox_1.value()):
				media_dic = {}
				cutSeparate_list = []
				media_dic["id"] = self.tableWidget_2.item(k, 0).text()
				media_dic["type"] = self.tableWidget_2.item(k, 1).text()
				if self.tableWidget_2.item(k, 2).text() != "" and self.tableWidget_2.item(k, 3).text() != "":
					item1 = int(self.tableWidget_2.item(k, 2).text())
					item2 = int(self.tableWidget_2.item(k, 3).text())
					media_dic["blur"] = {
						"type":	item1,
						"size": item2
					}
				item3 = float(self.tableWidget_2.item(k, 4).text())
				item4 = float(self.tableWidget_2.item(k, 5).text())
				item5 = float(self.tableWidget_2.item(k, 6).text())
				item6 = float(self.tableWidget_2.item(k, 7).text())
				item7 = float(self.tableWidget_2.item(k, 8).text())
				item8 = float(self.tableWidget_2.item(k, 9).text())
				item9 = float(self.tableWidget_2.item(k, 10).text())
				item10 = float(self.tableWidget_2.item(k, 11).text())
				media_dic["constraints"] = {
					"left":{
						"constant": item3,
						"percentage": item4
					},
					"top":{
						"constant": item5,
						"percentage": item6
					},
					"width":{
						"constant": item7,
						"percentage": item8
					},
					"height":{
						"constant": item9,
						"percentage": item10
					}
				}

				if self.spinBox_2.value() != 0:
					for i in range(self.spinBox_2.value()):
						background_dic = {}
						background_dic["id"] = self.tableWidget_3.item(i, 1).text()
						background_dic["type"] = int(self.tableWidget_3.item(i, 2).text())
						background_dic["resourceDirectory"] = self.tableWidget_3.item(i, 3).text()
						background_dic["animation"] = self.tableWidget_3.item(i, 4).text()
						item1 = float(self.tableWidget_3.item(i, 5).text())
						item2 = float(self.tableWidget_3.item(i, 6).text())
						item3 = float(self.tableWidget_3.item(i, 7).text())
						item4 = float(self.tableWidget_3.item(i, 8).text())
						background_dic["rect"] = {
							"x": item1,
							"y": item2,
							"width": item3,
							"height": item4
						}
						background_dic["keyPath"] = self.tableWidget_3.item(i, 9).text()
						if self.tableWidget_3.item(i, 10).text() != "":
							background_dic["filter"] = self.tableWidget_3.item(i, 10).text()
						background_dic["layers"] = []
						for j in range(self.spinBox_9.value()):
							if self.tableWidget_10.item(j, 1).text() == self.tableWidget_3.item(i, 1).text():
								layer = {"name": self.tableWidget_10.item(j, 2).text(), "resource": self.tableWidget_10.item(j, 3).text()}
								background_dic["layers"].append(layer)
						if media_dic["id"] == self.tableWidget_3.item(i, 0).text():
 							cutSeparate_list.append(background_dic)

				if self.spinBox_3.value() != 0:
					for i in range(self.spinBox_3.value()):
						underFloating_dic = {}
						underFloating_dic["id"] = self.tableWidget_4.item(i, 1).text()
						underFloating_dic["type"] = int(self.tableWidget_4.item(i, 2).text())
						underFloating_dic["adjust"] = int(self.tableWidget_4.item(i, 3).text())
						underFloating_dic["resourceDirectory"] = self.tableWidget_4.item(i, 4).text()
						underFloating_dic["animation"] = self.tableWidget_4.item(i, 5).text()
						item1 = float(self.tableWidget_4.item(i, 6).text())
						item2 = float(self.tableWidget_4.item(i, 7).text())
						item3 = float(self.tableWidget_4.item(i, 8).text())
						item4 = float(self.tableWidget_4.item(i, 9).text())
						underFloating_dic["rect"] = {
							"x": item1,
							"y": item2,
							"width": item3,
							"height": item4
						}
						if self.tableWidget_4.item(i, 10).text() != "":
							underFloating_dic["keyPath"] = self.tableWidget_4.item(i, 10).text()
						underFloating_dic["layers"] = []
						for j in range(self.spinBox_9.value()):
							if self.tableWidget_10.item(j, 1).text() == self.tableWidget_4.item(i, 1).text():
								layer = {"name": self.tableWidget_10.item(j, 2).text(), "resource": self.tableWidget_10.item(j, 3).text()}
								underFloating_dic["layers"].append(layer)
						if media_dic["id"] == self.tableWidget_4.item(i, 0).text():
							cutSeparate_list.append(underFloating_dic)


				if self.spinBox_5.value() != 0:
					for i in range(self.spinBox_5.value()):
						cutout_dic = {}
						cutout_dic["id"] = self.tableWidget_6.item(i, 1).text()
						cutout_dic["type"] = int(self.tableWidget_6.item(i, 2).text())
						cutout_dic["resourceDirectory"] = self.tableWidget_6.item(i, 3).text()
						cutout_dic["animation"] = self.tableWidget_6.item(i, 4).text()
						item1 = float(self.tableWidget_6.item(i, 5).text())
						item2 = float(self.tableWidget_6.item(i, 6).text())
						item3 = float(self.tableWidget_6.item(i, 7).text())
						item4 = float(self.tableWidget_6.item(i, 8).text())
						cutout_dic["rect"] = {
							"x": item1,
							"y": item2,
							"width": item3,
							"height": item4
						}
						cutout_dic["keyPath"] = self.tableWidget_6.item(i, 9).text()
						if self.tableWidget_6.item(i, 10).text() != "":
							cutout_dic["filter"] = self.tableWidget_6.item(i, 10).text()
						cutout_dic["layers"] = []
						for j in range(self.spinBox_9.value()):
							if self.tableWidget_10.item(j, 1).text() == self.tableWidget_6.item(i, 1).text():
								layer = {"name": self.tableWidget_10.item(j, 2).text(), "resource": self.tableWidget_10.item(j, 3).text()}
								cutout_dic["layers"].append(layer)
						if media_dic["id"] == self.tableWidget_6.item(i, 0).text():
							cutSeparate_list.append(cutout_dic)

				if self.spinBox_6.value() != 0:
					for i in range(self.spinBox_6.value()):
						aboveFloating_dic = {}
						aboveFloating_dic["id"] = self.tableWidget_7.item(i, 1).text()
						aboveFloating_dic["type"] = int(self.tableWidget_7.item(i, 2).text())
						aboveFloating_dic["adjust"] = int(self.tableWidget_7.item(i, 3).text())
						aboveFloating_dic["resourceDirectory"] = self.tableWidget_7.item(i, 4).text()
						aboveFloating_dic["animation"] = self.tableWidget_7.item(i, 5).text()
						item1 = float(self.tableWidget_7.item(i, 6).text())
						item2 = float(self.tableWidget_7.item(i, 7).text())
						item3 = float(self.tableWidget_7.item(i, 8).text())
						item4 = float(self.tableWidget_7.item(i, 9).text())
						aboveFloating_dic["rect"] = {
							"x": item1,
							"y": item2,
							"width": item3,
							"height": item4
						}
						if self.tableWidget_7.item(i, 10).text() != "":
							aboveFloating_dic["keyPath"] = self.tableWidget_7.item(i, 10).text()
						aboveFloating_dic["layers"] = []
						for j in range(self.spinBox_9.value()):
							if self.tableWidget_10.item(j, 1).text() == self.tableWidget_7.item(i, 1).text():
								layer = {"name": self.tableWidget_10.item(j, 2).text(), "resource": self.tableWidget_10.item(j, 3).text()}
								aboveFloating_dic["layers"].append(layer)
						if media_dic["id"] == self.tableWidget_7.item(i, 0).text():
							cutSeparate_list.append(aboveFloating_dic)

				if self.spinBox_7.value() != 0:
					for i in range(self.spinBox_7.value()):
						foreground_dic = {}
						foreground_dic["id"] = self.tableWidget_8.item(i, 1).text()
						foreground_dic["type"] = int(self.tableWidget_8.item(i, 2).text())
						foreground_dic["resourceDirectory"] = self.tableWidget_8.item(i, 3).text()
						foreground_dic["animation"] = self.tableWidget_8.item(i, 4).text()
						item1 = float(self.tableWidget_8.item(i, 5).text())
						item2 = float(self.tableWidget_8.item(i, 6).text())
						item3 = float(self.tableWidget_8.item(i, 7).text())
						item4 = float(self.tableWidget_8.item(i, 8).text())
						foreground_dic["rect"] = {
							"x": item1,
							"y": item2,
							"width": item3,
							"height": item4
						}
						if self.tableWidget_8.item(i, 9).text() != "":
							foreground_dic["keyPath"] = self.tableWidget_8.item(i, 9).text()
						foreground_dic["layers"] = []
						for j in range(self.spinBox_9.value()):
							if self.tableWidget_10.item(j, 1).text() == self.tableWidget_8.item(i, 1).text():
								layer = {"name": self.tableWidget_10.item(j, 2).text(), "resource": self.tableWidget_10.item(j, 3).text()}
								foreground_dic["layers"].append(layer)
						if media_dic["id"] == self.tableWidget_8.item(i, 0).text():
							cutSeparate_list.append(foreground_dic)

				if self.spinBox_4.value() != 0:
					for i in range(self.spinBox_4.value()):
						text_dic = {}
						text_dic["id"] = self.tableWidget_5.item(i, 1).text()
						text_dic["type"] = int(self.tableWidget_5.item(i, 2).text())
						text_dic["resourceDirectory"] = self.tableWidget_5.item(i, 3).text()
						text_dic["animation"] = self.tableWidget_5.item(i, 4).text()
						text_dic["fontSize"] = float(self.tableWidget_5.item(i, 5).text())
						text_dic["fontName"] = self.dict1[self.tableWidget_5.cellWidget(i, 6).currentText()]
						text_dic["placeHolder"] = self.tableWidget_5.item(i, 7).text()
						text_dic["lineSpacing"] = float(self.tableWidget_5.item(i, 8).text())
						text_dic["letterSpacing"] = float(self.tableWidget_5.item(i, 9).text())
						text_dic["textAlignment"] = self.tableWidget_5.item(i, 10).text()
						text_dic["textColor"] = self.tableWidget_5.item(i, 11).text()
						text_dic["canvasWidth"] = float(self.tableWidget_5.item(i, 12).text())
						text_dic["contentSize"] = [ int(self.tableWidget_5.item(i, 13).text()), int(self.tableWidget_5.item(i, 14).text())]
						text_dic["keyPath"] = self.tableWidget_5.item(i, 15).text()
						item1 = float(self.tableWidget_5.item(i, 16).text())
						item2 = float(self.tableWidget_5.item(i, 17).text())
						item3 = float(self.tableWidget_5.item(i, 18).text())
						item4 = float(self.tableWidget_5.item(i, 19).text())
						item5 = float(self.tableWidget_5.item(i, 20).text())
						item6 = float(self.tableWidget_5.item(i, 21).text())
						item7 = float(self.tableWidget_5.item(i, 22).text())
						item8 = float(self.tableWidget_5.item(i, 23).text())
						text_dic["constraints"] = {
							"left":{
								"constant": item1,
								"percentage": item2
							},
							"right":{
								"constant": item3,
								"percentage": item4
							},
							"top":{
								"constant": item5,
								"percentage": item6
							},
							"height":{
								"constant": item7,
								"percentage": item8
							}
						}
						text_dic["layers"] = []
						for j in range(self.spinBox_9.value()):
							if self.tableWidget_10.item(j, 1).text() == self.tableWidget_5.item(i, 1).text():
								layer = {"name": self.tableWidget_10.item(j, 2).text(), "resource": self.tableWidget_10.item(j, 3).text()}
								text_dic["layers"].append(layer)
						if media_dic["id"] == self.tableWidget_5.item(i, 0).text():
							cutSeparate_list.append(text_dic)
				media_dic["cutSeparate"] = cutSeparate_list
				media_list.append(media_dic)

		if self.spinBox_8.value() != 0:
			sticker_list = []
			for i in range(self.spinBox_8.value()):
				sticker_dic = {}
				sticker_dic["id"] = self.tableWidget_9.item(i, 0).text()
				sticker_dic["resourceDirectory"] = self.tableWidget_9.item(i, 1).text()
				item1 = float(self.tableWidget_9.item(i, 2).text())
				item2 = float(self.tableWidget_9.item(i, 3).text())
				item3 = float(self.tableWidget_9.item(i, 4).text())
				item4 = float(self.tableWidget_9.item(i, 5).text())
				sticker_dic["rect"] = {
					"x": item1,
					"y": item2,
					"width": item3,
					"height": item4
				}
				sticker_list.append(sticker_dic)

		if self.checkBox_1.isChecked():
				self.dic = {}
				self.dic["version"] = self.tableWidget_1.item(0, 0).text()
				if self.tableWidget_1.item(0, 1).text() != "":
					self.dic["music"] = self.tableWidget_1.item(0, 1).text()
				self.dic["templateId"] = self.tableWidget_1.item(0, 2).text()
				self.dic["elements"] = media_list
				if self.spinBox_8.value() != 0:
					self.dic["sticker"] = sticker_list

	def checkTableItem(self):
		if self.spinBox_1.value() != 0:
			for i in range(self.spinBox_1.value()):
				for j in range(self.tableWidget_2.columnCount()):
					if self.tableWidget_2.item(i,j) == None:
						message = "media表第" + str(i) + "行，第" + str(j) + "列，为空！" 
						QMessageBox.information(self, "提示", message)
						return False

		if self.spinBox_2.value() != 0:
			for i in range(self.spinBox_2.value()):
				for j in range(self.tableWidget_3.columnCount()):
					if self.tableWidget_3.item(i, j) == None:
						self.message = "background表第" + str(i) + "行，第" + str(j) + "列，为空！" 
						return False

		if self.spinBox_3.value() != 0:
			for i in range(self.spinBox_3.value()):
				for j in range(self.tableWidget_4.columnCount()):
					if self.tableWidget_4.item(i, j) == None:
						self.message = "underFloating表第" + str(i) + "行，第" + str(j) + "列，为空！" 
						return False

		if self.spinBox_4.value() != 0:
			for i in range(self.spinBox_4.value()):
				for j in range(self.tableWidget_5.columnCount()):
					if j != 6 and self.tableWidget_5.item(i, j) == None:
						self.message = "text表第" + str(i) + "行，第" + str(j) + "列，为空！" 
						return False

		if self.spinBox_5.value() != 0:
			for i in range(self.spinBox_5.value()):
				for j in range(self.tableWidget_6.columnCount()):
					if self.tableWidget_6.item(i, j) == None:
						self.message = "cutout表第" + str(i) + "行，第" + str(j) + "列，为空！" 
						return False

		if self.spinBox_6.value() != 0:
			for i in range(self.spinBox_6.value()):
				for j in range(self.tableWidget_7.columnCount()):
					if self.tableWidget_7.item(i, j) == None:
						self.message = "aboveFloating表第" + str(i) + "行，第" + str(j) + "列，为空！" 
						return False

		if self.spinBox_7.value() != 0:
			for i in range(self.spinBox_7.value()):
				for j in range(self.tableWidget_8.columnCount()):
					if self.tableWidget_8.item(i, j) != None:
						self.message = "forground表第" + str(i) + "行，第" + str(j) + "列，为空！" 
						return False

		if self.spinBox_8.value() != 0:
			for i in range(self.spinBox_8.value()):
				for j in range(self.tableWidget_9.columnCount()):
					if self.tableWidget_9.item(i, j) != None:
						self.message = "sticker表第" + str(i) + "行，第" + str(j) + "列，为空！" 
						return False
		return True

	def encryption(self):
		pathIn = self.workspacePath + "/" + self.comboBox_1.currentText() + "/in"
		pathOut = self.workspacePath + "/" + self.comboBox_1.currentText() + "/out"
		pathJar = "./resources/jar/encrypt.jar"
		command = "java -jar " + pathJar + " " + pathIn + " " + pathOut
		os.system(command)
		QMessageBox.information(self,"提示","加密到out文件夹成功！")

	def compressing(self):
		pathOut = self.workspacePath + "/" + self.comboBox_1.currentText() + "/out"
		pathOrigin = self.workspacePath + "/" + self.comboBox_1.currentText() + "/origin"
		for root,dirs,files in os.walk(pathOut):
			for dir in dirs:
				if root == pathOut:
					pathNeed = pathOut + "/" + dir + "/"
					targetFile = pathOrigin + "/" + dir + ".7z"
					command = "7z a " + targetFile + " " + pathNeed
					os.system(command)
		QMessageBox.information(self, "提示", "已压缩到origin文件夹！")

	def EnCom(self):
		if self.comboBox_1.currentText() != "":
			self.encryption()
			self.compressing()
		else:
			QMessageBox.information(self, "提示", "请选择素材组！")



    			
    				
    			
		
	



	
