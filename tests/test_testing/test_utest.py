import pytest

from ucloud.testing import utest


def test_value_at_path():
    d = {
        'Action': 'DescribeEIPResponse',
        'EIPSet': [{
            'Resource': {
                'ResourceID': 'uhost-war3png3', 'ResourceName': 'eip-s1-bgp', 'ResourceType': 'uhost',
                'Zone': 'cn-bj2-05'
            },
        }],
        'RetCode': 0, 'TotalBandwidth': 6, 'TotalCount': 3
    }
    assert utest.value_at_path(d, "EIPSet.0.Resource.ResourceID") == 'uhost-war3png3'
