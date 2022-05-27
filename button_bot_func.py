from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from REM import *

counterr_2 = 360

class BTN_Func(Ui_MainWindow):  

	def progress_line_2(self):


		# # print(end = "rem")
		# print(self.Fan_control.value())
		value = self.Fan_control.value()
		print(value)

		global counterr_2
		ram = """border-radius: 60px;
	
background-color: qconicalgradient(cx:0.5, cy:0.5, angle:{VALUE}, stop:0.0866477 rgba(130, 255, 0, 0), stop:0.0892553 rgba(128, 255, 255, 255), stop:0.241798 rgba(0, 22, 255, 255), stop:0.244405 rgba(130, 255, 0, 0), stop:0.425221 rgba(130, 255, 0, 0), stop:0.426525 rgba(128, 255, 255, 255), stop:0.579068 rgba(0, 22, 255, 255), stop:0.582979 rgba(130, 255, 0, 0), stop:0.764205 rgba(130, 255, 0, 0), stop:0.76942 rgba(128, 255, 255, 255), stop:0.912836 rgba(0, 22, 255, 255), stop:0.915443 rgba(130, 255, 0, 0));

"""
		newram = ram.replace("{VALUE}", str(counterr_2%360.0))
		if value != 3 :
			self.pushButton_7.hide()
			self.pushButton_8.hide()

		else:
			self.pushButton_7.show()
			self.pushButton_8.show()

		self.label_17.setStyleSheet(newram)
		counterr_2 -= value*0.25
		if counterr_2 < 0:
			counterr_2 = 360.0











