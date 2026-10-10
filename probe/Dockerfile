FROM python:2.7-slim
COPY . /app
RUN pip install -r /app/probe/requirements.txt
CMD ["python", "/app/probe/settings.py"]
