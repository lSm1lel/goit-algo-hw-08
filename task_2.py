"""Завдання 2. Сума всіх значень у двійковому дереві пошуку."""

from binary_tree import build_tree


def sum_tree(root):
    """Рекурсивно підсумовує всі вузли; для порожнього дерева повертає 0."""
    if root is None:
        return 0
    return root.value + sum_tree(root.left) + sum_tree(root.right)


def main():
    values = [10, 5, 15, 3, 7, 12, 18]
    root = build_tree(values)
    print("Завдання 2. Сума всіх значень у дереві")
    print("Значення для побудови дерева:", values)
    print("Сума всіх значень:", sum_tree(root))


if __name__ == "__main__":
    main()
