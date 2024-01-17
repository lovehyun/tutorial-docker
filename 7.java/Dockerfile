# 컨테이너 환경에서 컴파일 예시
FROM openjdk

ADD HelloWorld.java .

RUN javac HelloWorld.java 

ENTRYPOINT ["java", "HelloWorld"]
