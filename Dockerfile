FROM ubuntu:20.04
RUN apt update && apt upgrade -y
RUN apt-get install python
COPY /var/lib/jenkins/workspace/test/ 
