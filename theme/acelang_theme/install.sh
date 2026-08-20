#!/bin/bash

# Acelang VS Code Extension Installer
# Works on macOS, Linux, and Windows (Git Bash/WSL)

set -e

echo "🔧 Acelang VS Code Extension Installer"
echo "======================================"
echo ""

# Detect OS
detect_os() {
    case "$(uname -s)" in
        Linux*)     echo "linux";;
        Darwin*)    echo "macos";;
        CYGWIN*|MINGW*|MSYS*) echo "windows";;
        *)          echo "unknown";;
    esac
}

OS=$(detect_os)
echo "Detected OS: $OS"
echo ""

# Find VS Code CLI
find_vscode() {
    # Check if code is in PATH
    if command -v code &> /dev/null; then
        echo "code"
        return
    fi
    
    # Platform-specific paths
    case "$OS" in
        macos)
            if [ -f "/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code" ]; then
                echo "/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code"
                return
            fi
            ;;
        linux)
            if command -v code &> /dev/null; then
                echo "code"
                return
            fi
            if [ -f "/usr/share/code/bin/code" ]; then
                echo "/usr/share/code/bin/code"
                return
            fi
            if [ -f "/usr/bin/code" ]; then
                echo "usr/bin/code"
                return
            fi
            ;;
        windows)
            # Check common Windows paths
            if [ -f "/c/Program Files/Microsoft VS Code/bin/code" ]; then
                echo "/c/Program Files/Microsoft VS Code/bin/code"
                return
            fi
            if [ -f "$LOCALAPPDATA/Programs/Microsoft VS Code/bin/code" ]; then
                echo "$LOCALAPPDATA/Programs/Microsoft VS Code/bin/code"
                return
            fi
            if [ -f "$HOME/AppData/Local/Programs/Microsoft VS Code/bin/code" ]; then
                echo "$HOME/AppData/Local/Programs/Microsoft VS Code/bin/code"
                return
            fi
            ;;
    esac
    
    echo ""
    return 1
}

CODE_CMD=$(find_vscode)

if [ -z "$CODE_CMD" ]; then
    echo "❌ Error: VS Code CLI not found."
    echo ""
    echo "Please install VS Code and add 'code' to your PATH:"
    echo ""
    case "$OS" in
        macos)
            echo "  1. Open VS Code"
            echo "  2. Press Cmd+Shift+P"
            echo "  3. Type: Shell Command: Install 'code' command in PATH"
            ;;
        linux)
            echo "  1. Open VS Code"
            echo "  2. Press Ctrl+Shift+P"
            echo "  3. Type: Shell Command: Install 'code' command in PATH"
            ;;
        windows)
            echo "  1. Open VS Code"
            echo "  2. Press Ctrl+Shift+P"
            echo "  3. Type: Shell Command: Install 'code' command in PATH"
            echo "  Or install from: https://code.visualstudio.com/docs/setup/setup-overview"
            ;;
    esac
    exit 1
fi

echo "✅ Found VS Code at: $CODE_CMD"
echo ""

# Get the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if .vsix file exists
VSIX_FILE="$SCRIPT_DIR/acelang-theme-0.0.1.vsix"
if [ ! -f "$VSIX_FILE" ]; then
    echo "⚠️  .vsix file not found. Building extension..."
    echo ""
    
    # Check if npm is installed
    if ! command -v npm &> /dev/null; then
        echo "❌ Error: npm not found. Please install Node.js first."
        echo "   Download: https://nodejs.org/"
        exit 1
    fi
    
    # Build the extension
    cd "$SCRIPT_DIR"
    npm install
    npm run package
    
    if [ ! -f "$VSIX_FILE" ]; then
        echo "❌ Error: Failed to build extension."
        exit 1
    fi
    
    echo ""
fi

# Install the extension
echo "📦 Installing extension..."
"$CODE_CMD" --install-extension "$VSIX_FILE" --force

echo ""
echo "======================================"
echo "✅ Acelang extension installed successfully!"
echo "======================================"
echo ""
echo "Features:"
echo "  • Syntax highlighting for .ac files"
echo "  • Comments: # (single-line) and /; ... ;/ (multi-line)"
echo "  • Keywords: setr, set, sets, add_ace, ensure, etc."
echo "  • All FiveM server config commands highlighted"
echo ""
echo "To customize colors, add to your settings.json:"
echo '  "editor.tokenColorCustomizations": {'
echo '    "textMateRules": ['
echo '      {'
echo '        "scope": "keyword.command.server.acelang",'
echo '        "settings": { "foreground": "#ff6b9d" }'
echo '      },'
echo '      {'
echo '        "scope": "keyword.control.directive.acelang",'
echo '        "settings": { "foreground": "#ff6b9d" }'
echo '      }'
echo '    ]'
echo '  }'
