'''
Created on 3 thg 5, 2022

@author: A315-56
'''
from hashlib import new
from multiprocessing.sharedctypes import Value
import sys
import os
from types import new_class
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from clock import *
import datetime
import requests
import random

from canvas import *




from traitlets import Int
from datetime import date

os.system("pyuic5 -x Main.ui -o REM.py")
os.system("pyrcc5 -o Weather_Icon_rc.py Weather_Icon.qrc")
os.system("pyrcc5 -o Icon_rc.py Weather_Icon.qrc")

from REM import *
from style import *
from GUI_PyQt5_Func_1 import *
from button_bot_func import *

Counter = 0
	 
class MAIN(Ui_MainWindow):
	def __init__(self, mainwindow):
		self.setupUi(mainwindow)

		self.Time_Start()


		# self.Ui_MainWindow.verticalSlider.valueChanged.connect(self.slide_it)
		
		self.Top_stackedWidget.setCurrentWidget(self.Top_ControlPanel)
		self.Bot_stackedWidget.setCurrentWidget(self.Bot_ControlPanel)
		# self.Control_btn.setStyleSheet(Control_btn_active)

		self.slider_setting()

		#================ ĐÂT ======================

		self.verticalSlider.valueChanged.connect(self.slide_it)
		# self.verticalSlider_4.valueChanged.connect(self.slide_it_nhiet_do)
		self.verticalSlider_2.valueChanged.connect(self.slide_it_PH)

		# #================ không khí =================
		self.slide_it_do_am_kk(random.randint(0,100))
		self.slide_it_nhiet_do_kk(random.randint(0,100))

		# self.Top_Ctrl_frame2_body_do_am_vertical.valueChanged.connect(self.slide_it_do_am_kk)
		# self.Top_Ctrl_frame2_body_nhiet_do_vertical.valueChanged.connect(self.slide_it_nhiet_do_kk)
		# self.Top_Ctrl_frame2_body_nong_do_O2_vertical.valueChanged.connect(self.slide_it_PH_kk)

		# #=================== Lux ======================

		# self.Top_Ctrl_frame3_body_lux_vertical.valueChanged.connect(self.slide_it_LUX)
		self.slide_it_LUX(random.randint(0, 100))

		# #=================== Wh =======================
		self.verticalSlider_2.valueChanged.connect(self.slide_it_WH)

		# self.Top_Ctrl_frame4_body_Wh_vertical.valueChanged.connect(self.slide_it_WH)

		#=================== thời tiết và thời gian ================
		self.clock_time = Clock()
		self.Top_Ctrl_frame5_clock_widget.addWidget(self.clock_time)
		try:
			self.weather()
		except :
			self.User_name.setText("Ko co wifi")


		# self.verticalSlider_2.valueChanged.connect(self.PH)

		# self.Menu_btn.clicked.connect(lambda: UIFunctions.ToggleMenu      (self, 50, 250))
		# self.Control_btn.clicked.connect(lambda: UIFunctions.Select_Menu  (self, 1))
		# self.Parameter_btn.clicked.connect(lambda: UIFunctions.Select_Menu(self, 2))
		# self.Setting_btn.clicked.connect(lambda: UIFunctions.Select_Menu  (self, 3))

		#===================== chart =====================
		#__________1
		self.grafica_1 = Canvas_grafica()
		self.Top_Para_frame1_body_chart.addWidget(self.grafica_1)
		#__________2
		self.grafica_2 = Canvas_grafica_1()
		self.Top_Para_frame1_body_chart_PH.addWidget(self.grafica_2)
		#__________3
		self.grafica_3 = Canvas_grafica_2()
		self.Top_Para_frame1_body_chart_Do_Am_KK.addWidget(self.grafica_3)
		#__________4
		self.grafica_4 = Canvas_grafica_3()
		self.Top_Para_frame1_body_chart_T_KK.addWidget(self.grafica_4)
		# self.end_text.clicked.connect(self.test())

		self.Menu_btn.clicked.connect      (lambda: UIFunctions.ToggleMenu (self, 50, 300))
		self.Control_btn.clicked.connect   (lambda: UIFunctions.Select_Menu(self, 1))
		self.Parameter_btn.clicked.connect (lambda: UIFunctions.Select_Menu(self, 2))
		self.Setting_btn.clicked.connect   (lambda: UIFunctions.Select_Menu(self, 3))
		self.Properties_btn.clicked.connect(lambda: UIFunctions.Select_Menu(self, 4))

	# def test(self):

	def slider_setting(self):
		self.verticalSlider.setMinimum(0)
		self.verticalSlider.setMaximum(100)
		self.verticalSlider_2.setMinimum(0)
		self.verticalSlider_2.setMaximum(100)

