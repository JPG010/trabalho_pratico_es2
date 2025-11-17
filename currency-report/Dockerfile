FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py ./
ENV SERVICE_PORT=8100
EXPOSE 8100
CMD ["python", "app.py"]

