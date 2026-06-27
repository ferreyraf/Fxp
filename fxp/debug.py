from colorama import Fore, Style, init
import inspect
init(autoreset=True)

def err(string : str):
    print(Fore.RED + "[ERROR]" + Style.RESET_ALL,   f"{string}")
def warm(string : str):
        print(Fore.YELLOW + "[WARN]" + Style.RESET_ALL,   f"{string}")
def info(string : str):
        print(Fore.GREEN + "[INFO]" + Style.RESET_ALL,   f"{string}")
def debug(string : str):
        print(Fore.CYAN + "[DEBUG]" + Style.RESET_ALL,   f"{string}")