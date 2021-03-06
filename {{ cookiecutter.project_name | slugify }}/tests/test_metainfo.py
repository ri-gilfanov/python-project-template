import tomli

from {{ cookiecutter.project_name | slugify(separator='_') }} import __version__


def test_version() -> None:
    with open('./pyproject.toml', 'rb') as f:
        pyproject = tomli.load(f)
        version = pyproject['tool']['poetry']['version']
        assert __version__ == version

