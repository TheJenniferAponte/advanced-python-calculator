from calculator.plugins import Command

class AddCommand(Command):
    def execute(self, calculator, *args):
        if len(args) != 2:
            raise ValueError("Add requires 2 arguments")
        a, b = float(args[0]), float(args[1])
        result = calculator.add(a, b)
        print(f"Result: {result}")

class SubtractCommand(Command):
    def execute(self, calculator, *args):
        if len(args) != 2:
            raise ValueError("Subtract requires 2 arguments")
        a, b = float(args[0]), float(args[1])
        result = calculator.subtract(a, b)
        print(f"Result: {result}")

class MultiplyCommand(Command):
    def execute(self, calculator, *args):
        if len(args) != 2:
            raise ValueError("Multiply requires 2 arguments")
        a, b = float(args[0]), float(args[1])
        result = calculator.multiply(a, b)
        print(f"Result: {result}")

class DivideCommand(Command):
    def execute(self, calculator, *args):
        if len(args) != 2:
            raise ValueError("Divide requires 2 arguments")
        a, b = float(args[0]), float(args[1])
        result = calculator.divide(a, b)
        print(f"Result: {result}")