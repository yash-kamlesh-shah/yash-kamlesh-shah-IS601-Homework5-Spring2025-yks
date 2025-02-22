from app.commands import Command
from decimal import Decimal, InvalidOperation

class AddCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            print("Error: 'add' command requires exactly 2 arguments.")
            return

        try:
            a = Decimal(args[0])
            b = Decimal(args[1])
            result = a + b
            print(f"The result of {a} + {b} is {result}")
        except InvalidOperation:
            print("Invalid input: Please provide valid numbers.")