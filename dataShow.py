import sys
import readData
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication,
                             QLabel, QInputDialog)
from PyQt5.QtGui import QIcon
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(500,500,500,550)
        self.setWindowTitle('中国天气信息查询') #此处描述界面
        self.setWindowIcon(QIcon('amg.jpg'))

        self.lb1 = QLabel('城市',self)
        self.lb1.move(20,20)#此处表示城市界面

        self.lb2 = QLabel('北京',self)
        self.lb2.move(80,20)

        self.lb3 = QLabel('温度',self)
        self.lb3.move(20,80)

        self.lb4 = QLabel('0    ',self)#注意这里的空格应该尽量多，才能显示更多的数据。
        self.lb4.move(80,80)#温度中的度数

        self.lb5 = QLabel('度',self)
        self.lb5.move(130,80)#温度中的度数

        self.lb6 = QLabel('温差',self)
        self.lb6.move(20,120)

        self.lb7 = QLabel('0   ',self)
        self.lb7.move(80,120)

        self.lb8 = QLabel('度',self)
        self.lb8.move(130,120)

        self.bt1 = QPushButton('查询温度',self)
        self.bt1.move(200,20)

        self.bt2 = QPushButton('查询温差',self)
        self.bt2.move(200,80)

        self.show()
        #单击按钮连接对应的槽函数
        self.bt1.clicked.connect(self.showDialog)
        self.bt2.clicked.connect(self.showDialog)

    def showDialog(self):
        sender = self.sender()

        if sender == self.bt1:
            text, ok = QInputDialog.getText(self, '查询温度','请输入城市:')
            tem = readData.readCity('D:\\PycharmProjects\\MySpider\\temprature.txt',text)
            if ok:
                self.lb2.setText(text)
                self.lb4.setText(str(tem))
        elif sender == self.bt2:
            text, ok = QInputDialog.getText(self, '查询温差','请输入城市:')
            wencha = readData.readCity('D:\\PycharmProjects\\MySpider\\wencha.txt',text)
            if ok:
                self.lb2.setText(text)
                self.lb7.setText(str(wencha))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())