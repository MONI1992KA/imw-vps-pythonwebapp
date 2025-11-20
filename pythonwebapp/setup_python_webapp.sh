#!/usr/bin/env bash
set -euo pipefail

APP_DIR="/root/imw-vps-pythonwebapp/pythonwebapp"
ENV_DIR="$APP_DIR/venv"
SERVICE="pythonwebapp.service"

echo "🔄 Instalando Python y OpenSSL..."
apt update -y && apt install -y python3 python3-venv python3-pip openssl

echo "🐍 Creando entorno virtual..."
python3 -m venv "$ENV_DIR"
source "$ENV_DIR/bin/activate"

echo "📦 Instalando Flask..."
pip install flask

echo "🔐 Generando certificado SSL genérico..."
cd $APP_DIR
if [ ! -f "cert.pem" ] || [ ! -f "key.pem" ]; then
    openssl req -x509 -newkey rsa:2048 -nodes \
    -out cert.pem -keyout key.pem -days 365 \
    -subj "/CN=localhost"
fi


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
echo "🌐 HTTP  : http://<IP>:5000"
echo "🔐 HTTPS : https://<IP>:5001"
