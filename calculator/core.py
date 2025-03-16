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