from libraries import *

FILE_FORMAT = "%Y-%m-%d"

CURRENT_FILE = datetime.now().strftime(FILE_FORMAT)

DIRECTORY_PATH = f"logs/{CURRENT_FILE}.log"

TIME_FORMAT = "%H:%M:%S"

LEVELS = {
	"NOTSET_LEVEL": 0,

	"DEBUG_LEVEL": 10,

	"INFO_LEVEL": 20,

	"WARNING_LEVEL": 30,

	"ERROR_LEVEL": 40,

	"CRITICAL_LEVEL": 50,
}

NAMES = {
	"notset": "NOTSET",
	"debug": Fore.WHITE + "DEBUG",
	"info": Fore.GREEN + "INFO",
	"warning": Fore.YELLOW + "WARNING",
	"error": Fore.MAGENTA + "ERROR",
	"critical": Fore.RED + "CRITICAL",
}

CURRENT_TIME = datetime.now().strftime(TIME_FORMAT)

MIN_TO_LOG = 10

MIN_TO_CONSOLE = 30

IGNORE_LOG = False

IGNORE_CONSOLE = True