import pytest
from LinearDataStructures.DoublyLinkedList import DoublyLinkedList


# Fixture to create an empty DoublyLinkedList instance
@pytest.fixture
def empty_linkedlist():
    return DoublyLinkedList()


# Fixture to create a DoublyLinkedList instance with some nodes
@pytest.fixture
def linkedlist_with_nodes():
    ll = DoublyLinkedList()
    ll.add_node_to_back(1)
    ll.add_node_to_back(2)
    ll.add_node_to_back(2)
    ll.add_node_to_back(3)
    return ll


def test_add_node_to_back(empty_linkedlist):
    empty_linkedlist.add_node_to_back(1)
    empty_linkedlist.add_node_to_back(2)
    assert empty_linkedlist.__str__() == "1, 2"


def test_add_node_to_front(empty_linkedlist):
    empty_linkedlist.add_node_to_front(1)
    empty_linkedlist.add_node_to_front(2)
    assert empty_linkedlist.__str__() == "2, 1"


def test_remove_single_node_instance(linkedlist_with_nodes):
    linkedlist_with_nodes.remove_single_node_instance(3)
    assert linkedlist_with_nodes.__str__() == "1, 2, 2"


def test_remove_all_instances(linkedlist_with_nodes):
    removed_nodes = linkedlist_with_nodes.remove_all_instances(2)
    assert linkedlist_with_nodes.__str__() == "1, 3"
    assert [node.value for node in removed_nodes.values()] == [2, 2]


def test_remove_all_instances_empty(empty_linkedlist):
    with pytest.raises(ValueError):
        empty_linkedlist.remove_all_instances(2)


def test_remove_all_instances_head(linkedlist_with_nodes):
    removed_nodes = linkedlist_with_nodes.remove_all_instances(1)
    assert linkedlist_with_nodes.__str__() == "2, 2, 3"
    assert [node.value for node in removed_nodes.values()] == [1]


def test_remove_all_instances_tail(linkedlist_with_nodes):
    removed_nodes = linkedlist_with_nodes.remove_all_instances(3)
    assert linkedlist_with_nodes.__str__() == "1, 2, 2"
    assert [node.value for node in removed_nodes.values()] == [3]


def test_remove_all_instances_not_found(linkedlist_with_nodes):
    with pytest.raises(ValueError):
        linkedlist_with_nodes.remove_all_instances(4)
