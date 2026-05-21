import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class MainWindow(QMainWindow):
    def button_clicked(self):
        self.ui.label.setText("hello world")
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        ui_file = QFile("Pomedoro.ui")
        ui_file.open(QFile.ReadOnly)
        
        self.ui = loader.load(ui_file,self)

        print(self.ui)
        ui_file.close()

        self.setCentralWidget(self.ui)

        self.ui.pushButton.clicked.connect(self.button_clicked)




app = QApplication(sys.argv)

window = MainWindow()
window.ui.show()

sys.exit(app.exec())
