# Acelang

Acelang is a config language for FiveM servers. This repository contains:

- **acelang_theme/** - VS Code extension for syntax highlighting
- **acelang_python/** - Python library for parsing and validating .ac files

## Quick Install

### macOS / Linux

```bash
git clone https://github.com/n11kol11c/acelang.git
cd acelang/acelang_theme
./install.sh
```

### Windows (Command Prompt)

```cmd
git clone https://github.com/n11kol11c/acelang.git
cd acelang\acelang_theme
install.bat
```

### Windows (PowerShell)

```powershell
git clone https://github.com/n11kol11c/acelang.git
cd acelang\acelang_theme
.\install.bat
```

## Features

- **Syntax highlighting** for all FiveM server commands
- **Comments**: `#` (single-line) and `/;` ... `;/` (multi-line)
- **Keywords**: `setr`, `set`, `sets`, `add_ace`, `ensure`, `restart`, etc.
- **Convars**: All `sv_*`, `onesync_*`, `rateLimiter_*`, `steam_*` variables
- **Principals**: `group.*`, `builtin.*`, `identifier.*`, `resource.*`
- **Permissions**: `allow`, `deny`, `deny_socket`
- **Booleans**: `true`, `false`, `on`, `off`

## Customization

Add to your VS Code `settings.json` to customize colors:

```json
"editor.tokenColorCustomizations": {
    "textMateRules": [
        {
            "scope": "keyword.command.server.acelang",
            "settings": { "foreground": "#ff6b9d" }
        },
        {
            "scope": "keyword.control.directive.acelang",
            "settings": { "foreground": "#ff6b9d" }
        }
    ]
}
```

## Python Library

The `acelang_python/` directory contains a Python library for working with .ac files.

### Installation

```bash
cd acelang_python
pip install -e .
```

### Usage

```python
from acelang import AcelangParser, AcelangValidator

# Parse a .ac file
parser = AcelangParser()
result = parser.parse_file('server.cfg')

# Get specific commands
convars = parser.get_convars()
resources = parser.get_resources()
ace_permissions = parser.get_ace_permissions()

# Validate a .ac file
validator = AcelangValidator()
errors = validator.validate_file('server.cfg')
```

## Development

### VS Code Extension

```bash
cd acelang_theme
npm install          # Install dependencies
npm run compile      # Compile TypeScript
npm run package      # Build .vsix package
npm run watch        # Watch for changes
```

### Python Library

```bash
cd acelang_python
pip install -e .     # Install in development mode
```

## Project Structure

```
acelang/
├── acelang_theme/              # VS Code extension
│   ├── install.sh              # macOS/Linux installer
│   ├── install.bat             # Windows installer
│   ├── package.json            # Extension manifest
│   ├── syntaxes/
│   │   └── acelang.tmLanguage.json
│   ├── src/
│   │   └── extension.ts
│   ├── language-configuration.json
│   ├── tsconfig.json
│   └── fivem_api_reference.ac
│
└── acelang_python/             # Python library
    ├── setup.py
    ├── acelang/
    │   ├── __init__.py
    │   ├── parser.py
    │   └── validator.py
    └── README.md
```

## License

MIT
