FROM python:3.9-slim

RUN apt-get update && apt-get install -y stress-ng && rm -rf /var/lib/apt/lists/*
RUN pip install flask psutil

WORKDIR /app
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
