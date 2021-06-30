FROM chevalo123/debian_base_privesc
COPY ./flag.txt /home/ctf
RUN chmod 555 /opt
RUN dpkg --add-architecture i386
RUN apt update -y
RUN apt upgrade -y
RUN apt-get install gcc-multilib g++-multilib -y
WORKDIR /opt/
COPY ./wrapper ./wrapper
COPY ./auth_du_pauvre ./auth_du_pauvre
COPY ./readline /bin/readline
RUN chown ctf_cracked:ctf_cracked /bin/readline
RUN chmod 4755 /bin/readline
COPY ./flag1.txt /home/ctf_cracked/flag.txt
RUN chown ctf_cracked:ctf_cracked /home/ctf_cracked/flag.txt
RUN chmod 700 /home/ctf_cracked/flag.txt
RUN chmod -R 775 /home/ctf
EXPOSE 1234
CMD ["su","ctf","-c", "/opt/wrapper 1234 /opt/auth_du_pauvre"]



