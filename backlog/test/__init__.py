"""Tests for Backlog"""

import logging

logging.basicConfig(
    filename="/var/log/backlog.test.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d %(name)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logging.getLogger(__name__).debug("Testing Backlog...")
