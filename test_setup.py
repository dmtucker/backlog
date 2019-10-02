"""Test setup.py."""


import os
import subprocess
import sys

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
    assert all(
        any(
            os.path.isfile(
                os.path.join(
                    directory,
                    console_script.partition('=')[0].strip(),
                ),
            )
            for directory in os.environ['PATH'].split(':')
        )
        for console_script in setup.ENTRY_POINTS['console_scripts']
    )
