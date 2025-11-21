from flask import Flask, request, render_template_string, redirect, url_for
import platform
import datetime
import os

app = Flask(__name__)

# -------------------------- #
# Página principal (index)   #
# -------------------------- #
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    client_ip = request.remote_addr
    fecha_hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    python_version = platform.python_version()

    video_url = "/static/video.mp4"
    fondo_gif_url = "/static/fondo.gif"

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width,initial-scale=1"/>
    <title>💀 Aplicación Python - Red Cibernética</title>
    <style>
    :root {{
        --neon:#00ff9f; --accent:#00ffcc; --card-bg:rgba(0,0,0,0.6);
    }}
    html, body {{
        height:100%; margin:0;
        font-family:Segoe UI, Roboto, monospace;
        color:var(--neon); overflow:hidden;
    }}
    body {{
        display:flex; align-items:center; justify-content:center;
        background:url('{fondo_gif_url}') center/cover no-repeat;
    }}
    .card {{
        background:var(--card-bg); border:1px solid rgba(0,255,150,0.12);
        padding:32px 44px; border-radius:12px;
        box-shadow:0 12px 30px rgba(0,255,150,0.06);
        max-width:760px; text-align:center; z-index:1;
        backdrop-filter: blur(6px);
    }}
    h1 {{ color:var(--accent); margin-bottom:10px; }}
    p {{ margin:6px 0; color:#dfffe8; }}
    .show-btn, .contact-btn {{
        display:inline-block; margin-top:14px; padding:10px 18px;
        border-radius:8px; font-weight:700; text-decoration:none;
        border:1px solid rgba(255,255,255,0.06); cursor:pointer;
                transition:transform .12s ease, box-shadow .12s ease;
    }}
    .show-btn {{ background:linear-gradient(180deg,rgba(0,255,170,0.12),rgba(0,255,170,0.05)); color:#>
    .contact-btn {{ background:linear-gradient(180deg,rgba(0,150,255,0.12),rgba(0,150,255,0.05)); colo>
    .show-btn:hover,.contact-btn:hover {{
        transform:translateY(-4px); box-shadow:0 10px 30px rgba(0,255,150,0.08);
    }}
    footer {{
        position:fixed; bottom:0; left:50%; transform:translateX(-50%);
        font-size:0.82rem; color:rgba(0,255,150,0.5); padding:10px 0;
        text-align:center;
    }}
    .overlay {{
        position:fixed; inset:0; display:none; align-items:center;
        justify-content:center; z-index:9999; background:rgba(0,0,0,0.85);
        overflow:hidden; flex-direction:column;
    }}
    .overlay.show {{ display:flex; }}
    .gif-fill {{
        width:100%; height:100%; object-fit:cover;
        filter:contrast(1.05) saturate(1.2) brightness(0.95);
    }}
    .back-btn {{
        position:fixed; top:20px; right:20px; padding:10px 16px;
        border-radius:8px; background:rgba(0,0,0,0.6);
        color:var(--neon); font-weight:700; cursor:pointer;
        border:1px solid rgba(255,255,255,0.06); z-index:10010;
    }}
    </style>
    </head>
    <body>
    <div class="card">
        <h1>Información del Cliente 💀</h1>
        <p>📅 <strong>Fecha y hora del servidor:</strong> {fecha_hora}</p>
        <p>🌐 <strong>IP del cliente:</strong> {client_ip}</p>
        <p>🧭 <strong>Navegador:</strong> {user_agent}</p>
        <p>🐍 <strong>Versión de Python:</strong> {python_version}</p>
        <p>🖥 <strong>Resolución:</strong> <span id="resolution">Cargando...</span></p>
        <button class="show-btn" id="openAnim">Ver Quieres recuperarlo?</button>
        <br>
        <a href="/contacto" class="contact-btn">Contacto</a>
    </div>
    <footer>hecho por Alejandro Batista, Joel Santana y Yeremy Travieso</footer>
    <div class="overlay" id="overlay">
        <div class="gif-wrap">
            <video id="videoFill" class="gif-fill" src="{video_url}" loop playsinline></video>
        </div>
        <button class="back-btn" id="backBtn">Atrás</button>
    </div>
    <script>
        const resolution = document.getElementById('resolution');
    resolution.textContent = window.screen.width + ' x ' + window.screen.height;
    const openBtn=document.getElementById('openAnim');
    const overlay=document.getElementById('overlay');
    const backBtn=document.getElementById('backBtn');
    const video=document.getElementById('videoFill');
    openBtn.addEventListener('click',()=>{{overlay.classList.add('show');video.play();document.body.st>
    backBtn.addEventListener('click',()=>{{overlay.classList.remove('show');video.pause();document.bod>
    document.addEventListener('keydown',(e)=>{{if(e.key==='Escape'&&overlay.classList.contains('show')>
    </script>
    </body>
    </html>
    """
    return render_template_string(html)

# -------------------------- #
# Página de contacto         #
# -------------------------- #
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        print("📨 Formulario enviado!")
        return redirect(url_for('confirmacion'))
    fondo_gif_url = "/static/fondo.gif"
    return f"<h1 style='color:white;text-align:center;margin-top:40px;'>Contacto aquí (simplificado)</>

# -------------------------- #
# Página de confirmación     #
# -------------------------- #
@app.route('/confirmacion')
def confirmacion():
    return "<h1 style='color:lightgreen;text-align:center;margin-top:40px;'>Mensaje enviado correctame>

# -------------------------- #
# Ejecutar servidor          #
# -------------------------- #
def run_http():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run_http()


