FROM chevalo123/debian_base_privesc
RUN chmod 555 /opt
RUN apt update -y
RUN apt upgrade -y
RUN apt install -y python3
WORKDIR /opt/
COPY ./main.py ./main.py
EXPOSE 8080
CMD ["su", "ctf", "-c" ,"python3 /opt/main.py"]



