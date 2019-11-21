from ucloud.testing.driver import _scenario


class Specification:
    def __init__(self):
        self.scenarios = []

    def scenario(self, id_, title="", owners=None):
        scenario = _scenario.Scenario(self, id_, title, owners)
        self.scenarios.append(scenario)
        return scenario

    @property
    def status(self):
        if all([item.status == "skipped" for item in self.scenarios]):
            status = "skipped"
        elif any([item.status == "failed" for item in self.scenarios]):
            status = "failed"
        else:
            status = "passed"
        return status

    @property
    def start_time(self):
        times = [
            item.start_time
            for item in self.scenarios
            if item.status != "skipped"
        ]
        return min(times) if times else 0

    @property
    def end_time(self):
        times = [
            item.end_time for item in self.scenarios if item.status != "skipped"
        ]
        return max(times) if times else 0

    def json(self):
        return {
            "status": self.status,
            "execution": {
                "duration": self.end_time - self.start_time,
                "start_time": self.start_time,
                "end_time": self.end_time,
            },
            "scenarios": [item.json() for item in self.scenarios],
            "passed_count": len(
                [1 for item in self.scenarios if item.status == "passed"]
            ),
            "failed_count": len(
                [1 for item in self.scenarios if item.status == "failed"]
            ),
            "skipped_count": len(
                [1 for item in self.scenarios if item.status == "skipped"]
            ),
        }
