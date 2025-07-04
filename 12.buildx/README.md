# Docker Build Deprecated Warning and Buildx Migration

`docker build` 명령어를 사용할 때 `deprecated` 경고 메시지와 함께 `docker buildx`를 사용하라는 메시지가 나타나는 이유는, Docker가 기존의 `docker build`를 더 이상 권장하지 않고, 멀티 플랫폼 이미지를 지원하고 더 향상된 빌드 기능을 제공하는 `docker buildx`를 기본으로 채택했기 때문입니다.

## `docker buildx`란?
- **멀티 플랫폼 빌드 지원:** `docker buildx`는 ARM, x86 등 다양한 아키텍처용 이미지를 동시에 빌드할 수 있습니다.
- **캐싱 개선:** 고급 빌드 캐시를 제공하여 빌드 속도를 개선합니다.
- **분산 빌드:** 여러 노드를 사용한 분산 빌드 지원.
- **Dockerfile 호환:** 기존 Dockerfile과 호환됩니다.

## `docker build`에서 `docker buildx`로 전환 방법

1. **기본적으로 `buildx` 활성화하기**
   ```bash
   docker buildx install
   ```

2. **기본 빌더 확인 및 설정**
   ```bash
   docker buildx create --use
   ```

### `docker buildx` 설치 및 설정

`docker buildx`가 기본적으로 포함되지 않았을 경우, 아래와 같이 수동으로 설치할 수 있습니다:

```bash
mkdir -p ~/.docker/cli-plugins/
# curl -SL https://github.com/docker/buildx/releases/download/v0.15.0/buildx-v0.15.0.linux-amd64 -o ~/.docker/cli-plugins/docker-buildx
curl -SL https://github.com/docker/buildx/releases/latest/download/docker-buildx-linux-amd64 -o ~/.docker/cli-plugins/docker-buildx
chmod +x ~/.docker/cli-plugins/docker-buildx
```

### `docker buildx` 버전 확인
```bash
docker buildx version
github.com/docker/buildx v0.15.0 d3a53189f7e9c917eeff851c895b9aad5a66b108
```

### `docker buildx create --use`의 기능과 역할
- **빌더 인스턴스 생성:** `docker buildx create`는 새로운 빌더 인스턴스를 생성합니다. 빌더 인스턴스는 도커 이미지 빌드를 실행할 수 있는 환경을 의미합니다.
- **멀티플랫폼 지원:** 생성된 빌더는 멀티플랫폼 빌드를 지원할 수 있는 컨텍스트를 제공합니다.
- **빌더 활성화 (`--use` 옵션):** `--use` 옵션은 새로 생성한 빌더를 기본 빌더로 설정하여 이후의 `docker buildx build` 명령어에 적용되도록 합니다.

### `docker buildx create`로 생성된 빌더 확인 방법
- **생성된 빌더 리스트 확인:**
  ```bash
  docker buildx ls
  ```
- **빌더 상세 정보:**
  ```bash
  docker buildx inspect --bootstrap
  ```
- **빌더 인스턴스 삭제:**
  ```bash
  docker buildx rm mybuilder
  ```
- **로컬에 저장 경로:**
  생성된 빌더는 Docker 컨텍스트 내에 저장되며, Docker Desktop에서는 기본적으로 `~/.docker` 경로에 해당 정보가 저장됩니다.

### `docker buildx create --use` 사용 예제
```bash
docker buildx create --name mybuilder --use
docker buildx build --platform linux/amd64,linux/arm64 -t myimage:latest .
```

3. **이미지 빌드 명령어 예제 (기존과 동일하게 사용 가능)**
   ```bash
   docker buildx build -t myimage:latest .
   ```

4. **이미지 로컬 Docker 데몬에 로드하기**
   ```bash
   docker buildx build . -t hello --load
   ```

5. **이미지 레지스트리에 푸시하기**
   ```bash
   docker buildx build . -t username/hello --push
   ```

6. **멀티 아키텍처 빌드 예제**
   ```bash
   docker buildx build --platform linux/amd64,linux/arm64 -t hello --load .
   ```

## ⚠️ 주의사항
- `docker buildx`는 Docker Desktop 19.03 이상 버전에서 기본 제공되며, `buildx`가 없는 경우 수동 설치가 필요할 수 있습니다.
- `docker buildx`는 기존 `docker build`보다 더 강력하지만, 일부 오래된 기능은 제거되었을 수 있습니다.

이제 `docker build` 대신 `docker buildx`를 사용하는 것이 권장됩니다.
