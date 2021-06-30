#!/bin/sh 

apt-get install php-gd -y
service apache2 start
service mysql start
tail -f /var/log/apache2/access.log
