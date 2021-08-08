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
 - docker-compose up
 - docker-compose up -d
 - docker-compose down
 - docker-compose start
 - docker-compose stop

### 2. 상세 명령어
 - docker-compose -f myapp.yml -f myapp2.yml up -d
 - docker-compose ps
 - docker-compose config
 - docker-compose logs -f web
 - docker-compose run web env
 - docker-compose exec db psql postgres postgres

