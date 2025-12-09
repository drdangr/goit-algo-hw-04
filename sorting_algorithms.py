# sorting_algorithms.py

from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """Сортування вставками (повертає новий список)."""
    a = arr[:]  # працюємо з копією, щоб не пошкодити вихідні дані
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        # зсуваємо елементи, які більші за key, вправо
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def _merge(left: List[int], right: List[int]) -> List[int]:
    """Злиття двох відсортованих списків."""
    result = []
    i = j = 0

    # поки є елементи в обох половинах — вибираємо мінімальний
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # додаємо хвости, якщо залишилися елементи
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr: List[int]) -> List[int]:
    """Сортування злиттям (повертає новий список)."""
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def timsort(arr: List[int]) -> List[int]:
    """Обгортка над вбудованим sorted (Timsort)."""
    return sorted(arr)

if __name__ == "__main__":
    sample_data = [5, 2, 9, 1, 5, 6]
    print("Insertion Sort:", insertion_sort(sample_data))
    print("Merge Sort:", merge_sort(sample_data))
    print("Timsort:", timsort(sample_data))

"""Модуль, що реалізує різні алгоритми сортування."""
