import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from baidu import BaiDuAPI

class filedialogdemo(QWidget):

    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)
        layout = QVBoxLayout()

        self.filepath=None
        # Create a button in the window
        #self.button = QPushButton('Show text', self)
        #self.button.move(10, 50)
        #self.button.resize(80, 20)
        self.button = QPushButton()
        #self.button.clicked.connect(self.loadFile)
        self.button.setText("show name")
        layout.addWidget(self.button)

        #QWidget().resize(620, 240)
        # Create textbox
        #self.textbox = QLineEdit(self)
        #self.textbox.move(10, 75)
        #self.textbox.resize(280, 20)
        #layout.addWidget(self.resize)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)

        self.btn = QPushButton()
        self.btn.clicked.connect(self.loadFile)
        self.btn.setText("从文件中获取照片")
        layout.addWidget(self.btn)

        self.label = QLabel()
        layout.addWidget(self.label)

        #self.content = QTextEdit()
        #layout.addWidget(self.content)
        self.setWindowTitle("Hawkeye")

        self.setLayout(layout)

    def loadFile(self):
        global filepath
        print("load--file")
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'F:\github_repository\python-deep-learning-basics', 'Image files(*.jpg *.gif *.png)')
        self.label.setPixmap(QPixmap(fname))
        self.filepath = fname
        #print(self.filepath)
        return self.filepath

    @pyqtSlot()
    def on_click(self):
        #textboxValue = self.textbox.text()
        #QMessageBox.question(self, 'Message', "这是: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        #QMessageBox.question(self, 'Message', "这是: " + textboxValue)
        #self.textbox.setText("")
        #print(self.filepath)
        baiduapi = BaiDuAPI('passwd.ini')
        # plant.png
        QMessageBox.question(self, '植物名称', "This is: " + baiduapi.picture2Name(self.filepath)[0], QMessageBox.Ok,QMessageBox.Ok)
        #return textboxValue

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #print(filedialogdemo.on_click())
    fileload =  filedialogdemo()
    fileload.show()
    sys.exit(app.exec_())