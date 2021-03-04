import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets

from predictor_ui import Ui_MainWindow

class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.importFromFileAction.triggered.connect(self.open_file)
        self.predictAction.triggered.connect(self.switch_to_predict)
        self.seriesPredictAction.triggered.connect(self.switch_to_seriesPredict)

    def open_file(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, '选取文件', os.getcwd(), "CSV Files(*.csv)")
        print(fileName, fileType)
    
    def switch_to_predict(self):
        self.stackedWidget.setCurrentWidget(self.predictPage)

    def switch_to_seriesPredict(self):
        self.stackedWidget.setCurrentWidget(self.seriesPredictPage)


def main():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()