"""Завдання 3. З'єднання кабелів із мінімальними загальними витратами."""

import heapq


def min_connection_cost(lengths, show_steps=False):
    """Повертає мінімальну вартість; за потреби друкує порядок з'єднань.

    Довжини мають бути невід'ємними числами. Вхідний список не змінюється.
    Для порожнього списку або одного кабелю витрати дорівнюють нулю.
    """
    heap = list(lengths)
    if any(length < 0 for length in heap):
        raise ValueError("Довжини кабелів не можуть бути від'ємними")

    heapq.heapify(heap)
    total_cost = 0

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        combined = first + second
        total_cost += combined
        heapq.heappush(heap, combined)

        if show_steps:
            print(f"З'єднуємо {first} + {second} = {combined}")

    return total_cost


def main():
    lengths = [4, 3, 2, 6]
    print("Завдання 3. Мінімальні витрати на з'єднання кабелів")
    print("Довжини кабелів:", lengths)
    total_cost = min_connection_cost(lengths, show_steps=True)
    print("Мінімальні загальні витрати:", total_cost)


if __name__ == "__main__":
    main()
