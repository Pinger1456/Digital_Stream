"""Utility functions for terminal management."""

import shutil


def get_terminal_width():
    """Get the width of the terminal window."""
    width = shutil.get_terminal_size()[0]
    return width - 1  # Reduce by one to avoid newline issues
