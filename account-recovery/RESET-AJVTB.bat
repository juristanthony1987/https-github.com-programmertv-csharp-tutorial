@echo off
setlocal
cd /d "%~dp0"
call :run_reset
set "RESET_RESULT=%ERRORLEVEL%"
echo.
pause
exit /b %RESET_RESULT%

:run_reset
if exist ".venv\Scripts\python.exe" goto local_venv
if exist "venv\Scripts\python.exe" goto other_venv
where py >nul 2>&1
if not errorlevel 1 goto python_launcher
python reset_ajvtb_password.py
exit /b %ERRORLEVEL%

:local_venv
".venv\Scripts\python.exe" reset_ajvtb_password.py
exit /b %ERRORLEVEL%

:other_venv
"venv\Scripts\python.exe" reset_ajvtb_password.py
exit /b %ERRORLEVEL%

:python_launcher
py -3 reset_ajvtb_password.py
exit /b %ERRORLEVEL%
