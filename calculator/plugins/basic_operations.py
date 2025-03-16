from calculator.plugins import Command

class AddCommand(Command):
    def execute(self, calculator, *args):
        if len(args) != 2:
            raise ValueError("Add requires 2 arguments")
        result = calculator.add(args[0], args[1])
        print(f"Result: {result}")

class SubtractCommand(Command):
    def execute(self, calculator, *args):
        if len(args) != 2:
            raise ValueError("Subtract requires 2 arguments")
        result = calculator.subtract(args[0], args[1])
        print(f"Result: {result}")