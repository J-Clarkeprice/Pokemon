import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QStackedWidget,
    QHBoxLayout,
    QTextEdit,
    QComboBox,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Sets up the main window properties
        self.setWindowTitle("Cool Pokemon App")
        self.setGeometry(100, 100, 600, 400)

        # Sets a custom color palette for the application
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#2c3e50"))
        palette.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(palette)

        # Creates a QStackedWidget to manage different screens in the application
        self.stacked_widget = QStackedWidget(self)

        # Creates the main menu screen
        self.main_menu_widget = QWidget()
        self.setup_main_menu()

        # Adds the main menu screen to the stacked widget
        self.stacked_widget.addWidget(self.main_menu_widget)

        # Sets the layout for the main window to include the stacked widget
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

    def setup_main_menu(self):
        layout = QVBoxLayout()

        label = QLabel("Welcome to the Pokemon App!")
        label.setFont(QFont('Arial', 24))
        label.setStyleSheet("color: white; margin: 20px;")
        layout.addWidget(label)
        layout.addStretch()

        search_button = QPushButton("Search Pokémon")
        search_button.clicked.connect(self.show_search_screen)
        layout.addWidget(search_button)

        other_button1 = QPushButton("Other Feature 1")
        other_button1.clicked.connect(lambda: self.show_other_screen(1))
        layout.addWidget(other_button1)

        other_button2 = QPushButton("Other Feature 2")
        other_button2.clicked.connect(lambda: self.show_other_screen(2))
        layout.addWidget(other_button2)

        other_button3 = QPushButton("Other Feature 3")
        other_button3.clicked.connect(lambda: self.show_other_screen(3))
        layout.addWidget(other_button3)

        self.main_menu_widget.setLayout(layout)

    def setup_search_screen(self):
        search_widget = QWidget()
        layout = QVBoxLayout()

        # Create a horizontal layout for the label and search bar
        search_layout = QHBoxLayout()

        search_label = QLabel("Search for Pokémon by ID or Name:")
        search_label.setFont(QFont('Arial', 18))
        search_label.setStyleSheet("color: white; margin: 20px;")

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Enter Pokémon ID or Name")

        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_bar)
        search_layout.addStretch()

        search_button = QPushButton("Search by ID/Name")
        search_button.clicked.connect(self.search_pokemon)

        # Combo box for selecting Pokémon type
        self.type_combo_box = QComboBox()
        self.type_combo_box.addItem("Select Pokémon Type")
        pokemon_types = ['Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Flying',
                         'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Dragon',
                         'Dark', 'Fairy', 'Normal', 'Psychic']
        self.type_combo_box.addItems(pokemon_types)

        type_search_button = QPushButton("Search by Type")
        type_search_button.clicked.connect(self.search_pokemon_by_type)

        layout.addLayout(search_layout)
        layout.addWidget(search_button)
        layout.addWidget(self.type_combo_box)
        layout.addWidget(type_search_button)

        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)
        layout.addWidget(self.results_display)

        layout.addStretch()

        back_button = QPushButton("Back to Main Menu")
        back_button.clicked.connect(self.show_main_menu)
        layout.addWidget(back_button)

        search_widget.setLayout(layout)
        self.stacked_widget.addWidget(search_widget)
        self.stacked_widget.setCurrentWidget(search_widget)

    def search_pokemon(self):
        search_query = self.search_bar.text().strip()
        conn = sqlite3.connect('Data.db')  # Replace with your .db file path
        cursor = conn.cursor()

        # Adjusting the query to ignore case by using UPPER
        query = "SELECT * FROM Pokemon WHERE UPPER(ID) = UPPER(?) OR UPPER(Name) = UPPER(?)"
        cursor.execute(query, (search_query, search_query))

        results = cursor.fetchall()
        conn.close()

        if results:
            display_text = ""
            for row in results:
                display_text += f"ID: {row[0]}, Name: {row[1]}, Type: {row[2]}, Total: {row[3]}, HP: {row[4]}, Attack: {row[5]}, Def: {row[6]}, SpAtk: {row[7]}, SpDef: {row[8]}, Speed: {row[9]}, Evolution: {row[10]}\n"
            self.results_display.setPlainText(display_text)
        else:
            self.results_display.setPlainText("No Pokémon found.")

    def search_pokemon_by_type(self):
        selected_type = self.type_combo_box.currentText()

        if selected_type == "Select Pokémon Type":
            self.results_display.setPlainText("Please select a valid Pokémon type.")
            return

        conn = sqlite3.connect('Data.db')  # Replace with your .db file path
        cursor = conn.cursor()

        # Search for Pokémon by type
        query = "SELECT * FROM Pokemon WHERE Type = ?"
        cursor.execute(query, (selected_type,))

        results = cursor.fetchall()
        conn.close()

        if results:
            display_text = ""
            for row in results:
                display_text += f"ID: {row[0]}, Name: {row[1]}, Type: {row[2]}, Total: {row[3]}, HP: {row[4]}, Attack: {row[5]}, Def: {row[6]}, SpAtk: {row[7]}, SpDef: {row[8]}, Speed: {row[9]}, Evolution: {row[10]}\n"
            self.results_display.setPlainText(display_text)
        else:
            self.results_display.setPlainText("No Pokémon found of the selected type.")

    def show_search_screen(self):
        self.setup_search_screen()

    def show_main_menu(self):
        self.stacked_widget.setCurrentWidget(self.main_menu_widget)

    def show_other_screen(self, feature_number):
        feature_widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel(f"Feature {feature_number} is under construction.")
        label.setFont(QFont('Arial', 24))
        label.setStyleSheet("color: white; margin: 20px;")
        layout.addWidget(label)
        layout.addStretch()

        back_button = QPushButton("Back to Main Menu")
        back_button.clicked.connect(self.show_main_menu)
        layout.addWidget(back_button)
        layout.addStretch()

        feature_widget.setLayout(layout)
        self.stacked_widget.addWidget(feature_widget)
        self.stacked_widget.setCurrentWidget(feature_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
