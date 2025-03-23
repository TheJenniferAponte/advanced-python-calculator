import logging
import os
from dotenv import load_dotenv
from calculator.core import Calculator
from calculator.plugins import load_plugins

load_dotenv()
log_level = os.getenv("LOG_LEVEL", "INFO")
log_file = os.getenv("LOG_FILE", "calculator.log")

logging.basicConfig(
    level=getattr(logging, log_level),
    filename=log_file,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class REPL:
    def __init__(self):
        self.calculator = Calculator()
        self.plugins = load_plugins()
        self.running = True
        self.command_map = {
            "add": self.plugins.get("addcommand"),
            "subtract": self.plugins.get("subtractcommand"),
            "multiply": self.plugins.get("multiplycommand"),
            "divide": self.plugins.get("dividecommand")
        }
        # Log loaded commands for debugging
        logger.info(f"Loaded commands: {list(self.command_map.keys())}")
        for cmd, obj in self.command_map.items():
            logger.info(f"{cmd}: {obj}")

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
        for cmd in self.command_map.keys():
            print(f"- {cmd}")
        print("- history (load/save/clear/delete)")
        print("- exit")

    def execute_command(self, cmd_name, args):
        logger.info(f"Executing command: {cmd_name} with args: {args}")
        if cmd_name in self.command_map and self.command_map[cmd_name] is not None:
            try:
                result = self.command_map[cmd_name].execute(self.calculator, *args)
                if result is not None:
                    print(f"Result: {result}")
            except (ValueError, ZeroDivisionError) as e:
                logger.error(f"Command error: {e}")
                print(f"Error: {e}")
        elif cmd_name in ["load", "save", "clear", "delete"]:
            getattr(self.calculator.history, cmd_name)(*args)
        else:
            logger.warning(f"Unknown command: {cmd_name}")
            print("Unknown command. Type 'menu' for options.")

if __name__ == "__main__":
    REPL().start()