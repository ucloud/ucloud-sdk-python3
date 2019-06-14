UCloud SDK Python 3
===================

UCloud SDK is a Python client library for accessing the UCloud API.

This client can run on Linux, macOS and Windows. It requires Python 3.5 and above.

- Website: https://www.ucloud.cn/
- Free software: Apache 2.0 license
- `Documentation <https://ucloud-sdk-python3.readthedocs.org>`_

.. image:: https://img.shields.io/pypi/v/agen.svg
   :target: https://pypi.python.org/pypi/ucloud-sdk-python3/
   :alt: Latest Version
.. image:: https://travis-ci.org/yufeiminds/agen.svg?branch=master
   :target: https://travis-ci.org/ucloud/ucloud-sdk-python3
   :alt: Travis CI Status
.. image:: https://codecov.io/github/yufeiminds/agen/coverage.svg?branch=master
   :target: https://codecov.io/github/ucloud/ucloud-sdk-python3?branch=master
   :alt: Codecov Status
.. image:: https://readthedocs.org/projects/agen/badge/?version=latest
   :target: https://ucloud-sdk-python3.readthedocs.org/en/latest/?badge=latest
   :alt: Doc Status

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

    client = Client({
        "region": "cn-bj2",
        "project_id": "...",
        "public_key": "...",
        "private_key": "...",
    })

    resp = client.uhost().create_uhost_instance({
        'Name': 'sdk-python-example',
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

    print(resp)


.. note:: UHost created above cannot be accessed via Internet unless an EIP is created and bind to the UHost.

Advantage Usage
---------------

Type System
~~~~~~~~~~~

UCloud Python SDK has completed type system for static and runtime type checking.

Wait State Changed
~~~~~~~~~~~~~~~~~~

Feedback & Contribution
-----------------------

- `Issue <https://github.com/ucloud/ucloud-sdk-python3/issues>`_
- `Pull Request <https://github.com/ucloud/ucloud-sdk-python3/pulls>`_
