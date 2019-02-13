"""Test setup.py."""


import subprocess
import sys


def test_setup():
    """Run setup.py check."""
    command = [sys.executable, 'setup.py', 'check', '--metadata', '--strict']
    assert subprocess.run(command).returncode == 0


def test_console_scripts():
    """Ensure console scripts were installed correctly."""
    command = ['backlog', '--help']
    assert subprocess.run(command).returncode == 0
