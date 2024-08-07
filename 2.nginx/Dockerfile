FROM ubuntu:20.04

MAINTAINER shpark <emailaddress> 

RUN apt-get update && \
    apt-get install nginx -y && \
    echo -e "\ndaemon off;" >> /etc/nginx/nginx.conf && \
    echo "<h1>Hello SOMA</h1>" > /var/www/html/index.html

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT ["nginx"]
# CMD ["nginx"]
# CMD ["nginx", "-g", "daemon off;"]

EXPOSE 80
