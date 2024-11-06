from src.calc import arithmetic_ops


def test_add():
    assert arithmetic_ops.add(1, 1) == 2
    assert arithmetic_ops.add(2, 3) == 5


def test_sub():
    assert arithmetic_ops.sub(1, 1) == 0
    assert arithmetic_ops.sub(2, 3) == -1


def test_mul():
    assert arithmetic_ops.mul(2, 3) == 6


def test_div():
    assert arithmetic_ops.div(1, 1) == 1
    assert arithmetic_ops.div(2, 3) == 0
