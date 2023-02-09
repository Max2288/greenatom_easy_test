"""Testing file."""
import pytest
from third import find_tags


test_find_tags = [
    ('https://greenatom.ru', {'all': 774, 'with_attrs': 478}, True),
    ('https://greenatom.ru', {}, False)
]


@pytest.mark.parametrize("url, res, expect", test_find_tags)
def test_check_find_tags(url: str, res: dict, expect: bool) -> None:
    """Test find tags function.

    Args:
        url (str): url on page.
        res (dict): the result of the function.
        expect (bool): what we expect.
    """
    temp = find_tags(url) == res
    assert temp == expect
