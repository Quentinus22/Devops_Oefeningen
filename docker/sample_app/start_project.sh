#!/bin/bash

# Variabelen instellen
APP_IMAGE="mijn_examen_image"
APP_CONTAINER="mijn_examen_container"

echo "--- Starten van Examen Project ---"

# 1. Oude rommel opruimen
docker stop $APP_CONTAINER 2>/dev/null
docker rm $APP_CONTAINER 2>/dev/null

# 2. De image bouwen
echo "Bezig met bouwen van de image..."
docker build -t $APP_IMAGE .

# 3. De container starten
echo "Container opstarten op poort 7000..."
docker run -d -p 7000:7000 --name $APP_CONTAINER --privileged --pids-limit -1 $APP_IMAGE

# 4. Resultaat tonen
docker ps | grep $APP_CONTAINER
echo "Klaar! Check http://localhost:7000"