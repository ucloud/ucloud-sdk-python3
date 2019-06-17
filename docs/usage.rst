Usage
=====

Type System
-----------

UCloud Python SDK has type system for runtime checking.

For example:

.. code-block:: python

    client.uhost().create_uhost_instance({
        'CPU': "i am not a integer",
    })

it will raise :class:`ValidationException` with invalid integer and some required field is miss matched.

Wait State Changed
------------------

SDK also provide state waiter helper to improver usage experience.

**When using it?**

Waiter can wait for remote state is achieved to target state. such as,

- create and wait for resource state is completed.
- invoke/start/stop a resource and wait for it is finished.
- custom retry policies and wait for retrying is finished.

For example:

.. code-block:: python

    def mget_uhost_states(uhost_ids):
        resp = client.uhost().describe_uhost_instance({'UHostIds': uhost_ids})
        return [inst.get('State') for inst in resp.get('UHostSet')]

    # Stop all instances
    for uhost_id in uhost_ids:
        client.uhost().stop_uhost_instance({'UHostId': uhost_id})

    # Wait all instances is stopped
    wait.wait_for_state(
        target=['stopped'], pending=['pending'],
        timeout=300, # wait 5min
        refresh=lambda: (
            'stopped' if all([state == 'Stopped' for state in mget_uhost_states(uhost_ids)]) else 'pending'
        ),
    )

    # Remove all instances
    for uhost_id in uhost_ids:
        client.uhost().terminate_uhost_instance({'UHostId': uhost_id})

By the default, waiter will use exponential back-off delay between twice request.
it will raise :class:`WaitTimeoutException` when timeout is reached.

Client/Transport Middleware
---------------------------

UCloud SDK provide middleware feature to client or transport level request.

It allowed to add custom logic into the lifecycle of request/response.

For example:

.. code-block:: python

    @client.middleware.request
    def log_params(req):
        print('[REQ]', req)

    @client.middleware.response
    def log_response(resp):
        print('[RESP]', resp)


or transport:

.. code-block:: python

    from ucloud.core.transport import RequestsTransport

    transport = RequestsTransport()

    @transport.middleware.request
    def log_request(req):
        print('[REQ]', req)

    @transport.middleware.response
    def log_response(resp):
        print('[RESP]', resp)

    Client({'Region': 'cn-bj2'}, transport=transport)
