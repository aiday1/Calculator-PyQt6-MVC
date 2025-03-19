class Calculator:
    def __init__(self):
        """Initialize the calculator with an empty expression."""
        self.expression = ""

    def add_to_expression(self, char: str):
        """Add a character (digit/operator) to the expression."""
        if char == '.' and (self.expression.endswith('.') or not self.expression or self.expression[-1] in "+-*/"):
            return  # Prevent multiple decimals in a row
        self.expression += char

    def remove_last_character(self):
        """Remove the last character from the expression."""
        self.expression = self.expression[:-1]

    def clear_expression(self):
        """Clear the entire expression."""
        self.expression = ""

    def calculate(self):
        """Evaluate the expression and return the result."""
        try:
            result = eval(self.expression)  # Using eval carefully
            return str(result)
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception:
            return "Error: Invalid input"

    def get_expression(self):
        """Return the current expression."""
        return self.expression
