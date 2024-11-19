"""Main entry point for Digital Stream."""

from digitalstream import render_stream


def main():
    """Entry point of the Digital Stream screensaver."""
    print('Digital Stream, by Al Sweigart al@inventwithpython.com')
    print('Press Ctrl-C to quit.')
    render_stream()


if __name__ == "__main__":
    main()
