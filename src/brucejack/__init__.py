"""BruceJack: a Python package for approximating the Fibonacci sequence as a geometric series"""

import logging

logging.getLogger("brucejack").setLevel(logging.INFO)
try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"

