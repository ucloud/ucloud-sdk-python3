import logging
import time
import typing

from ucloud.core.transport import http
from ucloud.testing import exc, utest, op
from ucloud.testing.exc import ValueNotFoundError, CompareError

logger = logging.getLogger(__name__)


class Step:
    def __init__(
        self,
        scenario,
        invoker,
        max_retries: int = 0,
        retry_interval: int = 0,
        startup_delay: int = 0,
        retry_for: typing.Tuple = (CompareError, ValueNotFoundError),
        fast_fail: bool = False,
        validators: typing.Callable[[dict], typing.List[typing.Tuple]] = None,
        title: str = "",
        **kwargs
    ):
        """Step is the test step in a test scenario
        :param invoker: invoker is a callable function
        :param max_retries: the maximum retry number by the `retry_for` exception,
                            it will resolve the flaky testing case
        :param retry_interval: the interval between twice retrying
        :param retry_for: the exceptions to retrying
        :param startup_delay: the delay seconds before any action execution
        :param fast_fail: if fast fail is true, the test will fail when got
                          unexpected exception
        :return:
        """
        self.invoker = invoker
        self.validators = validators or (lambda _: [])

        self.max_retries = max_retries
        self.retry_interval = retry_interval
        self.retry_for = retry_for
        self.startup_delay = startup_delay
        self.fast_fail = fast_fail

        self.start_time = 0
        self.end_time = 0
        self.status = "skipped"

        self.title = title
        self.type = "api"
        self.errors = []

        self.extras = kwargs
        self.scenario = scenario
        self.store = scenario.store
        self.api_retries = []

    def run_api(self, client, *args, **kwargs):
        client.transport.middleware.response(self._handle_response, 0)
        try:
            result = self._run(
                self._set_default_response, client, *args, **kwargs
            )
        except Exception as e:
            raise e
        finally:
            client.transport.middleware.response_handlers.pop(0)
        return result

    def run_func(self, *args, **kwargs):
        return self._run(None, *args, **kwargs)

    def json(self):
        return {
            "title": self.title,
            "type": self.type,
            "status": self.status,
            "execution": {
                "max_retries": self.max_retries,
                "retry_interval": self.retry_interval,
                "startup_delay": self.startup_delay,
                "fast_fail": self.fast_fail,
                "duration": self.end_time - self.start_time,
                "start_time": self.start_time,
                "end_time": self.end_time,
            },
            "api_retries": self.api_retries,
            "errors": list(set([str(e) for e in self.errors])),
        }

    def _handle_response(self, resp: http.Response):
        req = resp.request.payload()
        req.pop("Signature", None)

        self.api_retries.append(
            {
                "request": req,
                "response": resp.json(),
                "request_uuid": resp.headers.get("X-UCLOUD-REQUEST-UUID"),
                "request_time": resp.request.request_time,
            }
        )
        return resp

    def _set_default_response(self, result):
        if result is None:
            return result
        result.setdefault("RetCode", 0)
        if "action" in self.extras:
            result["Action"] = "{}Response".format(self.extras["action"])
        return result

    def _run(self, invoke_callback=None, *args, **kwargs):
        self.start_time = time.time()

        try:
            result = self._run_with_callback(invoke_callback, *args, **kwargs)
        except Exception as e:
            raise e
        finally:
            self.end_time = time.time()

        return result

    def _run_with_callback(self, invoke_callback=None, *args, **kwargs):
        # wait for delay before startup
        if self.startup_delay:
            time.sleep(self.startup_delay)

        for i in range(self.max_retries + 1):
            self.errors.clear()

            # invoke function to load result
            try:
                result = self.invoker(self, *args, **kwargs)
            except Exception as e:
                result = None
                self.errors.append(e)
            else:
                invoke_callback and invoke_callback(result)

                for validator in self.validators(self.store):
                    try:
                        op.check(
                            validator[0],
                            utest.value_at_path(result, validator[1]),
                            validator[2],
                        )
                    except self.retry_for as e:
                        self.errors.append(e)
                    except Exception as e:
                        self.errors.append(e)

            # if got error, retrying or raise it
            if self.errors:
                if i == self.max_retries:
                    self.status = "failed"
                    raise exc.ValidateError(self.errors)

                if self.retry_interval:
                    time.sleep(self.retry_interval)
                continue

            self.status = "passed"
            return result or None
