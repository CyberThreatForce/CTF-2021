FROM chevalo123/debian_base_privesc
RUN chmod 555 /opt
RUN apt update -y
RUN apt upgrade -y
WORKDIR /opt/
COPY ./wrapper ./wrapper
COPY ./service ./service
EXPOSE 1234
CMD ["su","ctf","-c", "/opt/wrapper 1234 /opt/service"]
