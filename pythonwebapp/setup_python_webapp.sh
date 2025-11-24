#!/usr/bin/env bash
set -euo pipefail

# 📌 Carpeta del usuario actual
HOME_DIR="$HOME"

# 📌 Carpeta del proyecto (universal)
APP_DIR="$HOME_DIR/imw-vps-pythonwebapp/pythonwebapp"
ENV_DIR="$APP_DIR/venv"
SERVICE="pythonwebapp.service"

echo "�� Instalando Python..."
sudo apt update -y && sudo apt install -y python3 python3-venv python3-pip

echo "📁 Creando carpeta del proyecto (si no existe)..."
mkdir -p "$APP_DIR"

echo "🐍 Creando entorno virtual..."
python3 -m venv "$ENV_DIR"
source "$ENV_DIR/bin/activate"

echo "📦 Instalando Flask..."
pip install flask

echo "📁 Verificando carpeta static..."
mkdir -p "$APP_DIR/static"
if ! [[ -f "$APP_DIR/static/video.mp4" && -f "$APP_DIR/static/fondo.gif" ]]; then
    echo "⚠️ Debes copiar video.mp4 y fondo.gif en la ruta:"
    echo "👉 $APP_DIR/static"
    exit 1
fi

echo "🛠 Creando servicio systemd..."
sudo tee "/etc/systemd/system/$SERVICE" >/dev/null <<EOF
[Unit]
Description=Python Flask WebApp (HTTP)
After=network.target

[Service]
User=$USER
WorkingDirectory=$APP_DIR
Environment=PATH=$ENV_DIR/bin
ExecStart=$ENV_DIR/bin/python $APP_DIR/app.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

echo "🚀 Iniciando servicio..."
sudo systemctl daemon-reload
sudo systemctl enable $SERVICE
sudo systemctl restart $SERVICE

echo "🎉 Instalación completa!"
echo "�� HTTP disponible en: http://<IP>:5000"
echo "📌 Ejecutándose automáticamente si reinicias el sistema."
