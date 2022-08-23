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

## 튜토리얼 코드 설명
- 도커 튜토리얼을 따라히실 분들은 디렉토리 순서대로 학습 하시기 바랍니다.

### 1.hello
- 도커의 핼로우 월드
  - 빌드 : ` docker build --tag myhello:0.1 . `
  - 실행 : ` docker run --rm myhello:0.1 `
- 주요 관점
  1. 이미지 빌드하기
  2. Ubuntu 베이스 이미지와 Alpine 베이스 이미지의 용량 차이 비교
  3. 각종 주요 도커파일 키워드(명령어) 확인

### 2.nginx
- nginx 내손으로 만들기
  - 빌드 : ` docker build --tag mynginx:0.1 . `
  - 실행 : ` docker run -d -p 80:80 mynginx:0.1 `
- 주요 관점
  1. 리얼 이미지 만들기
  2. non-interactive 한 형태로 도커파일 만들기
  3. daemonize 되지 않는, foreground 형태로 실행파일 만들기 (콘솔 로그까지 출력되면 best)
  4. TZ 및 clean-up 까지 처리 하면 완벽한 마무리

### 3.flask
- flask 앱 만들기
  - 빌드 : ` docker build --tag myflask:0.1 . `
  - 실행 : ` docker run -p 5000:5000 myflask:0.1 `
- 주요 관점
  1. 실제 앱 만들기
  2. 파일의 복사
  3. 불필요한 파일의 예외처리(.dockerignore)

### 4.flask
- flask 앱 만들기
  - 빌드 : ` docker build --tag myflask:0.2 . `
  - 실행 : ` docker run -d -e APP_COLOR=red -p 5000:5000 myflask:0.2 `
- 주요 관점
  1. 더 리얼한 앱 만들기
  2. 파일 및 디렉토리의 복사
  3. 패키지의 설치 및 Dev 와 Ops 환경의 sync 맞추기

### 5.express
- express 앱 만들기
  - 빌드 : ` docker build --tag myexpress:0.1 . `
  - 실행 : ` docker run -d -p 8000:8000 myexpress:0.1 `
- 주요 관점
  1. JS 앱 만들기
  2. npm, package.json, package-lock.json 및 node_modules 의 명확한 이해
  3. 불필요한 개발도구 파일의 운영 환경에서의 제거
     - ```bash
       npm i express   # npm install express
       npm i -D nodemon   # npm install nodemon --save-dev

       npm install --production    # export NODE_ENV=production 및 npm install
       script { "start": "nodemon app.js" }
       npm start
       ```
  4. Dev 와 Ops 환경의 sync 맞추기

### 6.java
- java 앱 만들기
  - 빌드 : 
    ```bash
    docker build --tag javaapp:0.1 .
    docker build --tag javaapp:0.2 -f Dockerfile.v2 .
    docker build --tag javaapp:0.3 -f Dockerfile.v3 .
    ```
  - 실행 : ` docker run --rm javaapp:0.1 `
- 주요 관점
  1. 싱글 스테이지 빌드 (비효율적 컴파일)
  2. 싱글 스테이지 빌드 (잘못된 바이너리 복사)
  3. 멀티 스테이지 빌드 (올바른 컴파일 및 이미지 최적화)
  4. 멀티 스테이지 빌드 (BEST 예시)

### 7.golang
- golang 앱 만들기
- 빌드 : 
    ```bash
    docker build --tag goapp:0.1 .
    docker build --tag goapp:0.2 -f Dockerfile.v2 .
    ```
- 주요 관점
  1. 싱글 스테이지 빌드 (비효율적 컴파일)
  2. 멀티 스테이지 빌드 (올바른 컴파일 및 이미지 최적화)
  3. 멀티 스테이지 빌드 (BEST 예시)


### 9.dockercompose
- dockercompose 를 사용한 개발/배포/운영


## 도커허브
- https://hub.docker.com/

### 이미지 푸시
- 계정 로그인 : ` docker login `
- 이미지 태깅 : ` docker tag <my-local-image:tag> <account/image:tag> `
- 이미지 푸시 : ` docker push <account/image:tag> `
