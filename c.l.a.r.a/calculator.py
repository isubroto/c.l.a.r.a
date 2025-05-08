import math
import re
from sayAndListen import SayAndListen

class Calculator:
    def __init__(self):
        self.speech = SayAndListen()
        self.operations = {
            'plus': '+',
            'minus': '-',
            'times': '*',
            'multiplied by': '*',
            'divided by': '/',
            'over': '/',
            'to the power of': '**',
            'squared': '**2',
            'cubed': '**3',
            'square root of': 'math.sqrt',
            'cube root of': 'math.cbrt',
            'percent': '/100',
            'modulo': '%',
            'remainder': '%'
        }
    
    def _clean_expression(self, expression):
        """Clean and normalize the expression"""
        # Convert words to operators
        for word, operator in self.operations.items():
            expression = expression.replace(word, operator)
        
        # Handle special cases
        expression = expression.replace('x', '*')  # Common multiplication symbol
        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')
        
        # Remove extra spaces
        expression = expression.strip()
        
        return expression
    
    def _evaluate_expression(self, expression):
        """Safely evaluate a mathematical expression"""
        try:
            # Clean the expression
            clean_expr = self._clean_expression(expression)
            
            # Handle special cases
            if 'math.sqrt' in clean_expr:
                # Extract number from square root
                num = float(re.search(r'math\.sqrt\((\d+)\)', clean_expr).group(1))
                return math.sqrt(num)
            elif 'math.cbrt' in clean_expr:
                # Extract number from cube root
                num = float(re.search(r'math\.cbrt\((\d+)\)', clean_expr).group(1))
                return math.pow(num, 1/3)
            
            # Evaluate the expression
            result = eval(clean_expr)
            return result
        except Exception as e:
            return f"Error calculating: {str(e)}"
    
    def calculate(self, expression):
        """Calculate the result of a mathematical expression"""
        try:
            result = self._evaluate_expression(expression)
            
            # Format the result
            if isinstance(result, float):
                # Round to 2 decimal places if it's a float
                result = round(result, 2)
            
            return f"The result is {result}"
        except Exception as e:
            return f"Error calculating: {str(e)}"
    
    def process_calculator_command(self, command):
        """Process calculator-related commands"""
        command = command.lower()
        
        if "calculate" in command or "what is" in command:
            # Extract the expression
            expression = command.replace("calculate", "").replace("what is", "").strip()
            if expression:
                return self.calculate(expression)
            return "Please specify what to calculate"
        
        return "I didn't understand that calculator command" 