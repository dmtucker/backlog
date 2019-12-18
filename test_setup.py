"""Test setup.py."""


import os
import subprocess
import sys
import sysconfig

import setup


def test_setup():
    """Run setup.py check."""
    command = [
        sys.executable,
        setup.__file__,
        'check',
        '--metadata',
        '--strict',
    ]
    assert subprocess.run(command, check=False).returncode == 0


def test_console_scripts():
    """Ensure console scripts were installed correctly."""
    assert os.path.isfile(
        os.path.join(sysconfig.get_path('scripts'), 'backlog'),
    )
