from logging import Logging

if __name__ == '__main__':
	Logging.setting(min_console=0, min_log=0, ignore_console=False, ignore_log=False)
	Logging.notset("Hello World!")
	Logging.info("Hello World!")
	Logging.warning("Hello World!")
	Logging.error("Hello World!")
	Logging.critical("Hello World!")