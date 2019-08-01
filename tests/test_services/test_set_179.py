""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import pytest
import logging

from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)


scenario = utest.Scenario(255)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_179(client: utest.Client, variables: dict):
    scenario.initial(variables)

    scenario.variables["Region"] = "cn-bj2"
    scenario.variables["Zone"] = "cn-bj2-02"
    scenario.variables["DBTypeId"] = "mongodb-3.2"
    scenario.variables["InstanceMode"] = "Normal"
    scenario.variables["InstanceType"] = "Normal"
    scenario.variables["Port"] = 27017
    scenario.variables["MemoryLimit"] = 600
    scenario.variables["DiskSpace"] = 20
    scenario.variables["DBName"] = "AUTO-"
    scenario.variables["UseSSD"] = False
    scenario.variables["GroupName"] = "mongodb3.2默认WiredTiger-configsvr配置"
    scenario.variables["GroupNameMongos"] = "mongodb3.2默认mongos配置"

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
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeUDBParamGroupResponse"),
    ],
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
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateUDBInstance",
)
def create_udb_instance_02(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "Quantity": 1,
        "Port": variables.get("Port"),
        "ParamGroupId": funcs.search_value(
            variables.get("DataSet_paramGroup"),
            "GroupName",
            variables.get("GroupName"),
            "GroupId",
        ),
        "Name": "auto-config3.2",
        "MemoryLimit": variables.get("MemoryLimit"),
        "InstanceType": "Normal",
        "InstanceMode": "Configsvr",
        "DiskSpace": variables.get("DiskSpace"),
        "DBTypeId": variables.get("DBTypeId"),
        "ChargeType": "Month",
        "AdminUser": "root",
        "AdminPassword": "guanliyuanmima",
    }

    try:
        resp = client.udb().create_udb_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["configid"] = utest.value_at_path(resp, "DBId")
    return resp


@scenario.step(
    max_retries=10,
    retry_interval=10,
    startup_delay=500,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "State", "Running"),
    ],
    action="DescribeUDBInstanceState",
)
def describe_udb_instance_state_03(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "DBId": variables.get("configid"),
    }

    try:
        resp = client.udb().describe_udb_instance_state(d)
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
        ("str_eq", "Action", "CreateUDBRouteInstanceResponse"),
    ],
    action="CreateUDBRouteInstance",
)
def create_udb_route_instance_04(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "Port": variables.get("Port"),
        "ParamGroupId": funcs.search_value(
            variables.get("DataSet_paramGroup"),
            "GroupName",
            variables.get("GroupNameMongos"),
            "GroupId",
        ),
        "Name": "mongos-auto",
        "MemoryLimit": variables.get("MemoryLimit"),
        "DiskSpace": variables.get("DiskSpace"),
        "DBTypeId": variables.get("DBTypeId"),
        "ConfigsvrId": [variables.get("configid")],
    }

    try:
        resp = client.udb().create_udb_route_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["DBId"] = utest.value_at_path(resp, "DBId")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=20,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="ModifyUDBInstanceName",
)
def modify_udb_instance_name_05(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "Name": "Rename-auto-data3.0",
        "DBId": variables.get("DBId"),
    }

    try:
        resp = client.udb().modify_udb_instance_name(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=180,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="RestartUDBInstance",
)
def restart_udb_instance_06(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "DBId": variables.get("DBId"),
    }

    try:
        resp = client.udb().restart_udb_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="BackupUDBInstanceErrorLog",
)
def backup_udb_instance_error_log_07(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "DBId": variables.get("DBId"),
        "BackupName": "errorlog-test",
    }

    try:
        resp = client.udb().backup_udb_instance_error_log(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=1,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUDBLogPackage",
)
def describe_udb_log_package_08(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Type": 4,
        "Region": variables.get("Region"),
        "Offset": 0,
        "Limit": 100,
        "DBId": variables.get("DBId"),
    }

    try:
        resp = client.udb().describe_udb_log_package(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["backupidlog"] = utest.value_at_path(resp, "DataSet.0.BackupId")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=1,
    fast_fail=False,
    action="DescribeUDBBinlogBackupURL",
)
def describe_udb_binlog_backup_url_09(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "DBId": variables.get("DBId"),
        "BackupId": variables.get("backupidlog"),
    }

    try:
        resp = client.udb().describe_udb_binlog_backup_url(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteUDBLogPackage",
)
def delete_udb_log_package_10(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "BackupId": variables.get("backupidlog"),
    }

    try:
        resp = client.udb().delete_udb_log_package(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=10,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="ClearUDBLog",
)
def clear_udb_log_11(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "LogType": 30,
        "DBId": variables.get("DBId"),
    }

    try:
        resp = client.udb().clear_udb_log(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=60,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="StopUDBInstance",
)
def stop_udb_instance_12(client: utest.Client, variables: dict):
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
    max_retries=3,
    retry_interval=1,
    startup_delay=60,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="StopUDBInstance",
)
def stop_udb_instance_13(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "DBId": variables.get("configid"),
    }

    try:
        resp = client.udb().stop_udb_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=90,
    fast_fail=False,
    action="DeleteUDBInstance",
)
def delete_udb_instance_14(client: utest.Client, variables: dict):
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


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=90,
    fast_fail=False,
    action="DeleteUDBInstance",
)
def delete_udb_instance_15(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "DBId": variables.get("configid"),
    }

    try:
        resp = client.udb().delete_udb_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp
