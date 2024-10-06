from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QStackedWidget,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Sets up the main window properties
        self.setWindowTitle("Cool Pokemon App")  # Title of the application window
        self.setGeometry(100, 100, 600, 400)  # Position and size of the window

        # Sets a custom color palette for the application
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#2c3e50"))  # Dark blue-gray background color
        palette.setColor(QPalette.WindowText, Qt.white)  # White text color
        self.setPalette(palette)  # Apply the color palette to the window

        # Creates a QStackedWidget to manage different screens in the application
        self.stacked_widget = QStackedWidget(self)

        # Creates the main menu screen
        self.main_menu_widget = QWidget()
        self.setup_main_menu()  # Set up the main menu layout

        # Adds the main menu screen to the stacked widget
        self.stacked_widget.addWidget(self.main_menu_widget)

        # Sets the layout for the main window to include the stacked widget
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

    def setup_main_menu(self):
        layout = QVBoxLayout()  # Creates a vertical layout for the main menu

        # Creates and style the welcome label
        label = QLabel("Welcome to the Pokemon App!")
        label.setFont(QFont('Arial', 24))  # Set font style and size
        label.setStyleSheet("color: white; margin: 20px;")  # Set text color and margin
        layout.addWidget(label)  # Add the label to the layout

        # Creates a button for searching Pokémon
        search_button = QPushButton("Search Pokémon")
        search_button.clicked.connect(self.show_search_screen)  # Connect button click to the search function
        layout.addWidget(search_button)  # Add button to the layout

        # Creates buttons for other features
        other_button1 = QPushButton("Other Feature 1")
        other_button1.clicked.connect(lambda: self.show_other_screen(1))  # Navigate to feature 1
        layout.addWidget(other_button1)

        other_button2 = QPushButton("Other Feature 2")
        other_button2.clicked.connect(lambda: self.show_other_screen(2))  # Navigate to feature 2
        layout.addWidget(other_button2)

        other_button3 = QPushButton("Other Feature 3")
        other_button3.clicked.connect(lambda: self.show_other_screen(3))  # Navigate to feature 3
        layout.addWidget(other_button3)

        self.main_menu_widget.setLayout(layout)  # Sets the layout for the main menu widget

    def setup_search_screen(self):
        search_widget = QWidget()  # Creates a new widget for the search screen
        layout = QVBoxLayout()  # Creates a vertical layout for the search screen

        # Creates and style the search label
        search_label = QLabel("Search for Pokémon by ID or Name:")
        search_label.setFont(QFont('Arial', 18))  # Set font style and size
        search_label.setStyleSheet("color: white; margin: 20px;")  # Set text color and margin
        layout.addWidget(search_label)  # Add the label to the layout

        # Creates a search bar for user input
        self.search_bar = QLineEdit()  # Creates a line edit for search input
        self.search_bar.setPlaceholderText("Enter Pokémon ID or Name")  # Set placeholder text
        layout.addWidget(self.search_bar)  # Adds the search bar to the layout

        # Creates a back button to return to the main menu
        back_button = QPushButton("Back to Main Menu")
        back_button.clicked.connect(self.show_main_menu)  # Connecst button click to return function
        layout.addWidget(back_button)  # Adds the back button to the layout

        search_widget.setLayout(layout)  # Sets the layout for the search widget
        self.stacked_widget.addWidget(search_widget)  # Adds the new search widget to the stacked widget
        self.stacked_widget.setCurrentWidget(search_widget)  # Switchs to the search screen

    def show_search_screen(self):
        self.setup_search_screen()  # Creates and set up a new search screen instance

    def show_main_menu(self):
        self.stacked_widget.setCurrentWidget(self.main_menu_widget)  # Switchs back to the main menu

    def show_other_screen(self, feature_number):
        feature_widget = QWidget()  # Creates a new widget for the feature screen
        layout = QVBoxLayout()  # Creates a vertical layout for the feature screen
        
        # Creates a label indicating that the feature is under construction
        label = QLabel(f"Feature {feature_number} is under construction.")
        label.setFont(QFont('Arial', 24))  # Sets font style and size
        label.setStyleSheet("color: white; margin: 20px;")  # Sets text color and margin
        
        layout.addWidget(label)  # Adds the label to the layout
        
        # Creates a back button for returning to the main menu
        back_button = QPushButton("Back to Main Menu")
        back_button.clicked.connect(self.show_main_menu)  # Connect button click to return function
        layout.addWidget(back_button)  # Adds the back button to the layout
        
        # Creates a button to go to the screens that are under constrution
        feature_widget.setLayout(layout)  # Sets the layout for the feature widget
        self.stacked_widget.addWidget(feature_widget)  # Adds the new feature widget to the stacked widget
        self.stacked_widget.setCurrentWidget(feature_widget)  # Switchs to the feature screen

if __name__ == "__main__":
    app = QApplication([])  # Creates the application
    window = MainWindow()  # Creates an instance of the main window
    window.show()  # Show the main window
    app.exec_()  # Start the application event loop
