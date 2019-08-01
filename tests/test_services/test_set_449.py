""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import pytest
import logging

from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)


scenario = utest.Scenario(255)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_449(client: utest.Client, variables: dict):
    scenario.initial(variables)

    scenario.variables["Password"] = "Z3VhbmxpeXVhbm1pbWExMjMhQCM="
    scenario.variables["CreateBootDisk"] = 20
    scenario.variables["ChargeType"] = "Month"
    scenario.variables["CreateCPU"] = 1
    scenario.variables["CreateMem"] = 1024
    scenario.variables["CreateDiskspace"] = 0
    scenario.variables["NewPassword"] = "Z3VhbmxpeXVhbm1pbWExMjMhQCM="
    scenario.variables["Name"] = "uhost-basic-api"
    scenario.variables["ImageID"] = "#{u_get_image_resource($Region,$Zone)}"

    scenario.run(client)


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeImageResponse"),
    ],
    action="DescribeImage",
)
def describe_image_00(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "OsType": "Linux",
        "ImageType": "Base",
    }

    try:
        resp = client.uhost().describe_image(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["ImageID"] = utest.value_at_path(resp, "ImageSet.0.ImageId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=10,
    startup_delay=20,
    fast_fail=True,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateUHostInstance",
)
def create_uhost_instance_01(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "TimemachineFeature": "No",
        "Tag": "Default",
        "StorageType": "LocalDisk",
        "Region": variables.get("Region"),
        "Quantity": 1,
        "Password": "VXFhNzg5VGVzdCFAIyQ7LA==",
        "NetCapability": "Normal",
        "Name": variables.get("Name"),
        "Memory": variables.get("CreateMem"),
        "LoginMode": "Password",
        "ImageId": variables.get("ImageID"),
        "HotplugFeature": False,
        "HostType": "N2",
        "GPU": False,
        "DiskSpace": variables.get("CreateDiskspace"),
        "ChargeType": variables.get("ChargeType"),
        "CPU": variables.get("CreateCPU"),
        "BootDiskSpace": variables.get("CreateBootDisk"),
    }

    try:
        resp = client.uhost().create_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["hostId"] = utest.value_at_path(resp, "UHostIds.0")
    return resp


@scenario.step(
    max_retries=200,
    retry_interval=30,
    startup_delay=60,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "UHostSet.0.BasicImageId", variables.get("ImageID")),
        ("str_eq", "UHostSet.0.CPU", variables.get("CreateCPU")),
        ("str_eq", "UHostSet.0.Memory", variables.get("CreateMem")),
        ("str_eq", "UHostSet.0.UHostId", variables.get("hostId")),
        ("str_eq", "UHostSet.0.Name", variables.get("Name")),
        (
            "str_eq",
            "UHostSet.0.TotalDiskSpace",
            variables.get("CreateDiskspace"),
        ),
        ("str_eq", "UHostSet.0.HostType", "N2"),
        ("str_eq", "UHostSet.0.UHostType", "Normal"),
        ("str_eq", "UHostSet.0.StorageType", "LocalDisk"),
        ("str_eq", "UHostSet.0.State", "Running"),
        ("str_eq", "UHostSet.0.BootDiskState", "Normal"),
    ],
    action="DescribeUHostInstance",
)
def describe_uhost_instance_02(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostIds": [variables.get("hostId")],
        "Region": variables.get("Region"),
    }

    try:
        resp = client.uhost().describe_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=5,
    retry_interval=30,
    startup_delay=10,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "StopUHostInstanceResponse"),
    ],
    action="StopUHostInstance",
)
def stop_uhost_instance_03(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostId": variables.get("hostId"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.uhost().stop_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=30,
    retry_interval=10,
    startup_delay=10,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "UHostSet.0.BasicImageId", variables.get("ImageID")),
        ("str_eq", "UHostSet.0.CPU", variables.get("CreateCPU")),
        ("str_eq", "UHostSet.0.Memory", variables.get("CreateMem")),
        ("str_eq", "UHostSet.0.UHostId", variables.get("hostId")),
        ("str_eq", "UHostSet.0.Name", variables.get("Name")),
        (
            "str_eq",
            "UHostSet.0.TotalDiskSpace",
            variables.get("CreateDiskspace"),
        ),
        ("str_eq", "UHostSet.0.HostType", "N2"),
        ("str_eq", "UHostSet.0.UHostType", "Normal"),
        ("str_eq", "UHostSet.0.StorageType", "LocalDisk"),
        ("str_eq", "UHostSet.0.State", "Stopped"),
    ],
    action="DescribeUHostInstance",
)
def describe_uhost_instance_04(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostIds": [variables.get("hostId")],
        "Region": variables.get("Region"),
    }

    try:
        resp = client.uhost().describe_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=5,
    retry_interval=60,
    startup_delay=30,
    fast_fail=True,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="ReinstallUHostInstance",
)
def reinstall_uhost_instance_05(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostId": variables.get("hostId"),
        "Region": variables.get("Region"),
        "Password": variables.get("NewPassword"),
        "ImageId": variables.get("ImageID"),
    }

    try:
        resp = client.uhost().reinstall_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=200,
    retry_interval=30,
    startup_delay=30,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "UHostSet.0.BasicImageId", variables.get("ImageID")),
        ("str_eq", "UHostSet.0.Memory", variables.get("CreateMem")),
        ("str_eq", "UHostSet.0.UHostId", variables.get("hostId")),
        (
            "str_eq",
            "UHostSet.0.TotalDiskSpace",
            variables.get("CreateDiskspace"),
        ),
        ("str_eq", "UHostSet.0.Name", variables.get("Name")),
        ("str_eq", "UHostSet.0.CPU", variables.get("CreateCPU")),
        ("str_eq", "UHostSet.0.HostType", "N2"),
        ("str_eq", "UHostSet.0.UHostType", "Normal"),
        ("str_eq", "UHostSet.0.StorageType", "LocalDisk"),
        ("str_eq", "UHostSet.0.State", "Running"),
    ],
    action="DescribeUHostInstance",
)
def describe_uhost_instance_06(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostIds": [variables.get("hostId")],
        "Region": variables.get("Region"),
    }

    try:
        resp = client.uhost().describe_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=60,
    startup_delay=30,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="PoweroffUHostInstance",
)
def poweroff_uhost_instance_07(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostId": variables.get("hostId"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.uhost().poweroff_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=30,
    retry_interval=10,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "UHostSet.0.State", "Stopped"),
    ],
    action="DescribeUHostInstance",
)
def describe_uhost_instance_08(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostIds": [variables.get("hostId")],
        "Region": variables.get("Region"),
    }

    try:
        resp = client.uhost().describe_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=60,
    fast_fail=False,
    action="TerminateUHostInstance",
)
def terminate_uhost_instance_09(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostId": variables.get("hostId"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.uhost().terminate_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp
