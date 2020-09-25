class Middleware:
    """middleware is the object to store request/response handlers

    >>> middleware = Middleware()

    Add a request handler to prepare the request

    >>> @middleware.request
    ... def prepare(req):
    ...     req['Region'] = 'cn-bj2'
    ...     return req

    Add a response handler to log the response detail

    >>> @middleware.response
    ... def logged(resp):
    ...     print(resp)
    ...     return resp

    >>> len(middleware.request_handlers), len(middleware.response_handlers)
    (1, 1)
    """

    def __init__(self):
        self.request_handlers = []
        self.response_handlers = []
        self.exception_handlers = []

    def request(self, handler, index=-1):
        """request is the request handler register to add request handler.

        :param handler: request handler function, receive request object
                        and return a new request
        :param int index: the position of request in the handler list,
                          default is append it to end
        :return:
        """
        self.request_handlers.insert(index, handler)
        return handler

    def response(self, handler, index=-1):
        """response is the response handler register to add response handler.

        :param handler: response handler function, receive response object
                        and return a new response
        :param int index: the position of response in the handler list,
                          default is append it to end
        :return:
        """
        self.response_handlers.insert(index, handler)
        return handler

    def exception(self, handler, index=-1):
        """exception is the exception handler register to add exception handler.

        :param handler: exception handler function, receive exception object
                        and raise a new exception or ignore it
        :param int index: the position of handler in the handler list,
                          default is append it to end
        :return:
        """
        self.exception_handlers.insert(index, handler)
        return handler
