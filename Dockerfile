FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    xvfb \
    x11vnc \
    xfce4 \
    xfce4-goodies \
    dbus-x11 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY script.py .

CMD ["python", "script.py"]
