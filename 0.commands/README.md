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
  - 사용자 권한 : ` sudo usermod -aG docker ${USER} && newgrp docker `
- 도커 디렉토리 변경
  - ` docker info | grep -i "Root" `
  - 방법1 : (비추천) 도커 버전 업데이트 시 시스템 설정 파일 overwrite 될 수 있음
    - ` sudo vi /lib/systemd/system/docker.service `
    - ` ExecStart= (중략) --data-root=/data/docker_dir `
    - ` sudo systemctl daemon-reload `
    - ` sudo systemctl restart docker `
  - 방법2 : (추천) 도커 버전 업데이트와 무관하게 동작
    - ` sudo vi /etc/docker/daemon.json `
      ```json
      {
          "data-root":"/data/docker_dir"
      }
      ```

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
    - ` docker run -it ubuntu:14.04 bash `
      ```bash
      uname -a
      cat /etc/*-release
      ```

### 4. 실행, 접속, 종료 외
- 생성, 실행, 및 접속
    - ` docker create xxx `
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
    - ` docker run ubuntu sleep 100 `
    - ` docker ps -a `
    - ` docker exec <name> cat /etc/hosts `
- 실습2. 포트 바인딩
    - ` docker run nginx `
    - ` docker run --name mynginx -p 80:80 -d nginx `
- 실습3. 포트 바인딩
    - ` docker run redis `
    - ` docker run -d -p 6379:6379 redis `
    - ```bash
      telnet localhost 6379
      set hello world
      get hello
      ```
- 실습4. 환경변수, 디렉토리 바인딩(호스트패스, 볼륨)
    - ` docker run --name mysqldb -d -p 3306:3306 mysql:5.7 `
    - ` docker logs mysqldb `
    - ` docker run --name mysqldb -d -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=true mysql:5.7 `
    - ` docker logs -f xxxx `
    - ` mysql -h127.0.0.1 -uroot `
    - 호스트패스 바인딩 : ` docker run -d -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=true --name mysqldb -v /data/database:/var/lib/mysql mysql:5.7 ` 
    - 볼륨 생성 : ` docker volume create mysql_volume `
    - 볼륨 바인딩 : ` docker run -d -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=true --name mysqldb -v mysql_volume:/var/lib/mysql mysql:5.7 ` 
- 실습5. 네트워크
    - ` docker inspect xxx `
    - ` docker inspect xxx | grep "IPAddress" `
    - ` docker network create --driver bridge --subnet 192.168.222.0/24 my-network `
    - ` docker run ubuntu:16.04 --network=my-network bash `
      ```bash
      apt update
      apt install net-tools -y
      apt install iputils-ping
      ```
    - ` docker network ls `
    - ` docker network prune `
- 실습6. 도커간 연동 (워드프레스 & DB)
    - ` docker run -d -p 8080:80 --link mysql:mydatabase -e WORDPRESS_DB_HOST=mydatabase -e WORDPRESS_DB_NAME=wp -e WORDPRESS_DB_USER=wp -e WORDPRESS_DB_PASSWORD=wp wordpress `
    - ```bash
      mysql -h127.0.0.1 -uroot
      create database wp;
      grant all privileges on wp.* to wp@'%' identified by 'wp';
      flush privileges;
      quit
      ```
- 실습7. 컨테이너 이미지 저장 (vim 설치, main 변경 및 이미지 저장)
    - ` docker run --name my-nginx -p 80:80 -d nginx `
    - ` docker exec -it my-nginx bash `
      ```bash
      apt update
      apt install vim
      vi /usr/share/nginx/index.html
      ```
    - ` docker commit -m 'nginx + vim' my-nginx my-nginx:1.0 `
    - ` docker history my-nginx:1.0 `
