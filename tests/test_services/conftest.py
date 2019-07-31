import os
import pytest

from ucloud.client import Client
from ucloud.testing import utest


@pytest.fixture(scope="session", autouse=True, name="client")
def client_factory() -> Client:
    return Client(
        {
            "region": os.getenv("UCLOUD_REGION"),
            "project_id": os.getenv("UCLOUD_PROJECT_ID"),
            "public_key": os.getenv("UCLOUD_PUBLIC_KEY"),
            "private_key": os.getenv("UCLOUD_PRIVATE_KEY"),
            "max_retries": 3,
            "timeout": 60,
        }
    )


@pytest.fixture(scope="module", autouse=True, name="variables")
def variables_factory() -> dict:
    return {
        "Region": "cn-bj2",
        "Zone": "cn-bj2-05",
        "ProjectId": os.getenv("UCLOUD_PROJECT_ID"),
    }


@pytest.fixture(scope="module", autouse=True, name="test_set")
def test_set_factory(client, variables):
    return utest.TestSet(client, variables)
