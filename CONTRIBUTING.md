# Contributing to Acelang

Thank you for your interest in contributing to Acelang! This document provides guidelines and information for contributors.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find that the issue already exists. When creating a bug report, please include:

- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Environment details (OS, VS Code version, Python version)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- A clear description of the proposed enhancement
- The motivation behind it
- Use cases

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add or update tests if applicable
5. Update documentation if needed
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Development Setup

### VS Code Extension

```bash
cd packages/vscode
npm install
npm run compile
```

### Python SDK

```bash
cd packages/cli
pip install -e .
```

## Code Style

### TypeScript (VS Code Extension)

- Follow the existing code style
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small

### Python (SDK)

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for public methods
- Keep functions focused and testable

## Testing

### VS Code Extension

Test the extension by:
1. Opening the project in VS Code
2. Pressing F5 to launch the Extension Development Host
3. Opening a `.ac` file to verify syntax highlighting

### Python SDK

```bash
cd packages/cli
pytest
```

## Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Keep the first line under 72 characters
- Reference issues and pull requests where appropriate

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to open an issue for any questions about contributing!
