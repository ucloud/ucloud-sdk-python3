""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import pytest
import logging

from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)


scenario = utest.Scenario(255)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_2457(client: utest.Client, variables: dict):
    scenario.initial(variables)

    scenario.run(client)


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateVPC",
)
def create_vpc_00(client: utest.Client, variables: dict):
    d = {
        "Region": variables.get("Region"),
        "Network": ["192.168.0.0/16"],
        "Name": "ulb-ssl-vpc",
    }

    try:
        resp = client.vpc().create_vpc(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["vpc_id"] = utest.value_at_path(resp, "VPCId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateSubnet",
)
def create_subnet_01(client: utest.Client, variables: dict):
    d = {
        "VPCId": variables.get("vpc_id"),
        "SubnetName": "ulb-ssl-subnet",
        "Subnet": "192.168.111.0",
        "Region": variables.get("Region"),
    }

    try:
        resp = client.vpc().create_subnet(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["subnet_id"] = utest.value_at_path(resp, "SubnetId")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateULB",
)
def create_ulb_02(client: utest.Client, variables: dict):
    d = {
        "VPCId": variables.get("vpc_id"),
        "ULBName": "ulb-ssl-test",
        "Tag": "Default",
        "SubnetId": variables.get("subnet_id"),
        "Region": variables.get("Region"),
        "InnerMode": "No",
        "ChargeType": "Dynamic",
    }

    try:
        resp = client.ulb().create_ulb(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["ULBId"] = utest.value_at_path(resp, "ULBId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=30,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateVServer",
)
def create_vserver_03(client: utest.Client, variables: dict):
    d = {
        "VServerName": "vserver-test",
        "ULBId": variables.get("ULBId"),
        "Region": variables.get("Region"),
        "Protocol": "HTTPS",
        "PersistenceType": "UserDefined",
        "PersistenceInfo": "huangchao",
        "Method": "Roundrobin",
        "ListenType": "RequestProxy",
        "FrontendPort": 443,
        "ClientTimeout": 60,
    }

    try:
        resp = client.ulb().create_vserver(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["VServerId"] = utest.value_at_path(resp, "VServerId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateSSL",
)
def create_ssl_04(client: utest.Client, variables: dict):
    d = {
        "UserCert": "-----BEGIN CERTIFICATE-----\nMIIFzTCCBLWgAwIBAgIQQ8IswmAhEIKfNhrKqb0F3DANBgkqhkiG9w0BAQsFADCB\nlzELMAkGA1UEBhMCQ04xJTAjBgNVBAoTHFRydXN0QXNpYSBUZWNobm9sb2dpZXMs\nIEluYy4xHzAdBgNVBAsTFlN5bWFudGVjIFRydXN0IE5ldHdvcmsxHTAbBgNVBAsT\nFERvbWFpbiBWYWxpZGF0ZWQgU1NMMSEwHwYDVQQDExhUcnVzdEFzaWEgRFYgU1NM\nIENBIC0gRzUwHhcNMTYxMjA2MDAwMDAwWhcNMTcxMjA2MjM1OTU5WjAgMR4wHAYD\nVQQDDBVtLmVjb2xvZ3ktZW1vYmlsZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IB\nDwAwggEKAoIBAQDxBsuwGdCZdEUs40SQcvUt+9hlmLTgcfkq/h9f1QVPxLq/PC+O\nsG76hOgy6N8f7k7x5XgtPKi9O4ydFl8ViYhEXRjYQcUrTm3lu7s9UT2AIUmK0dI+\nPZgFU5gDwh8fQLoL24T2lPfkD9TngCnDanfo3xbx/e9hsJkf7hKWix8zrxtYYCUT\nt96pTpQeWjr7ggl2bDEfTayJNM+i5xoGBPiQFdxPnKWCjNmXi2dws0d2whi1euRW\ngI5wIXji5WKfUf6EvzG0Uzz6i8vsSLGv8pL7C0AuUI4MrPNDesFeA2LEYclQkpHE\nE49BkpQvCokCW9d8/r5ASUry+7SrJIncU6FxAgMBAAGjggKJMIIChTAgBgNVHREE\nGTAXghVtLmVjb2xvZ3ktZW1vYmlsZS5jb20wCQYDVR0TBAIwADBhBgNVHSAEWjBY\nMFYGBmeBDAECATBMMCMGCCsGAQUFBwIBFhdodHRwczovL2Quc3ltY2IuY29tL2Nw\nczAlBggrBgEFBQcCAjAZDBdodHRwczovL2Quc3ltY2IuY29tL3JwYTAfBgNVHSME\nGDAWgBRtWMd/GufhPy6mjJc1Qrv00zisPzAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0l\nBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMIGbBggrBgEFBQcBAQSBjjCBizA8Bggr\nBgEFBQcwAYYwaHR0cDovL3RydXN0YXNpYTItb2NzcC5kaWdpdGFsY2VydHZhbGlk\nYXRpb24uY29tMEsGCCsGAQUFBzAChj9odHRwOi8vdHJ1c3Rhc2lhMi1haWEuZGln\naXRhbGNlcnR2YWxpZGF0aW9uLmNvbS90cnVzdGFzaWFnNS5jcnQwggEDBgorBgEE\nAdZ5AgQCBIH0BIHxAO8AdQDd6x0reg1PpiCLga2BaHB+Lo6dAdVciI09EcTNtuy+\nzAAAAVjT7zdSAAAEAwBGMEQCIDCzWufc1q7hjmrrCetGyoA8EsEqpRSIhmZXStX5\n8b7zAiA6x5aAaDK+yMyeAgw71yi3tRVrWayHN+W0+4BxC8u5UQB2AO5Lvbd1zmC6\n4UJpH6vhnmajD35fsHLYgwDEe4l6qP3LAAABWNPvN4kAAAQDAEcwRQIgZ/LNgg7n\n7AE4O2yZkrXNcqAOmJ3NU2nT6zcnBxPFTTsCIQCjyPbMfWMZTD3kxgxPQ1COw5zJ\nsM0dfNmSr3MiU7EhqDANBgkqhkiG9w0BAQsFAAOCAQEAeyfgUhg9ZWVCaz0f+BQU\n6fMMfmQ1BDzvVFu+ORoAqyJQogxwIdfjrlz/63YFee5qpUsW/aaz4ma3bb4dpE1K\nGsgYe5N3o0xybYlOj+KB61sufYkzQS3HgDevCwjfUlGEbNl4dpO2xh5s5AANXlnz\ns/X0+AJ33/bm+fWIjAbIjluaEoM6GETHTXi4Tlxy0j3nsXsB9tIIUibAdTtButef\nJJRnikGRN+eHjrsLYe0RUmdKOQz1ik6teHt0MQX0aCe8OlXeyGDd9m8u7+y0nAnH\nTVaNuT7vXMWyyXLVUcV898wkBo3Bo3hUiaw0QR0ttgDrf5ZwqPfqpytRW2K5GMZT\nuw==\n-----END CERTIFICATE-----\n\n\n-----BEGIN CERTIFICATE-----\nMIIFZTCCBE2gAwIBAgIQOhAOfxCeGsWcxf/2QNXkQjANBgkqhkiG9w0BAQsFADCB\nyjELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQL\nExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMjAwNiBWZXJp\nU2lnbiwgSW5jLiAtIEZvciBhdXRob3JpemVkIHVzZSBvbmx5MUUwQwYDVQQDEzxW\nZXJpU2lnbiBDbGFzcyAzIFB1YmxpYyBQcmltYXJ5IENlcnRpZmljYXRpb24gQXV0\naG9yaXR5IC0gRzUwHhcNMTYwODExMDAwMDAwWhcNMjYwODEwMjM1OTU5WjCBlzEL\nMAkGA1UEBhMCQ04xJTAjBgNVBAoTHFRydXN0QXNpYSBUZWNobm9sb2dpZXMsIElu\nYy4xHzAdBgNVBAsTFlN5bWFudGVjIFRydXN0IE5ldHdvcmsxHTAbBgNVBAsTFERv\nbWFpbiBWYWxpZGF0ZWQgU1NMMSEwHwYDVQQDExhUcnVzdEFzaWEgRFYgU1NMIENB\nIC0gRzUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC39aSJZG/97x3a\n6Qmuc9+MubagegRAVUmFYHTYTs8IKB2pM7wXN7W8mekdZaEgUjDFxvRBK/DhTb7U\n8ONLsKKdT86aOhzbz2noCTn9wPWnGwkg+/4YKg/dPQQdV9tMsSu0cwqInWHxSAkm\nAI1hYFC9D7Sf7Hp/5cRcD+dK454YMRzNOGLQnCVI8JEqrz6o9SOvQNTqTcfqt6DC\n0UlXG+MPD1eNPjlzf1Vwaab+VSTgySoC+Ikbq2VsdykeOiGXW/OIiASH7+2LcR05\nPmQ7GEOlM8yzoVojFpM8sHz+WxI05ZOPri5+vX3HhHHjWr5432G0dVmgohnZvlVZ\noy8XrlbpAgMBAAGjggF2MIIBcjASBgNVHRMBAf8ECDAGAQH/AgEAMC8GA1UdHwQo\nMCYwJKAioCCGHmh0dHA6Ly9zLnN5bWNiLmNvbS9wY2EzLWc1LmNybDAOBgNVHQ8B\nAf8EBAMCAQYwLgYIKwYBBQUHAQEEIjAgMB4GCCsGAQUFBzABhhJodHRwOi8vcy5z\neW1jZC5jb20wYQYDVR0gBFowWDBWBgZngQwBAgEwTDAjBggrBgEFBQcCARYXaHR0\ncHM6Ly9kLnN5bWNiLmNvbS9jcHMwJQYIKwYBBQUHAgIwGRoXaHR0cHM6Ly9kLnN5\nbWNiLmNvbS9ycGEwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMCkGA1Ud\nEQQiMCCkHjAcMRowGAYDVQQDExFTeW1hbnRlY1BLSS0yLTYwMTAdBgNVHQ4EFgQU\nbVjHfxrn4T8upoyXNUK79NM4rD8wHwYDVR0jBBgwFoAUf9Nlp8Ld7LvwMAnzQzn6\nAq8zMTMwDQYJKoZIhvcNAQELBQADggEBABUphhBbeG7scE3EveIN0dOjXPgwgQi8\nI2ZAKYm6DawoGz1lEJVdvFmkyMbP973X80b7mKmn0nNbe1kjA4M0O0hHaMM1ZaEv\n7e9vHEAoGyysMO6HzPWYMkyNxcCV7Nos2Uv4RvLDpQHh7P4Kt6fUU13ipcynrtQD\n1lFUM0yoTzwwFsPu3Pk+94hL58ErqwqJQwxoHMgLIQeMVHeNKcWFy1bddSbIbCWU\nZs6cMxhrra062ZCpDCbxyEaFNGAtYQMqNz55Z/14XgSUONZ/cJTns6QKhpcgTOwB\nfnNzRnk+aWreP7osKhXlz4zs+llP7goBDKFOMMtoEXx3YjJCKgpqmBU=\n-----END CERTIFICATE-----",
        "SSLName": "证书-1",
        "Region": variables.get("Region"),
        "PrivateKey": "abc",
        "CaCert": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA8QbLsBnQmXRFLONEkHL1LfvYZZi04HH5Kv4fX9UFT8S6vzwv\njrBu+oToMujfH+5O8eV4LTyovTuMnRZfFYmIRF0Y2EHFK05t5bu7PVE9gCFJitHS\nPj2YBVOYA8IfH0C6C9uE9pT35A/U54Apw2p36N8W8f3vYbCZH+4SlosfM68bWGAl\nE7feqU6UHlo6+4IJdmwxH02siTTPoucaBgT4kBXcT5ylgozZl4tncLNHdsIYtXrk\nVoCOcCF44uVin1H+hL8xtFM8+ovL7Eixr/KS+wtALlCODKzzQ3rBXgNixGHJUJKR\nxBOPQZKULwqJAlvXfP6+QElK8vu0qySJ3FOhcQIDAQABAoIBAAPvZnfzk/JNcauv\n8jihh9s+V2QhQCLB+Z14FK8N3U5WGe5xXx1nSAiTDu912d69l1BfvLyQVvjv9fXC\nnb7ORglHs9YkDMIOP8EWdZIkt2pWIMtBbbtSah78JGk7TCLIfcEfzmXwPLPehk1Z\nTFVCcb69lbRRvwzLQ1TAIFGQ5+uCEkW02KAl6kx+JnVpsE8/BjqZKG1Ne+sM6dOC\nGRd44hgiNHKUT3Xtbw6jttiUFDLKYMYtb7PpRAkZFM8tgnBV6dWWJ3xTYW9kOjPh\nXnScNARfphUZVibRhA04og5p1q/MUz9Sz9g2DURuSlo/MP3WZMbVRvZiUN1xhz5v\n2WhsddkCgYEA+gWPFo0TbVbZXUrx9J/ptI9NXNx5zjyUrv87MDt1pnmMDgWrsCEI\nRqQR4Lp2G11GA7IudiA/ipcZqgcRIIFvb+gu1kObox3BGGs59x+DqFeAPXt6dFG2\nW10f9k96/tcbdursurqwd3Zv3cqQqRTKgaP4xHFmexlcwGCF5YwewWMCgYEA9sos\n2acNINXwcNRUPnpg82DOrG9Zjr1aiNo9PDJmwGEdC9QMOUWM85dq0M9g388ttiLU\nWr/U4r5yDuqWJPcKtff2BaxSsZpcQ4Id9eddD9L+sxaBGyD23RtOC+IOlkG6WS4g\niUYulQvW69tBHWiwxQu7YMSIE2B3EuySPOQYlBsCgYEAxNwvqB/4lfT2PUDPdj+b\ncnILBf0LY1nL8GZCol2O6z91CW1pm8rGi2iQMxRd/nnYsPxRHO2TWnpS2M+rqp5/\nsettRYQCPdMlwSZcg7oqnhgXf1GEP6Y/IX0Xt4cpXxLcKywarYRlggqdVlMyyA74\nzE7hhzuK5442u7rEctN7O+UCgYAoM78ipafp1XAZsT0YAG+Stg504J7CNe5tpL+c\n8sjyRd+pcZ2cJsxTUjNAWMf7LZDQvtPBBMb1OPjznRtgYi4IfqBBRFUkQXUOOkAP\nMuViEokTO3NErBYK5svL+8NMjuCAbpc2RYyJEyiru0fcNpW1Q7f+h4VzQp+jIY6h\nBLdMSQKBgGauU7OQksZCEY2MVAcD5dShYYvWLxOkj4dVVwISN1M6ImCAHwXZ6Nak\n6YlzCGT+NbRJbB2cPfsrKXtAJVX15I3iDCKAoGkb+9kiHnPj7Q71KVuWQE6BQx7E\nvE88TSsshwtX1s+qU9UWUrMPodK32q5nO3p8N033NvS9wLNfbcdc\n-----END RSA PRIVATE KEY-----",
    }

    try:
        resp = client.ulb().create_ssl(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["SSLId_01"] = utest.value_at_path(resp, "SSLId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateSSL",
)
def create_ssl_05(client: utest.Client, variables: dict):
    d = {
        "UserCert": "-----BEGIN CERTIFICATE-----\nMIIFzTCCBLWgAwIBAgIQQ8IswmAhEIKfNhrKqb0F3DANBgkqhkiG9w0BAQsFADCB\nlzELMAkGA1UEBhMCQ04xJTAjBgNVBAoTHFRydXN0QXNpYSBUZWNobm9sb2dpZXMs\nIEluYy4xHzAdBgNVBAsTFlN5bWFudGVjIFRydXN0IE5ldHdvcmsxHTAbBgNVBAsT\nFERvbWFpbiBWYWxpZGF0ZWQgU1NMMSEwHwYDVQQDExhUcnVzdEFzaWEgRFYgU1NM\nIENBIC0gRzUwHhcNMTYxMjA2MDAwMDAwWhcNMTcxMjA2MjM1OTU5WjAgMR4wHAYD\nVQQDDBVtLmVjb2xvZ3ktZW1vYmlsZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IB\nDwAwggEKAoIBAQDxBsuwGdCZdEUs40SQcvUt+9hlmLTgcfkq/h9f1QVPxLq/PC+O\nsG76hOgy6N8f7k7x5XgtPKi9O4ydFl8ViYhEXRjYQcUrTm3lu7s9UT2AIUmK0dI+\nPZgFU5gDwh8fQLoL24T2lPfkD9TngCnDanfo3xbx/e9hsJkf7hKWix8zrxtYYCUT\nt96pTpQeWjr7ggl2bDEfTayJNM+i5xoGBPiQFdxPnKWCjNmXi2dws0d2whi1euRW\ngI5wIXji5WKfUf6EvzG0Uzz6i8vsSLGv8pL7C0AuUI4MrPNDesFeA2LEYclQkpHE\nE49BkpQvCokCW9d8/r5ASUry+7SrJIncU6FxAgMBAAGjggKJMIIChTAgBgNVHREE\nGTAXghVtLmVjb2xvZ3ktZW1vYmlsZS5jb20wCQYDVR0TBAIwADBhBgNVHSAEWjBY\nMFYGBmeBDAECATBMMCMGCCsGAQUFBwIBFhdodHRwczovL2Quc3ltY2IuY29tL2Nw\nczAlBggrBgEFBQcCAjAZDBdodHRwczovL2Quc3ltY2IuY29tL3JwYTAfBgNVHSME\nGDAWgBRtWMd/GufhPy6mjJc1Qrv00zisPzAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0l\nBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMIGbBggrBgEFBQcBAQSBjjCBizA8Bggr\nBgEFBQcwAYYwaHR0cDovL3RydXN0YXNpYTItb2NzcC5kaWdpdGFsY2VydHZhbGlk\nYXRpb24uY29tMEsGCCsGAQUFBzAChj9odHRwOi8vdHJ1c3Rhc2lhMi1haWEuZGln\naXRhbGNlcnR2YWxpZGF0aW9uLmNvbS90cnVzdGFzaWFnNS5jcnQwggEDBgorBgEE\nAdZ5AgQCBIH0BIHxAO8AdQDd6x0reg1PpiCLga2BaHB+Lo6dAdVciI09EcTNtuy+\nzAAAAVjT7zdSAAAEAwBGMEQCIDCzWufc1q7hjmrrCetGyoA8EsEqpRSIhmZXStX5\n8b7zAiA6x5aAaDK+yMyeAgw71yi3tRVrWayHN+W0+4BxC8u5UQB2AO5Lvbd1zmC6\n4UJpH6vhnmajD35fsHLYgwDEe4l6qP3LAAABWNPvN4kAAAQDAEcwRQIgZ/LNgg7n\n7AE4O2yZkrXNcqAOmJ3NU2nT6zcnBxPFTTsCIQCjyPbMfWMZTD3kxgxPQ1COw5zJ\nsM0dfNmSr3MiU7EhqDANBgkqhkiG9w0BAQsFAAOCAQEAeyfgUhg9ZWVCaz0f+BQU\n6fMMfmQ1BDzvVFu+ORoAqyJQogxwIdfjrlz/63YFee5qpUsW/aaz4ma3bb4dpE1K\nGsgYe5N3o0xybYlOj+KB61sufYkzQS3HgDevCwjfUlGEbNl4dpO2xh5s5AANXlnz\ns/X0+AJ33/bm+fWIjAbIjluaEoM6GETHTXi4Tlxy0j3nsXsB9tIIUibAdTtButef\nJJRnikGRN+eHjrsLYe0RUmdKOQz1ik6teHt0MQX0aCe8OlXeyGDd9m8u7+y0nAnH\nTVaNuT7vXMWyyXLVUcV898wkBo3Bo3hUiaw0QR0ttgDrf5ZwqPfqpytRW2K5GMZT\nuw==\n-----END CERTIFICATE-----\n\n\n-----BEGIN CERTIFICATE-----\nMIIFZTCCBE2gAwIBAgIQOhAOfxCeGsWcxf/2QNXkQjANBgkqhkiG9w0BAQsFADCB\nyjELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQL\nExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMjAwNiBWZXJp\nU2lnbiwgSW5jLiAtIEZvciBhdXRob3JpemVkIHVzZSBvbmx5MUUwQwYDVQQDEzxW\nZXJpU2lnbiBDbGFzcyAzIFB1YmxpYyBQcmltYXJ5IENlcnRpZmljYXRpb24gQXV0\naG9yaXR5IC0gRzUwHhcNMTYwODExMDAwMDAwWhcNMjYwODEwMjM1OTU5WjCBlzEL\nMAkGA1UEBhMCQ04xJTAjBgNVBAoTHFRydXN0QXNpYSBUZWNobm9sb2dpZXMsIElu\nYy4xHzAdBgNVBAsTFlN5bWFudGVjIFRydXN0IE5ldHdvcmsxHTAbBgNVBAsTFERv\nbWFpbiBWYWxpZGF0ZWQgU1NMMSEwHwYDVQQDExhUcnVzdEFzaWEgRFYgU1NMIENB\nIC0gRzUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC39aSJZG/97x3a\n6Qmuc9+MubagegRAVUmFYHTYTs8IKB2pM7wXN7W8mekdZaEgUjDFxvRBK/DhTb7U\n8ONLsKKdT86aOhzbz2noCTn9wPWnGwkg+/4YKg/dPQQdV9tMsSu0cwqInWHxSAkm\nAI1hYFC9D7Sf7Hp/5cRcD+dK454YMRzNOGLQnCVI8JEqrz6o9SOvQNTqTcfqt6DC\n0UlXG+MPD1eNPjlzf1Vwaab+VSTgySoC+Ikbq2VsdykeOiGXW/OIiASH7+2LcR05\nPmQ7GEOlM8yzoVojFpM8sHz+WxI05ZOPri5+vX3HhHHjWr5432G0dVmgohnZvlVZ\noy8XrlbpAgMBAAGjggF2MIIBcjASBgNVHRMBAf8ECDAGAQH/AgEAMC8GA1UdHwQo\nMCYwJKAioCCGHmh0dHA6Ly9zLnN5bWNiLmNvbS9wY2EzLWc1LmNybDAOBgNVHQ8B\nAf8EBAMCAQYwLgYIKwYBBQUHAQEEIjAgMB4GCCsGAQUFBzABhhJodHRwOi8vcy5z\neW1jZC5jb20wYQYDVR0gBFowWDBWBgZngQwBAgEwTDAjBggrBgEFBQcCARYXaHR0\ncHM6Ly9kLnN5bWNiLmNvbS9jcHMwJQYIKwYBBQUHAgIwGRoXaHR0cHM6Ly9kLnN5\nbWNiLmNvbS9ycGEwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMCkGA1Ud\nEQQiMCCkHjAcMRowGAYDVQQDExFTeW1hbnRlY1BLSS0yLTYwMTAdBgNVHQ4EFgQU\nbVjHfxrn4T8upoyXNUK79NM4rD8wHwYDVR0jBBgwFoAUf9Nlp8Ld7LvwMAnzQzn6\nAq8zMTMwDQYJKoZIhvcNAQELBQADggEBABUphhBbeG7scE3EveIN0dOjXPgwgQi8\nI2ZAKYm6DawoGz1lEJVdvFmkyMbP973X80b7mKmn0nNbe1kjA4M0O0hHaMM1ZaEv\n7e9vHEAoGyysMO6HzPWYMkyNxcCV7Nos2Uv4RvLDpQHh7P4Kt6fUU13ipcynrtQD\n1lFUM0yoTzwwFsPu3Pk+94hL58ErqwqJQwxoHMgLIQeMVHeNKcWFy1bddSbIbCWU\nZs6cMxhrra062ZCpDCbxyEaFNGAtYQMqNz55Z/14XgSUONZ/cJTns6QKhpcgTOwB\nfnNzRnk+aWreP7osKhXlz4zs+llP7goBDKFOMMtoEXx3YjJCKgpqmBU=\n-----END CERTIFICATE-----",
        "SSLName": "证书-2",
        "Region": variables.get("Region"),
        "PrivateKey": "abc",
        "CaCert": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA8QbLsBnQmXRFLONEkHL1LfvYZZi04HH5Kv4fX9UFT8S6vzwv\njrBu+oToMujfH+5O8eV4LTyovTuMnRZfFYmIRF0Y2EHFK05t5bu7PVE9gCFJitHS\nPj2YBVOYA8IfH0C6C9uE9pT35A/U54Apw2p36N8W8f3vYbCZH+4SlosfM68bWGAl\nE7feqU6UHlo6+4IJdmwxH02siTTPoucaBgT4kBXcT5ylgozZl4tncLNHdsIYtXrk\nVoCOcCF44uVin1H+hL8xtFM8+ovL7Eixr/KS+wtALlCODKzzQ3rBXgNixGHJUJKR\nxBOPQZKULwqJAlvXfP6+QElK8vu0qySJ3FOhcQIDAQABAoIBAAPvZnfzk/JNcauv\n8jihh9s+V2QhQCLB+Z14FK8N3U5WGe5xXx1nSAiTDu912d69l1BfvLyQVvjv9fXC\nnb7ORglHs9YkDMIOP8EWdZIkt2pWIMtBbbtSah78JGk7TCLIfcEfzmXwPLPehk1Z\nTFVCcb69lbRRvwzLQ1TAIFGQ5+uCEkW02KAl6kx+JnVpsE8/BjqZKG1Ne+sM6dOC\nGRd44hgiNHKUT3Xtbw6jttiUFDLKYMYtb7PpRAkZFM8tgnBV6dWWJ3xTYW9kOjPh\nXnScNARfphUZVibRhA04og5p1q/MUz9Sz9g2DURuSlo/MP3WZMbVRvZiUN1xhz5v\n2WhsddkCgYEA+gWPFo0TbVbZXUrx9J/ptI9NXNx5zjyUrv87MDt1pnmMDgWrsCEI\nRqQR4Lp2G11GA7IudiA/ipcZqgcRIIFvb+gu1kObox3BGGs59x+DqFeAPXt6dFG2\nW10f9k96/tcbdursurqwd3Zv3cqQqRTKgaP4xHFmexlcwGCF5YwewWMCgYEA9sos\n2acNINXwcNRUPnpg82DOrG9Zjr1aiNo9PDJmwGEdC9QMOUWM85dq0M9g388ttiLU\nWr/U4r5yDuqWJPcKtff2BaxSsZpcQ4Id9eddD9L+sxaBGyD23RtOC+IOlkG6WS4g\niUYulQvW69tBHWiwxQu7YMSIE2B3EuySPOQYlBsCgYEAxNwvqB/4lfT2PUDPdj+b\ncnILBf0LY1nL8GZCol2O6z91CW1pm8rGi2iQMxRd/nnYsPxRHO2TWnpS2M+rqp5/\nsettRYQCPdMlwSZcg7oqnhgXf1GEP6Y/IX0Xt4cpXxLcKywarYRlggqdVlMyyA74\nzE7hhzuK5442u7rEctN7O+UCgYAoM78ipafp1XAZsT0YAG+Stg504J7CNe5tpL+c\n8sjyRd+pcZ2cJsxTUjNAWMf7LZDQvtPBBMb1OPjznRtgYi4IfqBBRFUkQXUOOkAP\nMuViEokTO3NErBYK5svL+8NMjuCAbpc2RYyJEyiru0fcNpW1Q7f+h4VzQp+jIY6h\nBLdMSQKBgGauU7OQksZCEY2MVAcD5dShYYvWLxOkj4dVVwISN1M6ImCAHwXZ6Nak\n6YlzCGT+NbRJbB2cPfsrKXtAJVX15I3iDCKAoGkb+9kiHnPj7Q71KVuWQE6BQx7E\nvE88TSsshwtX1s+qU9UWUrMPodK32q5nO3p8N033NvS9wLNfbcdc\n-----END RSA PRIVATE KEY-----",
    }

    try:
        resp = client.ulb().create_ssl(d)
    except exc.RetCodeException as e:
        resp = e.json()

    variables["SSLId_02"] = utest.value_at_path(resp, "SSLId")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.SSLId", "SSLId_01"),
    ],
    action="DescribeSSL",
)
def describe_ssl_06(client: utest.Client, variables: dict):
    d = {"SSLId": variables.get("SSLId_01"), "Region": variables.get("Region")}

    try:
        resp = client.ulb().describe_ssl(d)
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
        ("str_eq", "DataSet.0.SSLId", "SSLId_02"),
    ],
    action="DescribeSSL",
)
def describe_ssl_07(client: utest.Client, variables: dict):
    d = {"SSLId": variables.get("SSLId_02"), "Region": variables.get("Region")}

    try:
        resp = client.ulb().describe_ssl(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="BindSSL",
)
def bind_ssl_08(client: utest.Client, variables: dict):
    d = {
        "VServerId": variables.get("VServerId"),
        "ULBId": variables.get("ULBId"),
        "SSLId": variables.get("SSLId_01"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.ulb().bind_ssl(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=30,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="UpdateSSLBinding",
)
def update_ssl_binding_09(client: utest.Client, variables: dict):
    d = {
        "VServerId": variables.get("VServerId"),
        "ULBId": variables.get("ULBId"),
        "Region": variables.get("Region"),
        "OldSSLId": variables.get("SSLId_01"),
        "NewSSLId": variables.get("SSLId_02"),
    }

    try:
        resp = client.invoke("UpdateSSLBinding", d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="UnbindSSL",
)
def unbind_ssl_10(client: utest.Client, variables: dict):
    d = {
        "VServerId": variables.get("VServerId"),
        "ULBId": variables.get("ULBId"),
        "SSLId": variables.get("SSLId_02"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.ulb().unbind_ssl(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteSSL",
)
def delete_ssl_11(client: utest.Client, variables: dict):
    d = {
        "VServerId": variables.get("VServerId"),
        "ULBId": variables.get("ULBId"),
        "SSLId": variables.get("SSLId_01"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.ulb().delete_ssl(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteSSL",
)
def delete_ssl_12(client: utest.Client, variables: dict):
    d = {"SSLId": variables.get("SSLId_02"), "Region": variables.get("Region")}

    try:
        resp = client.ulb().delete_ssl(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteVServer",
)
def delete_vserver_13(client: utest.Client, variables: dict):
    d = {
        "VServerId": variables.get("VServerId"),
        "ULBId": variables.get("ULBId"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.ulb().delete_vserver(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteULB",
)
def delete_ulb_14(client: utest.Client, variables: dict):
    d = {"ULBId": variables.get("ULBId"), "Region": variables.get("Region")}

    try:
        resp = client.ulb().delete_ulb(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteSubnet",
)
def delete_subnet_15(client: utest.Client, variables: dict):
    d = {
        "SubnetId": variables.get("subnet_id"),
        "Region": variables.get("Region"),
    }

    try:
        resp = client.vpc().delete_subnet(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteVPC",
)
def delete_vpc_16(client: utest.Client, variables: dict):
    d = {"VPCId": variables.get("vpc_id"), "Region": variables.get("Region")}

    try:
        resp = client.vpc().delete_vpc(d)
    except exc.RetCodeException as e:
        resp = e.json()

    return resp
