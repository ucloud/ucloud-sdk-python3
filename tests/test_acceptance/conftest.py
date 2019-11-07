import json
import os
import pytest

from ucloud.testing.driver import spec
from ucloud.client import Client


@pytest.fixture(scope="session", autouse=True, name="client")
def client_factory() -> Client:
    return Client(
        {
            "region": "cn-bj2",
            "project_id": os.getenv("UCLOUD_PROJECT_ID"),
            "public_key": os.getenv("UCLOUD_PUBLIC_KEY"),
            "private_key": os.getenv("UCLOUD_PRIVATE_KEY"),
            "max_retries": 10,
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


@pytest.fixture(scope="session", autouse=True)
def save_report(request):
    def save_report_handler():
        with open("./report.json", "w") as f:
            json.dump(spec.json(), f)

    request.addfinalizer(save_report_handler)
