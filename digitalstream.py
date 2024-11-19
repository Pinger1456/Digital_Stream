"""Digital Stream rendering logic."""

import sys
import random
import shutil
import time
from config import MIN_STREAM_LENGTH, MAX_STREAM_LENGTH, \
    PAUSE, STREAM_CHARS, DENSITY


def get_terminal_width():
    """Retrieve the terminal width, adjusting for compatibility issues."""
    width = shutil.get_terminal_size().columns
    return width - 1  # Reduce by one to avoid newline issues on some platforms


def render_stream():
    """Render the digital stream in the terminal."""
    width = get_terminal_width()
    columns = [0] * width

    try:
        while True:
            # Set up the counter for each column:
            for i in range(width):
                if columns[i] == 0:
                    if random.random() <= DENSITY:
                        # Restart a stream on this column.
                        columns[i] = random.randint(MIN_STREAM_LENGTH,
                                                    MAX_STREAM_LENGTH)

                # Display an empty space or a 1/0 character.
                if columns[i] > 0:
                    print(random.choice(STREAM_CHARS), end='')
                    columns[i] -= 1
                else:
                    print(' ', end='')
            print()  # Print a newline at the end of the row of columns.
            sys.stdout.flush()  # Make sure text appears on the screen.
            time.sleep(PAUSE)
    except KeyboardInterrupt:
        sys.exit()  # Exit gracefully on Ctrl-C
