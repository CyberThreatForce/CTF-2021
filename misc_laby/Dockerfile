FROM chevalo123/debian_base_privesc
RUN chmod 555 /opt
WORKDIR /opt/
COPY ./maze/contribPerso .
EXPOSE 1234
CMD ["su","ctf", "-c", "/opt/contribPerso 1234"]



