import logging
from calculator.history import HistoryManager

logger = logging.getLogger(__name__)

class Calculator:
    def __init__(self):
        self.history = HistoryManager()

    def add(self, a, b):
        result = float(a) + float(b)
        logger.info(f"Adding {a} + {b} = {result}")
        self.history.add_record(f"{a} + {b}", result)
        return result

    def subtract(self, a, b):
        result = float(a) - float(b)
        logger.info(f"Subtracting {a} - {b} = {result}")
        self.history.add_record(f"{a} - {b}", result)
        return result

    # Add multiply and divide similarly








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