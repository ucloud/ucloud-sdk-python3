""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import pytest
import logging

from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)


scenario = utest.Scenario(255)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_503(client: utest.Client, variables: dict):
    scenario.initial(variables)

    scenario.variables["Region"] = "cn-bj2"
    scenario.variables["Zone"] = "cn-bj2-02"
    scenario.variables["DBTypeId"] = "mysql-5.7"
    scenario.variables["InstanceMode"] = "HA"
    scenario.variables["InstanceType"] = "Normal"
    scenario.variables["Port"] = 3306
    scenario.variables["MemoryLimit"] = 1000
    scenario.variables["DiskSpace"] = 20
    scenario.variables["DBName"] = "auto_habz_"
    scenario.variables["UseSSD"] = False

    scenario.run(client)


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUDBType",
)
def describe_udb_type_00(client: utest.Client, variables: dict):
    d = {"Zone": variables.get("Zone"), "Region": variables.get("Region")}

    try:
        resp = client.udb().describe_udb_type(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUDBParamGroup",
)
def describe_udb_param_group_01(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "Offset": 0,
        "Limit": 100,
    }

    try:
        resp = client.udb().describe_udb_param_group(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["DataSet_paramGroup"] = utest.value_at_path(resp, "DataSet")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUDBInstancePrice",
)
def describe_udb_instance_price_02(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "MemoryLimit": variables.get("MemoryLimit"),
        "DiskSpace": variables.get("DiskSpace"),
        "DBTypeId": variables.get("DBTypeId"),
        "Count": 1,
    }

    try:
        resp = client.udb().describe_udb_instance_price(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CheckUDBInstanceAllowance",
)
def check_udb_instance_allowance_03(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UseSSD": variables.get("UseSSD"),
        "Region": variables.get("Region"),
        "MemoryLimit": variables.get("MemoryLimit"),
        "DiskSpace": variables.get("DiskSpace"),
        "Count": 1,
        "ClassType": "SQL",
    }

    try:
        resp = client.invoke("CheckUDBInstanceAllowance", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=1,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateUDBInstance",
)
def create_udb_instance_04(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "Quantity": 0,
        "Port": variables.get("Port"),
        "ParamGroupId": funcs.search_value(
            variables.get("DataSet_paramGroup"),
            "DBTypeId",
            variables.get("DBTypeId"),
            "GroupId",
        ),
        "Name": funcs.concat(
            variables.get("DBName"), variables.get("DBTypeId")
        ),
        "MemoryLimit": variables.get("MemoryLimit"),
        "InstanceType": variables.get("InstanceType"),
        "InstanceMode": variables.get("InstanceMode"),
        "DiskSpace": variables.get("DiskSpace"),
        "DBTypeId": variables.get("DBTypeId"),
        "ChargeType": "Month",
        "AdminPassword": "guanliyuanmima",
    }

    try:
        resp = client.udb().create_udb_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["DBId"] = utest.value_at_path(resp, "DBId")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        (
            "str_eq",
            "DataSet.0.Name ",
            funcs.concat(variables.get("DBName"), variables.get("DBTypeId")),
        ),
        ("str_eq", "DataSet.0.DBTypeId", variables.get("DBTypeId")),
    ],
    action="DescribeUDBInstance",
)
def describe_udb_instance_05(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "Offset": 0,
        "Limit": 100,
        "DBId": variables.get("DBId"),
        "ClassType": "sql",
    }

    try:
        resp = client.udb().describe_udb_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=50,
    retry_interval=10,
    startup_delay=30,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "State", "Running"),
    ],
    action="DescribeUDBInstanceState",
)
def describe_udb_instance_state_06(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "DBId": variables.get("DBId"),
    }

    try:
        resp = client.udb().describe_udb_instance_state(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUDBInstanceUpgradePrice",
)
def describe_udb_instance_upgrade_price_07(
    client: utest.Client, variables: dict
):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "MemoryLimit": variables.get("MemoryLimit") + 1,
        "DiskSpace": variables.get("DiskSpace") + 1,
        "DBId": variables.get("DBId"),
    }

    try:
        resp = client.udb().describe_udb_instance_upgrade_price(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CheckUDBInstanceAllowance",
)
def check_udb_instance_allowance_08(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UseSSD": variables.get("UseSSD"),
        "Region": variables.get("Region"),
        "MemoryLimit": variables.get("MemoryLimit") + 1,
        "DiskSpace": variables.get("DiskSpace") + 1,
        "Count": 1,
        "ClassType": "SQL",
    }

    try:
        resp = client.invoke("CheckUDBInstanceAllowance", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=60,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="ResizeUDBInstance",
)
def resize_udb_instance_09(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UseSSD": variables.get("UseSSD"),
        "Region": variables.get("Region"),
        "MemoryLimit": variables.get("MemoryLimit") + 1,
        "DiskSpace": variables.get("DiskSpace") + 1,
        "DBId": variables.get("DBId"),
    }

    try:
        resp = client.udb().resize_udb_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=90,
    retry_interval=10,
    startup_delay=240,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        (
            "str_eq",
            "DataSet.0.Name ",
            funcs.concat(variables.get("DBName"), variables.get("DBTypeId")),
        ),
        ("str_eq", "DataSet.0.DBTypeId", variables.get("DBTypeId")),
        ("str_eq", "DataSet.0.State", "Running"),
        ("str_eq", "DataSet.0.MemoryLimit", variables.get("MemoryLimit") + 1),
        ("str_eq", "DataSet.0.DiskSpace", variables.get("DiskSpace") + 10),
    ],
    action="DescribeUDBInstance",
)
def describe_udb_instance_10(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "Offset": 0,
        "Limit": 100,
        "DBId": variables.get("DBId"),
        "ClassType": "sql",
    }

    try:
        resp = client.udb().describe_udb_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="StopUDBInstance",
)
def stop_udb_instance_11(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "DBId": variables.get("DBId"),
    }

    try:
        resp = client.udb().stop_udb_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=100,
    retry_interval=3,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        (
            "str_eq",
            "DataSet.0.Name ",
            funcs.concat(variables.get("DBName"), variables.get("DBTypeId")),
        ),
        ("str_eq", "DataSet.0.DBTypeId", variables.get("DBTypeId")),
        ("str_eq", "DataSet.0.State", "Shutoff"),
    ],
    action="DescribeUDBInstance",
)
def describe_udb_instance_12(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "Offset": 0,
        "Limit": 100,
        "DBId": variables.get("DBId"),
        "ClassType": "sql",
    }

    try:
        resp = client.udb().describe_udb_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=10,
    fast_fail=False,
    action="DeleteUDBInstance",
)
def delete_udb_instance_13(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "DBId": variables.get("DBId"),
    }

    try:
        resp = client.udb().delete_udb_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp
