""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import pytest
import logging

from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)


scenario = utest.Scenario(255)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_2174(client: utest.Client, variables: dict):
    scenario.initial(variables)

    scenario.variables["ConfigId"] = "03f58ca9-b64d-4bdd-abc7-c6b9a46fd801"
    scenario.variables["Password"] = "Z3VhbmxpeXVhbm1pbWE="
    scenario.variables["HighAvailability"] = "disable"
    scenario.variables["Version"] = 3.2
    scenario.variables["Protocol"] = "redis"
    scenario.variables["ResourceType"] = "single"
    scenario.variables["Name"] = "single_redis"

    scenario.run(client)


@scenario.step(
    max_retries=50,
    retry_interval=10,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateURedisGroup",
)
def create_uredis_group_00(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Version": variables.get("Version"),
        "Size": 1,
        "Region": variables.get("Region"),
        "Quantity": 1,
        "Protocol": variables.get("Protocol"),
        "Name": variables.get("Name"),
        "HighAvailability": variables.get("HighAvailability"),
        "ConfigId": variables.get("ConfigId"),
        "ChargeType": "Month",
        "BackupTime": 3,
        "AutoBackup": "enable",
    }

    try:
        resp = client.umem().create_uredis_group(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["group_id"] = utest.value_at_path(resp, "GroupId")
    return resp


@scenario.step(
    max_retries=30,
    retry_interval=10,
    startup_delay=20,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.State", "Running"),
    ],
    action="DescribeUMem",
)
def describe_umem_01(client: utest.Client, variables: dict):
    d = {
        "ResourceType": variables.get("ResourceType"),
        "ResourceId": variables.get("group_id"),
        "Region": variables.get("Region"),
        "Protocol": variables.get("Protocol"),
        "Offset": 0,
        "Limit": 1000,
    }

    try:
        resp = client.invoke("DescribeUMem", d)
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
        ("str_eq", "Action", "CheckURedisAllowanceResponse"),
    ],
    action="CheckURedisAllowance",
)
def check_uredis_allowance_02(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "SlaveZone": variables.get("Zone"),
        "Size": 1,
        "Region": variables.get("Region"),
        "Count": 1,
    }

    try:
        resp = client.invoke("CheckURedisAllowance", d)
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
        ("str_eq", "Action", "CreateURedisBackupResponse"),
    ],
    action="CreateURedisBackup",
)
def create_uredis_backup_03(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "GroupId": variables.get("group_id"),
        "BackupName": "backup_Redis",
    }

    try:
        resp = client.invoke("CreateURedisBackup", d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["backup_id"] = utest.value_at_path(resp, "BackupId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.State", "Running"),
    ],
    action="DescribeUMem",
)
def describe_umem_04(client: utest.Client, variables: dict):
    d = {
        "ResourceType": variables.get("ResourceType"),
        "ResourceId": variables.get("group_id"),
        "Region": variables.get("Region"),
        "Protocol": variables.get("Protocol"),
        "Offset": 0,
        "Limit": 1000,
    }

    try:
        resp = client.invoke("DescribeUMem", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeURedisBackupStateResponse"),
    ],
    action="DescribeURedisBackupState",
)
def describe_uredis_backup_state_05(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "GroupId": variables.get("group_id"),
        "BackupId": variables.get("backup_id"),
    }

    try:
        resp = client.invoke("DescribeURedisBackupState", d)
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
        ("str_eq", "Action", "DescribeURedisBackupResponse"),
    ],
    action="DescribeURedisBackup",
)
def describe_uredis_backup_06(client: utest.Client, variables: dict):
    d = {"Region": variables.get("Region")}

    try:
        resp = client.umem().describe_uredis_backup(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeURedisBackupURLResponse"),
    ],
    action="DescribeURedisBackupURL",
)
def describe_uredis_backup_url_07(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "BackupId": variables.get("backup_id"),
    }

    try:
        resp = client.umem().describe_uredis_backup_url(d)
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
        ("str_eq", "Action", "DeleteURedisBackupResponse"),
    ],
    action="DeleteURedisBackup",
)
def delete_uredis_backup_08(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "BackupId": variables.get("backup_id"),
    }

    try:
        resp = client.invoke("DeleteURedisBackup", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=15,
    retry_interval=5,
    startup_delay=30,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DeleteURedisGroupResponse"),
    ],
    action="DeleteURedisGroup",
)
def delete_uredis_group_09(client: utest.Client, variables: dict):
    d = {
        "Region": variables.get("Region"),
        "GroupId": variables.get("group_id"),
    }

    try:
        resp = client.umem().delete_uredis_group(d)
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
        ("str_eq", "Action", "DescribeURedisGroupResponse"),
        ("object_not_contains", "DataSet", variables.get("group_id")),
    ],
    action="DescribeURedisGroup",
)
def describe_uredis_group_10(client: utest.Client, variables: dict):
    d = {
        "Region": variables.get("Region"),
        "Offset": 0,
        "Limit": 100,
        "GroupId": variables.get("group_id"),
    }

    try:
        resp = client.umem().describe_uredis_group(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp
