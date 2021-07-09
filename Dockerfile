FROM ubuntu:20.04
COPY . /home/codes
WORKDIR /home/codes
RUN apt -y update && apt-get -y install python3 python3-pip git
RUN pip install -r requirements.txt
