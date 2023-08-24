import pytest
from src.LinearDataStructures.LinkedList import LinkedList


@pytest.fixture
def empty_linkedlist():
    """ Fixture to create an empty LinkedList instance """
    return LinkedList()


@pytest.fixture
def linkedlist_with_nodes():
    """ Fixture to create a LinkedList instance with some nodes """
    ll = LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    return ll


class TestAddNode:
    def test_add_node_to_empty_list(self, empty_linkedlist):
        empty_linkedlist.add_node(1)
        assert empty_linkedlist.__str__() == "1"

    def test_add_node_to_non_empty_list(self, linkedlist_with_nodes):
        linkedlist_with_nodes.add_node(4)
        assert linkedlist_with_nodes.__str__() == "1, 2, 3, 4"


class TestRemoveNode:
    def test_remove_node_head(self, linkedlist_with_nodes):
        removed_node = linkedlist_with_nodes.remove_node(1)
        assert linkedlist_with_nodes.__str__() == "2, 3"
        assert removed_node.value == 1

    def test_remove_node_middle(self, linkedlist_with_nodes):
        removed_node = linkedlist_with_nodes.remove_node(2)
        assert linkedlist_with_nodes.__str__() == "1, 3"
        assert removed_node.value == 2

    def test_remove_node_tail(self, linkedlist_with_nodes):
        removed_node = linkedlist_with_nodes.remove_node(3)
        assert linkedlist_with_nodes.__str__() == "1, 2"
        assert removed_node.value == 3

    def test_remove_node_not_found(self, linkedlist_with_nodes):
        with pytest.raises(ValueError):
            linkedlist_with_nodes.remove_node(100)

    def test_remove_node_empty(self, empty_linkedlist):
        with pytest.raises(ValueError):
            empty_linkedlist.remove_node(1)


class TestStringRepresentation:
    def test_string_representation_empty(self, empty_linkedlist):
        assert empty_linkedlist.__str__() == "Empty List"

    def test_string_representation_non_empty(self, linkedlist_with_nodes):
        assert linkedlist_with_nodes.__str__() == "1, 2, 3"
