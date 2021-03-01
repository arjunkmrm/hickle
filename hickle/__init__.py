# hickle imports
from .__version__ import __version__
from . import hickle
from .hickle import *

# All declaration
__all__ = ['hickle', *hickle.__all__]

# Author declaration
__author__ = "Danny Price, Ellert van der Velden and contributors"
