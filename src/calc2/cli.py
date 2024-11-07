"""Provide command line interface

コマンドラインインターフェースを提供する
"""

from _version import __version__
from common import arithmetic_ops


def add(lhs: int = 0, rhs: int = 0) -> None:
    """加算関数"""
    print(arithmetic_ops.add(lhs, rhs))


def mul(lhs: int, rhs: int) -> None:
    """乗算関数"""
    print(arithmetic_ops.mul(lhs, rhs))


def version() -> None:
    """print version"""
    print(f"{__version__}")


def main_cli() -> None:
    """main関数

    main関数
    """
    from jsonargparse import CLI

    CLI([add, mul], version=__version__)
