@echo off
echo ===========================================
echo Instalando Michibook en Windows...
echo ===========================================

REM 1. Crear entorno virtual si no existe
if not exist venv (
    echo Creando entorno virtual...
    python -m venv venv
) else (
    echo ℹ️ Entorno virtual ya existe.
)

REM 2. Instalar dependencias
echo Instalando dependencias...
call venv\Scripts\python -m pip install --upgrade pip
call venv\Scripts\pip install -r requirements.txt

REM 3. Crear archivo .env si no existe
if not exist ".env" (
    echo 📝 Creando archivo .env...
    (
        echo SECRET_KEY=coloca_tu_clave_aqui
        echo DEBUG=True
        echo ALLOWED_HOSTS=127.0.0.1,localhost
        REM echo REDIS_URL=redis://127.0.0.1:6379/0
    ) > .env
) else (
    echo ℹ️ Archivo .env ya existe, no se sobrescribirá.
)

REM 4. Migraciones
echo Aplicando migraciones...
call venv\Scripts\python manage.py migrate

echo ===========================================
echo Instalación completada.
echo ===========================================
echo Para activar el entorno virtual en esta terminal:
echo.
echo     call venv\Scripts\activate
echo.
echo Luego, para correr el servidor:
echo.
echo     python manage.py runserver
echo.
pause
