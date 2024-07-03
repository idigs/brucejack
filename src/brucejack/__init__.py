"""BruceJack: a Python package for exploring the Fibonacci sequence"""

import logging

logging.getLogger("brucejack").setLevel(logging.INFO)
try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"

