"""Provide command line interface

コマンドラインインターフェースを提供する
"""

import typer

from _version import __version__
from common import arithmetic_ops

app = typer.Typer()


@app.command()
def add(lhs: int = 0, rhs: int = 0) -> None:
    """加算関数"""
    print(arithmetic_ops.add(lhs, rhs))


@app.command()
def mul(lhs: int, rhs: int) -> None:
    """乗算関数"""
    print(arithmetic_ops.mul(lhs, rhs))


@app.command()
def version() -> None:
    """Print the version and exit"""
    print(f"{__version__}")


def version_callback(value: bool) -> None:
    if value:
        print(f"{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Print the version and exit",
    ),
) -> None:
    """main関数

    main関数
    """
    pass


def main_cli() -> None:
    app()
