# 도커 컴포즈 개요

## 도커 컴포즈 배경
- 생략 (수업 참고)

## 도커 설치
- 도커 설치 환경
  - Ubuntu 20.04 (VirtualBox)
- 설치 방법
  - 방법1 (추천) : ` sudo apt install docker-compose `

## 최신 도커 컴포즈 설치
Docker 공식 GPG 키 추가
```bash
sudo apt update
sudo apt install ca-certificates curl gnupg -y
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo tee /etc/apt/keyrings/docker.asc > /dev/null
```

Docker 공식 저장소 추가
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Docker Compose Plugin 설치
```bash
sudo apt update
sudo apt install docker-compose-plugin -y
docker compose version
```

기존 docker-compose 명령어는 더 이상 사용하지 않고, docker compose (띄어쓰기)로 실행합니다.
Docker Compose V2는 Docker CLI에 통합된 최신 방식입니다.


## 도커 컴포즈 문법
- https://docs.docker.com/compose/compose-file/
- https://docs.docker.com/compose/compose-file/compose-file-v3/
- https://docs.docker.com/compose/compose-file/compose-file-v2/

## 실습
### 1. 기본 명령어
- 생성/종료(삭제)/중지/시작
  - ` docker-compose up `
  - ` docker-compose up -d `
  - ` docker-compose down `
  - ` docker-compose stop `
  - ` docker-compose start `

### 2. 상세 명령어
- 특정 파일명으로 만들어진 컴포즈 파일 실행
  - ` docker-compose -f myapp.yml -f myapp2.yml up -d `
- 프로세스 상태 보기 (내가 관리하는 컴포즈 파일 내의 컨테이너)
  - ` docker-compose ps `
- 설정 파일 보기
  - ` docker-compose config `
- 프로세스 로그 보기 (내가 관리하는 컴포즈 파일 내의 컨테이너)
  - ` docker-compose logs -f web `
- 특정 서비스(컨테이너) 내의 명령어 실행 (별도 컨테이너로 생성 됨)
  - ` docker-compose run web env `
- 현재 서비스(컨테이너) 내의 명령어 실행 (동작중인 컨테이너에서 명령 실행)
  - ` docker-compose exec db psql postgres postgres `

### 3. 실습 예제
- 플라스크 앱 도커 컴포즈로 생성하기
  - ` docker-dompose-eg1.yml `
- 플라스크 앱 및 SQL 컨테이너 생성하기
  - ` docker-dompose-eg2.yml `
- 플라스크 앱 및 SQL 컨테이너 생성하기 (다양한 설정 - 볼륨, 네트워크, 연관성)
  - ` docker-dompose-eg3.yml `
  - https://docs.docker.com/compose/networking/
  - https://docs.docker.com/compose/startup-order/

### 4. 실제 예제
- 워드프레스/MySQL 예제 : demo1_wordpress
  - 설정파일 리뷰 및 실행
    - ` docker-compose up -d `
  - 필요 시 DB 계정 생성
    - ` mysql -u root -p `
      ```bash
      create database wordpress;
      create user wp-user@'10.0.%' identified by '<my-password>';
      grant all privileges on wordpress.* to wp-user@'10.0.%' identified by '<my-password>' with grant option;
      flush privileges;
      ```
  - 권한 조회
    - ` show grants for my-user@'10.0.%' `
  - 권한 삭제
    - ` revoke all on wordpress from wp-user@'10.0.%' `
- 워드프레스/MySQL/phpMyAdmin 예제 : demo1_wordpress
  - 환경변수 필요 시 생성 (.env)
    ```bash
    MYSQL_ROOT_PASSWORD=this-is-my-password
    MYSQL_USER=wp-user
    MYSQL_USER_PASWORD=this-is-my-password
    ```
  - 설정파일 리뷰 및 실행
    - ` docker-compose up -d -f .env `
