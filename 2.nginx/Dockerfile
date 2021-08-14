FROM ubuntu:20.04

MAINTAINER shpark <emailaddress> 

RUN apt-get update && \
    apt-get install nginx -y && \
    echo "\ndaemon off;" >> /etc/nginx/nginx.conf

ENTRYPOINT ["nginx"]
# CMD ["nginx", "-g", "daemon off;"]

EXPOSE 80
