# 우분투(ubuntu) 기반의 이미지에 타임존 설정
# ARG 는 docker build 에서만 설정되는 환경변수
# ENV 는 시스템에 설정되는 환경변수

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul

RUN apt-get install -y tzdata


# 알파인(alpine) 기반의 이미지에 타임존 설정

RUN apk --no-cache add tzdata && cp /usr/share/zoneinfo/Asia/Seoul /etc/localtime
