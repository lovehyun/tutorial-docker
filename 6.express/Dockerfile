# FROM node:alpine
# FROM node:18-slim
FROM node:20-slim

WORKDIR /app

COPY . .

# RUN npm install --production
RUN npm install --omit=dev

CMD ["node", "app.js"]
