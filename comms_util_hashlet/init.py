# hashlet/__init__.py - Core reversible hash from original fork
from .sha1664 import SHA1664  # Import our toy sponge

__version__ = "0.1.0"
__all__ = ["SHA1664"]
