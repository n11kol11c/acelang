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
from .identifier import (
    Keywords,
    get_identifier,
    is_valid_keyword,
    is_valid_cvar,
    is_valid_action,
    is_valid_principal,
    is_valid_state,
    get_token_type,
    get_token_prefix,
    resolve_identifier_type,
    split_identifier,
    format_identifier,
    get_sv_convars,
    get_onesync_convars,
    get_ratelimiter_convars,
    get_ratelimiter_pairs,
    get_group_principals,
    get_identifier_principals,
    get_resource_principals,
    get_command_permissions,
    get_txadmin_permissions,
    get_framework_permissions,
    validate_convar_value,
    get_keyword_suggestions,
    parse_line,
    build_line,
    parse_value,
    format_value,
    find_by_prefix,
    find_by_suffix,
    find_by_pattern,
    get_related,
    get_rate_pair,
    get_enabled_only,
    get_numeric_only,
    get_string_only,
    get_ace_args,
    get_principal_args,
    build_ace_line,
    build_principal_line,
    build_resource_line,
    build_convar_line,
    build_set_line,
    build_setr_line,
    build_sets_line,
    get_all_lines,
    get_stats,
)

__all__ = [
    "AcelangParser",
    "AcelangValidator",
    "Command",
    "Comment",
    "Directive",
    "Keywords",
    "get_identifier",
    "is_valid_keyword",
    "is_valid_cvar",
    "is_valid_action",
    "is_valid_principal",
    "is_valid_state",
    "get_token_type",
    "get_token_prefix",
    "resolve_identifier_type",
    "split_identifier",
    "format_identifier",
    "get_sv_convars",
    "get_onesync_convars",
    "get_ratelimiter_convars",
    "get_ratelimiter_pairs",
    "get_group_principals",
    "get_identifier_principals",
    "get_resource_principals",
    "get_command_permissions",
    "get_txadmin_permissions",
    "get_framework_permissions",
    "validate_convar_value",
    "get_keyword_suggestions",
    "parse_line",
    "build_line",
    "parse_value",
    "format_value",
    "find_by_prefix",
    "find_by_suffix",
    "find_by_pattern",
    "get_related",
    "get_rate_pair",
    "get_enabled_only",
    "get_numeric_only",
    "get_string_only",
    "get_ace_args",
    "get_principal_args",
    "build_ace_line",
    "build_principal_line",
    "build_resource_line",
    "build_convar_line",
    "build_set_line",
    "build_setr_line",
    "build_sets_line",
    "get_all_lines",
    "get_stats",
]
