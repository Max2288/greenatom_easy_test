"""Testing file."""
import pytest
from fourth import get_public_ip


test_public_ip = [
    ("85.174.196.98", True),
    ("85.174.196.99", False),
    ("", False),
    ("85.174", False)
]


@pytest.mark.parametrize("ip, expect", test_public_ip)
def test_get_public_ip(ip, expect):
    temp = get_public_ip() == ip
    assert temp == expect
