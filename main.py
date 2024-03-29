import sys
 
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QLineEdit, QMessageBox
from PySide2.QtCore import QFile, QObject
 
class Form(QObject):
 
    def __init__(self, ui_file, parent=None):
        super(Form, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
 
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
 
        self.line = self.window.findChild(QLineEdit, 'lineEdit')
 
        btn = self.window.findChild(QPushButton, 'pushButton')
        btn.clicked.connect(self.ok_handler)
        self.window.show()
 
    def ok_handler(self):
        msgBox = QMessageBox()
        msgBox.setText(self.line.text())
        msgBox.exec_()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form('mainwindow.ui')
    sys.exit(app.exec_())

