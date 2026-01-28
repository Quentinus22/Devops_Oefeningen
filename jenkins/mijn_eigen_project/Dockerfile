FROM python:3.9-slim
# We zetten de progress bar uit om de 'can't start new thread' error te voorkomen
RUN pip install --no-cache-dir --progress-bar off flask
COPY calc_app.py .
EXPOSE 6060
CMD ["python", "calc_app.py"]
