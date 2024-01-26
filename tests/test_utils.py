from ..utils import add
import pytest

def test_add():
    assert add(10) == 11
    assert add(12) == 13
    assert add(11) == 12
