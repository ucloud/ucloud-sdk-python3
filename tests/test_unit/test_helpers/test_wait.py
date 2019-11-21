import pytest

from ucloud.helpers import wait


def test_wait():
    with pytest.raises(wait.WaitTimeoutException):
        wait.wait_for_state(
            pending=["pending"],
            target=["running"],
            refresh=lambda: "pending",
            timeout=0.5,
        )

    wait.wait_for_state(
        pending=["pending"],
        target=["running"],
        refresh=lambda: "running",
        timeout=0.5,
    )
