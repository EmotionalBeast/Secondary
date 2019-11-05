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
		self.setupUi(self)
		self.workspacePath()

	def workspacePath(self):
		with open("./resources/json/setting.json", "r") as lf:
			jsonStr = lf.read()
			dic = json.loads(jsonStr, strict = False)
		self.path = dic["directory"]

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
			pathOrigin ="file:///" + self.path[:-2] + "origin/"
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
		for root,dirs,files in os.walk(self.path):
			for dir in dirs:
				if root == self.path:
					tempList.append(dir)
		return tempList

	#get template json in group checked and show them in comboBox_2
	def templateList(self, comboBoxText):
		if self.comboBox_2.count() != 0:
			self.comboBox_2.clear()
		tempList = []
		path = self.path + "/" + comboBoxText + "/in"
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
		path = self.path + "/" + temp_1 + "/in/" + temp_2[self.count:] + "/template.json" 
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
		self.cutSeparete_list = []
		self.sticker_list = []

		self.checkBox_5.setChecked(False)

	def showTemplateData(self):
		pass

	def editable(self):
		pass

	def setRefresh(self):
		bc = self.comboBox_1.count()
		text_1 = self.comboBox_1.currentText()
		self.comboBox_1.clear()
		self.comboBox_1.addItems(self.dirList())
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
    				
    			
    				
    			
		
	



	
