"""Проста реалізація двійкового дерева пошуку."""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    """Додає значення до дерева та повертає його корінь."""
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        # Повторювані значення також зберігаються — у правому піддереві.
        root.right = insert(root.right, value)
    return root


def build_tree(values):
    """Будує дерево зі списку значень."""
    root = None
    for value in values:
        root = insert(root, value)
    return root
