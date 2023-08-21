from typing import Any


class Node:
    def __init__(self, value: Any, next_node=None) -> None:
        """
        Initialise a new node with the given value

        :param value: The value to store in the node
        :param next_node: Reference to the next node in the sequence
        """
        self.value = value
        self.next_node = next_node

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

    def get_value(self) -> Any:
        """
        Getter method that returns the value assigned to the node

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: the value assigned to the node
        """
        return self.value


class Queue:
    def __init__(self, max_size=None) -> None:
        """
        Initialise a queue with an optional max size

        :param max_size: The maximum size of the queue
        """
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def add_to_queue(self, value) -> None:
        """
        Add a new node to the end of the queue

        Time Complexity: O(1)
        Space Complexity O(1)

        :param value: Value to assign to the node to be added to the end of the queue
        :raises ValueError: if the queue is full
        """
        # If the queue is full
        if not self.has_space():
            raise ValueError("The Queue is full")

        # Instantiate the node
        item = Node(value)

        # If queue is empty
        if self.is_empty():
            self.head = item
            self.tail = item
        # If queue is not empty
        else:
            self.tail.set_next_node(item)
            self.tail = item

        # Increase the size of the queue by 1
        self.increment_queue()

    def remove_from_queue(self) -> Any:
        """
        Remove a node from the front of the queue

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: The value of the removed item
        :raises ValueError: If the queue is empty
        """
        # If queue is empty
        if self.get_size() == 0:
            raise ValueError("The Queue is empty")

        item_to_remove = self.head

        # If there is one element in the queue
        if self.get_size() == 1:
            self.head = None
            self.tail = None

        # If there are multiple elements in the queue
        else:
            # Set the head of the queue as the next node in sequence
            self.head = self.head.get_next_node()

        # Decrement the size of the queue by 1
        self.decrement_queue()

        # Return the removed value
        return item_to_remove.get_value()

    def get_first_element(self) -> Any:
        """
        Returns the value of the first element of the queue

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: value of the first queue element
        :raises ValueError: If the queue is empty
        """
        # If Queue is empty
        if self.get_size() == 0:
            raise ValueError("The Queue is empty")

        # If there is a head node
        return self.head.get_value()

    def get_size(self) -> int:
        """
        Returns the size of the Queue

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: the size of the queue
        """
        return self.size

    def has_space(self) -> bool:
        """
        Checks whether the queue has space

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: boolean indicating if there is any space in the queue
        """
        # If there is no max size
        if self.max_size is None:
            return True

        # Check if the size is less than the max size
        return self.max_size > self.get_size()

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: boolean indicating if the queue is empty
        """
        return self.size == 0

    def increment_queue(self, n: int = 1) -> None:
        """
        Increase the size of the queue

        Time Complexity: O(1)
        Space Complexity: O(1)

        :param n: Amount to increment by, Default = 1
        """
        self.size += n

    def decrement_queue(self, n: int = 1) -> None:
        """
        Decrease the size of the queue

        Time Complexity: O(1)
        Space Complexity: O(1)

        :param n: Amount to decrement by, Default = 1
        """
        self.size -= n
