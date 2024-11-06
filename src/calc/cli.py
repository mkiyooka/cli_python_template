"""Provide command line interface

コマンドラインインターフェースを提供する
"""

import argparse
import sys

from . import arithmetic_ops
from .__about__ import __version__


def create_parser():
    """create_parser オプションパーサー生成

    オプションパーサーを生成する

    Returns:
        subparsers: parse_args(argv) メソッドを持つparserを返す
    """
    parser = argparse.ArgumentParser(description="python cli program template")
    version = "%(prog)s " + __version__
    parser.add_argument("--version", "-v", action="version", version=version)
    subparsers = parser.add_subparsers(title="subcommand add & sub op")

    parser_add = subparsers.add_parser("add", help="see `add -h`")
    parser_add.add_argument(
        "lhs", metavar="lhs", type=int, help="left-hand side of addition operator"
    )
    parser_add.add_argument(
        "rhs", metavar="rhs", type=int, help="right-hand side ofadditionplus operator"
    )
    parser_add.set_defaults(
        func=lambda args: print(arithmetic_ops.add(args.lhs, args.rhs))
    )
    parser_mul = subparsers.add_parser("mul", help="see `sub -h`")
    parser_mul.add_argument(
        "lhs", metavar="lhs", type=int, help="left-hand side of multiply operator"
    )
    parser_mul.add_argument(
        "rhs", metavar="rhs", type=int, help="right-hand side of multiply operator"
    )
    parser_mul.set_defaults(
        func=lambda args: print(arithmetic_ops.mul(args.lhs, args.rhs))
    )

    parser_help = subparsers.add_parser("help", help="see `help -h`")
    parser_help.add_argument("command", help="command name which help is shown")
    parser_help.set_defaults(
        func=lambda args: print(parser.parse_args([args.command, "--help"]))
    )

    return parser


def cli_main():
    """main関数

    main関数
    """
    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
