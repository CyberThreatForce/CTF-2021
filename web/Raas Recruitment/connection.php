<?php
$dbhost = 'localhost';
$dbusername = 'root';
$dbpassword = '';
$dbname = 'chall2';
$dbcon = mysqli_connect($dbhost, $dbusername, $dbpassword, $dbname) or die('Could not connect to MySQL');