# Using pytest
## Creating tests
* Check `backend/pytest.ini` to see what syntax are recognized by pytest

## Run all tests via CLI
* Get into the `backend` docker container with bash and run `pytest -v` (remove `-v` for not-verbose)

## Printing to console during tests
* To see any `print()` statements written inside tests, run `pytest -s`
