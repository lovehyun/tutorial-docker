# 도커 보안 고려사항
- 리소스 할당량 활용
- 도커 컨테이너, 루트로 실행 방지
- 도커 컨테이너 레지스트리의 보안 유지
- 신뢰할 수 있는 출처 사용
- 보안을 염두해 둔 API 및 네트워크 설계
- 컨테이너 내 라이브러리/소스코드 분석

# 도커 보안 체크리스트
- 최신 버전 업데이트
- 도커 데몬 소켓 관리 
  - -H 를 통한 TCP 오픈
  - docker.sock 노출
- 루트 실행 방지 (사용자 계정 생성)
  - docker run -u xxxx ubuntu
  - FROM alpine
    RUN groupadd -r mygroup && useradd -r -g mygroup user
    USER user
- 커널 레벨 역할/권한(capabilities) 제한
  - docker run --cap-drop xxx --cap-add xxx
- CVE 체크 도구 활용
  - clair, trivy 등의 오픈소스를 통한 이미지 취약점 점검


