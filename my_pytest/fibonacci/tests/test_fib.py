from typing import Callable

import pytest

from fibonacci.cached import fibonacci_cached, fibonacci_lru_cached
from fibonacci.dynamic import fibonacci_dynamic, fibonacci_dynamic_v2
from fibonacci.naive import fibonacci_naive


@pytest.mark.parametrize(
    "fib_func",
    [
        fibonacci_naive,
        fibonacci_cached,
        fibonacci_lru_cached,
        fibonacci_dynamic,
        fibonacci_dynamic_v2,
    ],
)
@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_fibonacci(fib_func: Callable[[int], int], n: int, expected: int) -> None:
    res = fib_func(n)
    assert res == expected
