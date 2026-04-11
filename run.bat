@echo off
setlocal enabledelayedexpansion

echo Launching PyAutoClicker Pro Modern...
python "AutoClicker Pro Modern.py"

if errorlevel 1 (
    echo.
    echo ERROR: Failed to run the application.
    echo Make sure you have run setup.bat first!
    echo.
    pause
)
