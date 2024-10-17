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

        # Define colors for different Pokémon types
        self.type_colors = {
            "Fire": "#FF4500",  # Red-orange
            "Water": "#1E90FF",  # Blue
            "Grass": "#32CD32",  # Green
            "Electric": "#FFD700",  # Yellow
            "Ice": "#ADD8E6",  # Light Blue
            "Fighting": "#8B0000",  # Dark Red
            "Flying": "#87CEEB",  # Sky Blue
            "Poison": "#9400D3",  # Purple
            "Ground": "#DEB887",  # Light Brown
            "Rock": "#A52A2A",  # Brown
            "Bug": "#9ACD32",  # Yellow-green
            "Ghost": "#4B0082",  # Indigo
            "Steel": "#B0C4DE",  # Light Steel Blue
            "Dragon": "#4682B4",  # Steel Blue
            "Dark": "#2F4F4F",  # Dark Slate Gray
            "Fairy": "#FFB6C1",  # Light Pink
            "Normal": "#D3D3D3",  # Light Gray
            "Psychic": "#FF69B4",  # Hot Pink
        }

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

        # Makes a banner to say welcome
        label = QLabel("Welcome to the Pokemon App!")
        label.setFont(QFont('Arial', 24))
        label.setStyleSheet("color: white; margin: 20px;")
        layout.addWidget(label)
        layout.addStretch()

        # Creates a button that takes you to the screen that searchs for Pokemon
        search_button = QPushButton("Search Pokémon")
        search_button.clicked.connect(self.show_search_screen)
        layout.addWidget(search_button)
        
        # Creates a button that takes you to the screen that searchs for Moves
        move_search_button = QPushButton("Search Moves")
        move_search_button.clicked.connect(self.show_move_search_screen)
        layout.addWidget(move_search_button)

        # Creates a button that takes you to the screen that searchs for screens that are under development
        other_button1 = QPushButton("Other Feature 1")
        other_button1.clicked.connect(lambda: self.show_other_screen(1))
        layout.addWidget(other_button1)

        # Creates a button that takes you to the screen that searchs for screens that are under development
        other_button2 = QPushButton("Other Feature 2")
        other_button2.clicked.connect(lambda: self.show_other_screen(2))
        layout.addWidget(other_button2)
        self.main_menu_widget.setLayout(layout)

    # This is the section of code that sets up the search screen for Pokemon
    # This is not the move search screen
    def setup_search_screen(self):
        search_widget = QWidget()
        layout = QVBoxLayout()

        # Creates a horizontal layout for the label and search bar
        search_layout = QHBoxLayout()
        search_label = QLabel("Search for Pokémon by ID or Name:")
        search_label.setFont(QFont('Arial', 18))
        search_label.setStyleSheet("color: white; margin: 20px;")

        # Creates the search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Enter Pokémon ID or Name")
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_bar)
        search_layout.addStretch()

        # This creates the button that allows you to execute the search function
        search_button = QPushButton("Search by ID/Name")
        search_button.clicked.connect(self.search_pokemon)

        # Creates drop down box for selecting Pokémon type
        self.type_combo_box = QComboBox()
        self.type_combo_box.addItem("Select Pokémon Type")
        pokemon_types = ['Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Flying',
                         'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Dragon',
                         'Dark', 'Fairy', 'Normal', 'Psychic']
        self.type_combo_box.addItems(pokemon_types)

        # This creates the button that allows you to search for Pokemon by type
        type_search_button = QPushButton("Search by Type")
        type_search_button.clicked.connect(self.search_pokemon_by_type)

        layout.addLayout(search_layout)
        layout.addWidget(search_button)
        layout.addWidget(self.type_combo_box)
        layout.addWidget(type_search_button)

        # This is the section of code that creates a display to show the data that was searched for
        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)
        layout.addWidget(self.results_display)

        # This moves the buttons & search bars to their correct postioning when the application window size is changed
        layout.addStretch()

        back_button = QPushButton("Back to Main Menu")
        back_button.clicked.connect(self.show_main_menu)
        layout.addWidget(back_button)

        search_widget.setLayout(layout)
        self.stacked_widget.addWidget(search_widget)
        self.stacked_widget.setCurrentWidget(search_widget)


    def update_palette_for_type(self, pokemon_type):
        """Update the color palette based on Pokémon or Move type. Handles dual types as well."""
        
        if "/" in pokemon_type:  # Check for dual type
            types = pokemon_type.split("/")  # Split the dual types
            type1 = types[0].strip()
            type2 = types[1].strip()
            
            # Get colors for both types
            color1 = self.type_colors.get(type1, "#2c3e50")  # Default color if type not found
            color2 = self.type_colors.get(type2, "#2c3e50")
            
            # Apply a gradient background using the two colors
            self.setStyleSheet(f"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:1 {color2});")
        
        else:
            # Single type Pokémon, just apply the regular color
            color = self.type_colors.get(pokemon_type, "#2c3e50")  # Default color if type not found
            self.setStyleSheet(f"background-color: {color};")

    def search_pokemon(self):
        search_query = self.search_bar.text().strip()
        conn = sqlite3.connect('Data.db')  # Connects to the data base
        cursor = conn.cursor()

        # Searches for the pokemon.
        query = "SELECT * FROM Pokemon WHERE UPPER(ID) = UPPER(?) OR UPPER(Name) = UPPER(?)"
        cursor.execute(query, (search_query, search_query))

        results = cursor.fetchall()
        conn.close()

        if results:
            display_text = ""
            pokemon_type = results[0][2]
            self.update_palette_for_type(pokemon_type) # Change the background color to reflect the Pokémon type, including dual types
            for row in results:
                display_text += f"ID: {row[0]}, Name: {row[1]}, Type: {row[2]}, Total: {row[3]}, HP: {row[4]}, Attack: {row[5]}, Def: {row[6]}, SpAtk: {row[7]}, SpDef: {row[8]}, Speed: {row[9]}, Evolution: {row[10]}\n"
            self.results_display.setPlainText(display_text)
        else:
            self.results_display.setPlainText("No Pokémon found.")
            self.update_palette_for_type("")# Reset to default color if nothing is found
            
    def search_pokemon_by_type(self):
        selected_type = self.type_combo_box.currentText()

        if selected_type == "Select Pokémon Type":
            self.results_display.setPlainText("Please select a valid Pokémon type.")
            return

        conn = sqlite3.connect('Data.db')  # Connects to the data base
        cursor = conn.cursor()

        # Search for Pokémon by type
        query = "SELECT * FROM Pokemon WHERE Upper(Type) LIKE(?)"
        cursor.execute(query, (f'%{selected_type}%',))

        results = cursor.fetchall()
        conn.close()

        if results:
            display_text = ""
            pokemon_type = selected_type
            self.update_palette_for_type(pokemon_type)
            for row in results:
                display_text += f"ID: {row[0]}, Name: {row[1]}, Type: {row[2]}, Total: {row[3]}, HP: {row[4]}, Attack: {row[5]}, Def: {row[6]}, SpAtk: {row[7]}, SpDef: {row[8]}, Speed: {row[9]}, Evolution: {row[10]}\n"
            self.results_display.setPlainText(display_text)
        else:
            self.results_display.setPlainText("No Pokémon found of the selected type.")
            self.update_palette_for_type("")  # Reset to default color if nothing is found

    def setup_move_search_screen(self):
        move_search_widget = QWidget()
        layout = QVBoxLayout()

        # Creates a horizontal layout for the search bar
        search_layout = QHBoxLayout()

        search_label = QLabel("Search for Moves by Name:")
        search_label.setFont(QFont('Arial', 18))
        search_label.setStyleSheet("color: white; margin: 20px;")

        self.move_search_bar = QLineEdit()
        self.move_search_bar.setPlaceholderText("Enter Move Name")

        search_layout.addWidget(search_label)
        search_layout.addWidget(self.move_search_bar)
        search_layout.addStretch()

        search_button = QPushButton("Search by Name")
        search_button.clicked.connect(self.search_moves_by_name)

        # Creates the drop down box for selecting move type
        self.move_type_combo_box = QComboBox()
        self.move_type_combo_box.addItem("Select Move Type")
        move_types = ['Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Flying',
                      'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Dragon',
                      'Dark', 'Fairy', 'Normal', 'Psychic']
        self.move_type_combo_box.addItems(move_types)

        type_search_button = QPushButton("Search by Type")
        type_search_button.clicked.connect(self.search_moves_by_type)

        layout.addLayout(search_layout)
        layout.addWidget(search_button)
        layout.addWidget(self.move_type_combo_box)
        layout.addWidget(type_search_button)

        self.move_results_display = QTextEdit()
        self.move_results_display.setReadOnly(True)
        layout.addWidget(self.move_results_display)

        layout.addStretch()

        back_button = QPushButton("Back to Main Menu")
        back_button.clicked.connect(self.show_main_menu)
        layout.addWidget(back_button)

        move_search_widget.setLayout(layout)
        self.stacked_widget.addWidget(move_search_widget)
        self.stacked_widget.setCurrentWidget(move_search_widget)

    def search_moves_by_name(self):
        search_query = self.move_search_bar.text().strip()
        if not search_query:
            self.move_results_display.setPlainText("Please enter a move name.")
            return

        conn = sqlite3.connect('Data.db')  # Connects to the data base
        cursor = conn.cursor()

        # Searches for Moves
        query = "SELECT * FROM Moves WHERE UPPER(Name) = UPPER(?)"
        cursor.execute(query, (search_query,))

        results = cursor.fetchall()
        conn.close()

        if results:
            display_text = ""
            Move_type = results[0][1]
            self.update_palette_for_type(Move_type) # Change the background color to reflect the Pokémon type, including dual types
            for row in results:
                display_text += (f"Name: {row[0]}, Type: {row[1]}, Category: {row[2]}, "
                                f"Power: {row[3]}, Accuracy: {row[4]}, PP: {row[5]}\n")
            self.move_results_display.setPlainText(display_text)
        else:
            self.move_results_display.setPlainText("No move found.")
            self.update_palette_for_type("")  # Reset to default color if nothing is found

    def search_moves_by_type(self):
        selected_type = self.move_type_combo_box.currentText()

        if selected_type == "Select Move Type":
            self.move_results_display.setPlainText("Please select a valid move type.")
            return

        conn = sqlite3.connect('Data.db') 
        cursor = conn.cursor()

        # Search for moves by type
        query = "SELECT * FROM Moves WHERE Upper(Type) LIKE(?)"
        cursor.execute(query, (f'%{selected_type}%',))

        results = cursor.fetchall()
        conn.close()

        if results:
            display_text = ""
            Move_type = selected_type
            self.update_palette_for_type(Move_type)
            for row in results:
                display_text += f"Name: {row[0]}, Type: {row[1]}, Category: {row[2]}, Power: {row[3]}, Accuracy: {row[4]}, PP: {row[5]}\n"
            self.move_results_display.setPlainText(display_text)
        else:
            self.move_results_display.setPlainText("No moves found of the selected type.")
            self.update_palette_for_type("")  # Reset to default color if nothing is found

    def show_move_search_screen(self):
        self.setup_move_search_screen()

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
