FROM ubuntu:latest
MAINTAINER Eric  "ermsa"
RUN  apt-get -y update
RUN  apt-get -y install python3-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["bikerack.py"]

