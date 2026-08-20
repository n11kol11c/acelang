#!/bin/bash

# Acelang - VS Code Extension Installer
# Cross-platform installer for macOS, Linux, and Windows (Git Bash/WSL)

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print with color
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Detect OS
detect_os() {
    case "$(uname -s)" in
        Linux*)     echo "linux";;
        Darwin*)    echo "macos";;
        CYGWIN*|MINGW*|MSYS*) echo "windows";;
        *)          echo "unknown";;
    esac
}

# Find VS Code CLI
find_vscode() {
    if command -v code &> /dev/null; then
        echo "code"
        return
    fi
    
    local os=$(detect_os)
    case "$os" in
        macos)
            if [ -f "/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code" ]; then
                echo "/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code"
                return
            fi
            ;;
        linux)
            if [ -f "/usr/share/code/bin/code" ]; then
                echo "/usr/share/code/bin/code"
                return
            fi
            if [ -f "/usr/bin/code" ]; then
                echo "/usr/bin/code"
                return
            fi
            ;;
        windows)
            if [ -f "/c/Program Files/Microsoft VS Code/bin/code" ]; then
                echo "/c/Program Files/Microsoft VS Code/bin/code"
                return
            fi
            if [ -f "$LOCALAPPDATA/Programs/Microsoft VS Code/bin/code" ]; then
                echo "$LOCALAPPDATA/Programs/Microsoft VS Code/bin/code"
                return
            fi
            ;;
    esac
    
    return 1
}

# Main installation
main() {
    echo ""
    echo "╔═══════════════════════════════════════════════════════════╗"
    echo "║           Acelang VS Code Extension Installer            ║"
    echo "╚═══════════════════════════════════════════════════════════╝"
    echo ""
    
    local os=$(detect_os)
    print_info "Detected OS: $os"
    
    # Find VS Code
    local code_cmd=$(find_vscode)
    
    if [ -z "$code_cmd" ]; then
        print_error "VS Code CLI not found."
        echo ""
        echo "Please install VS Code and add 'code' to your PATH:"
        echo ""
        case "$os" in
            macos)
                echo "  1. Open VS Code"
                echo "  2. Press Cmd+Shift+P"
                echo "  3. Type: Shell Command: Install 'code' command in PATH"
                ;;
            linux|windows)
                echo "  1. Open VS Code"
                echo "  2. Press Ctrl+Shift+P"
                echo "  3. Type: Shell Command: Install 'code' command in PATH"
                ;;
        esac
        exit 1
    fi
    
    print_success "Found VS Code at: $code_cmd"
    echo ""
    
    # Get script directory
    local script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    
    # Check for .vsix file
    local vsix_file="$script_dir/acelang-1.0.0.vsix"
    if [ ! -f "$vsix_file" ]; then
        print_warning ".vsix file not found. Building extension..."
        echo ""
        
        # Check for npm
        if ! command -v npm &> /dev/null; then
            print_error "npm not found. Please install Node.js first."
            echo "  Download: https://nodejs.org/"
            exit 1
        fi
        
        # Build
        cd "$script_dir"
        npm install
        npm run package
        
        if [ ! -f "$vsix_file" ]; then
            print_error "Failed to build extension."
            exit 1
        fi
        echo ""
    fi
    
    # Install extension
    print_info "Installing extension..."
    "$code_cmd" --install-extension "$vsix_file" --force
    
    echo ""
    echo "╔═══════════════════════════════════════════════════════════╗"
    echo "║              Installation Complete!                      ║"
    echo "╚═══════════════════════════════════════════════════════════╝"
    echo ""
    print_success "Acelang extension installed successfully!"
    echo ""
    echo "Features:"
    echo "  • Syntax highlighting for .ac files"
    echo "  • Single-line comments (#)"
    echo "  • Multi-line comments (/; ... ;/)"
    echo "  • All FiveM commands and convars"
    echo ""
    echo "Customize colors in VS Code settings.json:"
    echo '  "editor.tokenColorCustomizations": {'
    echo '    "textMateRules": ['
    echo '      {'
    echo '        "scope": "keyword.command.server.acelang",'
    echo '        "settings": { "foreground": "#ff6b9d" }'
    echo '      }'
    echo '    ]'
    echo '  }'
    echo ""
}

main "$@"
