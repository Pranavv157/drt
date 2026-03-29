"""drt — data reverse tool.

Reverse ETL for the code-first data stack.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("drt-core")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"
