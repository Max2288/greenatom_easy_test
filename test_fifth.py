"""Testing file."""
import pytest
from fifth import compare_versions


test_versions = [
    ("1.0", "1.0", 0),
    ("1.10", "1.1", 1),
    ("2.0", "1.9", 1),
    ("1.0", "1.01", -1)
]


@pytest.mark.parametrize("first_v, second_v, expect", test_versions)
def test_compare_versions(first_v: str, second_v: str, expect: int) -> None:
    """Test for compare versions.

    Args:
        first_v (str): first version.
        second_v (str): second version.
        expect (int): what we expect.
    """
    assert compare_versions(first_v, second_v) == expect
