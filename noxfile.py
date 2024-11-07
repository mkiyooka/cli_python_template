from pathlib import Path

import nox


@nox.session(venv_backend="uv", python=["3.12"], tags=["lint"])
def lint(session):
    session.install(".")
    session.install("ruff")
    session.run("ruff", "check")
    session.run("ruff", "format")


@nox.session(venv_backend="uv", python=["3.12"], tags=["mypy"])
def mypy(session):
    session.install(".")
    session.install("mypy")
    session.run("mypy", "src")


@nox.session(venv_backend="uv", python=["3.12"], tags=["test"])
def test(session):
    session.install(".")

    if session.posargs:
        test_files = session.posargs
    else:
        test_files = ["tests"]

    session.run("pytest", *test_files)
    try:
        session.run("coverage", "run", "-m", "pytest", *session.posargs)
    finally:
        session.notify("coverage")


@nox.session(venv_backend="uv", python=["3.12", "3.13"], tags=["test coverage"])
def coverage(session):
    session.install(".")
    if any(Path().glob(".coverage.*")):
        session.run("coverage", "combine")
    session.run("coverage", "report")
