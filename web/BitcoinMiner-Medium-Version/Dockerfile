FROM ubuntu

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt -yq upgrade

RUN mkdir /home/bitcoinminer
COPY ./ /home/bitcoinminer

RUN apt-get -yq install python3
RUN apt-get -yq install python3-pip
RUN pip3 install flask

EXPOSE 80
CMD ["cd","/home/bitcoinminer/"]
CMD ["python3","/home/bitcoinminer/main.py"]
