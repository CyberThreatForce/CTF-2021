<?php
$dbhost = 'localhost';
$dbusername = 'root';
$dbpassword = '';
$dbname = 'chall_dev';
$dbcon = mysqli_connect($dbhost, $dbusername, $dbpassword, $dbname) or die('Could not connect to MySQL');