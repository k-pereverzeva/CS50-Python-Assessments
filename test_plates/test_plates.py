from plates import is_valid

def test_start():
    assert is_valid('50CS') == False
    assert is_valid('2222') == False
    assert is_valid('CS50') == True


def test_zero():
    assert is_valid('CS05') == False


def test_middle():
    assert is_valid('CS50P') == False


def test_marks():
    assert is_valid('PI3.14') == False


def test_lenth():
    assert is_valid('H') == False
    assert is_valid('OUTATIME') == False


