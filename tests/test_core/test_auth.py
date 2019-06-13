from ucloud.core import auth


def test_verify_ac():
    d = {
        "Action": "CreateUHostInstance",
        "CPU": 2,
        "ChargeType": "Month",
        "DiskSpace": 10,
        "ImageId": "f43736e1-65a5-4bea-ad2e-8a46e18883c2",
        "LoginMode": "Password",
        "Memory": 2048,
        "Name": "Host01",
        "Password": "VUNsb3VkLmNu",
        "PublicKey": "ucloudsomeone@example.com1296235120854146120",
        "Quantity": 1,
        "Region": "cn-bj2",
        "Zone": "cn-bj2-04",
    }
    cred = auth.Credential(
        "ucloudsomeone@example.com1296235120854146120",
        "46f09bb9fab4f12dfc160dae12273d5332b5debe",
    )
    assert cred.verify_ac(d) == "4f9ef5df2abab2c6fccd1e9515cb7e2df8c6bb65"
