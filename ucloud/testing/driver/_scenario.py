import functools

from ucloud.testing.driver import _step


class Scenario:
    def __init__(self, spec, id_, title=None, owners=None):
        self.id = id_
        self.title = title
        self.store = {}
        self.errors = []
        self.steps = []
        self.spec = spec
        self.owners = owners

    def step(self, invoker, *args, **kwargs):
        step = _step.Step(self, invoker, *args, **kwargs)
        self.steps.append(step)
        return step

    def api(self, **step_kwargs):
        def deco(fn):
            step = self.step(fn, **step_kwargs)

            @functools.wraps(fn)
            def wrapped(*args, **kwargs):
                return step.run_api(*args, **kwargs)

            return wrapped

        return deco

    def func(self, **step_kwargs):
        def deco(fn):
            step = self.step(fn, **step_kwargs)

            @functools.wraps(fn)
            def wrapped(*args, **kwargs):
                return step.run_func(*args, **kwargs)

            return wrapped

        return deco

    @property
    def status(self):
        if all([item.status == "skipped" for item in self.steps]):
            status = "skipped"
        elif any([item.status == "failed" for item in self.steps]):
            status = "failed"
        else:
            status = "passed"
        return status

    @property
    def start_time(self):
        times = [
            item.start_time for item in self.steps if item.status != "skipped"
        ]
        return min(times) if times else 0

    @property
    def end_time(self):
        times = [
            item.end_time for item in self.steps if item.status != "skipped"
        ]
        return max(times) if times else 0

    def json(self):
        return {
            "title": self.title,
            "status": self.status,
            "steps": [item.json() for item in self.steps],
            "owners": self.owners,
            "execution": {
                "duration": self.end_time - self.start_time,
                "start_time": self.start_time,
                "end_time": self.end_time,
            },
            "passed_count": len(
                [1 for item in self.steps if item.status == "passed"]
            ),
            "failed_count": len(
                [1 for item in self.steps if item.status == "failed"]
            ),
            "skipped_count": len(
                [1 for item in self.steps if item.status == "skipped"]
            ),
        }

    def __call__(self, *args, **kwargs):
        for step in self.steps:
            step(step, *args, **kwargs)
