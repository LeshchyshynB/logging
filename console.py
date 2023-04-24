import settings

def write_in_console(message, attribute, level, ignore):
	settings.colorama_init()
	if not ignore:
		if settings.MIN_TO_CONSOLE <= level:
			print(f"{attribute} | [{settings.CURRENT_TIME}] |: {message}")