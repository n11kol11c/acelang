# Acelang Python Library

Python library for working with FiveM `.ac` config files.

## Installation

```bash
pip install -e .
```

## Usage

### Parsing .ac files

```python
from acelang import AcelangParser

parser = AcelangParser()
result = parser.parse_file('server.cfg')

# Get all commands
for cmd in result['commands']:
    print(f"{cmd.name}: {cmd.args}")

# Get specific commands
convars = parser.get_convars()
resources = parser.get_resources()
ace_permissions = parser.get_ace_permissions()
```

### Validating .ac files

```python
from acelang import AcelangValidator

validator = AcelangValidator()
errors = validator.validate_file('server.cfg')

for error in errors:
    print(f"Line {error['line']}: {error['message']}")
```

## Features

- Parse .ac files into structured data
- Validate syntax and command arguments
- Extract specific command types (convars, resources, ACE permissions)
- Handle comments (single-line and multi-line)
- Handle directives (@include, @from, etc.)
