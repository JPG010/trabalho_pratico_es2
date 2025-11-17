FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py ./
ENV SERVICE_PORT=8101
EXPOSE 8101
CMD ["python", "app.py"]

