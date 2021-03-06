# home-dashboard
a dash board for the home built using flask

## Setup

Requires python version: `3.8.*`

Setup a virtualenv and install requirements
```bash
python -m venv ./.venv
python --version  # 3.8.2
source .venv/bin/activate
pip install -r requirements.txt

# install precommit hooks
pre-commit install
```

Then to run the server locally:

```bash
python main.py
```

## Formatting and linting

[Black](https://black.readthedocs.io/en/stable/) and [flake 8](https://flake8.pycqa.org/en/latest/) is used for linting and formatting. If pre-commit is installed this will black will format on `git commit`

To run these on the command line:
```bash
# linting
flake8 .

# formatting
black . --exclude .venv
```

## Testing

[pytest](https://docs.pytest.org/en/latest/contents.html) is used for testing.

Run tests using `pytest` - this will run all tests with pattern following [this](https://docs.pytest.org/en/latest/getting-started.html#run-multiple-tests).

```bash
# all tests
pytest

# specific test
pytest tests/test_apples.py

# specific function in a file
pytest tests/test_apples.py::test_apples_taste_good
```

## Contributing
Branch off the master branch. Create a PR and make sure all CI (continuous integration) stages pass. CI is used for running tests, linting and formatting.
