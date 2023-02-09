def compare_versions(first_version: str, second_version: str):
    first_version_lst, second_version_lst = first_version.split("."), second_version.split(".")
    for element_first, element_second in zip(first_version_lst, second_version_lst):
        if int(element_first) > int(element_second):
            return 1
        elif int(element_first) < int(element_second):
            return -1
    return 0


print(compare_versions('1.10', '1.1'))
