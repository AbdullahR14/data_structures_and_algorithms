import pytest
from src.LinearDataStructures.DoublyLinkedList import DoublyLinkedList


@pytest.fixture
def empty_linkedlist():
    """ Fixture to create an empty DoublyLinkedList instance """
    return DoublyLinkedList()


@pytest.fixture
def linkedlist_with_nodes():
    """ Fixture to create a DoublyLinkedList instance with some nodes """
    ll = DoublyLinkedList()
    ll.add_node_to_back(1)
    ll.add_node_to_back(2)
    ll.add_node_to_back(2)
    ll.add_node_to_back(3)
    return ll


class TestAddNode:
    def test_add_node_to_back(self, empty_linkedlist):
        empty_linkedlist.add_node_to_back(1)
        empty_linkedlist.add_node_to_back(2)
        assert empty_linkedlist.__str__() == "1, 2"

    def test_add_node_to_front(self, empty_linkedlist):
        empty_linkedlist.add_node_to_front(1)
        empty_linkedlist.add_node_to_front(2)
        assert empty_linkedlist.__str__() == "2, 1"


class TestRemoveSingleNode:
    def test_remove_single_node_instance(self, linkedlist_with_nodes):
        linkedlist_with_nodes.remove_single_node_instance(3)
        assert linkedlist_with_nodes.__str__() == "1, 2, 2"

    def test_remove_single_node_instance_empty(self, empty_linkedlist):
        with pytest.raises(ValueError):
            empty_linkedlist.remove_single_node_instance(1)

    def test_remove_single_node_instance_head(self, linkedlist_with_nodes):
        linkedlist_with_nodes.remove_single_node_instance(1)
        assert linkedlist_with_nodes.__str__() == "2, 2, 3"

    def test_remove_single_node_instance_tail(self, linkedlist_with_nodes):
        linkedlist_with_nodes.remove_single_node_instance(3)
        assert linkedlist_with_nodes.__str__() == "1, 2, 2"

    def test_remove_single_node_instance_not_found(self, linkedlist_with_nodes):
        with pytest.raises(ValueError):
            linkedlist_with_nodes.remove_single_node_instance(100)


class TestRemoveAllNodeInstances:
    def test_remove_all_instances(self, linkedlist_with_nodes):
        removed_nodes = linkedlist_with_nodes.remove_all_instances(2)
        assert linkedlist_with_nodes.__str__() == "1, 3"
        assert [node.value for node in removed_nodes.values()] == [2, 2]

    def test_remove_all_instances_empty(self, empty_linkedlist):
        with pytest.raises(ValueError):
            empty_linkedlist.remove_all_instances(2)

    def test_remove_all_instances_head(self, linkedlist_with_nodes):
        removed_nodes = linkedlist_with_nodes.remove_all_instances(1)
        assert linkedlist_with_nodes.__str__() == "2, 2, 3"
        assert [node.value for node in removed_nodes.values()] == [1]

    def test_remove_all_instances_tail(self, linkedlist_with_nodes):
        removed_nodes = linkedlist_with_nodes.remove_all_instances(3)
        assert linkedlist_with_nodes.__str__() == "1, 2, 2"
        assert [node.value for node in removed_nodes.values()] == [3]

    def test_remove_all_instances_not_found(self, linkedlist_with_nodes):
        with pytest.raises(ValueError):
            linkedlist_with_nodes.remove_all_instances(4)
