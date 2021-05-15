FROM chevalo123/debian_base_privesc

RUN apt-get install gcc -y

RUN service ssh start
COPY ./flag.txt /home/ctf_cracked
RUN chown ctf_cracked:ctf_cracked /home/ctf_cracked/flag.txt
RUN chmod 400 /home/ctf_cracked/flag.txt
COPY ./sudoers /etc/sudoers
RUN chmod 555 /opt
COPY ./chevalo /opt/chevalo
RUN chmod 655 /opt/chevalo
EXPOSE 22


CMD ["/usr/sbin/sshd", "-D", "-e", "-f", "/etc/ssh/sshd_config"]
