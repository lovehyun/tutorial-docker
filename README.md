# Docker 튜토리얼
## 튜토리얼 코드 설명
- 도커 튜토리얼을 따라히실 분들은 디렉토리 순서대로 학습 하시기 바랍니다.
### 1.hello
- 도커의 핼로우 월드
- 빌드 : ` docker build --tag myecho:0.1 . `
- 실행 : ` docker run --rm myecho:0.1 `
### 2.nginx
- nginx 내손으로 만들기
- 빌드 : ` docker build --tag mynginx:0.1 . `
- 시행 : ` docker run -d -p 80:80 mynginx:0.1 `
### 3.flask
- flask 앱 만들기
- 빌드 : ` docker build --tag mypytonapp:0.1 . `
- 실행 : ` docker run -p 5000:5000 mypythonapp:0.1 `
### 4.flask
- flask 앱 만들기
- 빌드 : ` docker build --tag mypythonapp:0.2 . `
- 실행 : ` docker run -d -e APP_COLOR=red -p 5000:5000 mypythonapp:0.2 `
### 5.express
- express 앱 만들기
- 빌드 : ` docker build --tag myexpressapp:0.1 . `
- 실행 : ` docker run -d -p 8000:8000 myexpressapp:0.1 `
