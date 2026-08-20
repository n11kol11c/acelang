"""
Acelang - Python SDK for FiveM Configuration Files

This package provides tools for parsing, validating, and manipulating
FiveM server configuration files written in the Acelang syntax.

Example:
    >>> from acelang import AcelangParser, AcelangValidator
    >>> parser = AcelangParser()
    >>> result = parser.parse_file('server.cfg')
    >>> print(result['commands'])
"""

__version__ = "1.0.0"
__author__ = "Acelang Contributors"
__license__ = "MIT"

from .parser import AcelangParser, Command, Comment, Directive
from .validator import AcelangValidator

__all__ = [
    "AcelangParser",
    "AcelangValidator",
    "Command",
    "Comment",
    "Directive",
]
