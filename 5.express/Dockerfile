# FROM node:alpine
FROM node:10-alpine

RUN apk --no-cache add curl

WORKDIR /app

# ADD app.js /app
# ADD package.json /app
COPY . .

RUN npm install
# RUN npm install --production
# RUN npm clean-install

CMD ["node", "app.js"]
