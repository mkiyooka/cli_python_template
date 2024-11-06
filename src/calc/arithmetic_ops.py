def add(lhs: int | float, rhs: int | float) -> int | float:
    """加算関数

    足し算を行う関数。

    Args:
        lhs (int | float): Left hand side
        rhs (int | float): Right hand side

    Returns:
        (int|float): lhs と rhs の和

    Examples:
            関数の使い方

            >>> add(2, 3)
            5
    """
    return lhs + rhs


def sub(lhs: int | float, rhs: int | float):
    """減算関数

    減算を行う関数。

    Args:
        lhs (int|float): Left hand side
        rhs (int|float): Right hand side

    Returns:
        (int|float): lhs から rhs を減算した差
    """
    return lhs - rhs


def mul(lhs: int | float, rhs: int | float) -> int | float:
    """乗算関数

    掛け算を行う関数。

    Args:
        lhs (int|float): Left hand side
        rhs (int|float): Right hand side

    Returns:
        num: lhs * rhs
    """
    return lhs * rhs


def div(lhs: int | float, rhs: int | float) -> int | float:
    """割り算関数

    割り算関数

    Args:
        lhs (int | float): 左辺
        rhs (int | float): 右辺

    Returns:
        int | float: lhsをrhsによる商
    """
    return lhs // rhs
