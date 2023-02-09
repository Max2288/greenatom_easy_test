"""The solution of the fifth problem."""


def compare_versions(first_version: str, second_version: str) -> int:
    """Comparing versions.

    Args:
        first_version (str): first version of smth.
        second_version (str): second version of smth.

    Returns:
        int: 1 if first version > second version, -1 if first version < second version, 0 if they are equal.
    """
    first_version_lst, second_version_lst = first_version.split("."), second_version.split(".")
    for element_first, element_second in zip(first_version_lst, second_version_lst):
        if int(element_first) > int(element_second):
            return 1
        elif int(element_first) < int(element_second):
            return -1
    return 0


print(compare_versions('1.10', '1.1'))
