FROM jenkins/jenkins:latest
USER root
RUN mkdir -p /app/jenkins
WORKDIR /app/jenkins
COPY requirements.txt /app/jenkins/
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
WORKDIR /app/