FROM python:3.8-alpine

# RUN apk add --update curl && \
#     rm -rf /var/cache/apk/*

# RUN pip install flask

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]

EXPOSE 5000
