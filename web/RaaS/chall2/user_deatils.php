<?php
require 'connection.php';

$sql = "SELECT * FROM user_details";
if(mysqli_query($dbcon, $sql)) {
  $result = mysqli_query($dbcon, $sql);
  if(mysqli_num_rows($result) > 0) {
    while($rows = mysqli_fetch_assoc($result)){
      $user_details[] = $rows;
    }
    mysqli_free_result($result);
  } else {
    echo 'No result found';
  }
} else {
  echo 'Error: '.mysqli_error($dbcon);
}

mysqli_close($dbcon);