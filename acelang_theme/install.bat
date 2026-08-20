@echo off
REM Acelang VS Code Extension Installer for Windows
REM Works with Command Prompt and PowerShell

echo 🔧 Acelang VS Code Extension Installer
echo ======================================
echo.

REM Check if code is in PATH
where code >nul 2>nul
if %errorlevel% neq 0 (
    REM Check common Windows paths
    if exist "C:\Program Files\Microsoft VS Code\bin\code.cmd" (
        set "CODE_CMD=C:\Program Files\Microsoft VS Code\bin\code.cmd"
    ) else if exist "%LOCALAPPDATA%\Programs\Microsoft VS Code\bin\code.cmd" (
        set "CODE_CMD=%LOCALAPPDATA%\Programs\Microsoft VS Code\bin\code.cmd"
    ) else (
        echo ❌ Error: VS Code CLI not found.
        echo.
        echo Please install VS Code and add 'code' to your PATH:
        echo   1. Open VS Code
        echo   2. Press Ctrl+Shift+P
        echo   3. Type: Shell Command: Install 'code' command in PATH
        echo   Or install from: https://code.visualstudio.com/docs/setup/setup-overview
        pause
        exit /b 1
    )
) else (
    set "CODE_CMD=code"
)

echo ✅ Found VS Code
echo.

REM Get script directory
set "SCRIPT_DIR=%~dp0"

REM Check if .vsix file exists
if not exist "%SCRIPT_DIR%acelang-theme-0.0.1.vsix" (
    echo ⚠️  .vsix file not found. Building extension...
    echo.
    
    REM Check if npm is installed
    where npm >nul 2>nul
    if %errorlevel% neq 0 (
        echo ❌ Error: npm not found. Please install Node.js first.
        echo    Download: https://nodejs.org/
        pause
        exit /b 1
    )
    
    REM Build the extension
    cd /d "%SCRIPT_DIR%"
    call npm install
    call npm run package
    
    if not exist "%SCRIPT_DIR%acelang-theme-0.0.1.vsix" (
        echo ❌ Error: Failed to build extension.
        pause
        exit /b 1
    )
    
    echo.
)

REM Install the extension
echo 📦 Installing extension...
"%CODE_CMD%" --install-extension "%SCRIPT_DIR%acelang-theme-0.0.1.vsix" --force

echo.
echo ======================================
echo ✅ Acelang extension installed successfully!
echo ======================================
echo.
echo Features:
echo   • Syntax highlighting for .ac files
echo   • Comments: # (single-line) and /; ... ;/ (multi-line)
echo   • Keywords: setr, set, sets, add_ace, ensure, etc.
echo   • All FiveM server config commands highlighted
echo.
echo To customize colors, add to your settings.json:
echo   "editor.tokenColorCustomizations": {
echo     "textMateRules": [
echo       {
echo         "scope": "keyword.command.server.acelang",
echo         "settings": { "foreground": "#ff6b9d" }
echo       },
echo       {
echo         "scope": "keyword.control.directive.acelang",
echo         "settings": { "foreground": "#ff6b9d" }
echo       }
echo     ]
echo   }
echo.
pause
