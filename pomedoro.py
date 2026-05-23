import sys, os, time
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QTimer, QUrl
from PySide6.QtMultimedia import QSoundEffect


class MainWindow(QMainWindow):

    def button_clicked(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)
        return
    
    def button_clicked2(self):
        self.timer.stop()
        self.starting_minutes = 30
        self.starting_seconds = 0
        self.ui.lcdNumber.display(f"{self.starting_minutes:02d}:{self.starting_seconds:02d}")
        return



    def tick(self):
        if not self.starting_minutes and not self.starting_seconds:
            self.timer.stop()
            self.starting_minutes = 30
            self.starting_seconds = 0
            self.ui.lcdNumber.display(f"{self.starting_minutes:02d}:{self.starting_seconds:02d}")
            return
        else:
            if not self.starting_seconds:
                self.starting_minutes-=1
                self.starting_seconds=59
                self.ui.lcdNumber.display(f"{self.starting_minutes:02d}:{self.starting_seconds:02d}")
            else:
                self.starting_seconds-=1
                self.ui.lcdNumber.display(f"{self.starting_minutes:02d}:{self.starting_seconds:02d}")

            return



    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        ui_file = QFile("Pomedoro.ui")
        ui_file.open(QFile.ReadOnly)
        self.starting_minutes = 30
        self.starting_seconds = 0
        self.ui = loader.load(ui_file,self)
        ui_file.close()
        self.setCentralWidget(self.ui)
        self.ui.pushButton.clicked.connect(self.button_clicked)
        self.ui.lcdNumber.display(f"{self.starting_minutes:02d}:{self.starting_seconds:02d}")
        self.ui.pushButton_2.clicked.connect(self.button_clicked2)
        
       




app = QApplication(sys.argv)

window = MainWindow()
window.ui.show()

sys.exit(app.exec())
