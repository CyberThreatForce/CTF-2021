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
<title>Dev - APT 403</title>
<meta name="description" content="Login and Register Form Html Template">
<meta name="author" content="harnishdesign.net">

<!-- Web Fonts
========================= -->
<link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Poppins:100,200,300,400,500,600,700,800,900' type='text/css'>

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

<div id="main-wrapper" class="oxyy-login-register">
  <div class="hero-wrap d-flex align-items-center h-100">
    <div class="hero-mask opacity-4 bg-secondary"></div>
    <div class="hero-bg hero-bg-scroll" style="background-image:url('./images/login-bg-3.jpg');"></div>
    <div class="hero-content mx-auto w-100 h-100">
      <div class="container">
        <div class="row no-gutters min-vh-100"> 
          <!-- Welcome Text
		  ========================= -->
          <div class="col-md-6 d-flex flex-column">
            <div class="row no-gutters my-auto">
              <div class="col-10 col-lg-9 mx-auto text-center">
                <h1 class="text-5 font-weight-400 text-white mb-5">This panel is only for approved dev</h1>
                <p><img src="images/qr-code.png"      width="200" 
     height="200" class="shadow-lg" alt="qr code"></p>
                <p class="text-white mb-0">Log In with QR Code</p>
                <p class="text-light text-2 mx-lg-5">Scan this with your camera to login instantly.</p>
              </div>
            </div>
          </div>
          <!-- Welcome Text End --> 
          
          <!-- Login Form
		  ========================= -->
          <div class="col-md-6 d-flex align-items-center py-5">
            <div class="container my-auto py-4 shadow-lg bg-white">
              <div class="row">
                <div class="col-11 col-lg-11 mx-auto">
                  <h3 class="text-9 font-weight-600 text-center mt-2 mb-3">Login</h3>
                  <form method="post" action="index.php" name="loginform" id="loginForm">
                    <div class="form-group">
                      <label class="text-dark font-weight-600" for="username">Username</label>
                      <input id="login_input_username" id="username" class="form-control rounded-0" type="text" name="user_name" placeholder="Username" required />
                    </div>
                    <div class="form-group">
                      <label for="loginPassword" class="text-dark font-weight-600">Password</label>
                      <input id="login_input_password" class="form-control rounded-0" id="loginPassword" type="password" name="user_password" autocomplete="off" placeholder="Enter Password" required />
                    </div>
                    <button id="submit" class="btn btn-primary btn-block my-4"  type="submit"  name="login" value="Log in" >Login</button>
                  </form>
                </div>
              </div>
            </div>
          </div>
          <!-- Login Form End --> 
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Script --> 
<script src="vendor/jquery/jquery.min.js"></script> 
<script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script> 
<script src="js/theme.js"></script>
</body>
</html>