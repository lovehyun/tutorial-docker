FROM python:3.8-alpine

# RUN pip install flask
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

ENTRYPOINT ["python", "app.py"]

EXPOSE 5000
