import nox


@nox.session(reuse_venv=True, venv_backend="venv")
def tests(session: nox.Session) -> None:
    session.install("-r", "test-requirements.txt")
    session.install(".")
    session.run("pytest")
