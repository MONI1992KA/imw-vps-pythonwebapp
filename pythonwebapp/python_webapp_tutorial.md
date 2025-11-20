- **Introducción**

## 🔹 Características generales de Python

- - **Lenguaje:** Python
    - **Tipo:** Interpretado (no requiere compilación previa).
    - **Paradigma:** Multiparadigma (soporta programación estructurada, orientada a objetos y funcional).
    - **Facilidad:** Sintaxis sencilla, ideal para desarrollo rápido y aprendizaje.
    - **Popularidad:** Uno de los lenguajes más usados para desarrollo web, ciencia de datos, IA, automatización, etc.

## 🔹 Uso de Python en aplicaciones web

Python se utiliza ampliamente para el desarrollo de aplicaciones web dinámicas.

No se suele servir directamente desde el intérprete, sino que se apoya en frameworks web, que gestionan las peticiones HTTP y la generación de respuestas.

## 🔹 Frameworks comunes

- - **Flask:** minimalista y fácil de usar, ideal para proyectos pequeños o educativos.
    - **Django:** completo y estructurado, orientado a aplicaciones grandes.
    - **FastAPI:** moderno, rápido, ideal para APIs REST.

En este tutorial usaremos **Flask** por su sencillez.

- **Objetivo del tutorial**

Aprenderás a desplegar una aplicación web dinámica en Python usando Flask en un servidor Linux (por ejemplo Ubuntu), de forma que:

- - La web muestre información dinámica del cliente (IP, navegador, hora, etc.).
    - El servicio se inicie automáticamente al arrancar el servidor (systemd).
    - La aplicación pueda editarse remotamente desde VSCode vía SSH.

- **Requisitos previos**

## En el servidor

- - Linux (Ubuntu 22.04 recomendado)
    - Acceso SSH
    - Python 3 instalado
    - pip y venv disponibles
    - systemd (ya incluido en la mayoría de distribuciones)
    - VSCode o VSCodium con extensión **Open Remote - SSH - jeanp413**

## En el cliente (tu PC)

- - VSCode/VSCodium instalado
    - Conexión SSH configurada al servidor

- **Pasos del tutorial**

**Paso 1. Acceso al servidor** 

Conéctate por SSH:

ssh usuario@ip_del_servidor

## Paso 2. Crear un entorno de trabajo

mkdir ~/miweb 
cd ~/miweb
python3 -m venv venv 
source venv/bin/activate


## Paso 3. Instalar Flask

pip install flask

## Paso 4. Crear la aplicación Flask

Crea el archivo app.py:

**from flask import Flask, request, render_template_string, redirect, url_for**

**import platform import datetime import os**

**app = Flask( name )**

**@app.route('/') def index():**

**user_agent = request.headers.get('User-Agent') client_ip = request.remote_addr**

**fecha_hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') python_version = platform.python_version()**

**video_url = "/static/video.mp4" fondo_gif_url = "/static/fondo.gif"**