# #=========================================================================== TIMER =================================================================================

	def Time_Start(self):
		self.time = QtCore.QTimer()
		self.time.start(1000)
		self.time.timeout.connect(self.timer_Wh)

		self.time_fan = QtCore.QTimer()
		self.time_fan.start(1)
		self.time_fan.timeout.connect(lambda: BTN_Func.progress_line_2(self))


#============================================================================ ĐẤT ==================================================================================
	def progressBarValue(self, value):
		#biểu diễn thanh tiến trình
		styleSheet = """
			border-radius:85px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:{STOP_1} rgba(255, 255, 255, 255), stop:{STOP_2} rgba(0, 0, 0, 0));
		"""
		#láy giá trị của thanh tiến trình, chuyển đổi nó thành kiểu FLOAT
		# dừng giá trị từ 1 đến 0
		
		progress = (100-value)
		# Láy giá trị mới

		stop_1 = str(0.876423 - 0.0074707*progress)
		stop_2 = str(0.878799 - 0.0074707*progress)

		#Đặc giá trị đó vào cái STYLESHEET mới
		newStylsheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

		#Ungứ dụng giá trị mới vào styleSheet
		self.label_29.setStyleSheet(newStylsheet)

	def slide_it(self, value):
		Rem =""" <html><head/><body><p><span style=" font-size:16pt; color:#7f7f7f;">Độ ẩm</span></p><p><span style=" font-size:14pt; color:#7f7f7f;">        {VALUE}</span><span style=" font-size:14pt; color:#7f7f7f; vertical-align:super;">%</span></p></body></html>"""
		print(self.verticalSlider.value())
		newRem = Rem.replace("{VALUE}", str(value))
		self.progressBarValue(100 - int(value))
		self.label_31.setText(newRem)

	def progressBarValue_PH(self, value):
		#biểu diễn thanh tiến trình
		styleSheet = """
			border-radius:85px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:{STOP_1} rgba(255, 255, 255, 255), stop:{STOP_2} rgba(0, 0, 0, 0));
		"""
		#láy giá trị của thanh tiến trình, chuyển đổi nó thành kiểu FLOAT
		# dừng giá trị từ 1 đến 0

		progress = (100 - value)
		# Láy giá trị mới
		stop_1 = str(0.876423 - 0.0074707*progress)
		stop_2 = str(0.878799 - 0.0074707*progress)

		#Đặc giá trị đó vào cái STYLESHEET mới
		newStylsheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

		#Ungứ dụng giá trị mới vào styleSheet
		self.label_33.setStyleSheet(newStylsheet)

	def slide_it_PH(self, value):
		Rem = """<html><head/><body><p><span style=" font-size:16pt; color:#7f7f7f;">Độ PH</span></p><p><span style=" font-size:14pt; color:#7f7f7f;">        {VALUE}</span><span style=" font-size:14pt; color:#7f7f7f; vertical-align:super;">%</span></p></body></html>"""
		print(self.verticalSlider_2.value())
		newRem = Rem.replace("{VALUE}", str(value))
		self.progressBarValue_PH(100 - int(value))
		self.label_34.setText(newRem)

