#!/bin/bash

# 1. Bestaande container opruimen
docker stop calc-container 2>/dev/null || true
docker rm calc-container 2>/dev/null || true

# 2. Dockerfile 'on the fly' maken
cat <<EOF > Dockerfile
FROM python:3.9-slim
# We zetten de progress bar uit om de 'can't start new thread' error te voorkomen
RUN pip install --no-cache-dir --progress-bar off flask
COPY calc_app.py .
EXPOSE 6060
CMD ["python", "calc_app.py"]
EOF

# 3. Bouwen en draaien
docker build -t calc-image .
docker run -d -p 6060:6060 --name calc-container calc-image

echo "Klaar! Check http://localhost:6060"