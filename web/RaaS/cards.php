<?php
require_once("config/db.php");
require_once("classes/Login.php");

session_start();

$conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
                   $sql = "SELECT * FROM users A INNER JOIN cards B ON A.user_id = B.user_id WHERE A.user_name ='" . $_SESSION['user_name'] . "'";
                   $result = $conn->query($sql);
                   if ($result!== false && $result->num_rows < 2) {
                       $row = $result->fetch_assoc();
                       $number = mt_rand(1111111111111111, 9999999999999999);
                       $sql = "INSERT INTO cards (cardNumber, amount, user_id)
                       VALUES($number, '0', (SELECT user_id FROM users WHERE user_name = '" . $row["user_name"] . "'));";
                       $query_new_user_insert = $conn->query($sql);
                       header('Location: /index.php');
                   } else {
                       header('Location: /index.php?errorcode=toomuchcards');
                   }

