# Express 기반 Docker 보안 가이드

## 📦 1. 최소 권한 원칙 (Least Privilege)
- **루트 사용자 금지:** 애플리케이션을 실행할 사용자 계정을 생성하고, 해당 계정으로 컨테이너를 실행합니다.
```dockerfile
# 베이스 이미지로 공식 Node.js 버전 사용 (Alpine은 경량화 버전)
FROM node:18-alpine

# 애플리케이션 경로 및 사용자 생성
WORKDIR /app
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# 사용자 권한 변경
USER appuser
```

## 🔒 2. 종속성 검증 및 최신 버전 유지
- **의존성 검증:** `package.json` 내 불필요하거나 취약한 패키지 제거
- **의존성 최신화 및 취약점 점검:**
```bash
npm audit fix
npm update
```

## 📑 3. 다중 스테이지 빌드 (Multi-Stage Build)
- **빌드와 실행을 분리:** 불필요한 빌드 도구 제거
```dockerfile
# 빌드 스테이지
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# 실행 스테이지
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app .
USER appuser
CMD ["node", "index.js"]
```

## 🔥 4. 불필요한 권한 제거 (Capabilities 및 Privileges)
- **권한 제한:** `--cap-drop` 및 `--cap-add` 활용
```bash
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE <image>
```

## 📶 5. 네트워크 보안 및 방화벽
- **네트워크 세분화:** 브릿지 네트워크 대신 사용자 정의 네트워크 사용
```bash
docker network create --driver bridge secure_network
docker run --network secure_network <image>
```

## 📜 6. 환경변수 보안 및 `.env` 관리
- **민감한 정보 관리:** `.env` 파일을 `.dockerignore`에 추가
```dockerignore
.env
node_modules
```
- **환경변수 주입:** `Dockerfile`에 하드코딩 금지
```bash
docker run --env-file .env <image>
```

## 🔗 7. 이미지 서명 및 검증
- **신뢰할 수 있는 이미지 사용:** 서명 활성화
```bash
export DOCKER_CONTENT_TRUST=1
```

## 🛡️ 8. CVE 점검 및 보안 스캐닝
- **취약점 점검:** `trivy` 또는 `clair` 사용
```bash
trivy image <image>
clairctl analyze <image>
```

## 📂 9. 파일 시스템 및 경로 보호
- **읽기 전용 파일 시스템 적용:**
```bash
docker run --read-only <image>
```
- **특정 볼륨만 쓰기 가능:**
```bash
docker run --read-only -v /data/app:rw <image>
```

## ✅ 보안 강화 요약 체크리스트
- [x] 루트 사용자 실행 방지 (`USER` 명령어 사용)
- [x] 최소한의 권한만 부여 (`cap-drop=ALL`)
- [x] 다중 스테이지 빌드 활용
- [x] 불필요한 소프트웨어 제거 (경량화 이미지 사용)
- [x] 환경변수 보안 (`.env` 파일 관리)
- [x] 취약점 스캔 (`trivy`, `clair`)
- [x] 서명된 이미지 사용 (`DOCKER_CONTENT_TRUST`)
- [x] 파일 시스템 읽기 전용 모드 (`--read-only`)
