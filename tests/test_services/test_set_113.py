""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import pytest
import logging

from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)


scenario = utest.Scenario(113)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_113(client: utest.Client, variables: dict):
    scenario.initial(variables)

    scenario.variables["Region"] = "cn-bj2"
    scenario.variables["Zone"] = "cn-bj2-02"

    scenario.run(client)


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=3,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateUFSVolume",
)
def create_ufs_volume_00(client: utest.Client, variables: dict):
    d = {"Zone": variables.get("Zone"), "Size": 1024, "Region": variables.get("Region")}

    try:
        resp = client.invoke("CreateUFSVolume", d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["Volume_Id"] = utest.value_at_path(resp, "VolumeId")
    variables["Volume_Name"] = utest.value_at_path(resp, "VolumeName")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUFSVolume",
)
def describe_ufs_volume_01(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "VolumeId": variables.get("Volume_Id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.invoke("DescribeUFSVolume", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUHostLite",
)
def describe_uhost_lite_02(client: utest.Client, variables: dict):
    d = {"Zone": variables.get("Zone"), "Region": variables.get("Region")}

    try:
        resp = client.invoke("DescribeUHostLite", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUFSVolume",
)
def describe_ufs_volume_03(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "VolumeId": "Volume_Id",
        "Region": variables.get("Region"),
    }

    try:
        resp = client.invoke("DescribeUFSVolume", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="ClearUFSVolumeWhiteList",
)
def clear_ufs_volume_white_list_04(client: utest.Client, variables: dict):
    d = {"VolumeId": variables.get("Volume_Id"), "Region": variables.get("Region")}

    try:
        resp = client.invoke("ClearUFSVolumeWhiteList", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUFSVolume",
)
def describe_ufs_volume_05(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "VolumeId": "Volume_Id",
        "Region": variables.get("Region"),
    }

    try:
        resp = client.invoke("DescribeUFSVolume", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="ExtendUFSVolume",
)
def extend_ufs_volume_06(client: utest.Client, variables: dict):
    d = {
        "VolumeId": variables.get("Volume_Id"),
        "Size": 2048,
        "Region": variables.get("Region"),
    }

    try:
        resp = client.invoke("ExtendUFSVolume", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUFSVolume",
)
def describe_ufs_volume_07(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "VolumeId": "Volume_Id",
        "Region": variables.get("Region"),
    }

    try:
        resp = client.invoke("DescribeUFSVolume", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=30,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="RemoveUFSVolume",
)
def remove_ufs_volume_08(client: utest.Client, variables: dict):
    d = {"VolumeId": variables.get("Volume_Id"), "Region": variables.get("Region")}

    try:
        resp = client.invoke("RemoveUFSVolume", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp
