# Advanced Python Calculator

## Setup
1. Clone the repository: `git clone https://github.com/yourusername/advanced-python-calculator.git`
2. Activate virtual environment: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python calculator/repl.py`

## Usage
- `add 2 3` - Adds two numbers
- `save` - Saves history to CSV
- `menu` - Shows available commands

## Design Patterns
- **Facade**: [HistoryManager](calculator/history.py#L5) simplifies Pandas operations.
- **Command**: [Plugins](calculator/plugins/basic_operations.py#L3) structure REPL commands.
- **Factory**: [load_plugins](calculator/plugins/__init__.py#L10) creates command instances.

## Environment Variables
- Configured in [.env](.env#L1), used in [repl.py](calculator/repl.py#L6).

## Logging
- Configured dynamically in [repl.py](calculator/repl.py#L10) with levels and file output.

## Exception Handling
- LBYL and EAFP in [core.py](calculator/core.py#L10).

## Video Demo
- [Link to video](#) (to be added)