from typing import Any


class SingleNode:
    def __init__(self, value: Any, next_node=None) -> None:
        """
        Initialise a new node with the given value

        :param value: The value to store in the node
        :param next_node: Reference to the next node in the sequence
        """
        self.value = value
        self.next_node = next_node

    def get_value(self) -> Any:
        """
        Getter method that returns the value assigned to the node

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: the value assigned to the node
        """
        return self.value

    def get_next_node(self):
        """
        Getter method that returns the next node in the sequence

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: next node in the sequence or None if there is none
        """
        return self.next_node

    def set_next_node(self, next_node) -> None:
        """
        Setter method that sets the next_node in the sequence

        Time Complexity: O(1)
        Space Complexity O(1)

        :param next_node: next node in the sequence
        """
        self.next_node = next_node
