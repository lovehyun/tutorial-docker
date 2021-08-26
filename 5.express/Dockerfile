# FROM node:alpine
FROM node:10-alpine

WORKDIR /app

# ADD app.js /app
# ADD package.json /app
COPY . .

RUN npm install
# RUN npm install --production

CMD ["node", "app.js"]
