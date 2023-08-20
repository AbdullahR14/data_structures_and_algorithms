from typing import Any, Dict


class DoubleNode:
    def __init__(self, value: Any, next_node=None, prev_node=None) -> None:
        """
        Initialise a new node with the given value and optional next and previous node references
        :param value: The value to store in the node
        :param next_node: Reference to the next node in the sequence
        :param prev_node: Reference to the previous node in the sequence
        """
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class DoublyLinkedList:
    def __init__(self, head_node: DoubleNode = None, tail_node: DoubleNode = None) -> None:
        """
        Initialises a doubly linked list with optional head and tail nodes.

        :param head_node: The initial head node of the linked list
        :param tail_node: The initial tail node of the linked list a
        """
        self.head_node = head_node
        self.tail_node = tail_node

    def add_node_to_back(self, value: Any) -> None:
        """
        Adds a new node with the given value to the back of the doubly linked list.

        Time Complexity:
            - Empty List: O(1)
            - One Node: O(1)
            - Multiple Nodes: O(1)

        Space Complexity: O(1)

        :param value: The value to add to the back of the linked list
        """
        new_node = DoubleNode(value)

        # Empty List
        if not self.head_node and not self.tail_node:
            self.head_node = new_node
            self.tail_node = new_node
            return

        # One Node
        if self.head_node == self.tail_node:
            self.head_node.next_node = new_node
            new_node.prev_node = self.head_node
            self.tail_node = new_node
            return

        # Multiple Nodes
        self.tail_node.next_node = new_node
        new_node.prev_node = self.tail_node
        self.tail_node = new_node

    def add_node_to_front(self, value: Any) -> None:
        """
        Adds a new node with the given value to the front of the doubly linked list.

        Time Complexity:
            - Empty List: O(1)
            - One Node: O(1)
            - Multiple Nodes: O(1)

        Space Complexity: O(1)

        :param value: The value to add to the front of the linked list
        """
        new_node = DoubleNode(value)

        # Empty List
        if not self.head_node and not self.tail_node:
            self.head_node = new_node
            self.tail_node = new_node
            return

        # One Node
        if self.head_node == self.tail_node:
            self.head_node.prev_node = new_node
            new_node.next_node = self.head_node
            self.head_node = new_node
            return

        # Multiple Nodes
        self.head_node.prev_node = new_node
        new_node.next_node = self.head_node
        self.head_node = new_node

    def remove_single_node_instance(self, value_to_remove: Any) -> DoubleNode:
        """
        Removes a single instance of a node with the given value from the doubly linked list.

        Time Complexity:
            - Empty List: O(1)
            - Value at Head: O(1)
            - Value in Middle or tail: O(n)

        Space Complexity: O(1)

        :param value_to_remove: The value to search for and remove from the linked list.
        :return: The removed node
        :raises ValueError: If the value is not found in the linked list
        """
        # Empty List
        if not self.head_node:
            raise ValueError("The Linked List is empty")

        # Value matches head node
        if self.head_node.value == value_to_remove:
            if self.head_node.next_node:
                self.head_node.next_node.prev_node = None
            self.head_node = self.head_node.next_node
            return self.head_node

        current_node = self.head_node
        while current_node.next_node:
            if current_node.next_node.value == value_to_remove:
                if current_node.next_node.next_node:
                    current_node.next_node.next_node.prev_node = current_node
                current_node.next_node = current_node.next_node.next_node
                return current_node.next_node

            current_node = current_node.next_node

        raise ValueError("Value not found in Linked List")

    def remove_all_instances(self, value_to_remove: Any) -> Dict[int, DoubleNode]:
        """
        Removes all instances of nodes with the given value from the doubly linked list
        and returns a list of nodes containing the removed value.

        Time Complexity: O(n), where n is the number of nodes in the linked list.
        Space Complexity: O(1) for removal, O(k) for the returned list, where k is the number of removed nodes.

        :param value_to_remove: The value to search for and remove all instances of
        :return: A Dict of removed nodes with the key being the nodes position
        :raises ValueError:  if the value is not found in the linked list
        """
        removed_nodes = {}

        # Empty list
        if not self.head_node:
            raise ValueError("The Linked List is empty")

        # Remove from head
        position = 0
        while self.head_node and self.head_node.value == value_to_remove:
            removed_nodes[position] = self.head_node
            self.head_node = self.head_node.next_node
            if self.head_node:
                self.head_node.prev_node = None
            position += 1

        # Remove from middle and tail
        current_position = position
        current_node = self.head_node
        while current_node and current_node.next_node:
            if current_node.next_node.value == value_to_remove:
                removed_nodes[current_position] = current_node.next_node
                current_node.next_node = current_node.next_node.next_node
                if current_node.next_node:
                    current_node.next_node.prev_node = current_node
                current_position += 1
            else:
                current_node = current_node.next_node

        if not removed_nodes:
            raise ValueError("Value not found in Linked List")

        return removed_nodes

    def __str__(self) -> str:
        """
        Returns a string representation of the doubly linked list

        Time Complexity: O(n), where n is the number of nodes in the linked list.
        Space Complexity: O(n), as the result_list stores the values of all nodes.

        :return: A comma-seperated string of node values or "Empty List" for an empty list
        """
        # Empty List
        if not self.head_node:
            return "Empty List"

        result_list = []
        current_node = self.head_node
        while current_node:
            result_list.append(str(current_node.value))
            current_node = current_node.next_node
        return ", ".join(result_list)
