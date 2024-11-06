# Test

::: tests.test_arithmetic_ops.test_add

``` py title="sample.py" linenums="2" hl_lines="2-4"
from src.calc import arithmetic_operations


def test_add():
    assert arithmetic_operations.add(1, 1) == 2 # (1)
    assert arithmetic_operations.add(2, 3) == 5


def test_sub():
    assert arithmetic_operations.sub(1, 1) == 0
    assert arithmetic_operations.sub(2, 3) == -1


def test_mul():
    assert arithmetic_operations.mul(2, 3) == 6


def test_div():
    assert arithmetic_operations.div(1, 1) == 1
    assert arithmetic_operations.div(2, 3) == 0
```

1. this is annotation.
