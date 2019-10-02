"""Test backlog.__main__."""


import subprocess
import sys


def test_python_m():
    """Test python -m."""
    command = [sys.executable, '-m', 'backlog', '--help']
    assert subprocess.run(command, check=False).returncode == 0
