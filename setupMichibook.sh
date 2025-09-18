#!/usr/bin/env bash

# --------------------------------------------
# 🐱 Michibook - Script de Instalación y Ejecución
# --------------------------------------------

echo "🚀 Iniciando instalación de Michibook..."

# Verificar si Python está instalado
if ! command -v python3 &>/dev/null; then
    echo "❌ Python3 no está instalado. Por favor instala Python 3.10+."
    exit 1
fi

# Crear entorno virtual
echo "📦 Creando entorno virtual..."
python3 -m venv venv

# Activar entorno virtual
echo "🔑 Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias
if [ -f "requirements.txt" ]; then
    echo "📥 Instalando dependencias..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "⚠️ No se encontró requirements.txt. Abortando."
    exit 1
fi

# Crear archivo .env si no existe
if [ ! -f ".env" ]; then
    echo "📝 Creando archivo .env por defecto..."
    cat <<EOT >> .env
SECRET_KEY=coloca_tu_clave_aqui
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
# REDIS_URL=redis://127.0.0.1:6379/0
EOT
else
    echo "ℹ️ Archivo .env ya existe, no se sobrescribirá."
fi

# Migraciones
echo "📂 Aplicando migraciones..."
python manage.py migrate

# Crear superusuario (opcional)
read -p "¿Quieres crear un superusuario ahora? (y/n): " crear_super
if [ "$crear_super" = "y" ]; then
    python manage.py createsuperuser
fi

# Ejecutar servidor de desarrollo
read -p "¿Quieres iniciar el servidor ahora? (y/n): " iniciar
if [ "$iniciar" = "y" ]; then
    echo "🚀 Iniciando servidor en http://127.0.0.1:8000..."
    python manage.py runserver
else
    echo "✅ Instalación completada. Ejecuta 'source venv/bin/activate' y 'python manage.py runserver' para iniciar el proyecto."
fi
