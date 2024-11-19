"""Tests for stream module."""


from digitalstream import get_terminal_width


def test_get_terminal_width(monkeypatch):
    """Test terminal width retrieval."""
    # Mock the terminal size to control the output
    monkeypatch.setattr('shutil.get_terminal_size', lambda: (80, 24))
    width = get_terminal_width()
    assert width == 79, "Width should be terminal width - 1"
