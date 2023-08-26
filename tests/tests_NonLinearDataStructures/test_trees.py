import pytest

from src.NonLinearDataStructures.Trees import TreeNode


@pytest.fixture
def sample_tree():
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(TreeNode(4))
    child1.add_child(TreeNode(5))
    child2.add_child(TreeNode(6))
    return root


@pytest.fixture
def empty_tree():
    return TreeNode(1)


@pytest.fixture
def multi_level_tree():
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    grandchild1 = TreeNode(4)
    grandchild2 = TreeNode(5)
    grandchild3 = TreeNode(6)
    great_grandchild1 = TreeNode(7)
    great_grandchild2 = TreeNode(8)
    great_grandchild3 = TreeNode(9)
    great_grandchild4 = TreeNode(10)
    great_grandchild5 = TreeNode(11)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(grandchild1)
    child1.add_child(grandchild2)
    child2.add_child(grandchild3)
    grandchild1.add_child(great_grandchild1)
    grandchild1.add_child(great_grandchild2)
    grandchild2.add_child(great_grandchild3)
    grandchild2.add_child(great_grandchild4)
    grandchild3.add_child(great_grandchild5)
    return root


class TestAddChild:
    def test_add_child(self, sample_tree):
        sample_tree.add_child(TreeNode(7))
        assert sample_tree.children[2].value == 7

    def test_add_child_empty(self, empty_tree):
        empty_tree.add_child(TreeNode(2))
        assert empty_tree.children[0].value == 2


class TestRemoveChild:
    def test_remove_child(self, sample_tree):
        sample_tree.remove_child(sample_tree.children[0])
        assert sample_tree.children[0].value == 3

    def test_remove_child_empty(self, empty_tree):
        with pytest.raises(ValueError):
            empty_tree.remove_child(TreeNode(2))


class TestPrintTreeDiagram:
    def test_print_tree_diagram(self, sample_tree, capsys):
        sample_tree.print_tree_diagram()
        captured = capsys.readouterr()
        assert "\n" + captured.out == """
└── 1
    ├── 2
    │   ├── 4
    │   └── 5
    └── 3
        └── 6
"""

    def test_print_tree_diagram_empty(self, empty_tree, capsys):
        empty_tree.print_tree_diagram()
        captured = capsys.readouterr()
        assert captured.out == "└── 1\n"

    def test_print_tree_diagram_multi_level(self, multi_level_tree, capsys):
        multi_level_tree.print_tree_diagram()
        captured = capsys.readouterr()
        assert "\n" + captured.out == """
└── 1
    ├── 2
    │   ├── 4
    │   │   ├── 7
    │   │   └── 8
    │   └── 5
    │       ├── 9
    │       └── 10
    └── 3
        └── 6
            └── 11
"""
