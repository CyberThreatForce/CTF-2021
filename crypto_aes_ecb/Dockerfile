FROM chevalo123/debian_base_privesc
RUN chmod 555 /opt
RUN dpkg --add-architecture i386
RUN apt update -y
RUN apt upgrade -y
RUN apt-get install python3 python3-pip -y
RUN pip3 install crypto
RUN pip3 install pycryptodome
WORKDIR /opt/
COPY ./wrapper ./wrapper
COPY ./enc_test_ecb.py ./enc_test_ecb.py
COPY ./data.key ./data.key
EXPOSE 1234
CMD ["su","ctf","-c", "/opt/wrapper 1234 /opt/enc_test_ecb.py"]



