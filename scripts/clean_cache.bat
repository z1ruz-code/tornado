@echo off
cd /d "%~dp0.."
rmdir /s /q __pycache__ 2>nul
echo Cache cleaned.
pause
