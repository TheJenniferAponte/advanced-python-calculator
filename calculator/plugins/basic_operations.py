from .command import Command

class AddCommand(Command):
    def execute(self, calculator, *args):
        if len(args) != 2:
            raise ValueError("Add requires 2 arguments")
        a, b = float(args[0]), float(args[1])
        return calculator.add(a, b)

class SubtractCommand(Command):
    def execute(self, calculator, *args):
        if len(args) != 2:
            raise ValueError("Subtract requires 2 arguments")
        a, b = float(args[0]), float(args[1])
        return calculator.subtract(a, b)

class MultiplyCommand(Command):
    def execute(self, calculator, *args):
        if len(args) != 2:
            raise ValueError("Multiply requires 2 arguments")
        a, b = float(args[0]), float(args[1])
        return calculator.multiply(a, b)

class DivideCommand(Command):
    def execute(self, calculator, *args):
        if len(args) != 2:
            raise ValueError("Divide requires 2 arguments")
        a, b = float(args[0]), float(args[1])
        return calculator.divide(a, b)