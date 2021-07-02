<?php
require 'connection.php'; // called by ajax
session_start();

if($_SESSION['user_login_status'] != 1){
    header("Location: index.php");
}

$username = mysqli_real_escape_string($dbcon, htmlentities($_POST['username']));
$password = mysqli_real_escape_string($dbcon, htmlentities($_POST['password']));
$password2 = mysqli_real_escape_string($dbcon, htmlentities($_POST['password2']));



$checkusername = mysqli_query($dbcon, "SELECT * FROM user_details WHERE username = '".$_POST['username']."'");


if(is_null($username)){
  $errorUser = "Enter a username";
} elseif ($password != $password2) {
  $errorUser = "password is not the same";
} elseif(mysqli_num_rows($checkusername)) {
  $errorUser = "username already exist";
} else {
  $sql = "INSERT INTO user_details (username, passwordfinal) VALUES('$username', '$password')";
  if(mysqli_query($dbcon, $sql)) {
  } else {
    echo 'Error: '.mysqli_error($dbcon);
  }

  mysqli_close($dbcon);
}