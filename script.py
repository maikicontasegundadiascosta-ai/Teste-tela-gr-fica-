import os
import subprocess
import time

print("[*] Iniciando display virtual...")
os.system("Xvfb :99 -screen 0 1280x800x24 &")
time.sleep(2)

os.environ["DISPLAY"] = ":99"

print("[*] Iniciando D-Bus e XFCE4...")
subprocess.Popen(["dbus-launch", "startxfce4"])

vnc_port = os.environ.get("PORT", "10000")
print(f"[*] Iniciando VNC na porta {vnc_port}...")
os.system(f"x11vnc -display :99 -rfbport {vnc_port} -nopw -forever &")

while True:
    time.sleep(60)
    