# #============================================================================ Không khí ==================================================================================

	def progressBarValue_do_am_kk(self, value):
		#biểu diễn thanh tiến trình
		styleSheet = """
			border-radius:85px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:{STOP_1} rgba(255, 255, 255, 255), stop:{STOP_2} rgba(0, 0, 0, 0));
		"""
		#láy giá trị của thanh tiến trình, chuyển đổi nó thành kiểu FLOAT
		# dừng giá trị từ 1 đến 0

		progress = (100 - value)
		# Láy giá trị mới
		stop_1 = str(0.876423 - 0.0074707*progress)
		stop_2 = str(0.878799 - 0.0074707*progress)

		#Đặc giá trị đó vào cái STYLESHEET mới
		newStylsheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

		#Ungứ dụng giá trị mới vào styleSheet
		self.Top_Ctrl_frame2_body_do_am_3.setStyleSheet(newStylsheet)

	def slide_it_do_am_kk(self, value):
		Rem =""" <html><head/><body><p><span style=" font-size:16pt; color:#7f7f7f;">Độ ẩm</span></p><p><span style=" font-size:14pt; color:#7f7f7f;">        {VALUE}</span><span style=" font-size:14pt; color:#7f7f7f; vertical-align:super;">%</span></p></body></html>"""
		# print(self.Top_Ctrl_frame2_body_do_am_vertical.value())
		newRem = Rem.replace("{VALUE}", str(value))
		self.progressBarValue_do_am_kk(100 - int(value))
		self.Top_Ctrl_frame2_body_do_am_1.setText(newRem)

	def progressBarValue_nhiet_do_kk(self, value):
		#biểu diễn thanh tiến trình
		styleSheet = """
			border-radius:85px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:{STOP_1} rgba(255, 255, 255, 255), stop:{STOP_2} rgba(0, 0, 0, 0));
		"""
		#láy giá trị của thanh tiến trình, chuyển đổi nó thành kiểu FLOAT
		# dừng giá trị từ 1 đến 0

		progress = (100 - value)
		# Láy giá trị mới
		stop_1 = str(0.876423 - 0.0074707*progress)
		stop_2 = str(0.878799 - 0.0074707*progress)

		#Đặc giá trị đó vào cái STYLESHEET mới
		newStylsheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

		#Ungứ dụng giá trị mới vào styleSheet
		self.Top_Ctrl_frame2_body_do_ND_3.setStyleSheet(newStylsheet)

	def slide_it_nhiet_do_kk(self, value):
		Rem = """<html><head/><body><p><span style=" color:#ababab;">Nhiệt độ</span></p><p><span style=" color:#ababab;">{VALUE}</span><span style=" font-size:12pt; color:#ababab; vertical-align:super;">%</span></p></body></html>"""
		# print(self.Top_Ctrl_frame2_body_nhiet_do_vertical.value())
		newRem = Rem.replace("{VALUE}", str(value))
		self.progressBarValue_nhiet_do_kk(100 - int(value))
		self.Top_Ctrl_frame2_body_do_ND_1.setText(newRem)

# #============================================================================ LUX ==================================================================================

	def progressBarValue_LUX(self, value):
		#biểu diễn thanh tiến trình
		styleSheet = """
			border-radius:85px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:{STOP_1} rgba(255, 255, 255, 255), stop:{STOP_2} rgba(0, 0, 0, 0));
		"""
		#láy giá trị của thanh tiến trình, chuyển đổi nó thành kiểu FLOAT
		# dừng giá trị từ 1 đến 0

		progress = (100 - value)
		# Láy giá trị mới
		stop_1 = str(0.876423 - 0.0074707*progress)
		stop_2 = str(0.878799 - 0.0074707*progress)

		#Đặc giá trị đó vào cái STYLESHEET mới
		newStylsheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

		#Ungứ dụng giá trị mới vào styleSheet
		self.Top_Ctrl_frame3_body_lux_3.setStyleSheet(newStylsheet)

	def slide_it_LUX(self, value):
		Rem = """<html><head/><body><p><span style=" color:#ababab;">LUX</span></p><p><span style=" color:#ababab;">{VALUE}</span><span style=" font-size:12pt; color:#ababab; vertical-align:super;">%</span></p></body></html>"""
		newRem = Rem.replace("{VALUE}", str(value))
		self.progressBarValue_LUX(100 - int(value))
		self.Top_Ctrl_frame3_body_lux_1.setText(newRem)

