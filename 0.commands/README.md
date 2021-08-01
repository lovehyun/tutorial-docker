# 도커 개요

## 도커 배경
- 생략 (수업 참고)

## 도커 설치
- 도커 설치 환경
  - Ubuntu 20.04 (VirtualBox)
- 설치 방법
  - 방법1 (추천) : ` sudo apt install docker.io `
  - 방법2 (비추천) : ` curl -fsSL https://get.docker.com | sudo sh `
- 권한 부여
  - 사용자 권한 : ` sudo usermod -aG docker ${USER} `
- 도커 디렉토리 변경
  - ` docker info | grep -i "Root" `
  - ` sudo vi /lib/systemd/system/docker.service `
  - ` ExecStart= (중략) --data-root=/data/docker_dir `

## 도커 이미지
- 퍼블릭 도커 허브
  - 경로 : https://hub.docker.com

## 실습
### 1. Hello, Docker
- 명령: ` docker run hello-world `
- 명령: ` docker run docker/whalesay cowsay Hello World! ` 

### 2. 기본 명령어
- ` docker ps `
- ` docker ps -a `
- ` docker images `

### 3. 커널
- 이미지 풀
    - ` docker pull ubuntu:14.04 `
    - ` docker pull ubuntu:16.04 `
    - ` docker pull ubuntu:18.04 `
- 이미지 실행 및 버전 확인
    - <code> docker run -it ubuntu:14.04 bash \
        uname -a \
        cat /etc/*-release </code>

### 4. 실행, 접속, 종료
- 실행, 종료 및 접속
    - ` docker start xxx `
    - ` docker attach xxx `
- 종료, 삭제 (컨테이너)
    - ` docker stop xxx `
    - ` docker rm xxx `
    - ` docker rm -f xxx `
    - ` docker rm $(docker ps -aq) `
- 삭제 (이미지)
    - ` docker rmi xxx `
    - ` docker rmi $(docker images -q) `

### 5. 실습 예제 
- 실습1. 프로세스, 접속
    - <code> docker run ubuntu sleep 100 \
        docker ps -a \
        docker exec \<name\> cat /etc/hosts </code>
- 실습2. 포트 바인딩
    - ` docker run nginx `
    - ` docker run --name mynginx -p 80:80 -d nginx `
- 실습3. 포트 바인딩
    - ` docker run redis `
    - ` docker run -d -p 6379:6379 redis `
    - <code> telnet localhost 6379 \
        set hello world
        get hello </code>
- 실습4. 환경변수, 디렉토리 바인딩(호스트패스, 볼륨)
    - ` docker run --name mysqldb -d -p 3306:3306 mysql:5.7 `
    - ` docker logs mysqldb `
    - ` docker run --name mysqldb -d -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=true mysql:5.7 `
    - ` docker logs -f xxxx `
    - ` mysql -h127.0.0.1 -uroot `
    - ` docker run -d -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=true --name mysqldb -v /data/database:/var/lib/mysql mysql:5.7 ` 
    - ` docker volume create mysql_volume `
    - ` docker run -d -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=true --name mysqldb -v mysql_volume:/var/lib/mysql mysql:5.7 ` 
- 실습5. 네트워크
    - ` docker inspect xxx `
    - ` docker inspect xxx | grep "IPAddress" `
    - ` docker network create --driver bridge --subnet 192.168.222.0/24 my-network `
    - <code> docker run ubuntu:16.04 --network=my-network bash \
        apt update \
        apt install net-tools -y \
        apt install iputils-ping </code>
    - ` docker network ls `
    - ` docker network prune `
- 실습6. 도커간 연동 (워드프레스 & DB)
    - ` docker run -d -p 8080:80 --link mysql:mydatabase -e WORDPRESS_DB_HOST=mydatabase -e WORDPRESS_DB_NAME=wp -e WORDPRESS_DB_USER=wp -e WORDPRESS_DB_PASSWORD=wp wordpress `
    - <code> mysql -h127.0.0.1 -uroot \
        create database wp; \
        grant all privileges on wp.* to wp@'%' identified by 'wp'; \
        flush privileges; \
        quit </code>
