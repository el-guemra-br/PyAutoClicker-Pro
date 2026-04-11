@echo off
setlocal enabledelayedexpansion

echo.
echo ========================================
echo PyAutoClicker Pro - Setup
echo ========================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo Installing required packages...
echo.

:: Install dependencies
python -m pip install --upgrade pip -q
python -m pip install pyautogui keyboard Pillow cairosvg -q

if errorlevel 1 (
    echo ERROR: Failed to install packages.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo You can now run: run.bat
echo.
echo NOTE: SVG icons are optional. If they don't appear,
echo the app will use text buttons instead.
echo.
pause
