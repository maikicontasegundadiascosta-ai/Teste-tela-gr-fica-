import os
import subprocess
import time

print("[*] Iniciando o ambiente gráfico XFCE4...")

# 1. Configurando o display virtual
display_num = ":99"
resolution = "1280x800x24"
os.system(f"Xvfb {display_num} -screen 0 {resolution} &")
time.sleep(2)

os.environ["DISPLAY"] = display_num

# 2. Subindo a interface completa do XFCE4 em segundo plano
print("[*] Carregando o XFCE4...")
subprocess.Popen(["startxfce4"])

# 3. Iniciando o servidor VNC na porta correta do Render
vnc_port = os.environ.get("PORT", "5900")
print(f"[*] Iniciando o VNC na porta {vnc_port}...")
os.system(f"x11vnc -display {display_num} -rfbport {int(vnc_port)} -nopw -forever &")

print("[+] XFCE4 rodando com sucesso no servidor!")

while True:
    time.sleep(60)
