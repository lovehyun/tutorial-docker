# 도커의 환경 구성
/lib/systemd/system/docker.service 파일을 통한 각종 옵션 정의

## 추가적인 TCP 소켓 생성

ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock -H 0.0.0.0:12345

로 변경하게 되면 도커 서비스 재시작 이후 curl localhost:12345 통해 REST 통신 가능


# Unix domain socket 을 통한 REST 인터페이스 연동

위 설정을 통해 TCP 통신을 하지 않더라도, unix domain 소켓을 통해 기본적으로 REST 통신이 가능 함.

curl --unix-socket /var/run/docker.sock http://localhost/images/json | jq

curl --unix-socket /var/run/docker.sock http://localhost/containers/json | jq


그 외에도 컨테이너의 상태나 설정 등도 가능 함.

curl --unix-socket http://localhost/containers/xxxx/json | jq -r '.State.Status'

curl --unix-socket -X POST http://localhost/containers/xxxx/stop | jq -r '.'

