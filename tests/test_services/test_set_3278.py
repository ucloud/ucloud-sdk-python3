""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import pytest
import logging

from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)


scenario = utest.Scenario(3278)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_3278(client: utest.Client, variables: dict):
    scenario.initial(variables)

    scenario.variables[
        "Image_Id_cloud"
    ] = "#{u_get_image_resource($Region,$Zone)}"
    scenario.variables["saopaulo_image"] = "uimage-1bkjka"

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

    variables["Image_Id_cloud"] = utest.value_at_path(
        resp, "ImageSet.0.ImageId"
    )
    return resp


@scenario.step(
    max_retries=10,
    retry_interval=10,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateUHostInstance",
)
def create_uhost_instance_01(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "TimemachineFeature": "No",
        "Tag": "Default",
        "Region": variables.get("Region"),
        "Password": "VXFhNzg5VGVzdCFAIyQ7LA==",
        "Name": "ulb-host",
        "Memory": 1024,
        "LoginMode": "Password",
        "ImageId": variables.get("Image_Id_cloud"),
        "HotplugFeature": False,
        "DiskSpace": 0,
        "CPU": 1,
    }

    try:
        resp = client.uhost().create_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["UHostId_01"] = utest.value_at_path(resp, "UHostIds.0")
    variables["IP_01"] = utest.value_at_path(resp, "IPs.0")
    return resp


@scenario.step(
    max_retries=10,
    retry_interval=10,
    startup_delay=180,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateULB",
)
def create_ulb_02(client: utest.Client, variables: dict):
    d = {
        "ULBName": "测试",
        "Tag": "Default",
        "Region": variables.get("Region"),
        "InnerMode": "No",
    }

    try:
        resp = client.ulb().create_ulb(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["ULBId"] = utest.value_at_path(resp, "ULBId")
    return resp


@scenario.step(
    max_retries=10,
    retry_interval=10,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 4107)],
    action="CreateVServer",
)
def create_vserver_03(client: utest.Client, variables: dict):
    d = {
        "VServerName": "vserver-test",
        "ULBId": variables.get("ULBId"),
        "Region": variables.get("Region"),
        "Protocol": "HTTP",
        "PersistenceType": "UserDefined",
        "PersistenceInfo": "huangchao",
        "Method": "Roundrobin",
        "ListenType": "RequestProxy",
        "FrontendPort": 80,
        "ClientTimeout": 60,
    }

    try:
        resp = client.ulb().create_vserver(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=10,
    retry_interval=10,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("len_eq", "DataSet", 1),
    ],
    action="DescribeVServer",
)
def describe_vserver_04(client: utest.Client, variables: dict):
    d = {"ULBId": variables.get("ULBId"), "Region": variables.get("Region")}

    try:
        resp = client.ulb().describe_vserver(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["VServerId"] = utest.value_at_path(resp, "DataSet.0.VServerId")
    return resp


@scenario.step(
    max_retries=10,
    retry_interval=10,
    startup_delay=30,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 63016)],
    action="AllocateBackend",
)
def allocate_backend_05(client: utest.Client, variables: dict):
    d = {
        "VServerId": variables.get("VServerId"),
        "ULBId": variables.get("ULBId"),
        "ResourceType": "UHost",
        "ResourceId": variables.get("UHostId_01"),
        "Region": variables.get("Region"),
        "Port": 80,
        "Enabled": 1,
    }

    try:
        resp = client.ulb().allocate_backend(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=10,
    retry_interval=10,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("len_eq", "DataSet.0.BackendSet", 1),
    ],
    action="DescribeVServer",
)
def describe_vserver_06(client: utest.Client, variables: dict):
    d = {
        "VServerId": variables.get("VServerId"),
        "ULBId": variables.get("ULBId"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.ulb().describe_vserver(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["BackendId"] = utest.value_at_path(
        resp, "DataSet.0.BackendSet.0.BackendId"
    )
    return resp


@scenario.step(
    max_retries=10,
    retry_interval=10,
    startup_delay=30,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreatePolicy",
)
def create_policy_07(client: utest.Client, variables: dict):
    d = {
        "VServerId": variables.get("VServerId"),
        "ULBId": variables.get("ULBId"),
        "Type": "Domain",
        "Region": variables.get("Region"),
        "Match": "www.test.com",
        "BackendId": [variables.get("BackendId")],
    }

    try:
        resp = client.ulb().create_policy(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["PolicyId"] = utest.value_at_path(resp, "PolicyId")
    return resp


@scenario.step(
    max_retries=10,
    retry_interval=10,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="UpdatePolicy",
)
def update_policy_08(client: utest.Client, variables: dict):
    d = {
        "VServerId": variables.get("VServerId"),
        "ULBId": variables.get("ULBId"),
        "Type": "Domain",
        "Region": variables.get("Region"),
        "PolicyId": variables.get("PolicyId"),
        "Match": "www.testgai.com",
        "BackendId": [variables.get("BackendId")],
    }

    try:
        resp = client.ulb().update_policy(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=10,
    retry_interval=10,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeletePolicy",
)
def delete_policy_09(client: utest.Client, variables: dict):
    d = {
        "VServerId": variables.get("VServerId"),
        "Region": variables.get("Region"),
        "PolicyId": variables.get("PolicyId"),
    }

    try:
        resp = client.ulb().delete_policy(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=10,
    retry_interval=10,
    startup_delay=30,
    fast_fail=False,
    action="DeleteULB",
)
def delete_ulb_10(client: utest.Client, variables: dict):
    d = {"ULBId": variables.get("ULBId"), "Region": variables.get("Region")}

    try:
        resp = client.ulb().delete_ulb(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=30,
    startup_delay=5,
    fast_fail=False,
    action="PoweroffUHostInstance",
)
def poweroff_uhost_instance_11(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostId": variables.get("UHostId_01"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.uhost().poweroff_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=60,
    fast_fail=False,
    action="TerminateUHostInstance",
)
def terminate_uhost_instance_12(client: utest.Client, variables: dict):
    d = {
        "Zone": variables.get("Zone"),
        "UHostId": variables.get("UHostId_01"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.uhost().terminate_uhost_instance(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp
