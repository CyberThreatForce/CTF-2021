<?php
require 'connection.php'; // called by ajax

$username = mysqli_real_escape_string($dbcon, htmlentities($_POST['username']));
$email = mysqli_real_escape_string($dbcon, htmlentities($_POST['email']));
$radio = mysqli_real_escape_string($dbcon, $_POST['radio']);

$checkusername = mysqli_query($dbcon, "SELECT * FROM user_details WHERE username = '".$_POST['username']."'");


if(is_null($username)){
  header("Location: /index.php?errorcode=username");//echo "Bad email!!!";
  $errorUser = "username";
} elseif(mysqli_num_rows($checkusername)) {
  header("Location: /index.php?errorcode=usernamexist");//echo "Bad email!!!";
  $errorUser = "usernamexist";
} elseif(is_null($email) or !filter_var($email, FILTER_VALIDATE_EMAIL)) {
  header("Location: /index.php?errorcode=email");//echo "Bad email!!!";
  $errorUser = "email";
} elseif(is_null($radio)) {
  header("Location: /index.php?errorcode=?");//echo "Bad email!!!";
  $errorUser = "?";
} else {
  $sql = "INSERT INTO user_details (username, email, radio) VALUES('$username', '$email', '$radio')";
  if(mysqli_query($dbcon, $sql)) {
  } else {
    echo 'Error: '.mysqli_error($dbcon);
  }

  mysqli_close($dbcon);
}