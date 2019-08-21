import os
import logging
import random

from ucloud.client import Client
from ucloud.helpers import wait, utils

logger = logging.getLogger("ucloud")
logger.setLevel(logging.DEBUG)

# NOTE: find your public/private key at
# website `UAPI <https://console.ucloud.cn/uapi/apikey>`_
client = Client(
    {
        "region": "cn-bj2",
        "project_id": os.getenv("UCLOUD_PROJECT_ID"),
        "public_key": os.getenv("UCLOUD_PUBLIC_KEY"),
        "private_key": os.getenv("UCLOUD_PRIVATE_KEY"),
    }
)


def main():
    image_id = describe_image()

    uhost_ids = create_uhost_batch(image_id, 2)

    ulb_id = create_ulb()

    vserver_id = create_vserver(ulb_id)

    backend_ids = allocate_backend_batch(ulb_id, vserver_id, uhost_ids)

    backend_ids and release_backend_batch(ulb_id, vserver_id, backend_ids)

    vserver_id and delete_vserver(ulb_id, vserver_id)

    ulb_id and delete_ulb(ulb_id)

    uhost_ids and delete_uhost_batch(uhost_ids)


def describe_image():
    images = (
        client.uhost().describe_image({"ImageType": "Base"}).get("ImageSet", [])
    )
    if not images:
        return
    image = random.choice(images)
    return image.get("ImageId")


def mget_uhost_states(uhost_ids):
    resp = client.uhost().describe_uhost_instance({"UHostIds": uhost_ids})
    return [inst.get("State") for inst in resp.get("UHostSet")]


def create_uhost_batch(image_id, count):
    resp = client.uhost().create_uhost_instance(
        {
            "Name": "sdk-python3-example-two-tier",
            "Zone": "cn-bj2-05",
            "ImageId": image_id,
            "LoginMode": "Password",
            "Password": utils.gen_password(20),
            "CPU": 1,
            "Memory": 1024,
            "MaxCount": count,
        }
    )
    uhost_ids = resp.get("UHostIds", [])
    wait.wait_for_state(
        target=["running"],
        pending=["pending"],
        timeout=300,
        refresh=lambda: (
            "running"
            if all(
                [state == "Running" for state in mget_uhost_states(uhost_ids)]
            )
            else "pending"
        ),
    )
    return uhost_ids


def create_ulb():
    resp = client.ulb().create_ulb({"Name": "sdk-python3-example-two-tier"})
    return resp.get("ULBId")


def create_vserver(ulb_id):
    resp = client.ulb().create_vserver(
        {"Name": "sdk-python3-example-two-tier", "ULBId": ulb_id}
    )
    return resp.get("VServerId")


def allocate_backend_batch(ulb_id, vserver_id, uhost_ids):
    backend_ids = []
    for uhost_id in uhost_ids:
        resp = client.ulb().allocate_backend(
            {
                "ULBId": ulb_id,
                "VServerId": vserver_id,
                "ResourceId": uhost_id,
                "ResourceType": "UHost",
            }
        )
        backend_ids.append(resp.get("BackendId"))
    return backend_ids


def release_backend_batch(ulb_id, vserver_id, backend_ids):
    for backend_id in backend_ids:
        client.ulb().release_backend(
            {"ULBId": ulb_id, "VServerId": vserver_id, "BackendId": backend_id}
        )


def delete_vserver(ulb_id, vserver_id):
    client.ulb().delete_vserver({"ULBId": ulb_id, "VServerId": vserver_id})


def delete_ulb(ulb_id):
    client.ulb().delete_ulb({"ULBId": ulb_id})


def delete_uhost_batch(uhost_ids):
    for uhost_id in uhost_ids:
        client.uhost().stop_uhost_instance({"UHostId": uhost_id})

    wait.wait_for_state(
        target=["stopped"],
        pending=["pending"],
        timeout=300,
        refresh=lambda: (
            "stopped"
            if all(
                [state == "Stopped" for state in mget_uhost_states(uhost_ids)]
            )
            else "pending"
        ),
    )

    for uhost_id in uhost_ids:
        client.uhost().terminate_uhost_instance({"UHostId": uhost_id})


if __name__ == "__main__":
    main()
