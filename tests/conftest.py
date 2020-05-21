import pytest

from home_dashboard.app_init import create_app


@pytest.fixture(scope="session")
def client():
    test_app = create_app()
    test_app.test_client

    return test_app.test_client()
