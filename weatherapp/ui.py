from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLineEdit, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Weather App")
        
        button = QPushButton("Start")
        button.clicked.connect(self.ask_city)
        
        self.setCentralWidget(button)
        
        
    def ask_city(self):
        
        city_selector = QHBoxLayout()
        
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Enter city name")
        line_edit.returnPressed.connect(self.get_city_name)
        self.setCentralWidget(line_edit)
        
        city_selector.addWidget(line_edit)
        
        self.setCentralWidget(city_selector)
        
    
    
    def get_city_name(self, city_name):
        print(city_name)
        return city_name
        
                
app = QApplication()

window = MainWindow()

window.show()
app.exec()