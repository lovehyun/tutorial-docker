# Setup
https://wiki.archlinux.org/title/Sudo
alias sudo='sudo '
alias my-docker="go run main.go"
cp main2.go main.go


# main1.go
Basic template - 실제 동작 안함



# main2.go
프로세스 포크해서 hello world, ls 등 실행하는 기본 golang 코드

go run main2.go run echo hello world
go run main2.go run ls
go run main2.go run ls -l



# main3.go
UTS (Unix Time-sharing System = hostname) 격리 예제

sudo go run main3.go run hostname
sudo go run main3.go run hostname container

sudo go run main3.go run bash
hostname container



# main4.go
실행 시 바로 격리된 호스트네임으로 출력 예제

sudo go run main4.go run bash
호스트네임 쉘프롬프트에 PS1

ps
ps x
<프로세스는 아직 미격리>



# main5.go
프로세스 분리 시도 (그러나 프로세스가 분리 되더라도 proc 파일시스템으로 인해 동작 X)

sudo go run main5.go run bash
<시작시 PID>

ps
ps x
<shared - proc 으로 인해서..>



# main6.go
여러개의 도커가 이것저것 파일 시스템 마운트 하게 된다면? (NS = Filesystem 격리)

sudo go run main6.go run bash
<디렉토리 격리>
ps
ps x
<격리>
mount
<shared>

ps -C sleep
ls -l /proc/<pid>/root
cat /proc/<pid>/mounts



# main7.go
그래서 ROOT_DIR 새로 생성해서 작업 (편의 상 ubuntu 이미지를 기반으로 새로운 루트파일 시스템 생성)

mkdir ROOT_DIR
cd ROOT_DIR
touch CONTAINER_ROOT
mkdir bin
mkdir etc
mkdir lib
mkdir lib64
mkdir proc
cp -r /bin .
cp -r /lib/x86_64-linux-gnu ./lib
cp -r /lib64 .
또는...
docker export $(docker create ubuntu:20.04) | tar -xf - -C ROOT_DIR


sudo go run main7.go run bash
<디렉토리 격리>

ps
<안됨>

mount -t proc proc /proc

ln -s /proc/self/mounts /etc/mtab
mount
<shared>



# main8.go
프로세스 격리, ROOT 파이 시스템 마운트, proc 파일시스템 자동 마운트 예제

sudo go run main8.go run bash
<디렉토리 격리>

ps
ps x
<격리>



# main9.go

cd /sys/fs/cgroup/memory
cat memory.limit_in_bytes
docker run --rm -it ubuntu /bin/bash
docker run --rm -it ubuntu --memory=10M /bin/bash
cat docker/xxxxx/memory.limit_in_bytes


