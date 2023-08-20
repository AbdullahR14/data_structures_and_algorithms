import pytest
from LinearDataStructures.LinkedList import LinkedList


# Fixture to create an empty LinkedList instance
@pytest.fixture
def empty_linkedlist():
    return LinkedList()


# Fixture to create a LinkedList instance with some nodes
@pytest.fixture
def linkedlist_with_nodes():
    ll = LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    return ll


def test_add_node_to_empty_list(empty_linkedlist):
    empty_linkedlist.add_node(1)
    assert empty_linkedlist.__str__() == "1"


def test_add_node_to_non_empty_list(linkedlist_with_nodes):
    linkedlist_with_nodes.add_node(4)
    assert linkedlist_with_nodes.__str__() == "1, 2, 3, 4"


def test_remove_node_head(linkedlist_with_nodes):
    removed_node = linkedlist_with_nodes.remove_node(1)
    assert linkedlist_with_nodes.__str__() == "2, 3"
    assert removed_node.value == 1


def test_remove_node_middle(linkedlist_with_nodes):
    removed_node = linkedlist_with_nodes.remove_node(2)
    assert linkedlist_with_nodes.__str__() == "1, 3"
    assert removed_node.value == 2


def test_remove_node_tail(linkedlist_with_nodes):
    removed_node = linkedlist_with_nodes.remove_node(3)
    assert linkedlist_with_nodes.__str__() == "1, 2"
    assert removed_node.value == 3


def test_remove_node_not_found(linkedlist_with_nodes):
    with pytest.raises(ValueError):
        linkedlist_with_nodes.remove_node(100)


def test_remove_node_empty(empty_linkedlist):
    with pytest.raises(ValueError):
        empty_linkedlist.remove_node(1)


def test_string_representation_empty(empty_linkedlist):
    assert empty_linkedlist.__str__() == "Empty List"


def test_string_representation_non_empty(linkedlist_with_nodes):
    assert linkedlist_with_nodes.__str__() == "1, 2, 3"
