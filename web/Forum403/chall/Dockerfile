FROM chevalo123/ezneh_apache_php_sql

COPY ./apache/001-challenge.conf /etc/apache2/sites-available
RUN a2ensite 001-challenge.conf
COPY ./mysql/ch4ll3ng3.sql /root
COPY ./mysql/conf_base.sql /root
RUN mysqld --user=mysql --bootstrap --verbose=0 --skip-name-resolve --skip-networking=0 < /root/conf_base.sql
RUN mysqld --user=mysql --bootstrap --verbose=0 --skip-name-resolve --skip-networking=0 < /root/ch4ll3ng3.sql
COPY ./public_html /var/www/html
RUN rm -rf /root/*
COPY run.sh /root/
RUN chmod a+x /root/run.sh
ENTRYPOINT ["/root/run.sh"]
