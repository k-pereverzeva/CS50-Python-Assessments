from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert('5/2')


def test_gauge():
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'
    assert gauge(15) == '15%'


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        2/0
