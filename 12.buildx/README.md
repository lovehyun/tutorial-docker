# Docker Buildx 설치 및 설정

## Docker buildx 설치 (기본 미포함)
```
mkdir -p ~/.docker/cli-plugins/
curl -SL https://github.com/docker/buildx/releases/download/v0.15.0/buildx-v0.15.0.linux-amd64 -o ~/.docker/cli-plugins/docker-buildx
chmod +x ~/.docker/cli-plugins/docker-buildx
```

## Docker buildx 확인
```
docker buildx version
github.com/docker/buildx v0.15.0 d3a53189f7e9c917eeff851c895b9aad5a66b108
```

## 빌더 인스턴스 생성 및 활성화
```
docker buildx create --name mybuilder --use
docker buildx inspect --bootstrap
```

### 빌더 인스턴스 확인
```
docker buildx ls
```

### 빌더 인스턴스 삭제
```
docker buildx rm mybuilder
```

## 이미지 빌드
```
docker buildx build . -t hello
```

### 이미지 로컬 Docker 데몬에 로드하기
```
docker buildx build . -t hello --load
```

### 이미지 레지스트리에 푸시하기
```
docker buildx build . -t username/hello --push
```

### 여러 플랫폼용 이미지 빌드
```
docker buildx build --platform linux/amd64,linux/arm64 -t hello --load .
```
