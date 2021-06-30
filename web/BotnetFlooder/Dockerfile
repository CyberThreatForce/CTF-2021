FROM chevalo123/debian_base_privesc

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt -yq upgrade

RUN mkdir /home/botnetflooder
COPY ./ /home/botnetflooder
COPY ./flag.txt /home/ctf/
RUN chown root:root /home/ctf/flag.txt
RUN chmod 444 /home/ctf/flag.txt
WORKDIR /home/botnetflooder/

RUN apt-get -yq install python3
RUN apt-get -yq install python3-pip
RUN pip3 install flask


EXPOSE 80
CMD ["su","ctf","-c","python3 /home/botnetflooder/main.py"]
