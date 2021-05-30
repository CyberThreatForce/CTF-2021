FROM chevalo123/debian_base_privesc
COPY ./flag.txt /home/ctf
RUN chmod 555 /opt
RUN dpkg --add-architecture i386
RUN apt update -y
RUN apt upgrade -y
RUN apt-get install gcc-multilib g++-multilib -y
WORKDIR /opt/
COPY ./wrapper ./wrapper
COPY ./chall ./chall
EXPOSE 1234
CMD ["su","ctf","-c", "/opt/wrapper 1234 /opt/chall"]



