import pytest
from SearchingAlgorithms import LinearSearch


@pytest.fixture
def empty_list():
    """ Fixture to create an empty Iterable """
    return []


@pytest.fixture
def list_with_items():
    """ Fixture to create an Iterable with some items """
    return [1, 2, 3, 4, 5]


@pytest.fixture
def list_with_duplicates():
    """ Fixture to create an iterable with duplicate values """
    return [1, 2, 2]


class TestLinearSearch:
    def test_linear_search_empty_list(self, empty_list):
        with pytest.raises(ValueError):
            LinearSearch.linear_search(empty_list, 1)

    def test_linear_search_item_list(self, list_with_items):
        assert LinearSearch.linear_search(list_with_items, 3) == 2

    def test_linear_search_not_found(self, list_with_items):
        with pytest.raises(ValueError):
            LinearSearch.linear_search(list_with_items, 6)


class TestFindDuplicates:
    @pytest.fixture
    def list_with_all_duplicates(self):
        """ Fixture to create an iterable with all duplicate values """
        return [1, 1, 1]

    def test_find_duplicates_empty(self, empty_list):
        with pytest.raises(ValueError):
            LinearSearch.find_all_instances(empty_list, 1)

    def test_find_duplicates_with_duplicates(self, list_with_duplicates):
        assert LinearSearch.find_all_instances(list_with_duplicates, 2) == [1, 2]

    def test_find_duplicates_not_found(self, list_with_items):
        with pytest.raises(ValueError):
            LinearSearch.find_all_instances(list_with_items, 6)

    def test_find_duplicates_all_duplicates(self, list_with_all_duplicates):
        assert LinearSearch.find_all_instances(list_with_all_duplicates, 1) == [0, 1, 2]


class TestFindMaxValue:
    @pytest.fixture
    def list_with_negative_values(self):
        """ Fixture to create an iterable with negative values """
        return [-1, -2, -3]

    def test_find_max_value_empty(self, empty_list):
        with pytest.raises(ValueError):
            LinearSearch.find_max_value(empty_list)

    def test_find_max_value_single(self, list_with_items):
        assert LinearSearch.find_max_value(list_with_items) == (4, 5)

    def test_find_max_value_multiple(self, list_with_duplicates):
        assert LinearSearch.find_max_value(list_with_duplicates) == (1, 2)

    def test_find_max_value_negative(self, list_with_negative_values):
        assert LinearSearch.find_max_value(list_with_negative_values) == (0, -1)
