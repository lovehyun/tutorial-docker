# 도커 컴포즈 개요

## 도커 컴포즈 배경
- 생략 (수업 참고)

## 도커 설치
- 도커 설치 환경
  - Ubuntu 20.04 (VirtualBox)
- 설치 방법
  - 방법1 (추천) : ` sudo apt install docker-compose `

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

