FROM python:3.8-alpine

RUN pip install flask

WORKDIR /app
COPY . /app

CMD ["python", "app.py"]

EXPOSE 5000
