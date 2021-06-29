FROM chevalo123/debian_base_privesc
RUN chmod 555 /opt
RUN apt update -y
RUN apt upgrade -y
RUN apt -y install curl wget netcat python3
WORKDIR /opt/
COPY ./wrapper ./wrapper
COPY ./service ./service
COPY ./flag2.txt /home/ctf/flag.txt
RUN chmod 444 /home/ctf/flag.txt
COPY ./stage2.py /bin/check
RUN chown ctf_cracked:ctf_cracked /bin/check
RUN chmod 555 /bin/check
RUN chmod +s /bin/check
COPY ./flag3.txt /home/ctf_cracked/flag.txt
RUN chown ctf_cracked:ctf_cracked /home/ctf_cracked/flag.txt
RUN chmod 400 /home/ctf_cracked/flag.txt
EXPOSE 1234
CMD ["su","ctf","-c", "/opt/wrapper 1234 /opt/service"]
