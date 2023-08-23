import pytest

from LinearDataStructures.Queues import Queue


@pytest.fixture
def queue_with_elements():
    """ Fixture to create a queue with elements """
    q = Queue()
    q.add_to_queue(1)
    q.add_to_queue(2)
    q.add_to_queue(3)
    return q


@pytest.fixture
def empty_queue():
    """ Fixture to create an empty queue """
    return Queue()


@pytest.fixture
def full_queue():
    """ Fixture to create a full queue """
    q = Queue(max_size=3)
    q.add_to_queue(1)
    q.add_to_queue(2)
    q.add_to_queue(3)
    return q


class TestAddToQueue:
    def test_add_to_queue(self, queue_with_elements):
        queue_with_elements.add_to_queue(4)
        assert queue_with_elements.__str__() == "1, 2, 3, 4"

    def test_add_to_queue_full_queue(self, full_queue):
        with pytest.raises(ValueError):
            full_queue.add_to_queue(4)

    def test_add_to_queue_empty_queue(self, empty_queue):
        empty_queue.add_to_queue(1)
        assert empty_queue.__str__() == "1"


class TestRemoveFromQueue:
    def test_remove_from_queue(self, queue_with_elements):
        queue_with_elements.remove_from_queue()
        assert queue_with_elements.__str__() == "2, 3"

    def test_remove_from_full_queue(self, full_queue):
        full_queue.remove_from_queue()
        assert full_queue.__str__() == "2, 3"

    def test_remove_from_empty_queue(self, empty_queue):
        with pytest.raises(ValueError):
            empty_queue.remove_from_queue()

    def test_remove_from_full_then_add(self, full_queue):
        full_queue.remove_from_queue()
        full_queue.add_to_queue(4)
        assert full_queue.__str__() == "2, 3, 4"


class TestGetFirstElement:
    def test_get_first_element(self, queue_with_elements):
        assert queue_with_elements.get_first_element() == 1

    def test_get_first_element_full_queue(self, full_queue):
        assert full_queue.get_first_element() == 1

    def test_get_first_element_empty_queue(self, empty_queue):
        with pytest.raises(ValueError):
            empty_queue.get_first_element()


class TestHasSpace:
    def test_has_space(self, queue_with_elements):
        assert queue_with_elements.has_space() is True

    def test_has_space_full_queue(self, full_queue):
        assert full_queue.has_space() is False

    def test_has_space_empty_queue(self, empty_queue):
        assert empty_queue.has_space() is True


class TestIsEmpty:
    def test_is_empty(self, queue_with_elements):
        assert queue_with_elements.is_empty() is False

    def test_is_empty_full_queue(self, full_queue):
        assert full_queue.is_empty() is False

    def test_is_empty_empty_queue(self, empty_queue):
        assert empty_queue.is_empty() is True


class TestQueueStringRepresentation:
    def test_string_representation(self, queue_with_elements):
        assert queue_with_elements.__str__() == "1, 2, 3"

    def test_string_representation_full_queue(self, full_queue):
        assert full_queue.__str__() == "1, 2, 3"

    def test_string_representation_empty_queue(self, empty_queue):
        assert empty_queue.__str__() == "Empty Queue"


class TestQueueIncrementAndDecrement:
    def test_increment_queue(self, queue_with_elements):
        initial_size = queue_with_elements.get_size()
        queue_with_elements.add_to_queue(4)
        assert queue_with_elements.get_size() == initial_size + 1

    def test_decrement_queue(self, queue_with_elements):
        initial_size = queue_with_elements.get_size()
        queue_with_elements.remove_from_queue()
        assert queue_with_elements.get_size() == initial_size - 1

    def test_increment_queue_full_queue(self, full_queue):
        initial_size = full_queue.get_size()
        with pytest.raises(ValueError):
            full_queue.add_to_queue(4)

        # Make sure the queue is still full
        assert full_queue.get_size() == initial_size

    def test_decrement_queue_empty_queue(self, empty_queue):
        initial_size = empty_queue.get_size()
        with pytest.raises(ValueError):
            empty_queue.remove_from_queue()

        # Make sure the queue is still empty
        assert empty_queue.get_size() == initial_size
