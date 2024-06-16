# Dockerfile 내의 주요 옵션
## 우분투(ubuntu) 기반의 이미지에 타임존 설정
- ARG 는 docker build 에서만 설정되는 환경변수
- ENV 는 시스템에 설정되는 환경변수

  ```
  ARG DEBIAN_FRONTEND=noninteractive
  ENV TZ=Asia/Seoul
  RUN apt-get install -y tzdata
  ```

## 알파인(alpine) 기반의 이미지에 타임존 설정
```
RUN apk --no-cache add tzdata && cp /usr/share/zoneinfo/Asia/Seoul /etc/localtime
```

## 우분투에서 dpkg 관련 warning 해결
```
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"
```

## Clean up APT when done.
```
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
```


# 도커 유용한 명령어

## Dangling 이미지 삭제하기
```
docker rmi $(docker images -f "dangling=true" -q)
```


# Alpine 리눅스 주요 명령어

## 알파인(alpine) 리눅스의 기본 패키지 업데이트 및 설정
```
apk update
apk add curl
```
