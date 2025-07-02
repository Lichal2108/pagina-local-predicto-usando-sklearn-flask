@echo off
echo Iniciando Predictor de Cancer de Mama con Gemini API...
echo.
echo Verificando dependencias...

REM Verificar si Python está disponible
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python no encontrado en PATH, usando ruta completa...
    C:\Users\Richard\AppData\Local\Programs\Python\Python313\python.exe prueba.py
) else (
    echo Python encontrado, iniciando aplicacion...
    python prueba.py
)

pause 