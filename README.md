# home-dashboard
a dash board for the home built using flask

## Setup

Python version: `3.8.*`

Setup a virtualenv and install requirements
```bash
python -m venv ./.venv
python --version  # 3.8.2
source .venv/bin/activate
pip install -r requirements.txt

# install precommit hooks
pre-commit install
```

## Formatting

[Black](https://black.readthedocs.io/en/stable/) is used as an autoformatter. If pre-commit is installed properly this 

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
TODO
- PR
- CI pipeline
  - failures and stuff
  - flake, black, tests
