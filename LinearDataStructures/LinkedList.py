from typing import Any


class Node:
    def __init__(self, value: Any, next_node=None) -> None:
        """
        Initialise a new node with the given value and optional next_node reference.

        :param value: The value to store in the node.
        :param next_node: Reference to the next node in the sequence.
        """
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, head_node: Node = None) -> None:
        """
        Initialise a linked list with an optional head node.

        :param head_node: The initial head node of the linked list.
        """
        self.head_node = head_node

    def add_node(self, value: Any) -> None:
        """
        Add a new node with the given value to the end of the linked list.

        Time Complexity:
            - Empty List: O(1)
            - Non-empty List: O(n), where n is the number of nodes in the list.

        Space Complexity: O(1)

        :param value: The value to add to the linked list.
        """
        new_node = Node(value)
        if not self.head_node:
            self.head_node = new_node
        else:
            current_node = self.head_node
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def remove_node(self, value_to_remove: Any) -> Node:
        """
        Remove the first occurrence of a node with the given value from the linked list.

        Time Complexity:
            - Empty List: O(1)
            - Value at Head: O(1)
            - Value in Middle or Tail: O(n)

        Space Complexity: O(1)

        :param value_to_remove: The value to search for and remove from the linked list.
        :return: The removed node
        :raises ValueError: If the value is not found in the linked list.
        """
        # Empty List
        if not self.head_node:
            raise ValueError("The Linked List is empty")

        # Value matches head node
        if self.head_node.value == value_to_remove:
            removed_node = self.head_node
            self.head_node = self.head_node.next_node
            if self.head_node:
                self.head_node.prev_node = None  # Update the new head's prev_node reference
            return removed_node

        current_node = self.head_node
        while current_node.next_node:
            if current_node.next_node.value == value_to_remove:
                removed_node = current_node.next_node
                current_node.next_node = current_node.next_node.next_node
                if current_node.next_node:
                    current_node.next_node.prev_node = current_node  # Update next node's prev_node reference
                return removed_node
            current_node = current_node.next_node

        raise ValueError("Value not found in Linked List")

    def __str__(self) -> str:
        """
        Return a string representation of the linked list.

        Time Complexity: O(n), where n is the number of nodes in the list.
        Space Complexity: O(n), for the result_list storing the values of nodes.

        :return: A comma-separated string of node values or "Empty List" for an empty list.
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
