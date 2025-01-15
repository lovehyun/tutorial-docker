# Flask 기반 Docker 보안 가이드

## 📦 1. 최소 권한 원칙 (Least Privilege)
- **루트 사용자 금지:** 비루트 계정을 생성하고, 해당 계정으로 Flask 앱을 실행합니다.
```dockerfile
# 경량 Python 이미지 사용 및 비루트 사용자 설정
FROM python:3.11-slim

# 사용자 생성 및 설정
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# 작업 디렉토리 설정 및 권한 변경
WORKDIR /app
COPY . /app

# 종속성 설치 (필요 시 only production 사용)
RUN pip install --no-cache-dir -r requirements.txt

# 사용자 변경 및 실행
USER appuser
CMD ["python", "app.py"]
```

## 🔒 2. 종속성 검증 및 최신 버전 유지
- **패키지 취약점 검사:** `pip-audit` 사용
```bash
pip install pip-audit
pip-audit
```

## 📑 3. 다중 스테이지 빌드 (Multi-Stage Build)
- **빌드와 실행 환경 분리:**
```dockerfile
# 빌드 단계
FROM python:3.11-slim AS builder
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# 실행 단계
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app .
USER appuser
CMD ["python", "app.py"]
```

## 🔥 4. 불필요한 권한 제거 (Capabilities 및 Privileges)
```bash
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE <image>
```

## 📶 5. 네트워크 보안 및 방화벽
```bash
docker network create --driver bridge secure_network
docker run --network secure_network <image>
```

## 📜 6. 환경변수 보안 및 `.env` 관리
```dockerignore
.env
__pycache__
```
```bash
docker run --env-file .env <image>
```

## 🔗 7. 이미지 서명 및 검증
```bash
export DOCKER_CONTENT_TRUST=1
```

## 🛡️ 8. CVE 점검 및 보안 스캐닝
```bash
trivy image <image>
clairctl analyze <image>
```

## 📂 9. 파일 시스템 및 경로 보호
```bash
docker run --read-only <image>
```
```bash
docker run --read-only -v /data/app:rw <image>
```

## ✅ 보안 체크리스트 요약
- [x] 루트 사용자 실행 방지 (`USER` 명령어 적용)
- [x] 최소한의 커널 권한 사용 (`--cap-drop=ALL`)
- [x] 다중 스테이지 빌드 사용
- [x] 최신 보안 패키지 (`pip-audit`)
- [x] 환경변수 파일 보호 (`.env` 관리)
- [x] 취약점 검사 (`trivy`, `clair`)
- [x] 이미지 서명 (`DOCKER_CONTENT_TRUST`)
- [x] 읽기 전용 파일시스템 (`--read-only`)