**html = f"""**

**&lt;!DOCTYPE html&gt;**

**&lt;html lang="es"&gt;**

**&lt;head&gt;**

**&lt;meta charset="utf-8"/&gt;**

**&lt;meta name="viewport" content="width=device-width,initial-scale=1"/&gt;**

**&lt;title&gt;💀 Aplicación Python - Red Cibernética&lt;/title&gt;**

**&lt;style&gt;**

**:root {{**

**\--neon: #00ff9f;**

**\--accent: #00ffcc;**

**\--card-bg: rgba(0,0,0,0.6);**

**}}**

**html, body {{**

**height:100%; margin:0;**

**font-family:Segoe UI, Roboto, monospace; color:var(--neon); overflow:hidden;**

**}}**

**body {{**

**display:flex;**

**align-items:center; justify-content:center;**

**background: url('{fondo_gif_url}') center/cover**

**no-repeat;**

**}}**

**.card {{**

**background: var(--card-bg);**

**border:1px solid rgba(0,255,150,0.12); padding:32px 44px;**

**border-radius:12px;**

**box-shadow:0 12px 30px rgba(0,255,150,0.06);**

**max-width:760px; text-align:center; z-index:1;**

**backdrop-filter: blur(6px);**

**}}**

**h1 {{ color:var(--accent); margin:0 0 8px 0; font-size:1.6rem; }}**

**p {{ margin:6px 0; color:#dfffe8; }}**

**.show-btn {{**

**display:inline-block; margin-top:14px; padding:10px 18px; border-radius:8px;**

**background: linear-gradient(180deg, rgba(0,255,170,0.12), rgba(0,255,170,0.05));**

**color:#bfffe6; font-weight:700;**

**text-decoration:none;**

**border:1px solid rgba(255,255,255,0.06); cursor:pointer;**

**transition:transform .12s ease, box-shadow .12s ease;**

**}}**

**.show-btn:hover {{ transform:translateY(-4px);**

**box-shadow:0 10px 30px rgba(0,255,150,0.08);**

**}}**

**.contact-btn {{ display:inline-block; margin:10px; padding:10px 18px; border-radius:8px;**

**background: linear-gradient(180deg, rgba(0,150,255,0.12), rgba(0,150,255,0.05));**

**color:#bfe6ff; font-weight:700;**

**text-decoration:none;**

**border:1px solid rgba(255,255,255,0.06); cursor:pointer;**

**transition:transform .12s ease, box-shadow .12s ease;**

**}}**

**.contact-btn:hover {{ transform:translateY(-4px);**

**box-shadow:0 10px 30px rgba(0,150,255,0.08);**

**}}**

**footer {{**

**position:fixed; bottom:0; left:50%;**

**transform:translateX(-50%); font-size:0.82rem; color:rgba(0,255,150,0.5); padding:10px 0;**

**text-align:center;**

**}}**

**.overlay {{**

**position:fixed; inset:0; display:none;**

**align-items:center; justify-content:center; z-index:9999;**

**background:rgba(0,0,0,0.85); overflow:hidden;**

**flex-direction:column;**

**}}**

**.overlay.show {{ display:flex; }}**

**.gif-fill {{**

**width:100%; height:100%; object-fit:cover;**

**filter:contrast(1.05) saturate(1.2) brightness(0.95);**

**}}**

**.back-btn {{**

**position:fixed; top:20px; right:20px; padding:10px 16px; border-radius:8px;**

**background: rgba(0,0,0,0.6);**

**color: var(--neon); font-weight:700; cursor:pointer;**

**border:1px solid rgba(255,255,255,0.06); z-index:10010;**

**}}**

**&lt;/style&gt;**

**&lt;/head&gt;**

**&lt;body&gt;**

**&lt;div class="card" role="main" aria-labelledby="tit"&gt;**

**&lt;h1 id="tit"&gt;Información del Cliente 💀&lt;/h1&gt;**

**&lt;p&gt;📅 &lt;strong&gt;Fecha y hora del servidor:&lt;/strong&gt;**

**{fecha_hora}&lt;/p&gt;**

**&lt;p&gt;🌐 &lt;strong&gt;IP del cliente:&lt;/strong&gt; {client_ip}&lt;/p&gt;**

**&lt;p&gt;🧭 &lt;strong&gt;Navegador:&lt;/strong&gt; {user_agent}&lt;/p&gt;**

**&lt;p&gt;🐍 &lt;strong&gt;Versión de Python:&lt;/strong&gt;**

**{python_version}&lt;/p&gt;**

**&lt;p&gt;🖥 &lt;strong&gt;Resolución de pantalla:&lt;/strong&gt; &lt;span id="resolution"&gt;Cargando...&lt;/span&gt;&lt;/p&gt;**

**&lt;button class="show-btn" id="openAnim"&gt;Ver Quieres recuperarlo?&lt;/button&gt;**

**&lt;br&gt;**

**&lt;a href="/contacto" class="contact-btn"&gt;Contacto&lt;/a&gt;**

**&lt;/div&gt;**

**&lt;footer&gt;hecho por Alejandro Batista, Joel Santana y Yeremy Travieso&lt;/footer&gt;**

**&lt;div class="overlay" id="overlay"&gt;**

**&lt;div class="gif-wrap"&gt;**

**&lt;video id="videoFill" class="gif-fill" src="{video_url}" loop playsinline&gt;&lt;/video&gt;**

**&lt;/div&gt;**

**&lt;button class="back-btn" id="backBtn"&gt;Atrás&lt;/button&gt;**

**&lt;/div&gt;**

**&lt;script&gt;**

**const resolution = document.getElementById('resolution'); resolution.textContent = window.screen.width + ' x ' +**

**window.screen.height;**

**const openBtn = document.getElementById('openAnim'); const overlay = document.getElementById('overlay'); const backBtn = document.getElementById('backBtn'); const video = document.getElementById('videoFill');**

**openBtn.addEventListener('click', () => {{ overlay.classList.add('show'); video.play(); document.body.style.overflow = 'hidden';**

**}});**

**backBtn.addEventListener('click', () => {{ overlay.classList.remove('show'); video.pause(); document.body.style.overflow = '';**

**}});**

**document.addEventListener('keydown', (e) => {{ if(e.key === 'Escape' &&**

**overlay.classList.contains('show')) {{**

**overlay.classList.remove('show'); video.pause(); document.body.style.overflow = '';**

**}}**

**}});**

**&lt;/script&gt;**

**&lt;/body&gt;**

**&lt;/html&gt; """**

