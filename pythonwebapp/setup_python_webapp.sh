#!/usr/bin/env bash
set -euo pipefail

APP_DIR="/root/imw-vps-pythonwebapp/pythonwebapp"
ENV_DIR="$APP_DIR/venv"
SERVICE="pythonwebapp.service"

echo "🔄 Instalando Python..."
apt update -y && apt install -y python3 python3-venv python3-pip

echo "🐍 Creando entorno virtual..."
python3 -m venv "$ENV_DIR"
source "$ENV_DIR/bin/activate"

echo "📦 Instalando Flask..."
pip install flask

echo "📁 Verificando carpeta static..."
mkdir -p "$APP_DIR/static"

if ! [[ -f "$APP_DIR/static/video.mp4" && -f "$APP_DIR/static/fondo.gif" ]]; then
    echo "⚠️ Debes copiar video.mp4 y fondo.gif en $APP_DIR/static"
    exit 1
fi

echo "🛠 Creando servicio systemd..."
cat > "/etc/systemd/system/$SERVICE" <<EOF
[Unit]
Description=Python Flask MultiProtocol WebApp
After=network.target

[Service]
User=root
WorkingDirectory=$APP_DIR
Environment=PATH=$ENV_DIR/bin
ExecStart=$ENV_DIR/bin/python $APP_DIR/app.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

echo "🚀 Iniciando servicio..."
systemctl daemon-reload
systemctl enable $SERVICE
systemctl restart $SERVICE

echo "🎉 Instalación completa!"
echo "🌐 HTTP : http://<IP>:5000"

