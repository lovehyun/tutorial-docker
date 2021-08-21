# Docker 튜토리얼
## 도커 개요
- (생략 - 수업 참조)

## 도커 명령어 기초 배우기
### 0.commands
- [README.md 참고](https://github.com/lovehyun/tutorial-docker/tree/master/0.commands)

## 도커 이미지 빌드
- 공식 메뉴얼 : ` https://docs.docker.com/engine/reference/commandline/build/ `
- 이미지 빌드 후 생긴 <none> 이미지들 모두 삭제
  - ` docker rmi $(docker images --filter "dangling=true" -q --no-trunc) `
- 이미지 빌드 시 <none> 생기지 않도록 빌드
  - ` docker build --rm --tag myimage:0.1 . `

## 튜토리얼 코드 설명
- 도커 튜토리얼을 따라히실 분들은 디렉토리 순서대로 학습 하시기 바랍니다.

### 1.hello
- 도커의 핼로우 월드
- 빌드 : ` docker build --tag myhello:0.1 . `
- 실행 : ` docker run --rm myhello:0.1 `

### 2.nginx
- nginx 내손으로 만들기
- 빌드 : ` docker build --tag mynginx:0.1 . `
- 시행 : ` docker run -d -p 80:80 mynginx:0.1 `

### 3.flask
- flask 앱 만들기
- 빌드 : ` docker build --tag myflask:0.1 . `
- 실행 : ` docker run -p 5000:5000 myflask:0.1 `

### 4.flask
- flask 앱 만들기
- 빌드 : ` docker build --tag myflask:0.2 . `
- 실행 : ` docker run -d -e APP_COLOR=red -p 5000:5000 myflask:0.2 `

### 5.express
- express 앱 만들기
- 빌드 : ` docker build --tag myexpress:0.1 . `
- 실행 : ` docker run -d -p 8000:8000 myexpress:0.1 `

### 9.dockercompose
- dockercompose 를 사용한 개발/배포/운영


## 도커허브
- https://hub.docker.com/

### 이미지 푸시
- 계정 로그인 : ` docker login `
- 이미지 태깅 : ` docker tag <my-local-image:tag> <account/image:tag> `
- 이미지 푸시 : ` docker push <account/image:tag> `
