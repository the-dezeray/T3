@echo off
cd /d "%~dp0"
windows-terminal\WindowsTerminal.exe -d . cmd /c "python\python.exe your_script.py & pause"
