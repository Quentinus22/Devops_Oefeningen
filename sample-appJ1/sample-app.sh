#!/bin/bash
set -e

# 0. cleaning
echo "Oude mappen en containers opruimen..."
rm -rf tempdir
docker stop samplerunning 2>/dev/null || true
docker rm samplerunning 2>/dev/null || true

# 1. Mappenstructuur aanmaken
mkdir -p tempdir
mkdir -p tempdir/templates
mkdir -p tempdir/static

# 2. Bestanden kopiëren (zorg dat deze bestaan in je huidige map!)
cp sample_app.py tempdir/
cp -r templates/* tempdir/templates/
cp -r static/* tempdir/static/

# 3. Dockerfile aanmaken (De Veilige Versie)
echo "Dockerfile genereren..."
echo "FROM python:3.9-slim" > tempdir/Dockerfile
echo "RUN pip install flask --no-cache-dir --disable-pip-version-check --progress-bar off" >> tempdir/Dockerfile
echo "COPY  ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY  ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY  sample_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python /home/myapp/sample_app.py" >> tempdir/Dockerfile

# 4. Bouwen en Starten
echo "Container bouwen..."
cd tempdir
docker build -t sampleapp .

echo "Container starten..."
docker run -t -d -p 5050:5050 --name samplerunning sampleapp
docker ps -a
