<?php
    session_start();
    $_SESSION['user_name'] = 'guest';
?>

<!DOCTYPE html>
<meta charset="UTF-8">
<html>
    <head>
        <script type="text/javascript">
            function AlertBox() {
                alert("Hi agent root ~ ");
            }
            window.onload = AlertBox();
        </script>
        <title>Stage 2</title>
        <script type="text/javascript" src="style.js"></script>

    </head>

    <!-- APT 403 -->


    <body>
<body background= "https://i1.wp.com/lecoindescritiquescine.com/wp-content/uploads/2019/06/black-background-1468370534d5s.jpg" style="background-repeat: no-repeat; background-position: large;">

        <div align="center" style="padding-top: 100px">
            <br />
            <br />
            <form name="login" method="POST" onsubmit="return validateForm()">
                User: <input type="text" name="username" />
                <br />
                <br />
                Pass: <input type="password" name="password" />
                <br />
                <br />
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <input type="submit" name="submit" value="Login" />
            </form>
        </div>
        <div align="center">
        </div>
    </body>

    <!-- APT 403 -->
</html>
