#coding: utf-8
#author: Jhin Yao

import sys
from PyQt5.Qtwidgets import QApplication
from MainWindow import MyMainWindow

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = MyMainWindow()
	myWinow.show()
	sys.exit(app.exec_())

	