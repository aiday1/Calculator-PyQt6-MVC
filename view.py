from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt6.QtGui import QFont


class CalculatorView(QWidget):
    def __init__(self):
        """Initialize the calculator GUI with improved styling."""
        super().__init__()

        # Set window properties
        self.setWindowTitle("MVC Calculator")
        self.setGeometry(100, 100, 320, 450)
        self.setStyleSheet("background-color: #2C3E50;")  # Dark background color

        # Create main layout
        layout = QVBoxLayout()

        # Create display field
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFont(QFont("Arial", 24))
        self.display.setStyleSheet(
            "background-color: white; padding: 15px; border-radius: 5px;"
            "color: black; font-size: 24px; text-align: right;"
        )
        layout.addWidget(self.display)

        # Create button grid layout
        grid_layout = QGridLayout()

        # Button labels
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0, 1, 4)  # 'C' spans across 4 columns
        ]

        # Dictionary to store button references
        self.buttons = {}

        # Create buttons and add to layout
        for text, row, col, *span in buttons:
            button = QPushButton(text)
            button.setFont(QFont("Arial", 20))
            button.setStyleSheet(
                "background-color: #34495E; color: white; padding: 15px;"
                "border-radius: 5px; font-size: 18px;"
            )
            if text in {'+', '-', '*', '/', '='}:
                button.setStyleSheet("background-color: #E67E22; color: white; font-size: 20px;")
            elif text == 'C':
                button.setStyleSheet("background-color: #E74C3C; color: white; font-size: 20px;")

            if span:
                grid_layout.addWidget(button, row, col, *span)  # Span across columns
            else:
                grid_layout.addWidget(button, row, col)

            self.buttons[text] = button  # Store button reference

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def get_display_text(self):
        """Get text from display."""
        return self.display.text()

    def set_display_text(self, text):
        """Set text in display."""
        self.display.setText(text)

    def clear_display(self):
        """Clear the display."""
        self.display.clear()
