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

    def setup_search_screen(self):
        search_widget = QWidget()
        layout = QVBoxLayout()
        self.reset_button_styles()

        # Creates a horizontal layout for the label, search bar, buttons, and combo box
        search_layout = QHBoxLayout()

        search_label = QLabel("Search for Pokémon by ID or Name:")
        search_label.setFont(QFont('Arial', 18))
        search_label.setStyleSheet("color: white; margin: 20px;")

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Enter Pokémon ID or Name")
        self.search_bar.setFixedWidth(250)
        self.search_bar.setStyleSheet("background-color: white; color: black;")

        # Button to search by ID/Name
        search_button = QPushButton("Search by ID/Name")
        search_button.setFixedWidth(150)
        search_button.clicked.connect(self.search_pokemon)

        # Combo box for selecting Pokémon type
        self.type_combo_box = QComboBox()
        self.type_combo_box.addItem("Select Pokémon Type")
        pokemon_types = ['Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Flying',
                         'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Dragon',
                         'Dark', 'Fairy', 'Normal', 'Psychic']
        self.type_combo_box.addItems(pokemon_types)
        self.type_combo_box.setFixedWidth(200)
        self.type_combo_box.setStyleSheet("background-color: white; color: black;")

        # Button to search by type
        type_search_button = QPushButton("Search by Type")
        type_search_button.setFixedWidth(150)
        type_search_button.clicked.connect(self.search_pokemon_by_type)

        # Add widgets to the search layout in the desired order
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(search_button)
        search_layout.addWidget(self.type_combo_box)
        search_layout.addWidget(type_search_button)
        search_layout.addStretch()

        layout.addLayout(search_layout)  # Add the horizontal search layout

        # Add navigation arrow buttons
        navigation_layout = QHBoxLayout()

        # Left arrow button (previous Pokémon)
        self.left_arrow_button = QPushButton("←")
        self.left_arrow_button.setFixedWidth(50)
        self.left_arrow_button.clicked.connect(self.show_previous_pokemon)
        navigation_layout.addWidget(self.left_arrow_button)

        # Right arrow button (next Pokémon)
        self.right_arrow_button = QPushButton("→")
        self.right_arrow_button.setFixedWidth(50)
        self.right_arrow_button.clicked.connect(self.show_next_pokemon)
        navigation_layout.addWidget(self.right_arrow_button)

        layout.addLayout(navigation_layout)

        # Display area for search results
        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)
        self.results_display.setStyleSheet("background-color: white; color: black;")
        layout.addWidget(self.results_display)
        
        layout.addStretch()

        back_button = QPushButton("Back to Main Menu")
        back_button.clicked.connect(self.show_main_menu)
        layout.addWidget(back_button)

        search_widget.setLayout(layout)
        self.stacked_widget.addWidget(search_widget)
        self.stacked_widget.setCurrentWidget(search_widget)

        # Initialize current Pokémon ID tracker
        self.current_pokemon_id = 1

    def show_previous_pokemon(self):
        if self.current_pokemon_id > 1:  # Prevent going below ID 1
            self.current_pokemon_id -= 1
            self.fetch_pokemon_by_id(self.current_pokemon_id)
        else:
            self.results_display.setPlainText("This is the first Pokémon.")

    def show_next_pokemon(self):
        conn = sqlite3.connect('Data.db')
        cursor = conn.cursor()
    
        # Find the max ID in the database
        cursor.execute("SELECT MAX(ID) FROM Pokemon")
        max_id = cursor.fetchone()[0]
        conn.close()

        if self.current_pokemon_id < max_id:  # Prevent going past the last Pokémon
            self.current_pokemon_id += 1
            self.fetch_pokemon_by_id(self.current_pokemon_id)
        else:
            self.results_display.setPlainText("This is the last Pokémon.")

    def fetch_pokemon_by_id(self, pokemon_id):
        conn = sqlite3.connect('Data.db')
        cursor = conn.cursor()

        # Fetch Pokémon by ID
        query = "SELECT * FROM Pokemon WHERE ID = ?"
        cursor.execute(query, (pokemon_id,))
        result = cursor.fetchone()
        conn.close()

        if result:
            display_text = (f"ID: {result[0]}, Name: {result[1]}, Type: {result[2]}, Total: {result[3]}, "
                            f"HP: {result[4]}, Attack: {result[5]}, Defense: {result[6]}, SpAtk: {result[7]}, "
                            f"SpDef: {result[8]}, Speed: {result[9]}, Evolution: {result[10]}")
            self.update_palette_for_type(result[2])
            self.results_display.setPlainText(display_text)
        else:
            self.results_display.setPlainText(f"No Pokémon found with ID {pokemon_id}.")

    def reset_button_styles(self):
        # Resets the style of buttons to default for all buttons in the current window
        buttons = self.findChildren(QPushButton)
        for button in buttons:
            button.setStyleSheet("color: black; background-color: #f0f0f0;")

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

        self.reset_button_styles()

    def reset_to_default_palette(self):
        self.setStyleSheet("background-color: #2c3e50;")
        self.reset_button_styles()
        
    def reset_button_styles(self):
        buttons = self.findChildren(QPushButton)
        for button in buttons:
            button.setStyleSheet("color: black; background-color: #f0f0f0;")
        
    def search_pokemon(self):
        search_query = self.search_bar.text().strip()
        conn = sqlite3.connect('Data.db')  # Connects to the data base
        cursor = conn.cursor()

        if search_query.isdigit():
            pokemon_id = int(search_query)
            self.fetch_pokemon_by_id(pokemon_id)
            # Update current Pokémon ID to the searched one
            self.current_pokemon_id = pokemon_id
        else:
            self.fetch_pokemon_by_name(query)

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
            self.pokemon_image_label.clear()
            
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
        self.reset_button_styles()

        # Creates a horizontal layout for the search bar, buttons, and combo box
        search_layout = QHBoxLayout()

        search_label = QLabel("Search for Moves by Name:")
        search_label.setFont(QFont('Arial', 18))
        search_label.setStyleSheet("color: white; margin: 20px;")

        self.move_search_bar = QLineEdit()
        self.move_search_bar.setPlaceholderText("Enter Move Name")
        self.move_search_bar.setFixedWidth(250)
        self.move_search_bar.setStyleSheet("background-color: white; color: black;")

        # Button to search by move name
        search_button = QPushButton("Search by Name")
        search_button.setFixedWidth(150)
        search_button.clicked.connect(self.search_moves_by_name)

        # Combo box for selecting move type
        self.move_type_combo_box = QComboBox()
        self.move_type_combo_box.addItem("Select Move Type")
        move_types = ['Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Flying',
                      'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Dragon',
                      'Dark', 'Fairy', 'Normal', 'Psychic']
        self.move_type_combo_box.addItems(move_types)
        self.move_type_combo_box.setFixedWidth(200)
        self.move_type_combo_box.setStyleSheet("background-color: white; color: black;")

        # Button to search by move type
        type_search_button = QPushButton("Search by Type")
        type_search_button.setFixedWidth(150)
        type_search_button.clicked.connect(self.search_moves_by_type)

        # Add widgets to the search layout in the desired order
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.move_search_bar)
        search_layout.addWidget(search_button)
        search_layout.addWidget(self.move_type_combo_box)
        search_layout.addWidget(type_search_button)
        search_layout.addStretch()

        layout.addLayout(search_layout)  # Add the horizontal search layout

        # Display area for move search results
        self.move_results_display = QTextEdit()
        self.move_results_display.setReadOnly(True)
        self.move_results_display.setStyleSheet("background-color: white; color: black;")
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
        self.reset_to_default_palette()

    def show_search_screen(self):
        self.setup_search_screen()
        self.reset_to_default_palette()
        
    def show_main_menu(self):
        self.reset_to_default_palette()
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