# #=========================================================================== WH =============================================================================================

	def progressBarValue_WH(self, value):
  
		styleSheet_rem = """
			border-radius: 105px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:{STOP_1}, stop:0.995399 rgba(0, 0, 42, 0), stop:0.996435 rgba(255, 0, 0, 255), stop:0.998964 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 42, 0));
		"""

		# dừng giá trị từ 1 đến 0
		progress = int(100-value)
		# Láy giá trị mới
		stop_1 = str(1.8*progress)
		#Đặc giá trị đó vào cái STYLESHEET mới
		newStylsheet_rem = styleSheet_rem.replace("{STOP_1}", stop_1)

		#Ungứ dụng giá trị mới vào styleSheet
 
		self.Top_Ctrl_frame4_body_Wh_4.setStyleSheet(newStylsheet_rem)

	def slide_it_WH(self, value):

		# print(self.Top_Ctrl_frame4_body_Wh_vertical.value())

		self.progressBarValue_WH(int(value))
		# self.Top_Ctrl_frame4_body_Wh_1.setText(newRem)

	def timer_Wh(self):
		global Counter
		Rem_1 ="""<html><head/><body><p><span style=" font-size:16pt; color:#ff0000;">0 0 0 0 {VALUE_1}</span></p></body></html>"""
		Rem_2 ="""<html><head/><body><p><span style=" font-size:16pt; color:#ff0000;">0 0 0 {VALUE_1} {VALUE_2}</span></p></body></html>"""
		Rem_3 ="""<html><head/><body><p><span style=" font-size:16pt; color:#ff0000;">0 0 {VALUE_1} {VALUE_2} {VALUE_3}</span></p></body></html>"""
		Rem_4 ="""<html><head/><body><p><span style=" font-size:16pt; color:#ff0000;">0 {VALUE_1} {VALUE_2} {VALUE_3} {VALUE_4}</span></p></body></html>"""
		Rem_5 ="""<html><head/><body><p><span style=" font-size:16pt; color:#ff0000;">{VALUE_1} {VALUE_2} {VALUE_3} {VALUE_4} {VALUE_5}</span></p></body></html>"""
		if Counter > 10000:
			Counter = 0
		Counter += 1
		if Counter < 10:
			newRem = Rem_1.replace("{VALUE_1}", str(Counter))
			self.Top_Ctrl_frame4_body_metter.setText(newRem)
		elif Counter >= 10 and Counter < 100:
			newRem = Rem_2.replace("{VALUE_1}", str(Counter//10)).replace("{VALUE_2}", str(Counter%10))
			self.Top_Ctrl_frame4_body_metter.setText(newRem)
		elif Counter >= 100 and Counter < 1000:
			newRem = Rem_3.replace("{VALUE_1}", str(Counter//100)).replace("{VALUE_2}", str(Counter//10%10)).replace("{VALUE_3}", str(Counter%10))
			self.Top_Ctrl_frame4_body_metter.setText(newRem)
		elif Counter >= 1000 and Counter < 10000:
			newRem = Rem_4.replace("{VALUE_1}", str(Counter//1000)).replace("{VALUE_2}", str(Counter//100%10)).replace("{VALUE_3}", str(Counter//10%10)).replace("{VALUE_4}", str(Counter%10))
			self.Top_Ctrl_frame4_body_metter.setText(newRem)
		elif Counter >= 10000 and Counter < 100000:
			newRem = Rem_4.replace("{VALUE_1}", str(Counter//10000)).replace("{VALUE_2}", str(Counter//1000%10)).replace("{VALUE_3}", str(Counter//100%10)).replace("{VALUE_4}", str(Counter//10%10)).replace("{VALUE_5}", str(Counter%10))
			self.Top_Ctrl_frame4_body_metter.setText(newRem)


# #=========================================================================================== thời tiết ================================================================================

	def weather(self):
		today = date.today()
		days=["T2","T3","T4","T5","T6","T7","CN"]
		dayNumber=today.weekday()
		print(days[dayNumber])

		_translate = QtCore.QCoreApplication.translate
		api_address='https://api.openweathermap.org/data/2.5/weather?lat=10.850145464871641&lon=106.7716601973813&appid=59e434bde2d8ff7f30cfdb363d79aa61&lang=vi'
		json_data = requests.get(api_address).json()
		format_add = json_data['main']

		T_weather = """<html><head/><body><p><span style=" font-size:18pt; color:#ff0808;">{VALUE}</span><span style=" font-size:18pt; color:#ff0808; vertical-align:super;">0</span><span style=" font-size:18pt; color:#ff0808;">C</span></p></body></html>"""
		Value_1 = str(int(format_add["temp"]-273))

		new_T_Weather = T_weather.replace("{VALUE}",Value_1)
		self.T_Weather_label.setText(new_T_Weather)

		# rem = json_data['main']['humidity']
		# ram = json_data['weather'][0]['description']
		print(json_data["weather"][0]["icon"])

		#============================== thu ngay ===================================

		if dayNumber == 0:
			self.T2.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			self.T2.setText(days[dayNumber])
			self.T3.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			day = str(today.day) + "/" + str(today.month)
			self.T3.setText(day)


		elif dayNumber == 1:
			self.T3.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			self.T3.setText(days[dayNumber])
			self.T4.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			day = str(today.day) + "/" + str(today.month)
			self.T4.setText(day)


		elif dayNumber == 3:
			self.T4.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			self.T4.setText(days[dayNumber])
			self.T5.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			day = str(today.day) + "/" + str(today.month)
			self.T5.setText(day)


		elif dayNumber == 4:
			self.T5.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			self.T5.setText(days[dayNumber])
			self.T6.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			day = str(today.day) + "/" + str(today.month)
			self.T6.setText(day)

		elif dayNumber == 5:
			self.T6.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			self.T6.setText(days[dayNumber])
			self.T7.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			day = str(today.day) + "/" + str(today.month)
			self.T7.setText(day)


		elif dayNumber == 6:
			self.T7.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			self.T7.setText(days[dayNumber])
			self.CN.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			day = str(today.day) + "/" + str(today.month)
			self.CN.setText(day)

		#============================== Thoi tiet ==================================


		if json_data['weather'][0]['main'] == 'Rain':
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap(":/Weather/animated/rainy-7.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.pushButton_3.setIcon(icon)
			text_do_am = """<html><head/><body><p><span style=" font-size:18pt; color:#3ec5ff;">{VALUE_D}%</span></p></body></html>"""
			new_text_do_am = text_do_am.replace("{VALUE_D}",str(format_add["humidity"]))
			self.pushButton_3.setIcon(icon)
			self.T_Do_Am_label_2.setText(new_text_do_am)
			self.pushButton_6.setText(_translate("MainWindow", "Mưa gòi :'("))

		elif json_data['weather'][0]['main'] == 'Thunderstorm':
			text_do_am = """<html><head/><body><p><span style=" font-size:18pt; color:#3ec5ff;">{VALUE_D}%</span></p></body></html>"""
			new_text_do_am = text_do_am.replace("{VALUE_D}",str(format_add["humidity"]))
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap(":/Weather/animated/thunder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.pushButton_3.setIcon(icon)
			self.T_Do_Am_label_2.setText(new_text_do_am)
			self.pushButton_6.setText(_translate("MainWindow", "Sét đánh vở đầu"))


		elif json_data['weather'][0]['main'] == 'Clouds':
			text_do_am = """<html><head/><body><p><span style=" font-size:18pt; color:#3ec5ff;">{VALUE_D}%</span></p></body></html>"""
			new_text_do_am = text_do_am.replace("{VALUE_D}",str(format_add["humidity"]))
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap(":/Weather/animated/cloudy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.pushButton_3.setIcon(icon)
			self.T_Do_Am_label_2.setText(new_text_do_am)
			self.pushButton_6.setText(_translate("MainWindow", "Nhiều may"))
		#print(json_data)
		print("Thời Tiết thì  {0} Nhiệt độ thấp nhất là {1} Nhiệt độ cao nhất là {2} Độ C".format(
		json_data['weather'][0]['main'],float(format_add['temp_min']-273),float(format_add['temp_max']-273)))
