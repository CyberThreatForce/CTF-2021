<?php require_once("config/db.php"); 


echo("GG now take you flag:\r\nCYBERTF{L0ok_M0m_i_C4n_FouNd_XsS_aNd_3xpLoiT_It}");
echo("</br>");

$db_connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

$username2 = $_SESSION['user_name'];

$sql = "DELETE FROM user_details WHERE username= '$username2'";

if ($db_connection->query($sql) === TRUE) {
    echo "</br> This account is now deleted (we dont'want a random guy find the login/pass with luck and get the flag without exploit)";
    $_SESSION = array();
    session_destroy();
  } else {
    echo "Error contact an admin please ";
}


?>