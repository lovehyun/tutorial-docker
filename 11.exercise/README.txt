# a.reverse-proxy-local

# standalone 서버에서 동작 테스트
sudo systemctl start nginx
sudo cp service1 /etc/nginx/sites-available/service
sudo ln -s /etc/nginx/sites-available/service /etc/nginx/sites-enable/service
sudo nginx -t
sudo systemctl restart nginx

# 단계별로 변경하며 테스트
sudo cp service2 /etc/nginx/sites-available/service
sudo cp service3 /etc/nginx/sites-available/service
sudo cp service4 /etc/nginx/sites-available/service


# proxy 서버 설정되어 올바른 client IP 가 로그에 주소가 출력되지 않을때 ProxyFix 사용
# https://flask.palletsprojects.com/en/2.0.x/deploying/wsgi-standalone/



# b.reverse-proxy-docker

# 도커 서비스 하나씩 띄워서 개별 확인
docker run --name my-flask1 -d -p 8000:5000 -e APP_COLOR=green lovehyun/flask-app:1.2
docker run --name my-flask2 -d -p 8001:5000 -e APP_COLOR=orange lovehyun/flask-app:1.2
docker run --name my-flask3 -d -p 8002:5000 -e APP_COLOR=red lovehyun/flask-app:1.2

curl localhost:8000
curl localhost:8001
curl localhost:8002


# 웹 서비스 띄우고 reverse_proxy 확인

# 설정 파일 내에서 IP 를 변경해 주어야 함 (아래 명령어로 IP 찾아서...)
docker inspect -f "{{ .NetworkSettings.IPAddress }}" my-flask

# 링크를 통해 컨테이너 이름으로 연결 할 수도 있음
docker run -d --name my-nginx --link my-flask <옵션 중략> nginx

# 설정파일 로컬에서 마운트 (full-path 를 사용해야 함)
docker run --name my-nginx -v /<full-path>/nginx/conf:/etc/nginx/conf.d:ro -d -p 80:80 nginx
docker run --name my-nginx -v /<full-path>/nginx/conf:/etc/nginx/conf.d:ro -d --link my-flask -d -p 80:80 nginx


# 웹 서비스 설정 변경하고 reverse_proxy + load_balancing 확인
docker run --name my-nginx -v /<full-path>/nginx/conf:/etc/nginx/conf.d:ro -d --link my-flask1:my-flask1 --link my-flask2:my-flask2 --link my-flask3:my-flask3 -d -p 80:80 nginx

curl localhost



# c.reverse-proxy-dockercompose

# 모든 서비스 한번에 로딩
docker-compose up -d
docker-compose down
