import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from vibeleftpad import leftpad
from dotenv import load_dotenv

load_dotenv()


def test_basic_padding():
    assert leftpad("hello", 10) == "     hello"


def test_custom_pad_char():
    assert leftpad("test", 8, "0") == "0000test"
    assert leftpad("x", 5, "*") == "****x"


def test_no_padding_needed():
    assert leftpad("hello", 5) == "hello"
    assert leftpad("longer", 4) == "longer"
    assert leftpad("exact", 5) == "exact"


def test_empty_string():
    assert leftpad("", 5) == "     "
    assert leftpad("", 3, "0") == "000"


def test_single_char():
    assert leftpad("a", 5) == "    a"
    assert leftpad("x", 3, "0") == "00x"


def test_zero_length():
    assert leftpad("test", 0) == "test"