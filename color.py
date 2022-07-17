# https://stackoverflow.com/a/46482050/11645649

from copy import copy
from logging import Formatter

# ANSI Color codes
# Value 	Color
# \e[0;30m 	Black
# \e[0;31m 	Red
# \e[0;32m 	Green
# \e[0;33m 	Yellow
# \e[0;34m 	Blue
# \e[0;35m 	Purple
# \e[0;36m 	Cyan
# \e[0;37m 	White

# Log coloring start
MAPPING = {
    'DEBUG'     : 36,  # Cyan
    'NOTICE'    : 35,  # Purple
    'WARNING'   : 33,  # Yellow
    'ERROR'     : 31,  # Red
    'CRITICAL'  : 41   # White on red bg
}

PREFIX = '\u001b['
SUFFIX = '\u001b[0m'


class ColoredFormatter(Formatter):
    def __init__(self, pattern):
        Formatter.__init__(self, pattern)

    def format(self, record):
        colored_record = copy(record)
        levelname = colored_record.levelname
        seq = MAPPING.get(levelname, 37)  # Default white
        colored_levelname = ('{0}{1}m{2}{3}') \
            .format(PREFIX, seq, levelname, SUFFIX)
        colored_record.levelname = colored_levelname
        return Formatter.format(self, colored_record)
