"""Testing file."""
import pytest
from second import add_one, create_handlers

test_add_one = [(1, 2, True), (-1, 0, True), (1, 10, False), (5, 7, False)]


@pytest.mark.parametrize("number, result, expect", test_add_one)
def test_check_add_one(number: int, result: int, expect: bool) -> None:
    """Test add one function.

    Args:
        number (int): input data.
        result (int): the result of the function.
        expect (bool): what we expect.
    """
    temp = add_one(number) == result
    assert temp == expect


test_create_handlers = [
    ([1, 2, 3, 4, 5], True),
    ([-1, 0, 1, 2, 3], False),
    ([2, 3, 4, 5], False),
    ([5, 6, 7, 8], False)
]


@pytest.mark.parametrize("result, expect", test_create_handlers)
def test_check_create_handlers(result: list, expect: bool) -> None:
    """Test for create handlers.

    Args:
        result (list): the result after executing.
        expect (bool): what we expect.
    """
    temp = [function() for function in create_handlers(add_one)] == result
    assert temp == expect
