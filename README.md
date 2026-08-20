<p align="center">
  <img src="https://img.shields.io/badge/VS%20Code-Extension-blue?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VS Code Extension">
  <img src="https://img.shields.io/badge/Python-Library-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Library">
  <img src="https://img.shields.io/badge/FiveM-Config%20Language-orange?style=for-the-badge&logo=fivem&logoColor=white" alt="FiveM">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<h1 align="center">Acelang</h1>

<p align="center">
  <strong>A modern configuration language for FiveM servers</strong>
</p>

<p align="center">
  Acelang provides a structured, readable syntax for managing FiveM server configurations.<br>
  Parse, validate, and highlight your server configs with powerful tooling.
</p>

---

## Features

| Feature | Description |
|---------|-------------|
| **Syntax Highlighting** | Full VS Code support with color-coded keywords, convars, and principals |
| **Multi-line Comments** | Use `/;` and `;/` for block comments alongside standard `#` comments |
| **Python Parser** | Programmatically read and manipulate `.ac` files |
| **Validator** | Catch errors before deploying your server configuration |
| **Cross-Platform** | Works on Windows, macOS, and Linux |

---

## Quick Start

### VS Code Extension

**macOS / Linux:**
```bash
git clone https://github.com/n11kol11c/acelang.git
cd acelang/acelang_theme
./install.sh
```

**Windows:**
```cmd
git clone https://github.com/n11kol11c/acelang.git
cd acelang\acelang_theme
install.bat
```

### Python Library

```bash
git clone https://github.com/n11kol11c/acelang.git
cd acelang/kit
pip install -e .
```

---

## Syntax Overview

```ac
# Single-line comment

/;
  Multi-line comment
;/

# Server configuration
sv_hostname "My Awesome Server"
sv_maxClients 48
sv_licenseKey "your_license_key"
onesync on

# Resource management
ensure mapmanager
ensure chat
ensure spawnmanager

# ACE permissions
add_ace group.admin command allow
add_ace group.admin txAdmin.kick allow

# Principal management
add_principal identifier.license:abc123 group.admin
```

---

## What's Highlighted

| Category | Examples |
|----------|----------|
| **Commands** | `setr`, `set`, `sets`, `ensure`, `restart`, `add_ace` |
| **Convars** | `sv_hostname`, `sv_maxClients`, `onesync_enableInfinity` |
| **Principals** | `group.admin`, `builtin.everyone`, `identifier.license:*` |
| **Permissions** | `allow`, `deny`, `deny_socket` |
| **Booleans** | `true`, `false`, `on`, `off` |
| **Resources** | `mapmanager`, `chat`, `spawnmanager`, `baseevents` |

---

## Python Usage

```python
from acelang import AcelangParser, AcelangValidator

# Parse a configuration file
parser = AcelangParser()
result = parser.parse_file('server.cfg')

# Access parsed data
for command in result['commands']:
    print(f"{command.name}: {command.args}")

# Get specific command types
convars = parser.get_convars()
resources = parser.get_resources()
ace_permissions = parser.get_ace_permissions()

# Validate configuration
validator = AcelangValidator()
errors = validator.validate_file('server.cfg')

if not errors:
    print("Configuration is valid!")
```

---

## Customization

Customize syntax colors in your VS Code `settings.json`:

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

---

## Project Structure

```
acelang/
├── acelang_theme/          # VS Code Extension
│   ├── install.sh          # macOS/Linux Installer
│   ├── install.bat         # Windows Installer
│   ├── syntaxes/           # TextMate Grammar
│   ├── src/                # Extension Source
│   └── fivem_api_reference.ac
│
└── kit/                    # Python Library
    ├── setup.py
    └── acelang/
        ├── parser.py       # .ac File Parser
        └── validator.py    # Configuration Validator
```

---

## Development

### VS Code Extension

```bash
cd acelang_theme
npm install
npm run compile
npm run watch
```

### Python Library

```bash
cd kit
pip install -e .
python -c "from acelang import AcelangParser; print('OK')"
```

---

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="center">
  Made with ❤️ for the FiveM community
</p>
