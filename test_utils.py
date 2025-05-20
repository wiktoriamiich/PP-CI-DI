import pytest
import utils

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (3, 4, 7),
    (4, 5, 9)
])
def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, -1),
    (2, 3, -1),
    (3, 4, -1),
    (4, 5, -1)
])
def test_subtract(a, b, expected):
    result = utils.subtract(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (2, 3, 6),
    (3, 4, 12),
    (4, 5, 20)
])
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 0.5),
    (3, 4, 0.75),
    (4, 5, 0.8)
])
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == pytest.approx(expected)

#def test_divide_by_zero():
   # with pytest.raises(ValueError):
    #    utils.divide(1, 0)

@pytest.mark.parametrize("text, expected", [
    ("Hello world", 2),
    ("One two three", 3),
    ("", 0),
    ("   Lots    of spaces   ", 3)
])
def test_word_count(text, expected):
    result = utils.word_count(text)
    assert result == expected
