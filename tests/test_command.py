import subprocess

import pytest


@pytest.mark.parametrize("cmd,return_code", [
    (["phort", "-h"], 0),
    (["phort"], 0),
])
def test_command(cmd, return_code):
    r = subprocess.run(cmd)
    assert r.returncode == return_code
