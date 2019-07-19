import os
import pytest

from ucloud.client import Client


@pytest.fixture(scope="session", autouse=True)
def client() -> Client:
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


@pytest.fixture(scope="module", autouse=True)
def variables() -> dict:
    return {
        "Region": "cn-bj2",
        "Zone": "cn-bj2-05",
        "ProjectId": os.getenv("UCLOUD_PROJECT_ID"),
    }
