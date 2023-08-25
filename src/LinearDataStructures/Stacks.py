from typing import Any, Union

from src.LinearDataStructures.SingleNode import SingleNode


class Stack:
    def __init__(self, max_size: Union[int, None] = None) -> None:
        """
        Initialise a stack with an optional max size

        :param max_size: The maximum size of the stack
        """
        # Initialise top node as a "None Node"
        self.top_node = SingleNode(None)
        self.max_size = max_size
        self.size = 0

    def add_to_stack(self, value) -> None:
        """
        Add a new node to the top of the stack

        Time Complexity: O(1)
        Space Complexity O(1)

        :param value: Value to assign to the node to be added to the top of the stack
        :raises ValueError: if the stack is full
        """
        # If the stack is full
        if not self.has_space():
            raise ValueError("The Stack is full")

        # Instantiate the node
        item = SingleNode(value)

        # If stack is empty
        if self.is_empty():
            self.top_node = item
        # If stack is not empty
        else:
            item.set_next_node(self.top_node)
            self.top_node = item

        # Increase the size of the stack by 1
        self.increment_stack()

    def remove_from_stack(self) -> Any:
        """
        Remove a node from the top of the stack

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: The value of the removed item
        :raises ValueError: If the stack is empty
        """
        # If stack is empty
        if self.is_empty():
            raise ValueError("The Stack is empty")

        item_to_remove = self.top_node
        self.top_node = item_to_remove.get_next_node()

        # Decrease the size of the stack by 1
        self.decrement_stack()

        return item_to_remove.get_value()

    def get_first_element(self) -> Any:
        """
        Return the value of the top node in the stack

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: The value of the top node in the stack
        """
        # If stack is empty
        if self.is_empty():
            raise ValueError("The Stack is empty")

        return self.top_node.get_value()

    def __str__(self) -> str:
        """
        Return a string representation of the stack

        Time Complexity: O(n)
        Space Complexity: O(n)

        :return: A comma separated string of the stack values or "Empty Stack" for an empty stack
        """
        # If stack is empty
        if self.is_empty():
            return "Empty Stack"

        # If stack is not empty
        result_list = []
        current_node = self.top_node
        while current_node:
            result_list.append(str(current_node.get_value()))
            current_node = current_node.get_next_node()
        return ", ".join(result_list)

    def has_space(self) -> bool:
        """
        Check if the stack has space for another node

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: True if the stack has space for another node, False otherwise
        """
        # If there is no max size
        if self.max_size is None:
            return True

        # If there is a max size
        return self.get_size() < self.max_size

    def is_empty(self) -> bool:
        """
        Check if the stack is empty

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: True if the stack is empty, False otherwise
        """
        return self.get_size() == 0

    def get_size(self) -> int:
        """
        Return the size of the stack

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: The size of the stack
        """
        return self.size

    def increment_stack(self, n: int = 1) -> None:
        """
        Increase the size of the stack

        Time Complexity: O(1)
        Space Complexity: O(1)

        :param n: Amount to increment by, Default = 1
        """
        self.size += n

    def decrement_stack(self, n: int = 1) -> None:
        """
        Decrease the size of the stack

        Time Complexity: O(1)
        Space Complexity: O(1)

        :param n: Amount to decrement by, Default = 1
        """
        self.size -= n
