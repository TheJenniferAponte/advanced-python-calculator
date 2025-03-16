import logging
from calculator.core import Calculator
from calculator.plugins import load_plugins

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class REPL:
    def __init__(self):
        self.calculator = Calculator()
        self.plugins = load_plugins()
        self.running = True

    def start(self):
        logger.info("Starting REPL")
        print("Welcome to the Advanced Calculator. Type 'exit' to quit, 'menu' for commands.")
        while self.running:
            try:
                command = input("> ").strip().split()
                if not command:
                    continue
                cmd_name = command[0].lower()
                if cmd_name == "exit":
                    self.running = False
                elif cmd_name == "menu":
                    self.show_menu()
                else:
                    self.execute_command(cmd_name, command[1:])
            except Exception as e:
                logger.error(f"Error in REPL: {e}")
                print(f"Error: {e}")

    def show_menu(self):
        print("Available commands:")
        for cmd in self.plugins.keys():
            print(f"- {cmd}")
        print("- history (load/save/clear/delete)")
        print("- exit")

    def execute_command(self, cmd_name, args):
        if cmd_name in self.plugins:
            self.plugins[cmd_name].execute(self.calculator, *args)
        elif cmd_name in ["load", "save", "clear", "delete"]:
            getattr(self.calculator.history, cmd_name)(*args)
        else:
            print("Unknown command. Type 'menu' for options.")

if __name__ == "__main__":
    REPL().start()



import os
from dotenv import load_dotenv

load_dotenv()
log_level = os.getenv("LOG_LEVEL", "INFO")
log_file = os.getenv("LOG_FILE", "calculator.log")

logging.basicConfig(
    level=getattr(logging, log_level),
    filename=log_file,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)