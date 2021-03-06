import msvcrt

def getch_windows(NONBLOCK=False, encoding='utf-8', raw=None):
	if NONBLOCK and not msvcrt.kbhit():
		return ''
	if encoding:
		return msvcrt.getch().decode(encoding)
	else:
		return msvcrt.getwch()
