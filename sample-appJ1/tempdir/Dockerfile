FROM python:3.9-slim
RUN pip install flask --no-cache-dir --disable-pip-version-check --progress-bar off
COPY  ./static /home/myapp/static/
COPY  ./templates /home/myapp/templates/
COPY  sample_app.py /home/myapp/
EXPOSE 5050
CMD python /home/myapp/sample_app.py
