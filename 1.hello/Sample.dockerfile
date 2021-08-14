# Full Docs : https://docs.docker.com/engine/reference/builder/

# FROM 이미지:태그 - 태그 기본값은 latest
FROM ubuntu:20.04

# 제작자 - 이 또한 하나의 layer로 생성됨
MAINTAINER shpark <emailaddress> 

# MAINTAINER 는 deprecated 되고, LABEL 을 사용해서 정의
# LABEL <key>=<value> <key>=<value> ...
LABEL org.opencontainers.image.authors="shpark@emailaddress"
LABEL version="1.0" \
      description="This is my app"

# 해당 컨테이너 안에서 실행할 명령어 
# RUN 하나당 하나의 layer 생성. 불필요한 layer 줄이기 위해서는 && \  사용해서 하나의 명령어로 변경
RUN apt-get update 
RUN apt-get install nginx -y && \
    echo "\ndaemon off;" >> /etc/nginx/nginx.conf

# 시작 디렉토리 정의
WORKDIR /data/myapp

# 컨테이너 안으로 파일 복사
# ADD 명령어 사용 시 복사와 함께 풀려서 들어감 - 또한 외부 URL 참조 시 해당 URL 풀어서 들어감
# COPY 명령어 사용 시 원본 그대로 복사 됨
ADD myapp.tar.gz /data/myapp
COPY myapp.tar.gz /data/myapp

# 컨테이너 시작 시 출발점 (명령어)
# CMD 는 컨테이너 실행 시 param 으로 대체됨. Entrypoint 는 대체되지 않음
# 각 명령어의 파라미터는 개별 인자로 입력
ENTRYPOINT ["python", "app.py"]
CMD ["echo", "hello, world"]
CMD ["ls", "-al"]
CMD ["ls", "-a", "-l"]

# 엔트리 포인트와 CMD 혼용해서 사용또한 가능 함
# 단 한 도커파일 내에 하나의 ENTRYPOINT 와 하나의 CMD 만 있어야 함
ENTRYPOINT ["node"]
CMD ["index.js"]

# 컨테이너 내부 파일/디렉토리를 외부와 연결할 수 있음
VOLUME ["/var/lib/mysql"]

# 컨테이너 내부 포트를 외부에서 연결할 수 있음 - 이것과 무관하게 컨테이너 실행 시 -p 명령어 사용 필수
# 기본적으로는 tcp
EXPOSE 5000
EXPOSE 80/tcp
EXPOSE 80/udp

# 컨테이너 내부 실행 시 사용자 계정/권한 - 생략 시 root
USER www-data
