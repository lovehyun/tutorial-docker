# 이미지 빌드
docker build . -t my-express-app:1.0

# 노드 빌드 환경
# 개발 환경 패키지 추가 (--save-dev, -D)
npm install --save-dev nodemon

"scripts": {
    "start": "nodemon app.js"
}

npm start


# 설치 시 (개발도구 제외)
npm install --production


# 추가로 package-lock.json 을 참고해서 정확한(동일한) 버전을 재설치 시
npm clean-install
