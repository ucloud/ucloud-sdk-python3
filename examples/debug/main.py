import os
import logging
import random

from ucloud.client import Client
from ucloud.helpers import wait, utils

logging.basicConfig()
logger = logging.getLogger('ucloud')
logger.setLevel(logging.DEBUG)
from pprint import pprint


def main():
    client = Client({
        "region": "cn-bj2",
        "project_id": os.getenv("UCLOUD_PROJECT_ID"),
        "public_key": os.getenv("UCLOUD_PUBLIC_KEY"),
        "private_key": os.getenv("UCLOUD_PRIVATE_KEY"),
    })

    client.uhost().create_uhost_instance({
        'CPU': "i am not a integer",
    })


if __name__ == '__main__':
    main()
