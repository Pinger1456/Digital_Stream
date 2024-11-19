"""Tests for config module."""

from config import MIN_STREAM_LENGTH, MAX_STREAM_LENGTH, \
    PAUSE, STREAM_CHARS, DENSITY


def test_min_stream_length():
    """MIN_STREAM_LENGTH should be greater than 0"""
    assert MIN_STREAM_LENGTH > 0


def test_max_stream_length():
    """MAX_STREAM_LENGTH should be greater than MIN_STREAM_LENGTH"""
    assert MAX_STREAM_LENGTH > MIN_STREAM_LENGTH


def test_pause():
    """PAUSE should be a positive number"""
    assert PAUSE > 0


def test_stream_chars():
    """STREAM_CHARS should be a list. STREAM_CHARS should not be empty"""
    assert isinstance(STREAM_CHARS, list)
    assert len(STREAM_CHARS) > 0


def test_density():
    """DENSITY should be between 0.0 and 1.0"""
    assert 0.0 <= DENSITY <= 1.0
