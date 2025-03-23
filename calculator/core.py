import logging
from calculator.history import HistoryManager

logger = logging.getLogger(__name__)

class Calculator:
    def __init__(self):
        self.history = HistoryManager()

    def add(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            logger.error(f"Invalid input for add: {a}, {b}")
            raise ValueError("Inputs must be numbers")
        result = float(a) + float(b)
        logger.info(f"Adding {a} + {b} = {result}")
        self.history.add_record(f"{a} + {b}", result)
        return result

    def subtract(self, a, b):
        try:
            result = float(a) - float(b)
            logger.info(f"Subtracting {a} - {b} = {result}")
            self.history.add_record(f"{a} - {b}", result)
            return result
        except ValueError as e:
            logger.error(f"Invalid input for subtract: {e}")
            raise

    def multiply(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            logger.error(f"Invalid input for multiply: {a}, {b}")
            raise ValueError("Inputs must be numbers")
        result = float(a) * float(b)
        logger.info(f"Multiplying {a} * {b} = {result}")
        self.history.add_record(f"{a} * {b}", result)
        return result

    def divide(self, a, b):
        try:
            result = float(a) / float(b)
            logger.info(f"Dividing {a} / {b} = {result}")
            self.history.add_record(f"{a} / {b}", result)
            return result
        except ZeroDivisionError:
            logger.error("Division by zero")
            raise
        except ValueError as e:
            logger.error(f"Invalid input for divide: {e}")
            raise







def add(self, a, b):
    # LBYL: Check before operation
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        logger.error(f"Invalid input for add: {a}, {b}")
        raise ValueError("Inputs must be numbers")
    result = float(a) + float(b)
    self.history.add_record(f"{a} + {b}", result)
    return result

def subtract(self, a, b):
    # EAFP: Try and catch
    try:
        result = float(a) - float(b)
        self.history.add_record(f"{a} - {b}", result)
        return result
    except ValueError as e:
        logger.error(f"Invalid input for subtract: {e}")
        raise