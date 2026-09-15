FROM python:3.9-slim

# Instala o XFCE4, o servidor gráfico virtual e o VNC de forma limpa
RUN apt-get update && apt-get install -y \
    xvfb \
    x11vnc \
    xfce4 \
    xfce4-goodies \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY script.py .

CMD ["python", "script.py"]
