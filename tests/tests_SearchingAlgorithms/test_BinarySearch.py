import pytest
from SearchingAlgorithms.BinarySearch import binary_search_recursive, binary_search_iterative


@pytest.mark.parametrize(
    "iterable, search_value, result",
    [
        ([1, 2, 3, 4, 5], 1, 0),       # Test left most value
        ([1, 2, 3, 4, 5], 3, 2),       # Test middle value
        ([1, 2, 3, 4, 5], 5, 4),       # Test right most value
        ([1, 2, 3, 3], 3, 2),          # Test list with duplicate values
        ([1, 1, 1], 1, 1),             # Test list that only contains duplicates
        ([-3, -2, -1], -1, 2),         # Test list that contains negative value
        ([1.1, 2.2, 3.3], 1.1, 0),     # Test with float values
        ([-3, 0, 1, 2.2, 3], 2.2, 3),  # Test with multiple value types
        ([42], 42, 0),                 # Test list with single value
    ]
)
class TestBinarySearchSuccess:
    def test_binary_search_recursive(self, iterable, search_value, result):
        assert binary_search_recursive(iterable, 0, len(iterable) - 1, search_value) == result

    def test_binary_search_iterative(self, iterable, search_value, result):
        assert binary_search_iterative(iterable, search_value) == result


@pytest.mark.parametrize(
    "iterable, search_value",
    [
        ([1, 2, 3, 4, 5], 6),  # Test search value not in the list
        ([], 42),              # Test with an empty list
        ([1, 2, 3, 4, 5], 0),  # Test search value less than the minimum
        ([1, 2, 3, 4, 5], 6),  # Test search value greater than the maximum
    ]
)
class TestBinarySearchFailure:
    def test_binary_search_recursive_empty(self, iterable, search_value):
        with pytest.raises(ValueError):
            binary_search_recursive(iterable, 0, len(iterable) - 1, search_value)

    def test_binary_search_iterative_empty(self, iterable, search_value):
        with pytest.raises(ValueError):
            binary_search_iterative(iterable, search_value)
