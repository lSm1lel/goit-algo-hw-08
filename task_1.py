"""Завдання 1. Найменше значення у двійковому дереві пошуку."""

from binary_tree import build_tree


def find_min(root):
    """Повертає найменше значення або None, якщо дерево порожнє."""
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left
    return current.value


def main():
    values = [10, 5, 15, 3, 7, 12, 18]
    root = build_tree(values)
    print("Завдання 1. Найменше значення в дереві")
    print("Значення для побудови дерева:", values)
    print("Найменше значення:", find_min(root))


if __name__ == "__main__":
    main()
