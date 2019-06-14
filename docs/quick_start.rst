QuickStart
==========

Installation
------------

Install with pip:

.. code:: shell

    pip install ucloud-sdk-python3

Install with source code:

.. code:: shell

    clone https://github.com/ucloud/ucloud-sdk-python3.git
    cd ucloud-sdk-python3
    python setup.py install

QuickStart
----------

Currently, user public key & private key is the only method of authenticating with the API. You could get your keys here:

- `Key Generation <https://console.ucloud.cn/uapi/apikey>`_

You can then use your keys to create a new client of uhost service:

.. code-block:: python

    from ucloud.core import exc
    from ucloud.client import Client

    client = Client({
        "region": "cn-bj2",
        "project_id": "...",
        "public_key": "...",
        "private_key": "...",
    })

    try:
        resp = client.uhost().create_uhost_instance({
            'Name': 'sdk-python-quickstart',
            'Zone': image["zone"],
            'ImageId': image["image_id"],
            'LoginMode': "Password",
            'Password': utils.b64encode(utils.gen_password(20)),
            'CPU': 1,
            'Memory': 1,
            'Disks': [{
                'Size': 10,
                'Type': 'CLOUD_SSD'
            }],
        })
    except exc.UCloudException as e
        print(e)
    else:
        print(resp)

.. note:: UHost created above cannot be accessed via Internet unless an EIP is created and bind to the UHost.
