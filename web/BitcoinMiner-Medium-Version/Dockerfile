FROM chevalo123/debian_base_privesc

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt -yq upgrade

RUN mkdir /home/bitcoinminer
COPY ./ /home/bitcoinminer

RUN apt-get -yq install python3
RUN apt-get -yq install python3-pip
RUN pip3 install flask

EXPOSE 80
WORKDIR /home/bitcoinminer/

CMD ["su","ctf","-c","python3 /home/bitcoinminer/main.py"]
