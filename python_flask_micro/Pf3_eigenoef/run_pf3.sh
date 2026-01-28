#!/bin/bash
set -e

# 1. Oude processen opruimen
echo "Oude microservice processen opruimen..."
pkill -f pf3_service.py || true

# 2. Flask lokaal installeren (zonder de thread-fout van pip)
echo "Flask installeren..."
pip3 install flask --no-cache-dir --progress-bar off --user

# 3. De service starten op de achtergrond
echo "Microservice Pf3 starten op poort 9000..."
nohup python3 pf3_service.py > pf3.log 2>&1 &

echo "----------------------------------------"
echo "Klaar! Check de microservice op:"
echo "Webpagina: http://localhost:9000"
echo "API-Status: http://localhost:9000/status"
echo "----------------------------------------"