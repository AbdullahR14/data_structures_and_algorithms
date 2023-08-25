from typing import Any

from LinearDataStructures.SingleNode import SingleNode


class DoubleNode(SingleNode):
    def __init__(self, value: Any, next_node=None, prev_node=None) -> None:
        """
        Initialise a new node with the given value and optional next and previous node references
        :param value: The value to store in the node
        :param next_node: Reference to the next node in the sequence
        :param prev_node: Reference to the previous node in the sequence
        """
        super().__init__(value, next_node)
        self.prev_node = prev_node

    def get_prev_node(self):
        """
        Getter method that returns the previous node in the sequence

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: previous node in the sequence or None if there is none
        """
        return self.prev_node

    def set_prev_node(self, prev_node) -> None:
        """
        Setter method that sets the prev_node in the sequence

        Time Complexity: O(1)
        Space Complexity O(1)

        :param prev_node: previous node in the sequence
        """
        self.prev_node = prev_node
