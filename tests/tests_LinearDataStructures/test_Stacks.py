import pytest

from LinearDataStructures.Stacks import Stack


@pytest.fixture
def stack_with_elements():
    """ Fixture to create a stack with elements """
    s = Stack()
    s.add_to_stack(1)
    s.add_to_stack(2)
    s.add_to_stack(3)
    return s


@pytest.fixture
def empty_stack():
    """ Fixture to create an empty stack """
    return Stack()


@pytest.fixture
def full_stack():
    """ Fixture to create a full stack """
    s = Stack(max_size=3)
    s.add_to_stack(1)
    s.add_to_stack(2)
    s.add_to_stack(3)
    return s


class TestAddToStack:
    def test_add_to_stack(self, stack_with_elements):
        stack_with_elements.add_to_stack(4)
        assert stack_with_elements.__str__() == "4, 3, 2, 1"

    def test_add_to_stack_full_stack(self, full_stack):
        with pytest.raises(ValueError):
            full_stack.add_to_stack(4)

    def test_add_to_stack_empty_stack(self, empty_stack):
        empty_stack.add_to_stack(1)
        assert empty_stack.__str__() == "1"


class TestRemoveFromStack:
    def test_remove_from_stack(self, stack_with_elements):
        stack_with_elements.remove_from_stack()
        assert stack_with_elements.__str__() == "2, 1"

    def test_remove_from_full_stack(self, full_stack):
        full_stack.remove_from_stack()
        assert full_stack.__str__() == "2, 1"

    def test_remove_from_empty_stack(self, empty_stack):
        with pytest.raises(ValueError):
            empty_stack.remove_from_stack()

    def test_remove_from_full_then_add(self, full_stack):
        full_stack.remove_from_stack()
        full_stack.add_to_stack(4)
        assert full_stack.__str__() == "4, 2, 1"


class TestGetFirstElement:
    def test_get_first_element(self, stack_with_elements):
        assert stack_with_elements.get_first_element() == 3

    def test_get_first_element_full_stack(self, full_stack):
        assert full_stack.get_first_element() == 3

    def test_get_first_element_empty_stack(self, empty_stack):
        with pytest.raises(ValueError):
            empty_stack.get_first_element()


class TestHasSpace:
    def test_has_space(self, stack_with_elements):
        assert stack_with_elements.has_space() is True

    def test_has_space_full_stack(self, full_stack):
        assert full_stack.has_space() is False

    def test_has_space_empty_stack(self, empty_stack):
        assert empty_stack.has_space() is True


class TestIsEmpty:
    def test_is_empty(self, stack_with_elements):
        assert stack_with_elements.is_empty() is False

    def test_is_empty_full_stack(self, full_stack):
        assert full_stack.is_empty() is False

    def test_is_empty_empty_stack(self, empty_stack):
        assert empty_stack.is_empty() is True


class TestStackStringRepresentation:
    def test_string_representation(self, stack_with_elements):
        assert stack_with_elements.__str__() == "3, 2, 1"

    def test_string_representation_full_stack(self, full_stack):
        assert full_stack.__str__() == "3, 2, 1"

    def test_string_representation_empty_stack(self, empty_stack):
        assert empty_stack.__str__() == "Empty Stack"


class TestStackIncrementAndDecrement:
    def test_increment_stack(self, stack_with_elements):
        initial_size = stack_with_elements.get_size()
        stack_with_elements.add_to_stack(4)
        assert stack_with_elements.get_size() == initial_size + 1

    def test_decrement_stack(self, stack_with_elements):
        initial_size = stack_with_elements.get_size()
        stack_with_elements.remove_from_stack()
        assert stack_with_elements.get_size() == initial_size - 1

    def test_increment_full_stack(self, full_stack):
        initial_size = full_stack.get_size()
        with pytest.raises(ValueError):
            full_stack.add_to_stack(4)

        # Make sure that the stack is still full
        assert full_stack.get_size() == initial_size

    def test_decrement_empty_stack(self, empty_stack):
        initial_size = empty_stack.get_size()
        with pytest.raises(ValueError):
            empty_stack.remove_from_stack()

        # Make sure that the stack is still empty
        assert empty_stack.get_size() == initial_size
