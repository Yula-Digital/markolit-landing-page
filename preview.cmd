@echo off
REM ── תצוגה מקדימה מקומית של דף הנחיתה ──
REM פותח שרת מקומי. מה שרואים כאן = בדיוק מה שיעלה לאוויר.
cd /d "%~dp0production_deploy"
echo.
echo  פתח בדפדפן:  http://localhost:8765
echo  לעצירה: Ctrl+C
echo.
python -m http.server 8765
