""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import pytest
import logging

from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)


scenario = utest.Scenario(255)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_283(client: utest.Client, variables: dict):
    scenario.initial(variables)

    scenario.variables["HostName"] = "auto_host_test1"
    scenario.variables["Password"] = "Z3VhbmxpeXVhbm1pbWExMjMhQCM="
    scenario.variables["ChargeType"] = "Month"
    scenario.variables["CreateCPU"] = 1
    scenario.variables["CreateMem"] = 1024
    scenario.variables["ImageId"] = "#{u_get_image_resource($Region,$Zone)}"
    scenario.variables["BootSize"] = 20
    scenario.variables["BootType"] = "CLOUD_SSD"
    scenario.variables["BootBackup"] = "NONE"
    scenario.variables["DiskSize"] = 20
    scenario.variables["DiskType"] = "CLOUD_NORMAL"
    scenario.variables["DiskBackup"] = "NONE"
    scenario.variables["UHostType"] = "N2"
    scenario.variables["UDiskType"] = "DataDisk"
    scenario.variables["UDiskName"] = "auto_udisk_noArk"
    scenario.variables["UDataArkMode"] = "No"
    scenario.variables["Size"] = 1

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

    variables["ImageId"] = utest.value_at_path(resp, "ImageSet.0.ImageId")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUDiskPrice",
)
def describe_udisk_price_01(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDataArkMode": variables.get("UDataArkMode"),
        "Size": variables.get("Size"),
        "Region": variables.get("Region"),
        "Quantity": 1,
        "DiskType": variables.get("UDiskType"),
        "ChargeType": "Month",
    }

    try:
        resp = client.udisk().describe_udisk_price(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=True,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CheckUDiskAllowance",
)
def check_udisk_allowance_02(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Size": variables.get("Size"),
        "Region": variables.get("Region"),
        "Count": 1,
    }

    try:
        resp = client.invoke("CheckUDiskAllowance", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=1,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateUDisk",
)
def create_udisk_03(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDataArkMode": variables.get("UDataArkMode"),
        "Size": variables.get("Size"),
        "Region": variables.get("Region"),
        "Quantity": 0,
        "Name": variables.get("UDiskName"),
        "DiskType": variables.get("UDiskType"),
        "ChargeType": "Month",
    }

    try:
        resp = client.udisk().create_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["udisk_noArk_id"] = utest.value_at_path(resp, "UDiskId.0")
    return resp


@scenario.step(
    max_retries=20,
    retry_interval=3,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeUDiskResponse"),
        ("str_eq", "DataSet.0.Status", "Available"),
        ("str_eq", "DataSet.0.Tag", "Default"),
    ],
    action="DescribeUDisk",
)
def describe_udisk_04(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="RenameUDisk",
)
def rename_udisk_05(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskName": funcs.concat("re_", variables.get("UDiskName")),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().rename_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        (
            "str_eq",
            "DataSet.0.Name",
            funcs.concat("re_", variables.get("UDiskName")),
        ),
    ],
    action="DescribeUDisk",
)
def describe_udisk_06(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
        "Offset": 0,
        "Limit": 100,
    }

    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeUDiskUpgradePriceResponse"),
    ],
    action="DescribeUDiskUpgradePrice",
)
def describe_udisk_upgrade_price_07(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "SourceId": variables.get("udisk_noArk_id"),
        "Size": variables.get("Size") + 1,
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().describe_udisk_upgrade_price(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "ResizeUDiskResponse"),
    ],
    action="ResizeUDisk",
)
def resize_udisk_08(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Size": variables.get("Size") + 1,
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().resize_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeUDiskResponse"),
        ("str_eq", "DataSet.0.Size", variables.get("Size") + 1),
    ],
    action="DescribeUDisk",
)
def describe_udisk_09(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


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
def describe_image_10(client: utest.Client, variables: dict):
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

    variables["ImageId"] = utest.value_at_path(resp, "ImageSet.0.ImageId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "CreateUHostInstanceResponse"),
    ],
    action="CreateUHostInstance",
)
def create_uhost_instance_11(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostType": variables.get("UHostType"),
        "TimemachineFeature": "No",
        "Tag": "Default",
        "Region": variables.get("Region"),
        "Quantity": 1,
        "Password": "VGVzdDEyMzRUZXN0MTIzNA==",
        "NetCapability": "Normal",
        "Name": variables.get("HostName"),
        "Memory": variables.get("CreateMem"),
        "LoginMode": "Password",
        "ImageId": variables.get("ImageId"),
        "HotplugFeature": False,
        "GPU": False,
        "Disks": [
            {
                "BackupType": variables.get("BootBackup"),
                "IsBoot": True,
                "Size": variables.get("BootSize"),
                "Type": variables.get("BootType"),
            }
        ],
        "ChargeType": variables.get("ChargeType"),
        "CPU": variables.get("CreateCPU"),
    }

    try:
        resp = client.uhost().create_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["uhost_id"] = utest.value_at_path(resp, "UHostIds.0")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=30,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "UHostSet.0.UHostId", variables.get("uhost_id")),
    ],
    action="DescribeUHostInstance",
)
def describe_uhost_instance_12(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostIds": [variables.get("uhost_id")],
        "Region": variables.get("Region"),
    }

    try:
        resp = client.uhost().describe_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=120,
    retry_interval=5,
    startup_delay=0,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "UHostSet.0.State", "Running"),
    ],
    action="DescribeUHostInstance",
)
def describe_uhost_instance_13(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostIds": [variables.get("uhost_id")],
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
    startup_delay=1,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("ne", "TotalCount", 0),
    ],
    action="DescribeUHostLite",
)
def describe_uhost_lite_14(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "Offset": 0,
        "Limit": 60,
    }

    try:
        resp = client.invoke("DescribeUHostLite", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=60,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="AttachUDisk",
)
def attach_udisk_15(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostId": variables.get("uhost_id"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().attach_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=200,
    retry_interval=3,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.Status", "InUse"),
    ],
    action="DescribeUDisk",
)
def describe_udisk_16(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
        "Offset": 0,
        "Limit": 100,
    }

    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "UDiskId", variables.get("udisk_noArk_id")),
        ("str_eq", "UHostId", variables.get("uhost_id")),
    ],
    action="DetachUDisk",
)
def detach_udisk_17(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostId": variables.get("uhost_id"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().detach_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=60,
    retry_interval=5,
    startup_delay=60,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.Status", "Available"),
    ],
    action="DescribeUDisk",
)
def describe_udisk_18(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
        "Offset": 0,
        "Limit": 100,
    }

    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteUDisk",
)
def delete_udisk_19(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.udisk().delete_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="PoweroffUHostInstance",
)
def poweroff_uhost_instance_20(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostId": variables.get("uhost_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.uhost().poweroff_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=20,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "UHostSet.0.State", "Stopped"),
    ],
    action="DescribeUHostInstance",
)
def describe_uhost_instance_21(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostIds": [variables.get("uhost_id")],
        "Region": variables.get("Region"),
    }

    try:
        resp = client.uhost().describe_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=3,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="TerminateUHostInstance",
)
def terminate_uhost_instance_22(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostId": variables.get("uhost_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.uhost().terminate_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp
