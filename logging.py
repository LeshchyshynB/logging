from settings import *
import settings
import loger

class Logging:

	@classmethod
	def notset(self, message):
		loger.write_in_log(message, NAMES["notset"], LEVELS["NOTSET_LEVEL"])
	
	@classmethod
	def debug(self, message, ignore=False):
		loger.write_in_log(message, NAMES["debug"], LEVELS["DEBUG_LEVEL"], ignore)

	@classmethod
	def info(self, message, ignore=False):
		loger.write_in_log(message, NAMES["info"], LEVELS["INFO_LEVEL"], ignore)

	@classmethod
	def warning(self, message, ignore=False):
		loger.write_in_log(message, NAMES["warning"], LEVELS["WARNING_LEVEL"], ignore)

	@classmethod
	def error(self, message, ignore=False):
		loger.write_in_log(message, NAMES["error"], LEVELS["ERROR_LEVEL"], ignore)

	@classmethod
	def critical(self, message, ignore=False):
		loger.write_in_log(message, NAMES["critical"], LEVELS["CRITICAL_LEVEL"], ignore)

	@classmethod
	def setting(self, min_console=30, min_log=10, ignore_console=True, ignore_log=False):
		settings.MIN_TO_LOG = min_log
		settings.MIN_TO_CONSOLE = min_console
		settings.IGNORE_LOG = ignore_log
		settings.IGNORE_CONSOLE = ignore_console