**return render_template_string(html)**

**#**

**\# Página de contacto #**

**@app.route('/contacto', methods=\['GET', 'POST'\]) def contacto():**

**if request.method == 'POST':**

**nombre = request.form.get('nombre') email = request.form.get('email') mensaje = request.form.get('mensaje')**

**print(f"Datos del formulario - Nombre: {nombre}, Email:**

**{email}, Mensaje: {mensaje}")**

**return redirect(url_for('confirmacion'))**

**fondo_gif_url = "/static/fondo.gif"**

**html_form = f"""**

**&lt;!DOCTYPE html&gt;**

**&lt;html lang="es"&gt;**

**&lt;head&gt;**

**&lt;meta charset="utf-8"/&gt;**

**&lt;meta name="viewport" content="width=device-width,initial-scale=1"/&gt;**

**&lt;title&gt;📝 Formulario de Contacto&lt;/title&gt;**

**&lt;style&gt;**

**:root {{**

**\--neon: #00ff9f;**

**\--accent: #00ffcc;**

**\--card-bg: rgba(0,0,0,0.6);**

**}}**

**html, body {{**

**height:100%; margin:0;**

**font-family:Segoe UI, Roboto, monospace; color:var(--neon);**

**overflow:auto;**

**}}**

**body {{**

**display:flex; align-items:center; justify-content:center;**

**background: url('{fondo_gif_url}') center/cover**

**no-repeat;**

**padding:20px;**

**}}**

**.card {{**

**background: var(--card-bg);**

**border:1px solid rgba(0,255,150,0.12); padding:32px 44px;**

**border-radius:12px;**

**box-shadow:0 12px 30px rgba(0,255,150,0.06); max-width:600px;**

**width:100%;**

**backdrop-filter: blur(6px);**

**}}**

**h1 {{ color:var(--accent); margin:0 0 20px 0; text-align:center; }}**

**&lt;/style&gt;**

**&lt;/head&gt;**

**&lt;body&gt;**

**&lt;div class="card"&gt;**

**&lt;h1&gt;📝 Formulario de Contacto&lt;/h1&gt;**

**&lt;form method="POST"&gt;**

**&lt;label for="nombre"&gt;Nombre:&lt;/label&gt;**

**&lt;input type="text" id="nombre" name="nombre" required&gt;**

**&lt;label for="email"&gt;Email:&lt;/label&gt;**

**&lt;input type="email" id="email" name="email" required&gt;**

**&lt;label for="mensaje"&gt;Mensaje:&lt;/label&gt;**

**&lt;textarea id="mensaje" name="mensaje" placeholder="Escribe tu mensaje aquí..." required&gt;&lt;/textarea&gt;**

**&lt;br&gt;&lt;br&gt;**

**&lt;button type="submit"&gt;Enviar&lt;/button&gt;**

**&lt;a href="/"&gt;Volver&lt;/a&gt;**

**&lt;/form&gt;**

**&lt;/div&gt;**

**&lt;footer&gt;hecho por Alejandro Batista, Joel Santana y Yeremy Travieso&lt;/footer&gt;**

**&lt;/body&gt;**

**&lt;/html&gt; """**

**return render_template_string(html_form)**

**#**

**\# Página de confirmación #**

**@app.route('/confirmacion') def confirmacion():**

**fondo_gif_url = "/static/fondo.gif"**

**html_confirmacion = f"""**

**&lt;!DOCTYPE html&gt;**

**&lt;html lang="es"&gt;**

**&lt;head&gt;**

**&lt;meta charset="utf-8"/&gt;**

**&lt;meta name="viewport" content="width=device-width,initial-scale=1"/&gt;**

**&lt;title&gt;✅ Mensaje Enviado&lt;/title&gt;**

**&lt;style&gt;**

**:root {{**

**\--neon: #00ff9f;**

**\--accent: #00ffcc;**

**\--card-bg: rgba(0,0,0,0.6);**

**}}**

**html, body {{**

**height:100%; margin:0;**

**font-family:Segoe UI, Roboto, monospace; color:var(--neon);**

**}}**

**body {{**

**display:flex; align-items:center; justify-content:center;**

**background: url('{fondo_gif_url}') center/cover**

**no-repeat;**

**}}**

**.card {{**

**background: var(--card-bg); padding:32px 44px;**

**border-radius:12px; text-align:center;**

**}}**

**&lt;/style&gt;**

**&lt;/head&gt;**

**&lt;body&gt;**

**&lt;div class="card"&gt;**

**&lt;div class="success-icon"&gt;✅&lt;/div&gt;**

**&lt;h1&gt;¡Mensaje Enviado!&lt;/h1&gt;**

**&lt;p&gt;Tu formulario ha sido recibido correctamente.&lt;/p&gt;**

**&lt;p&gt;Gracias por contactarnos.&lt;/p&gt;**

**&lt;a href="/"&gt;Volver al Inicio&lt;/a&gt;**

**&lt;br&gt;&lt;br&gt;**

**&lt;a href="/contacto"&gt;Enviar otro mensaje&lt;/a&gt;**

**&lt;/div&gt;**

**&lt;footer&gt;hecho por Alejandro Batista, Joel Santana y Yeremy Travieso&lt;/footer&gt;**

**&lt;/body&gt;**

**&lt;/html&gt; """**

**return render_template_string(html_confirmacion)**

**#**

**\# Ejecutar servidor #**

**if name == " main ":**

**app.run(host="0.0.0.0", port=5000)**

Guarda y ejecuta:

python app.py

Abre en el navegador:

http://IP_DEL_SERVIDOR:5000


## Paso 5. Crear servicio systemd

Archivo: /etc/systemd/system/miweb.service 

\[Unit\]
Description=Aplicación web Flask 
After=network.target

\[Service\] 
User=usuario
WorkingDirectory=/home/usuario/miweb 
ExecStart=/home/usuario/miweb/myapp_env/bin/python app.py 
Restart=always

\[Install\]
WantedBy=multi-user.target

Recarga y activa:

sudo systemctl daemon-reload
sudo systemctl enable miweb.service 
sudo systemctl start miweb.service

Verifica:
sudo systemctl status miweb.service

Ahora para tenerlo por https:

# PASO 1: Modificar el archivo app.py

Reemplaza TODO el contenido de tu app.py con este código:

from flask import Flask, request, render_template_string, redirect, url_for

import platform import datetime import os

import ssl

from threading import Thread app = Flask( name )

#

\# Página principal (index) #

@app.route('/') def index():

user_agent = request.headers.get('User-Agent') client_ip = request.remote_addr

fecha_hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') python_version = platform.python_version()

video_url = "/static/video.mp4" fondo_gif_url = "/static/fondo.gif"

html = f"""

&lt;!DOCTYPE html&gt;

&lt;html lang="es"&gt;

&lt;head&gt;

&lt;meta charset="utf-8"/&gt;

&lt;meta name="viewport" content="width=device-width,initial-scale=1"/&gt;

&lt;title&gt;💀 Aplicación Python - Red Cibernética&lt;/title&gt;

&lt;style&gt;

:root {{

\--neon: #00ff9f;

\--accent: #00ffcc;

\--card-bg: rgba(0,0,0,0.6);

}}

html, body {{

height:100%; margin:0;

font-family:Segoe UI, Roboto, monospace; color:var(--neon); overflow:hidden;

}}

body {{

display:flex; align-items:center; justify-content:center;

background: url('{fondo_gif_url}') center/cover

no-repeat;

}}

.card {{

background: var(--card-bg);

border:1px solid rgba(0,255,150,0.12); padding:32px 44px;

border-radius:12px;

box-shadow:0 12px 30px rgba(0,255,150,0.06); max-width:760px;

text-align:center; z-index:1;

backdrop-filter: blur(6px);

}}

h1 {{ color:var(--accent); margin:0 0 8px 0; font-size:1.6rem; }}

.protocol-badge {{

background: linear-gradient(45deg, #ff6b6b, #4ecdc4); color: white;

padding: 8px 15px; border-radius: 20px; font-weight: bold; margin: 10px 0; display: inline-block; font-size: 0.9rem;

}}

p {{ margin:6px 0; color:#dfffe8; }}

.show-btn, .contact-btn {{ display:inline-block; margin-top:14px; padding:10px 18px; border-radius:8px; font-weight:700;

text-decoration:none;

border:1px solid rgba(255,255,255,0.06); cursor:pointer;

transition:transform .12s ease, box-shadow .12s ease;

}}

.show-btn {{

background: linear-gradient(180deg, rgba(0,255,170,0.12), rgba(0,255,170,0.05));

color: #bfffe6;

}}

.contact-btn {{

background: linear-gradient(180deg, rgba(0,150,255,0.12), rgba(0,150,255,0.05));

color: #bfe6ff;

}}

.show-btn:hover, .contact-btn:hover {{ transform:translateY(-4px);

box-shadow:0 10px 30px rgba(0,255,150,0.08);

}}

footer {{

position:fixed; bottom:0; left:50%; transform:translateX(-50%);

font-size:0.82rem; color:rgba(0,255,150,0.5);

padding:10px 0; text-align:center;

}}

.overlay {{

position:fixed; inset:0; display:none;

align-items:center; justify-content:center; z-index:9999;

background:rgba(0,0,0,0.85); overflow:hidden; flex-direction:column;

}}

.overlay.show {{ display:flex; }}

.gif-fill {{

width:100%; height:100%; object-fit:cover;

filter:contrast(1.05) saturate(1.2) brightness(0.95);

}}

.back-btn {{

position:fixed; top:20px; right:20px; padding:10px 16px;

border-radius:8px; background: rgba(0,0,0,0.6); color: var(--neon);

font-weight:700; cursor:pointer;

border:1px solid rgba(255,255,255,0.06); z-index:10010;

}}

&lt;/style&gt;

&lt;/head&gt;

&lt;body&gt;

&lt;div class="card" role="main" aria-labelledby="tit"&gt;

&lt;div class="protocol-badge"&gt;🔓 Protocolo:

{request.scheme.upper()}&lt;/div&gt;

&lt;h1 id="tit"&gt;Información del Cliente 💀&lt;/h1&gt;

&lt;p&gt;📅 &lt;strong&gt;Fecha y hora del servidor:&lt;/strong&gt;

{fecha_hora}&lt;/p&gt;

&lt;p&gt;🌐 &lt;strong&gt;IP del cliente:&lt;/strong&gt; {client_ip}&lt;/p&gt;

&lt;p&gt;🧭 &lt;strong&gt;Navegador:&lt;/strong&gt; {user_agent}&lt;/p&gt;

&lt;p&gt;🐍 &lt;strong&gt;Versión de Python:&lt;/strong&gt;

{python_version}&lt;/p&gt;

&lt;p&gt;🖥 &lt;strong&gt;Resolución de pantalla:&lt;/strong&gt; &lt;span id="resolution"&gt;Cargando...&lt;/span&gt;&lt;/p&gt;

&lt;button class="show-btn" id="openAnim"&gt;Ver Quieres recuperarlo?&lt;/button&gt;

&lt;br&gt;

&lt;a href="/contacto" class="contact-btn"&gt;Contacto&lt;/a&gt;

&lt;br&gt;

&lt;div style="margin-top: 15px;"&gt;

<a [href="http://192.168.1.15:5000"](http://192.168.1.15:5000/) class="contact-btn" style="background: linear-gradient(45deg, #ff6b6b, #ee5a24);">HTTP&lt;/a&gt;

&lt;a href="<https://192.168.1.15:5001>" class="contact-btn" style="background: linear-gradient(45deg, #00b894, #00cec9);"&gt;HTTPS&lt;/a&gt;

&lt;/div&gt;

&lt;/div&gt;

&lt;footer&gt;hecho por Alejandro Batista, Joel Santana y Yeremy Travieso&lt;/footer&gt;

&lt;div class="overlay" id="overlay"&gt;

&lt;div class="gif-wrap"&gt;

&lt;video id="videoFill" class="gif-fill" src="{video_url}" loop playsinline&gt;&lt;/video&gt;

&lt;/div&gt;

&lt;button class="back-btn" id="backBtn"&gt;Atrás&lt;/button&gt;

&lt;/div&gt;

&lt;script&gt;

const resolution = document.getElementById('resolution'); resolution.textContent = window.screen.width + ' x ' +

window.screen.height;

const openBtn = document.getElementById('openAnim'); const overlay = document.getElementById('overlay'); const backBtn = document.getElementById('backBtn'); const video = document.getElementById('videoFill');

openBtn.addEventListener('click', () => {{ overlay.classList.add('show'); video.play(); document.body.style.overflow = 'hidden';

}});

backBtn.addEventListener('click', () => {{ overlay.classList.remove('show');

video.pause(); document.body.style.overflow = '';

}});

document.addEventListener('keydown', (e) => {{ if (e.key === 'Escape' &&

overlay.classList.contains('show')) {{

overlay.classList.remove('show'); video.pause(); document.body.style.overflow = '';

}}

}});

&lt;/script&gt;

&lt;/body&gt;

&lt;/html&gt; """

return render_template_string(html)

#

\# Página de contacto #

@app.route('/contacto', methods=\['GET', 'POST'\]) def contacto():

if request.method == 'POST':

nombre = request.form.get('nombre') email = request.form.get('email') mensaje = request.form.get('mensaje')

print(f"Datos del formulario - Nombre: {nombre}, Email:

{email}, Mensaje: {mensaje}")

return redirect(url_for('confirmacion'))

"""

fondo_gif_url = "/static/fondo.gif"

html_form = f""" ... (contenido igual que tu formulario actual) ... return render_template_string(html_form)

#

\# Página de confirmación #

@app.route('/confirmacion')

def confirmacion():

fondo_gif_url = "/static/fondo.gif"

html_confirmacion = f""" ... (contenido igual que tu confirmación actual) ... """

return render_template_string(html_confirmacion)

#

\# Servidores HTTP y HTTPS #

def run_https():

"""Ejecutar servidor HTTPS en puerto 5001"""

if not os.path.exists('cert.pem') or not os.path.exists('key.pem'): print("🔐 Generando certificados SSL...")

os.system('openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365 -subj "/C=ES/CN=192.168.1.15" 2>/dev/null')

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2) ssl_context.load_cert_chain('cert.pem', 'key.pem') print("🚀 Servidor HTTPS ejecutándose en:

<https://192.168.1.15:5001>")

app.run(host="0.0.0.0", port=5001, ssl_context=ssl_context, debug=False, use_reloader=False)

def run_http():

"""Ejecutar servidor HTTP en puerto 5000"""

print("🚀 Servidor HTTP ejecutándose en: [http://192.168.1.15:5000"](http://192.168.1.15:5000/)) app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)

#

\# Iniciar ambos servidores #

if name == " main ":

https_thread = Thread(target=run_https) http_thread = Thread(target=run_http)

https_thread.daemon = True http_thread.daemon = True

https_thread.start()

http_thread.start()

print("🎯 Servidores iniciados!")

print("📡 HTTP: [http://192.168.1.15:5000"](http://192.168.1.15:5000/)) print("🔐 HTTPS: <https://192.168.1.15:5001>") print("⏹ Presiona Ctrl+C para detener")

try:

while True: pass

except KeyboardInterrupt:

print("\\n🛑 Deteniendo servidores...")


# PASO 3: Configurar auto-inicio

Ejecuta este comando:

sudo nano /etc/systemd/system/miweb.service

Pega esto:

\[Unit\]
Description=Web Flask con HTTP y HTTPS 
After=network.target

\[Service\] 
Type=simple 
User=isard 
Group=isard
WorkingDirectory=/home/isard/miweb 
Environment=PATH=/home/isard/miweb/venv/bin 
ExecStart=/home/isard/miweb/myapp_env/bin/python
/home/isard/miweb/app.py 
Restart=always RestartSec=5

\[Install\]
WantedBy=multi-user.target

# PASO 4: Activar el servicio

Ejecuta estos comandos:

sudo systemctl daemon-reload
sudo systemctl enable miweb.service 
sudo systemctl start miweb.service 
sudo systemctl status miweb.service