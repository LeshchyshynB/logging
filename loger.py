import settings
import console

def write_in_log(message, attribute, level, ignore=False):
	if not ignore:
		if settings.MIN_TO_LOG <= level:
			with open(settings.DIRECTORY_PATH, 'a') as file:
				file.write(f"{attribute[5:]} | [{settings.CURRENT_TIME}] |: {message}\n")
	console.write_in_console(message, attribute, level, ignore)