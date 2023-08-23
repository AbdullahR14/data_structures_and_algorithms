from typing import Any
from enum import Enum

from LinearDataStructures.Node import Node


class QueueState(Enum):
    """ Enum to represent the state of the queue (NOT IMPLEMENTED YET) """
    FULL = 0
    ACCEPTING = 1
    EMPTY = 2


class Queue:
    def __init__(self, max_size: int = None) -> None:
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

    def __str__(self) -> str:
        """
        Returns a string representation of the Queue

        Time Complexity: O(n)
        Space Complexity: O(n)

        :return: A comma-seperated string of node values or "Empty List" for an empty Queue
        """
        # Empty Queue
        if self.is_empty():
            return "Empty Queue"

        result_list = []
        current_element = self.head
        while current_element:
            result_list.append(str(current_element.get_value()))
            current_element = current_element.get_next_node()
        return ", ".join(result_list)

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
