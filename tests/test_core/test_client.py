import os
import pytest
import logging

from ucloud.core.client import Client
from ucloud.core.testing import env

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def client():
    return Client(
        {
            "region": os.getenv("UCLOUD_REGION"),
            "project_id": os.getenv("UCLOUD_PROJECT_ID"),
            "public_key": os.getenv("UCLOUD_PUBLIC_KEY"),
            "private_key": os.getenv("UCLOUD_PRIVATE_KEY"),
            "timeout": 10,
        }
    )


def test_pre_check(client):
    env.pre_check_env()


class TestAccClient:
    @pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
    def test_client_invoke(self, client):
        resp = client.invoke("DescribeUHostInstance")
        assert resp["RetCode"] == 0
