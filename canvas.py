from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd
#pip install openpyxl
#pip3 install xlrd

xl = pd.ExcelFile('D:/M4T/4T_main_end/data/chart.xlsx')
df = pd.read_excel(xl, 0, header=None)


class Canvas_grafica(FigureCanvas) :
    def __init__(self):
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(1, 1), 
            sharey=True, facecolor='white') #khởi tạo 1 subplots API hướng đối tượng để vẻ các đồ thị phức tạo, figsize tùy chỉnh độ dài rộng của đồ thị fig là hình lớn tổng còn ax là các hình nhỏ đc vẻ lên
        super().__init__(self.fig)
        self.a = []
        self.data = df.head(1)
        for i in self.data:
            self.a.append(self.data[i])

        self.rem = [1, 2, 3, 4, 5, 6, 7, 8] # rem là chiều ngang

        self.ram = self.data # ram là chiều dọc
        self.i = self.ram[0]
        self.ram.pop(7) # xóa 1 phần tử trong list

        # self.fig.suptitle("REM", size = 9) #đặt tên cho hình chính

        self.ax.plot(self.rem, self.a, marker = ".", markersize = 20)
        # self.ax.plot(rem, ram)

class Canvas_grafica_1(FigureCanvas) :
    def __init__(self):
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(1, 1), 
            sharey=True, facecolor='white') #khởi tạo 1 subplots API hướng đối tượng để vẻ các đồ thị phức tạo, figsize tùy chỉnh độ dài rộng của đồ thị fig là hình lớn tổng còn ax là các hình nhỏ đc vẻ lên
        super().__init__(self.fig)
        self.a = []
        self.data = df.head(1)
        for i in self.data:
            self.a.append(self.data[i])

        self.rem = [1, 2, 3, 4, 5, 6, 7, 8] # rem là chiều ngang

        self.ram = self.data # ram là chiều dọc
        self.i = self.ram[0]
        self.ram.pop(7) # xóa 1 phần tử trong list

        # self.fig.suptitle("REM", size = 9) #đặt tên cho hình chính

        self.ax.plot(self.rem, self.a, marker = ".", markersize = 20)
        # self.ax.plot(rem, ram)

class Canvas_grafica_2(FigureCanvas) :
    def __init__(self):
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(1, 1), 
            sharey=True, facecolor='white') #khởi tạo 1 subplots API hướng đối tượng để vẻ các đồ thị phức tạo, figsize tùy chỉnh độ dài rộng của đồ thị fig là hình lớn tổng còn ax là các hình nhỏ đc vẻ lên
        super().__init__(self.fig)
        self.a = []
        self.data = df.head(1)
        for i in self.data:
            self.a.append(self.data[i])

        self.rem = [1, 2, 3, 4, 5, 6, 7, 8] # rem là chiều ngang

        self.ram = self.data # ram là chiều dọc
        self.i = self.ram[0]
        self.ram.pop(7) # xóa 1 phần tử trong list

        # self.fig.suptitle("REM", size = 9) #đặt tên cho hình chính

        self.ax.plot(self.rem, self.a, marker = ".", markersize = 20)
        # self.ax.plot(rem, ram)

class Canvas_grafica_3(FigureCanvas) :
    def __init__(self):
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(1, 1), 
            sharey=True, facecolor='white') #khởi tạo 1 subplots API hướng đối tượng để vẻ các đồ thị phức tạo, figsize tùy chỉnh độ dài rộng của đồ thị fig là hình lớn tổng còn ax là các hình nhỏ đc vẻ lên
        super().__init__(self.fig)
        self.rem = [1, 2, 3, 4, 5, 6, 7, 8] # rem là chiều ngang 
        self.ram = [15, 15, 30, 1, 5, 53, 10, 12] # ram là chiều dọc
        self.i = self.ram[0]
        self.ram.insert(0, self.i) # chèn 1 phần tử vào list
        self.ram.pop(7) # xóa 1 phần tử trong list

        self.fig.suptitle("REM", size = 9) #đặt tên cho hình chính

        self.ax.plot(self.rem, self.ram, marker = ".", markersize = 20)
        # self.ax.plot(rem, ram)