# 이미지 빌드
docker build . -t my-express-app:1.0

# 노드 빌드 환경
# 개발 환경 패키지 추가 (--save-dev, -D)
npm install --save-dev nodemon

"scripts": {
    "start": "nodemon app.js"
}

npm start
