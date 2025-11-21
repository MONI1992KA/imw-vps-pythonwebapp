# Tutorial para poner en marcha el programa atraves de un script.

## Pasos

Conéctate al servidor por SSH:
ssh isard@<server-ip>

Tenemos que estar en root directamente para que funcione nuestra aplicación. 

## Clona el repositorio:

git clone https://github.com/MONI1992KA/imw-vps-pythonwebapp

Asigna permisos de ejecución y ejecuta el script:

chmod +x setup_python_webapp.sh
./setup_python_webapp.sh

# Instrucciones posteriores a la instalación

Si vieras algún fallo podemos usar los siguientes comandos para parar, reiniciar y ver el estado. 

sudo systemctl stop pythonwebapp.service

sudo systemctl restart pythonwebapp.service

sudo systemctl status pythonwebapp.service
