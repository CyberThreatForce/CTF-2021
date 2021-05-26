FROM chevalo123/debian_base_privesc
COPY ./flag.txt /home/ctf
RUN chmod 555 /opt
RUN apt update -y
RUN apt upgrade -y
RUN apt-get install python3 -y
RUN ln -s /usr/bin/python3 /bin/python
WORKDIR /opt/
COPY ./wrapper ./wrapper
COPY ./chall.py ./chall.py
EXPOSE 1234
CMD ["su","ctf","-c", "/opt/wrapper 1234 /opt/chall.py"]



