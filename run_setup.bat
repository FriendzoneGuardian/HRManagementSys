@echo off
echo 🦅 Clarion HRMS Launcher 🦅
echo.

:: Check for venv
if exist venv\Scripts\activate.bat (
    echo [*] Activating virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo [!] Virtual environment not found. Using system Python...
)

:: Run the application (which includes auto-setup)
echo [*] Starting Clarion HRMS...
python backend/run.py

pause
