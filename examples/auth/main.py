from ucloud.core import auth


def main():
    cred = auth.Credential(
        "ucloudsomeone@example.com1296235120854146120",
        "46f09bb9fab4f12dfc160dae12273d5332b5debe",
    )
    d = {'Action': 'DescribeUHostInstance', 'Region': 'cn-bj2', 'Limit': 10}
    print(cred.verify_ac(d))


if __name__ == '__main__':
    main()
