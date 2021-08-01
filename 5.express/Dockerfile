FROM node:alpine

WORKDIR /app

# ADD app.js /app
# ADD package.json /app
COPY . /app

RUN npm install

CMD ["node", "app.js"]
