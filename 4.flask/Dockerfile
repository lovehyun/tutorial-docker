FROM python:3.8-alpine

# RUN apk add --update curl && \
#     rm -rf /var/cache/apk/*

# RUN pip install flask

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]

# Using unbuffered output to see the python "print" in "docker logs my-app"
# ENTRYPOINT ["python", "-u", "app.py"]
# or -e PYTHONUNBUFFERED=1 with docker cmd

EXPOSE 5000
