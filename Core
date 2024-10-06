from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

app = QApplication([])

# Creates the main window as a QWidget
window = QWidget()
# Sets the title of the window
window.setWindowTitle("Cool Pokemon App")
window.setGeometry(100, 100, 600, 400)

# Setting a custom color palette for the window 
palette = QPalette()
# Sets the background color of the window to a dark blue-gray color
palette.setColor(QPalette.Window, QColor("#2c3e50"))
# Sets the text color for the window to white
palette.setColor(QPalette.WindowText, Qt.white)
# Apply a custom palette to the window
window.setPalette(palette)

# Creates a QLabel to display a welcome message
label = QLabel("Welcome to the Pokemon App!")
# Sets the font of the label to Arial, with a size of 24
label.setFont(QFont('Arial', 24))
# Sets the style of the label with custom CSS-like styling
# The label's text color is set to white, and margin is added for spacing
label.setStyleSheet("color: white; margin: 20px;")

# Creates a QPushButton with the label "Click Me
button = QPushButton("Click Me")
# Set custom styling for the button using CSS-like syntax
button.setStyleSheet("""
    QPushButton {
        background-color: #3498db;  
        color: white;                
        padding: 10px;               
        border-radius: 5px;          
        font-size: 18px;             
    }
    QPushButton:hover {              
        background-color: #2980b9;   
    }
""")

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)
window.show()

# Starts the application event loop
app.exec_()
