from typing import Any, List


class TreeNode:
    def __init__(self, value: Any) -> None:
        """
        Initialise a new tree node with the given value

        :param value: The value to store in the node
        """
        self.value = value
        self.children: List[TreeNode] = []

    def add_child(self, child_node) -> None:
        """
        Add a child node to the current node

        Time Complexity: O(1)
        Space Complexity: O(1)

        :param child_node: The child node to add
        """
        self.children.append(child_node)

    def remove_child(self, child_node) -> None:
        """
        Remove a child node from the current node

        Time Complexity: O(n)
        Space Complexity: O(1)

        :param child_node: The child node to remove
        :raises ValueError: If the child node is not found in the children
        """
        if child_node not in self.children:
            raise ValueError("Child node not found in children")
        self.children.remove(child_node)

    def get_value(self) -> Any:
        """
        Getter method that returns the value of the node

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: The value of the node
        """
        return self.value

    def print_tree_diagram(self, prefix: str = "", is_tail: bool = True) -> None:
        """
        Print a tree diagram of the current node and its children

        Time Complexity: O(n)
        Space Complexity: O(n)

        :param prefix: The prefix to print before the current node
        :param is_tail: Whether the current node is the last child of its parent
        """
        marker = "└── " if is_tail else "├── "
        print(prefix + marker + str(self.value))
        child_count = len(self.children)
        for i, child in enumerate(self.children):
            is_last_child = (i == child_count - 1)
            child_prefix = prefix + ("│   " if not is_tail and i < child_count else "    ")
            child.print_tree_diagram(child_prefix, is_last_child)
