<p align="center">
  <img src="https://img.shields.io/badge/VS%20Code-Extension-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VS Code">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FiveM-Server-orange?style=for-the-badge" alt="FiveM">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge" alt="PRs Welcome">
</p>

<h1 align="center">Acelang</h1>

<p align="center">
  <strong>Professional configuration language and tooling for FiveM servers</strong>
</p>

<p align="center">
  Acelang provides a structured, human-readable syntax for managing FiveM server configurations.<br>
  Complete with syntax highlighting, parsing, and validation tools.
</p>

---

## Overview

Acelang is a configuration language designed specifically for FiveM game servers. It offers:

- **Clean Syntax** - Readable, maintainable server configurations
- **VS Code Extension** - Full syntax highlighting and language support
- **Python SDK** - Parse, validate, and manipulate configurations programmatically
- **Cross-Platform** - Works on Windows, macOS, and Linux

---

## Quick Start

### VS Code Extension

Install syntax highlighting for `.ac` files:

```bash
# Clone the repository
git clone https://github.com/n11kol11c/acelang.git
cd acelang/packages/vscode

# Run installer
./install.sh        # macOS / Linux
install.bat         # Windows
```

### Python SDK

Install the Python library for configuration management:

```bash
cd acelang/packages/cli
pip install -e .
```

---

## Syntax Example

```ac
# Server Configuration
sv_hostname "My RP Server"
sv_maxClients 48
sv_licenseKey "your_key_here"

# Enable OneSync for 32+ players
onesync on

# Resource Management
ensure mapmanager
ensure chat
ensure spawnmanager
ensure baseevents

# ACE Permissions
add_ace group.admin command allow
add_ace group.admin txAdmin.kick allow

# Principal Management
add_principal identifier.license:abc123 group.admin
```

---

## Language Features

| Feature | Syntax | Description |
|---------|--------|-------------|
| Single-line Comment | `# comment` | Standard hash comments |
| Multi-line Comment | `/; ... ;/` | Block comments for documentation |
| Convars | `sv_*`, `onesync_*` | Server configuration variables |
| Resources | `ensure`, `start`, `stop` | Resource lifecycle management |
| Permissions | `add_ace`, `remove_ace` | ACE permission system |
| Principals | `add_principal` | User/group hierarchy |
| Directives | `@include`, `@from` | File inclusion system |

---

## Python SDK

```python
from acelang import AcelangParser, AcelangValidator

# Parse configuration
parser = AcelangParser()
result = parser.parse_file('server.cfg')

# Access commands
for cmd in result['commands']:
    print(f"{cmd.name}: {cmd.args}")

# Get specific types
convars = parser.get_convars()
resources = parser.get_resources()

# Validate
validator = AcelangValidator()
errors = validator.validate_file('server.cfg')
```

---

## Customization

Customize syntax colors in VS Code `settings.json`:

```json
{
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
}
```

---

## Project Structure

```
acelang/
├── packages/
│   ├── vscode/                # VS Code Extension
│   │   ├── src/               # TypeScript Source
│   │   ├── syntaxes/          # TextMate Grammar
│   │   ├── install.sh         # Unix Installer
│   │   ├── install.bat        # Windows Installer
│   │   └── package.json       # Extension Manifest
│   │
│   └── cli/                   # Python SDK
│       ├── acelang/           # Package Source
│       │   ├── parser.py      # Configuration Parser
│       │   └── validator.py   # Syntax Validator
│       └── setup.py           # Package Setup
│
├── README.md
└── LICENSE
```

---

## Development

### Prerequisites

- Node.js 18+
- Python 3.8+
- VS Code

### VS Code Extension

```bash
cd packages/vscode
npm install
npm run compile
npm run watch
```

### Python SDK

```bash
cd packages/cli
pip install -e .
pytest  # Run tests
```

---

## Contributing

Contributions are welcome! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built with ❤️ for the FiveM community
</p>
