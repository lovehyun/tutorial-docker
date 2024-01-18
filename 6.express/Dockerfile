# FROM node:alpine
FROM node:18-slim

WORKDIR /app

COPY . .

RUN npm install --production

CMD ["node", "app.js"]
