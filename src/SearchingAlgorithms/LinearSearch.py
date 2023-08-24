from typing import Iterable, Any, List


def linear_search(search_iterable: Iterable, search_value: Any) -> int:
    """
    Linear search algorithm implementation

    Time Complexity: O(n)
    Space Complexity: O(1)

    :param search_iterable: An iterable to search through
    :param search_value: The value to search for
    :return: index of the search_value in the search_iterable
    :raises: ValueError if the search_value is not found in the search_iterable
    """
    for index, value in enumerate(search_iterable):
        if value == search_value:
            return index
    raise ValueError("Value not found in iterable")


def find_all_instances(search_iterable: Iterable, search_value: Any) -> List[int]:
    """
    Linear Search implementation to find all instances of a value within an iterable

    Time Complexity: O(n)
    Space Complexity O(1)

    :param search_iterable: An iterable to search through
    :param search_value: The value to search for
    :return: A list of indices of the search_value in the search_iterable
    :raises: ValueError if the search_value is not found in the search_iterable
    """
    instances = []
    for idx, value in enumerate(search_iterable):
        if value == search_value:
            instances.append(idx)
    if len(instances) == 0:
        raise ValueError("Value not found in iterable")

    return instances


def find_max_value(search_iterable: Iterable[int]) -> tuple[int, int]:
    """
    Linear Search implementation to find the maximum value within an iterable

    Time Complexity: O(n)
    Space Complexity O(1)

    :param search_iterable: An iterable to search through
    :return: Tuple containing the index of the value and the value itself
    :raises: ValueError if the search_iterable is empty
    """
    if len(search_iterable) == 0:
        raise ValueError("Iterable is empty")

    max_value = search_iterable[0]
    max_index = 0
    for idx, value in enumerate(search_iterable):
        if value > max_value:
            max_value = value
            max_index = idx

    return max_index, max_value
