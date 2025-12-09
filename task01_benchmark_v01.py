# benchmark.py

import random
import timeit
from typing import List, Callable, Dict

from sorting_algorithms import insertion_sort, merge_sort, timsort


def generate_random_list(n: int) -> List[int]:
    return [random.randint(0, n) for _ in range(n)]


def generate_sorted_list(n: int) -> List[int]:
    return list(range(n))


def generate_reversed_list(n: int) -> List[int]:
    return list(range(n, 0, -1))


def generate_almost_sorted_list(n: int, swaps: int = 10) -> List[int]:
    """Майже відсортований список: кілька випадкових перестановок."""
    arr = list(range(n))
    for _ in range(min(swaps, n)):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def measure_time(
    func: Callable[[List[int]], List[int]],
    data: List[int],
    number: int = 5
) -> float:
    """Вимірює час виконання func(data.copy()) number разів."""
    def wrapper():
        func(data.copy())

    return timeit.timeit(wrapper, number=number)

def run_benchmarks():
    sizes = [1_000, 5_000, 10_000, 20_000]
    data_generators: Dict[str, Callable[[int], List[int]]] = {
        "random": generate_random_list,
        "sorted": generate_sorted_list,
        "reversed": generate_reversed_list,
        "almost_sorted": generate_almost_sorted_list,
    }

    algorithms: Dict[str, Callable[[List[int]], List[int]]] = {
        "insertion_sort": insertion_sort,
        "merge_sort": merge_sort,
        "timsort": timsort,
    }

    repeats = 3

    for size in sizes:
        print(f"\n=== Size: {size} ===")
        for data_name, gen in data_generators.items():
            data = gen(size)
            print(f"\n  Dataset: {data_name}")
            for algo_name, algo in algorithms.items():
                t = measure_time(algo, data, number=repeats)
                print(f"    {algo_name}: {t:.4f} s (repeats={repeats})")

if __name__ == "__main__":
    run_benchmarks()              