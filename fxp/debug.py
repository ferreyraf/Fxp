from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)

def _time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def _log(level: str, color, msg: str):
    print(f"[{_time()}] {color}{level:<7}{Style.RESET_ALL} {msg}")

def err(msg):   _log("[ERROR]", Fore.RED, msg)
def warn(msg):  _log("[WARN]", Fore.YELLOW, msg)
def info(msg):  _log("[INFO]", Fore.GREEN, msg)
def debug(msg): _log("[DEBUG]", Fore.CYAN, msg)
