FROM ubuntu:20.04

MAINTAINER shpark <emailaddress> 

RUN apt-get update && \
    apt-get install nginx -y && \
    echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
    sed -i 's|access_log /var/log/nginx/access.log;|access_log /dev/stdout;|g' /etc/nginx/nginx.conf && \
    sed -i 's|error_log /var/log/nginx/error.log;|error_log /dev/stderr;|g' /etc/nginx/nginx.conf

RUN echo "<h1>Hello SOMA</h1>" > /var/www/html/index.html

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT ["nginx"]
# CMD ["nginx"]
# CMD ["nginx", "-g", "daemon off;"]
# CMD ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf", "-g", "error_log /dev/stderr; access_log /dev/stdout;"]

EXPOSE 80
