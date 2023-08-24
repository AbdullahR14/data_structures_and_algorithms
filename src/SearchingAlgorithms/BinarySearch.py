from typing import List, Union


def binary_search_recursive(search_iterable: List[Union[int, float]], left_pointer: int, right_pointer: int,
                            search_value: Union[int, float]) -> int:
    """
    Recursive Binary Search implementation

    Time Complexity: O(log n)
    Space Complexity: O(1)

    :param search_iterable: An iterable to search through
    :param left_pointer: The left pointer of the search range
    :param right_pointer: The right pointer of the search range
    :param search_value: The value to search for
    :return: index of the search_value in the search_iterable
    :raises: ValueError if the search_value is not found in the search_iterable
    """
    # Empty List
    if left_pointer > right_pointer:
        raise ValueError("Value not found in iterable")

    # Find the middle of the list
    mid_pointer = (left_pointer + right_pointer) // 2

    # Check if the middle value is the search value
    if search_iterable[mid_pointer] == search_value:
        return mid_pointer

    # Check if the middle value is greater than the search value
    if search_iterable[mid_pointer] > search_value:
        # return recursive call with the right pointer set to the middle pointer - 1
        return binary_search_recursive(search_iterable, left_pointer, mid_pointer - 1, search_value)

    # Check if the middle value is less than the search value
    if search_iterable[mid_pointer] < search_value:
        # return recursive call with the left pointer set to the middle pointer + 1
        return binary_search_recursive(search_iterable, mid_pointer + 1, right_pointer, search_value)


def binary_search_iterative(search_iterable: List[Union[int, float]], search_value: Union[int, float]) -> int:
    """
    Iterative Binary Search implementation

    Time Complexity: O(log n)
    Space Complexity: O(1)

    :param search_iterable: An iterable to search through
    :param search_value: The value to search for
    :return: index of the search_value in the search_iterable
    :raises: ValueError if the search_value is not found in the search_iterable
    """
    left_pointer = 0
    right_pointer = len(search_iterable) - 1

    while left_pointer <= right_pointer:
        # Find the middle of the list
        mid_pointer = (left_pointer + right_pointer) // 2

        # Check if the middle value is the search value
        if search_iterable[mid_pointer] == search_value:
            return mid_pointer

        # Check if the middle value is greater than the search value
        if search_iterable[mid_pointer] > search_value:
            # set the right pointer to the middle pointer - 1
            right_pointer = mid_pointer - 1

        # Check if the middle value is less than the search value
        if search_iterable[mid_pointer] < search_value:
            # set the left pointer to the middle pointer + 1
            left_pointer = mid_pointer + 1

    raise ValueError("Value not found in iterable")
