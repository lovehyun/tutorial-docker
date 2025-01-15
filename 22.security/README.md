# 도커 보안 고려사항

## 리소스 할당량 활용
도커 컨테이너의 리소스를 제한하여 자원 과다 사용을 방지할 수 있습니다.
```bash
docker run --memory <memory_limit> --cpus <cpu_limit> <image>
```

## 도커 컨테이너 루트로 실행 방지
컨테이너를 루트로 실행하는 것은 보안상 위험할 수 있습니다. 비루트 사용자로 실행하거나, 이미지를 생성할 때 계정을 생성하여 보안을 강화할 수 있습니다.
```bash
docker run -u <username> <image>
```
### 이미지 내 사용자 계정 생성
```dockerfile
FROM alpine
RUN groupadd -r mygroup && useradd -r -g mygroup user
USER user
```

### 기본 사용자 계정 설정 (데몬 설정)
```json
{
  "userns-remap": "default"
}
```

## 도커 컨테이너 레지스트리의 보안 유지
- 신뢰할 수 있는 공식 레지스트리 사용
- 프라이빗 레지스트리 사용 시 인증 및 접근 제어 적용
- 이미지 서명 및 검증 적용 (Docker Content Trust 사용)
```bash
export DOCKER_CONTENT_TRUST=1
```

## 보안을 염두해 둔 API 및 네트워크 설계
- Docker API는 TLS를 사용하여 보호
- 불필요한 포트 노출 방지
- 네트워크 세그먼트 분리 및 방화벽 사용

## 컨테이너 내 라이브러리/소스코드 분석
이미지 내 취약점을 점검하기 위해 오픈소스 도구를 활용할 수 있습니다.
```bash
trivy image <image>
clairctl analyze <image>
```

---

# 도커 보안 체크리스트

## 1. 최신 버전 업데이트
- 도커 엔진, 플러그인 및 관련 도구를 최신 버전으로 유지

## 2. 도커 데몬 소켓 관리
- TCP 소켓 오픈 시 인증 및 암호화 적용
- `/var/run/docker.sock` 노출 금지

## 3. 루트 실행 방지
- 사용자 계정 생성 및 비루트 계정 실행 적용

## 4. 커널 레벨 역할/권한 제한 (capabilities 관리)
- 불필요한 커널 권한 제거
```bash
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE <image>
```

## 5. CVE 체크 도구 활용
- `clair`, `trivy` 등의 도구를 이용한 이미지 취약점 검사

## 6. 도커 파일 보안
- `FROM` 구문에 신뢰할 수 있는 공식 이미지 사용
- `COPY` 대신 `ADD` 사용 지양 (URL 다운로드 기능 때문)

## 7. 이미지 서명 및 검증
- Docker Content Trust 활성화

## 8. 네트워크 보안
- 브릿지 네트워크 대신 사용자 정의 네트워크 사용
- 네트워크 트래픽 제어 및 방화벽 설정 적용

## 9. 데이터 보호
- 데이터 암호화 및 보관 정책 적용

## 10. 로깅 및 모니터링
- 도커 로그 드라이버 구성
- 보안 이벤트 모니터링 및 알림 설정
