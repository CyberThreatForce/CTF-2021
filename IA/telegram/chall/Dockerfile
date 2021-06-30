FROM chevalo123/ezneh_apache_php_sql

COPY ./apache/001-challengestego.conf /etc/apache2/sites-available
RUN a2ensite 001-challengestego.conf
COPY ./public_html /var/www/html
RUN rm -rf /root/*
COPY run.sh /root/
RUN chmod a+x /root/run.sh
ENTRYPOINT ["/root/run.sh"]
