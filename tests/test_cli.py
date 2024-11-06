from src.calc import cli


def test_create_parser(capfd):
    parser = cli.create_parser()

    args = parser.parse_args(["add", "10", "20"])
    if hasattr(args, "func"):
        args.func(args)
    out, err = capfd.readouterr()
    assert out.strip() == "30"
    assert err.strip() == ""

    args = parser.parse_args(["mul", "10", "20"])
    args.func(args)
    out, err = capfd.readouterr()
    assert out.strip() == "200"
    assert err.strip() == ""
