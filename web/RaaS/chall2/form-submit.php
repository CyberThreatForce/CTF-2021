<?php
require 'connection.php'; // called by ajax

$username = mysqli_real_escape_string($dbcon, htmlentities($_POST['username']));
$email = mysqli_real_escape_string($dbcon, htmlentities($_POST['email']));
$radio = mysqli_real_escape_string($dbcon, $_POST['radio']);

$checkusername = mysqli_query($dbcon, "SELECT * FROM user_details WHERE username = '".$_POST['username']."'");


if(is_null($username)){
  $errorUser = "A valid email address is required.";
} elseif(mysqli_num_rows($checkusername)) {
  $errorUser = "username already exist";
} elseif(is_null($email) or !filter_var($email, FILTER_VALIDATE_EMAIL)) {
  $errorUser = "A valid email address is required.";
} elseif(is_null($radio)) {
  $errorUser = "what are you trying to do ?";
} else {
  $sql = "INSERT INTO user_details (username, email, radio) VALUES('$username', '$email', '$radio')";
  if(mysqli_query($dbcon, $sql)) {
  } else {
    echo 'Error: '.mysqli_error($dbcon);
  }

  mysqli_close($dbcon);
}