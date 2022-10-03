# 이미지 빌드
docker build .
docker build --tag myhello:0.1 .


# 빌드 현황 모니터링
docker build --progress=plain .


# 이전 캐쉬 사용하지 않고 빌드
docker build --no-cache .

