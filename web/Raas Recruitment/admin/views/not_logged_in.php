<?php
// show potential errors / feedback (from login object)
if (isset($login)) {
    if ($login->errors) {
        foreach ($login->errors as $error) {
            echo $error;
        }
    }
    if ($login->messages) {
        foreach ($login->messages as $message) {
            echo $message;
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1.0, shrink-to-fit=no">
<link href="images/favicon.png" rel="icon" />
<title>Oxyy - Login and Register Form Html Template</title>
<meta name="description" content="Login and Register Form Html Template">
<meta name="author" content="harnishdesign.net">

<!-- Web Fonts
========================= -->
<link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Rubik:300,300i,400,400i,500,500i,700,700i,900,900i' type='text/css'>

<!-- Stylesheet
========================= -->
<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css" />
<link rel="stylesheet" type="text/css" href="vendor/font-awesome/css/all.min.css" />
<link rel="stylesheet" type="text/css" href="css/stylesheet.css" />
</head>
<body>

<!-- Preloader -->
<div class="preloader">
  <div class="lds-ellipsis">
    <div></div>
    <div></div>
    <div></div>
    <div></div>
  </div>
</div>
<!-- Preloader End -->

<div id="main-wrapper" class="oxyy-login-register h-100 d-flex flex-column bg-transparent">
  <div class="container my-auto">
    <div class="row">
      <div class="col-md-9 col-lg-7 col-xl-5 mx-auto">
        <div class="bg-white shadow-md rounded p-4 px-sm-5 mt-4">
          <div class="logo"> <a class="d-flex justify-content-center" href="index.html" title="Oxyy"><img src="images/logo-lg.png" alt="Oxyy"></a> </div>
          <hr class="mx-n4 mx-sm-n5">
          <p class="lead text-center">We are glad to see you again!</p>
          <form method="post" action="index.php" name="loginform" id="loginForm">
            <div class="form-group">
              <label for="username">Username</label>
              <input id="login_input_username" id="username" class="form-control" type="text" name="user_name" placeholder="Username" required />
            </div>
            <div class="form-group">
              <label for="loginPassword">Password</label>
              <input id="login_input_password" class="form-control" id="loginPassword" type="password" name="user_password" autocomplete="off" placeholder="Enter Password" required />
            </div>
            <button id="submit" class="btn btn-primary btn-block my-4"  type="submit"  name="login" value="Log in" >Login</button>
          </form>
        </div>
      </div>
    </div>
  </div>
  <div class="container-fluid py-3">
    <p class="text-center text-2 text-muted mb-0">Copyright © 2020 <a href="#">Oxyy</a>. All Rights Reserved.</p>
  </div>
</div>

<!-- Script --> 
<script src="vendor/jquery/jquery.min.js"></script> 
<script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script> 
<script src="js/theme.js"></script>
</body>
</html>