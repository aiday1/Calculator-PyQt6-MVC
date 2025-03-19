from PyQt6.QtWidgets import QApplication
from view import CalculatorView
from calculator import Calculator


class CalculatorWindow:
    def __init__(self):
        """Initialize the controller to link the model and view."""
        self.app = QApplication([])
        self.view = CalculatorView()
        self.model = Calculator()

        self._connect_signals()
        self.view.show()
        self.app.exec()

    def _connect_signals(self):
        """Connect button signals to their respective event handlers."""
        for text, button in self.view.buttons.items():
            if text in "0123456789+-*/.":
                button.clicked.connect(lambda _, t=text: self._handle_button_click(t))
            elif text == "=":
                button.clicked.connect(self._calculate_result)
            elif text == "C":
                button.clicked.connect(self._clear_display)
            elif text == "⌫":  # Backspace button
                button.clicked.connect(self._handle_backspace)

    def _handle_button_click(self, char):
        """Handle digit and operator button clicks."""
        self.model.add_to_expression(char)
        self.view.set_display_text(self.model.get_expression())

    def _calculate_result(self):
        """Handle the calculation when '=' is pressed."""
        result = self.model.calculate()
        self.view.set_display_text(result)
        self.model.clear_expression()

    def _clear_display(self):
        """Clear the calculator display and reset the model."""
        self.model.clear_expression()
        self.view.clear_display()

    def _handle_backspace(self):
        """Remove the last character from the expression."""
        self.model.remove_last_character()
        self.view.set_display_text(self.model.get_expression())


if __name__ == "__main__":
    CalculatorWindow()
