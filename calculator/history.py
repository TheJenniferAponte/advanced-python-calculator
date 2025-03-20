import pandas as pd
import logging
import os

logger = logging.getLogger(__name__)

class HistoryManager:
    def __init__(self):
        # Initialize with explicit dtypes to avoid FutureWarning
        self.df = pd.DataFrame({"operation": pd.Series(dtype="str"), "result": pd.Series(dtype="float")})
        self.filepath = "history.csv"

    def add_record(self, operation, result):
        new_record = pd.DataFrame({"operation": [operation], "result": [result]})
        self.df = pd.concat([self.df, new_record], ignore_index=True)
        logger.info(f"Added record: {operation} = {result}")

    def save(self):
        self.df.to_csv(self.filepath, index=False)
        logger.info("History saved to CSV")

    def load(self):
        if os.path.exists(self.filepath):
            self.df = pd.read_csv(self.filepath)
            logger.info("History loaded from CSV")
        else:
            logger.warning("No history file found")

    def clear(self):
        self.df = pd.DataFrame({"operation": pd.Series(dtype="str"), "result": pd.Series(dtype="float")})
        logger.info("History cleared")

    def delete(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
        self.clear()
        logger.info("History deleted")