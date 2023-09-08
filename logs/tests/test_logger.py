# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\logs\\tests')

from logs.logger import Logger, LoggingLevel
from time import sleep

log = Logger()

log.settings.print_timestamp = True
log.settings.output_file = 'logs/tests/log.txt'
log.settings.minimum_console_level = LoggingLevel.INFO

log.debug('Debug')
log.error('Error')

# Result: Should only show error with timestamp

# Simple progress bar
for i in log.progress(range(5), 'Testing progress'):
    # We should avoid nested progress bars, but they are possible like so
    for i in log.progress(range(5), 'Testing inner progress', position=1, leave=False):
        sleep(0.1)